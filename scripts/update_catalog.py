from __future__ import annotations

import argparse
import hashlib
import json
import os
import ssl
import time
import urllib.error
import urllib.request
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Any

from catalog_schema import (
    CATALOG_PATH,
    DATA_DIR,
    SNAPSHOTS_PATH,
    empty_record,
    load_catalog,
    load_json,
    record_key,
    today_utc,
    write_catalog,
    write_json,
)


OPENROUTER_MODELS_URL = "https://openrouter.ai/api/v1/models"
MANUAL_CATALOG_PATH = DATA_DIR / "manual_catalog.json"
MAX_SNAPSHOTS = 80
REQUEST_TIMEOUT_SECONDS = 20
MAX_RETRIES = 3


def build_https_context() -> ssl.SSLContext:
    try:
        import certifi  # type: ignore

        return ssl.create_default_context(cafile=certifi.where())
    except Exception:
        return ssl.create_default_context()


def request_json(
    url: str,
    *,
    timeout: int = REQUEST_TIMEOUT_SECONDS,
    headers: dict[str, str] | None = None,
    retries: int = MAX_RETRIES,
) -> tuple[Any, int, bytes]:
    request_headers = {
        "Accept": "application/json",
        "User-Agent": "free-llm-api-watch/0.2 (catalog updater)",
    }
    request_headers.update(headers or {})
    request = urllib.request.Request(url, headers=request_headers)
    last_error: Exception | None = None
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(
                request, timeout=timeout, context=build_https_context()
            ) as response:
                body = response.read()
                status = int(getattr(response, "status", 200))
            if status >= 400:
                raise urllib.error.HTTPError(url, status, "HTTP error", None, None)
            return json.loads(body.decode("utf-8")), status, body
        except urllib.error.HTTPError as exc:
            last_error = exc
            retryable = exc.code in {408, 425, 429} or exc.code >= 500
            if not retryable or attempt + 1 >= retries:
                raise
        except (urllib.error.URLError, TimeoutError, OSError, json.JSONDecodeError) as exc:
            last_error = exc
            if attempt + 1 >= retries:
                raise
        time.sleep(0.5 * (attempt + 1))
    if last_error:
        raise last_error
    raise RuntimeError("request failed without an exception")


def decimal_is_zero(value: Any) -> bool:
    try:
        return Decimal(str(value)) == Decimal("0")
    except (InvalidOperation, TypeError, ValueError):
        return False


def is_free_openrouter_model(model: dict[str, Any]) -> bool:
    """Require both main prices and every reported price dimension to be zero."""
    model_id = str(model.get("id", "")).strip()
    pricing = model.get("pricing")
    if not model_id or not isinstance(pricing, dict):
        return False
    if not decimal_is_zero(pricing.get("prompt")):
        return False
    if not decimal_is_zero(pricing.get("completion")):
        return False
    return all(decimal_is_zero(value) for value in pricing.values())


def normalize_existing(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    normalized: list[dict[str, Any]] = []
    defaults = empty_record()
    for original in records:
        if not isinstance(original, dict):
            continue
        record = dict(defaults)
        record.update(original)
        if "verified_at" not in original:
            record["verified_at"] = str(original.get("last_checked", ""))
        if "data_origin" not in original:
            record["data_origin"] = (
                "official_api"
                if original.get("provider_id") == "openrouter"
                and original.get("record_level") == "model"
                else "manual"
            )
        if "verification_status" not in original:
            record["verification_status"] = (
                "active" if original.get("is_recommended") else "unverified"
            )
        if (
            record.get("provider_id") == "openrouter"
            and record.get("record_level") == "model"
            and not record.get("offer_id")
        ):
            record["offer_id"] = "openrouter-free-model-route"
        normalized.append(record)
    return normalized


def build_manual_records() -> list[dict[str, Any]]:
    seed = load_json(MANUAL_CATALOG_PATH, {})
    if not isinstance(seed, dict):
        raise ValueError(f"{MANUAL_CATALOG_PATH} must contain a JSON object")
    providers = seed.get("providers", [])
    offers = seed.get("offers", [])
    models = seed.get("models", [])
    if not all(isinstance(rows, list) for rows in (providers, offers, models)):
        raise ValueError("manual_catalog.json providers, offers, and models must be arrays")

    provider_by_id: dict[str, dict[str, Any]] = {}
    records: list[dict[str, Any]] = []
    for source in providers:
        if not isinstance(source, dict):
            continue
        provider_id = str(source.get("provider_id", ""))
        if not provider_id:
            continue
        provider_by_id[provider_id] = source
        record = empty_record(
            record_level="provider",
            provider_id=provider_id,
            data_origin="manual",
            is_recommended=False,
        )
        record.update(source)
        records.append(record)

    offer_by_key: dict[tuple[str, str], dict[str, Any]] = {}
    for source in offers:
        if not isinstance(source, dict):
            continue
        provider_id = str(source.get("provider_id", ""))
        offer_id = str(source.get("offer_id", ""))
        if not provider_id or not offer_id:
            continue
        provider = provider_by_id.get(provider_id, {})
        offer_by_key[(provider_id, offer_id)] = source
        record = empty_record(
            record_level="offer",
            provider_id=provider_id,
            offer_id=offer_id,
            data_origin="manual",
            is_recommended=False,
        )
        record.update(provider_metadata(provider))
        record.update(source)
        records.append(record)

    for source in models:
        if not isinstance(source, dict):
            continue
        provider_id = str(source.get("provider_id", ""))
        offer_id = str(source.get("offer_id", ""))
        model_id = str(source.get("model_id", ""))
        if not provider_id or not model_id:
            continue
        provider = provider_by_id.get(provider_id, {})
        offer = offer_by_key.get((provider_id, offer_id), {})
        record = empty_record(
            record_level="model",
            provider_id=provider_id,
            offer_id=offer_id,
            model_id=model_id,
            data_origin="manual",
            is_recommended=False,
        )
        record.update(provider_metadata(provider))
        record.update(offer_metadata(offer))
        record.update(source)
        record["record_level"] = "model"
        record["provider_id"] = provider_id
        record["offer_id"] = offer_id
        record["model_id"] = model_id
        record["free_type"] = source.get("free_type", offer.get("free_type", "not_free_or_unverified"))
        record["free_quota"] = source.get("free_quota", offer.get("free_quota", ""))
        record["free_quota_unit"] = source.get(
            "free_quota_unit", offer.get("free_quota_unit", "")
        )
        record["rate_limits"] = source.get("rate_limits", offer.get("rate_limits", {}))
        records.append(record)
    return records


def provider_metadata(provider: dict[str, Any]) -> dict[str, Any]:
    fields = (
        "provider",
        "channel_type",
        "country_or_region",
        "official",
        "api_base",
        "openai_compatible",
        "anthropic_compatible",
        "privacy_notes",
        "terms_risk",
    )
    return {field: provider[field] for field in fields if field in provider}


def offer_metadata(offer: dict[str, Any]) -> dict[str, Any]:
    fields = (
        "free_type",
        "free_quota",
        "free_quota_unit",
        "quota_reset",
        "expires",
        "requires_card",
        "requires_identity_verification",
        "requires_phone_region",
        "quota_scope",
        "applies_to_models",
        "rate_limits",
        "source_type",
        "source_name",
        "source_url",
        "evidence_summary",
        "last_checked",
        "verified_at",
        "confidence",
        "verification_status",
        "is_recommended",
        "recommendation_reason",
        "fetch_status",
    )
    return {field: offer[field] for field in fields if field in offer}


def merge_records(
    existing: list[dict[str, Any]], incoming: list[dict[str, Any]]
) -> list[dict[str, Any]]:
    merged: dict[tuple[str, str, str, str], dict[str, Any]] = {}
    for record in existing:
        merged[record_key(record)] = record
    for record in incoming:
        key = record_key(record)
        if key in merged:
            combined = dict(merged[key])
            combined.update(record)
            merged[key] = combined
        else:
            merged[key] = record
    return list(merged.values())


def infer_modalities(model: dict[str, Any]) -> list[str]:
    architecture = model.get("architecture") or {}
    values = architecture.get("input_modalities") or []
    outputs = architecture.get("output_modalities") or []
    modalities = {str(value).lower() for value in [*values, *outputs]}
    if not modalities:
        text = " ".join(
            [
                str(model.get("id", "")),
                str(model.get("name", "")),
                str(architecture.get("modality", "")),
            ]
        ).lower()
        modalities.add("text")
        for modality in ("image", "audio", "video"):
            if modality in text or modality in {"vision"}:
                if modality == "vision":
                    modalities.add("image")
                else:
                    modalities.add(modality)
    return sorted(modalities)


def model_type_from_modalities(modalities: list[str]) -> str:
    if "audio" in modalities or "video" in modalities or "image" in modalities:
        return "multimodal"
    return "chat"


def build_openrouter_record(model: dict[str, Any], checked: str) -> dict[str, Any]:
    model_id = str(model.get("id", "")).strip()
    pricing = model.get("pricing") or {}
    context = model.get("context_length")
    try:
        context_window = int(context) if context is not None else None
    except (TypeError, ValueError):
        context_window = None
    modalities = infer_modalities(model)
    record = empty_record(
        provider="OpenRouter",
        record_level="model",
        provider_id="openrouter",
        offer_id="openrouter-free-model-route",
        channel_type="third_party_router",
        country_or_region="Global; model availability varies by account/region",
        official=False,
        api_base="https://openrouter.ai/api/v1",
        openai_compatible="yes",
        anthropic_compatible="unknown",
        free_type="free_router",
        free_quota="All reported model price dimensions are zero while listed as free",
        free_quota_unit="model_pricing",
        quota_reset="Rate limits are set by OpenRouter and may vary by account",
        expires="Model free status may change without notice",
        requires_card="no",
        quota_scope="per_model",
        model_id=model_id,
        model_name=str(model.get("name") or model_id),
        model_type=model_type_from_modalities(modalities),
        model_family=model_id.split("/", 1)[0] if "/" in model_id else "unknown",
        context_window=context_window,
        modalities=modalities,
        model_pricing={"unit": "USD per token", **pricing},
        privacy_notes="Third-party routing; review OpenRouter and upstream provider terms before sending sensitive data.",
        terms_risk="Free routing, model eligibility and limits can change without notice.",
        source_type="official_api",
        source_name="OpenRouter models API",
        source_url=OPENROUTER_MODELS_URL,
        evidence_summary=(
            "OpenRouter's official models API reported exact zero prompt and completion pricing "
            "and no nonzero additional price dimensions."
        ),
        last_checked=checked,
        verified_at=checked,
        confidence="high",
        verification_status="active",
        data_origin="official_api",
        is_recommended=True,
        recommendation_reason="The current OpenRouter models API reports zero for prompt, completion, and every other returned pricing dimension.",
        fetch_status="ok",
    )
    return record


def active_openrouter_records(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [
        record
        for record in records
        if record.get("provider_id") == "openrouter"
        and record.get("record_level") == "model"
        and record.get("data_origin") == "official_api"
        and record.get("verification_status") == "active"
        and record.get("is_recommended") is True
    ]


def make_snapshot(
    *,
    source_url: str,
    status: int | str,
    body: bytes,
    page_title: str,
    parser_status: str,
    extracted_fields: dict[str, Any],
    error: str = "",
) -> dict[str, Any]:
    excerpt = "Official API response summarized; raw response body is not stored."
    if error:
        excerpt = f"Fetch/parser issue: {error[:430]}"
    return {
        "source_url": source_url,
        "fetched_at": today_utc(),
        "http_status": status,
        "page_title": page_title[:120],
        "relevant_excerpt": excerpt[:500],
        "extracted_fields": extracted_fields,
        "hash": hashlib.sha256(body).hexdigest() if body else "",
        "parser_status": parser_status,
    }


def store_snapshot(snapshot: dict[str, Any]) -> None:
    snapshots = load_json(SNAPSHOTS_PATH, [])
    if not isinstance(snapshots, list):
        snapshots = []
    source_url = snapshot["source_url"]
    snapshots = [item for item in snapshots if item.get("source_url") != source_url]
    snapshots.append(snapshot)
    write_json(SNAPSHOTS_PATH, snapshots[-MAX_SNAPSHOTS:])


def update_openrouter(records: list[dict[str, Any]], offline: bool = False) -> tuple[list[dict[str, Any]], str]:
    records = dedupe_records(records)
    checked = today_utc()
    previous = active_openrouter_records(records)
    if offline:
        return mark_openrouter_stale(records, "offline mode requested", checked), "skipped"
    try:
        payload, status, body = request_json(OPENROUTER_MODELS_URL)
        if not isinstance(payload, dict) or not isinstance(payload.get("data"), list):
            raise ValueError("OpenRouter response field 'data' is not a list")
        models = [model for model in payload["data"] if isinstance(model, dict)]
        free_models = [model for model in models if is_free_openrouter_model(model)]
        if previous and not free_models:
            raise ValueError(
                f"abnormal free-model count drop: {len(previous)} previously active, "
                "zero returned; preserving old records for review"
            )
        if len(previous) >= 5 and len(free_models) < len(previous) / 2:
            raise ValueError(
                f"abnormal free-model count drop: {len(previous)} previously active, "
                f"{len(free_models)} returned; preserving old records for review"
            )

        api_by_id = {str(model.get("id", "")): model for model in models if model.get("id")}
        new_by_id = {
            str(model.get("id", "")): build_openrouter_record(model, checked)
            for model in free_models
        }
        merged: list[dict[str, Any]] = []
        for record in records:
            if not (
                record.get("provider_id") == "openrouter"
                and record.get("record_level") == "model"
                and record.get("data_origin") == "official_api"
            ):
                merged.append(record)
                continue
            model_id = str(record.get("model_id", ""))
            if model_id in new_by_id:
                merged.append(new_by_id.pop(model_id))
                continue
            withdrawn = dict(record)
            live_model = api_by_id.get(model_id)
            withdrawn["verification_status"] = "withdrawn"
            withdrawn["is_recommended"] = False
            withdrawn["free_type"] = "not_free_or_unverified"
            withdrawn["fetch_status"] = "ok"
            withdrawn["last_checked"] = checked
            withdrawn["verified_at"] = checked
            withdrawn["confidence"] = "high"
            withdrawn["recommendation_reason"] = (
                "Current OpenRouter API no longer reports this model as completely zero-priced."
                if live_model
                else "Model ID was absent from the current complete OpenRouter models API response."
            )
            if live_model and isinstance(live_model.get("pricing"), dict):
                withdrawn["model_pricing"] = {
                    "unit": "USD per token",
                    **live_model["pricing"],
                }
            withdrawn["evidence_summary"] = withdrawn["recommendation_reason"]
            merged.append(withdrawn)
        merged.extend(new_by_id.values())

        offer_key = ("openrouter", "offer", "", "openrouter-free-model-route")
        for record in merged:
            if record_key(record) == offer_key:
                record["applies_to_models"] = sorted(new_by_id.keys()) if new_by_id else sorted(
                    r["model_id"] for r in merged
                    if r.get("provider_id") == "openrouter"
                    and r.get("record_level") == "model"
                    and r.get("verification_status") == "active"
                    and r.get("is_recommended")
                )
                record["last_checked"] = checked
                record["fetch_status"] = "ok"
                record["verification_status"] = "active"
                record["confidence"] = "high"
                record["is_recommended"] = True
                record["error_summary"] = ""
        snapshot = make_snapshot(
            source_url=OPENROUTER_MODELS_URL,
            status=status,
            body=body,
            page_title="OpenRouter Models API",
            parser_status="ok",
            extracted_fields={
                "total_model_count": len(models),
                "free_model_count": sum(1 for model in models if is_free_openrouter_model(model)),
                "selection_rule": "prompt and completion exactly zero; every returned pricing value parses to zero",
            },
        )
        store_snapshot(snapshot)
        return dedupe_records(merged), "ok"
    except Exception as exc:
        error = safe_error_summary(exc)
        store_snapshot(
            make_snapshot(
                source_url=OPENROUTER_MODELS_URL,
                status="failed",
                body=b"",
                page_title="OpenRouter Models API",
                parser_status="failed",
                extracted_fields={"previous_active_count": len(previous)},
                error=error,
            )
        )
        return mark_openrouter_stale(records, error, checked), "failed"


def safe_error_summary(error: Exception) -> str:
    # Never emit request headers, API keys, or full URLs that could contain credentials.
    message = str(error)
    for name in ("GEMINI_API_KEY", "GROQ_API_KEY", "SILICONFLOW_API_KEY", "MODELSCOPE_API_TOKEN", "CLOUDFLARE_API_TOKEN", "COHERE_API_KEY"):
        secret = os.getenv(name, "")
        if secret:
            message = message.replace(secret, "[redacted]")
    return f"{type(error).__name__}: {message}"[:300]


def mark_openrouter_stale(
    records: list[dict[str, Any]], error: str, checked: str
) -> list[dict[str, Any]]:
    result: list[dict[str, Any]] = []
    found = False
    for original in records:
        record = dict(original)
        if (
            record.get("provider_id") == "openrouter"
            and record.get("record_level") == "model"
            and record.get("data_origin") == "official_api"
            and record.get("verification_status") != "withdrawn"
        ):
            found = True
            record["verification_status"] = "stale"
            record["is_recommended"] = False
            record["fetch_status"] = "failed"
            record["confidence"] = "low"
            record["error_summary"] = error[:300]
            record["recommendation_reason"] = "Last known model is stale because the latest official API check failed; not shown as current recommendation."
        if (
            record.get("provider_id") == "openrouter"
            and record.get("record_level") == "offer"
            and record.get("offer_id") == "openrouter-free-model-route"
        ):
            record["verification_status"] = "stale"
            record["is_recommended"] = False
            record["fetch_status"] = "failed"
            record["confidence"] = "low"
            record["error_summary"] = error[:300]
        result.append(record)
    if not found:
        result.append(
            empty_record(
                provider="OpenRouter",
                record_level="provider",
                provider_id="openrouter-update-monitor",
                channel_type="third_party_router",
                country_or_region="Global",
                official=False,
                api_base="https://openrouter.ai/api/v1",
                openai_compatible="yes",
                source_type="official_api",
                source_name="OpenRouter models API",
                source_url=OPENROUTER_MODELS_URL,
                evidence_summary="No model-level free claim is made because the official model API check failed.",
                last_checked=checked,
                verified_at="",
                confidence="low",
                verification_status="stale",
                is_recommended=False,
                recommendation_reason="API check failed; retry later and inspect the provider list manually.",
                fetch_status="failed",
                error_summary=error[:300],
            )
        )
    return result


def dedupe_records(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    result: dict[tuple[str, str, str, str], dict[str, Any]] = {}
    for record in records:
        key = record_key(record)
        if key in result:
            combined = dict(result[key])
            combined.update(record)
            result[key] = combined
        else:
            result[key] = record
    return list(result.values())


def extract_model_ids(payload: Any) -> list[str]:
    if isinstance(payload, list):
        rows = payload
    elif isinstance(payload, dict):
        rows = payload.get("data") or payload.get("models") or payload.get("items") or []
        if isinstance(rows, dict):
            rows = list(rows.values())
    else:
        rows = []
    ids: set[str] = set()
    if isinstance(rows, list):
        for row in rows:
            if isinstance(row, str):
                ids.add(row)
            elif isinstance(row, dict):
                model_id = row.get("id") or row.get("name") or row.get("model")
                if model_id:
                    ids.add(str(model_id))
    return sorted(ids)


def optional_monitors() -> list[dict[str, Any]]:
    monitors: list[dict[str, Any]] = []
    groq_key = os.getenv("GROQ_API_KEY", "")
    if groq_key:
        monitors.append({
            "provider_id": "groqcloud",
            "url": "https://api.groq.com/openai/v1/models",
            "headers": {"Authorization": f"Bearer {groq_key}"},
            "title": "Groq models API",
        })
    siliconflow_key = os.getenv("SILICONFLOW_API_KEY", "")
    if siliconflow_key:
        monitors.append({
            "provider_id": "siliconflow",
            "url": "https://api.siliconflow.cn/v1/models",
            "headers": {"Authorization": f"Bearer {siliconflow_key}"},
            "title": "SiliconFlow models API",
        })
    google_key = os.getenv("GEMINI_API_KEY", "")
    if google_key:
        monitors.append({
            "provider_id": "google-gemini",
            "url": "https://generativelanguage.googleapis.com/v1beta/models",
            "headers": {"x-goog-api-key": google_key},
            "title": "Gemini models API",
        })
    modelscope_key = os.getenv("MODELSCOPE_API_TOKEN", "")
    if modelscope_key:
        monitors.append({
            "provider_id": "modelscope",
            "url": "https://api-inference.modelscope.cn/v1/models",
            "headers": {"Authorization": f"Bearer {modelscope_key}"},
            "title": "ModelScope models API",
        })
    cloudflare_token = os.getenv("CLOUDFLARE_API_TOKEN", "")
    cloudflare_account = os.getenv("CLOUDFLARE_ACCOUNT_ID", "")
    if cloudflare_token and cloudflare_account:
        monitors.append({
            "provider_id": "cloudflare-workers-ai",
            "url": f"https://api.cloudflare.com/client/v4/accounts/{cloudflare_account}/ai/models/search",
            "headers": {"Authorization": f"Bearer {cloudflare_token}"},
            "title": "Cloudflare Workers AI models API",
        })
    cohere_key = os.getenv("COHERE_API_KEY", "")
    if cohere_key:
        monitors.append({
            "provider_id": "cohere",
            "url": "https://api.cohere.com/v2/models",
            "headers": {"Authorization": f"Bearer {cohere_key}"},
            "title": "Cohere models API",
        })
    return monitors


def update_optional_model_inventories() -> list[str]:
    warnings: list[str] = []
    monitors = optional_monitors()
    if not monitors:
        print("Optional authenticated model-list checks skipped: no provider API keys configured.")
    for index, monitor in enumerate(monitors):
        if index:
            time.sleep(1)
        url = monitor["url"]
        try:
            payload, status, body = request_json(url, headers=monitor["headers"])
            model_ids = extract_model_ids(payload)
            if not model_ids:
                raise ValueError("model inventory response contained no recognizable IDs")
            store_snapshot(
                make_snapshot(
                    source_url=url,
                    status=status,
                    body=body,
                    page_title=monitor["title"],
                    parser_status="ok",
                    extracted_fields={
                        "provider_id": monitor["provider_id"],
                        "model_count": len(model_ids),
                        "model_ids": model_ids[:500],
                        "inventory_only_not_free_proof": True,
                    },
                )
            )
            print(f"Model inventory checked: {monitor['provider_id']} ({len(model_ids)} IDs)")
        except Exception as exc:
            error = safe_error_summary(exc)
            warnings.append(f"{monitor['provider_id']}: {error}")
            store_snapshot(
                make_snapshot(
                    source_url=url,
                    status="failed",
                    body=b"",
                    page_title=monitor["title"],
                    parser_status="failed",
                    extracted_fields={"provider_id": monitor["provider_id"]},
                    error=error,
                )
            )
            print(f"WARNING: optional model inventory failed: {monitor['provider_id']}: {error}")
    return warnings


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Update free LLM API catalog.")
    parser.add_argument("--offline", action="store_true", help="Do not make network requests.")
    parser.add_argument(
        "--skip-optional-apis",
        action="store_true",
        help="Skip authenticated model-list checks for providers with configured API keys.",
    )
    parser.add_argument("--catalog", type=Path, default=CATALOG_PATH)
    args = parser.parse_args(argv)

    records = normalize_existing(load_catalog(args.catalog))
    records = merge_records(records, build_manual_records())
    records, openrouter_status = update_openrouter(records, offline=args.offline)
    optional_warnings: list[str] = []
    if not args.offline and not args.skip_optional_apis:
        optional_warnings = update_optional_model_inventories()
    write_catalog(records, args.catalog)
    active_free_models = sum(
        1 for record in records
        if record.get("record_level") == "model"
        and record.get("is_recommended") is True
        and record.get("verification_status") == "active"
    )
    print(
        f"Wrote {len(records)} records; {active_free_models} recommended model records; "
        f"OpenRouter update={openrouter_status}; optional API warnings={len(optional_warnings)}"
    )
    if openrouter_status == "failed":
        print("WARNING: OpenRouter data was retained as stale and excluded from current recommendations.")
    github_output = os.getenv("GITHUB_OUTPUT", "")
    if github_output:
        with Path(github_output).open("a", encoding="utf-8") as output_file:
            output_file.write(f"openrouter_status={openrouter_status}\n")
            output_file.write(f"source_failures={len(optional_warnings) + (openrouter_status == 'failed')}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
