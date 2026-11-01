from __future__ import annotations

import argparse
from datetime import date
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Any

from catalog_schema import (
    CATALOG_PATH,
    CORE_LLM_TYPES,
    ENUMS,
    MODEL_CAPABILITIES,
    MODEL_TYPES,
    MODALITY_TYPES,
    PROTOCOL_REFERENCE_IDS,
    RECOMMENDABLE_FREE_TYPES,
    RECOMMENDABLE_SOURCE_TYPES,
    RELATED_AI_TYPES,
    REQUIRED_FIELDS,
    SNAPSHOT_REQUIRED_FIELDS,
    SNAPSHOTS_PATH,
    load_catalog,
    load_json,
    record_key,
)


def validate_record(record: dict[str, Any], index: int) -> list[str]:
    errors: list[str] = []
    label = f"record[{index}]"

    for field in REQUIRED_FIELDS:
        if field not in record:
            errors.append(f"{label}: missing required field {field}")

    for field, allowed in ENUMS.items():
        value = record.get(field)
        if value not in allowed:
            errors.append(f"{label}.{field}: expected one of {sorted(allowed)}, got {value!r}")
        if isinstance(value, str) and "/" in value:
            errors.append(
                f"{label}.{field}: looks like an enum template string, choose one concrete value"
            )

    if not isinstance(record.get("official"), bool):
        errors.append(f"{label}.official: must be boolean")
    if not isinstance(record.get("is_recommended"), bool):
        errors.append(f"{label}.is_recommended: must be boolean")
    modalities = record.get("modalities")
    if not isinstance(modalities, list) or any(value not in MODALITY_TYPES for value in modalities):
        errors.append(f"{label}.modalities: must be a list of supported modality labels")
    for field in ("input_modalities", "output_modalities"):
        values = record.get(field)
        if not isinstance(values, list) or any(value not in MODALITY_TYPES for value in values):
            errors.append(f"{label}.{field}: must be a list of supported modality labels")
    capabilities = record.get("capabilities")
    if not isinstance(capabilities, list) or any(value not in MODEL_CAPABILITIES for value in capabilities):
        errors.append(f"{label}.capabilities: must be a list of supported capability tags")
    if not isinstance(record.get("model_pricing"), dict):
        errors.append(f"{label}.model_pricing: must be an object")
    if not isinstance(record.get("rate_limits"), dict):
        errors.append(f"{label}.rate_limits: must be an object")
    applies_to_models = record.get("applies_to_models")
    if not isinstance(applies_to_models, list) or any(
        not isinstance(model_id, str) or not model_id for model_id in applies_to_models
    ):
        errors.append(f"{label}.applies_to_models: must be an array of non-empty model IDs")

    context_window = record.get("context_window")
    if context_window is not None and not isinstance(context_window, int):
        errors.append(f"{label}.context_window: must be integer or null")

    provider_id = str(record.get("provider_id", ""))
    if not provider_id:
        errors.append(f"{label}.provider_id: must not be empty")

    record_level = record.get("record_level")
    if record_level == "model" and not str(record.get("model_id", "")):
        errors.append(f"{label}.model_id: model-level records must set model_id")
    if record_level == "model":
        model_type = record.get("model_type")
        model_scope = record.get("model_scope")
        if model_type not in MODEL_TYPES:
            errors.append(f"{label}.model_type: unsupported model type {model_type!r}")
        expected_scope = (
            "core_llm" if model_type in CORE_LLM_TYPES
            else "related_ai_api" if model_type in RELATED_AI_TYPES
            else "unknown"
        )
        if model_scope != expected_scope:
            errors.append(f"{label}.model_scope: {model_type!r} must use {expected_scope!r}")
        if model_type in CORE_LLM_TYPES and (
            "text" not in record.get("input_modalities", [])
            or "text" not in record.get("output_modalities", [])
        ):
            errors.append(f"{label}: core LLMs must record text input and text output")
        input_values = record.get("input_modalities") if isinstance(record.get("input_modalities"), list) else []
        output_values = record.get("output_modalities") if isinstance(record.get("output_modalities"), list) else []
        modality_values = record.get("modalities") if isinstance(record.get("modalities"), list) else []
        if model_type == "multimodal_llm" and not (set(input_values) | set(output_values)) - {"text"}:
            errors.append(f"{label}: multimodal LLMs must record a non-text modality")
        directional_union = set(input_values) | set(output_values)
        if directional_union and set(modality_values) != directional_union:
            errors.append(f"{label}.modalities: must equal the input/output modality union")
        has_capability_claim = bool(record.get("capabilities")) or any(
            record.get(field) == "supported"
            for field in ("tool_calling", "structured_output", "reasoning", "web_search")
        )
        if has_capability_claim and not str(record.get("capabilities_source_url", "")).startswith(("https://", "http://")):
            errors.append(f"{label}.capabilities_source_url: required when capabilities are claimed")
    if record_level == "offer" and not str(record.get("offer_id", "")):
        errors.append(f"{label}.offer_id: offer-level records must set offer_id")

    last_checked = str(record.get("last_checked", ""))
    try:
        date.fromisoformat(last_checked)
    except ValueError:
        errors.append(f"{label}.last_checked: must be YYYY-MM-DD")
    verified_at = str(record.get("verified_at", ""))
    if verified_at:
        try:
            date.fromisoformat(verified_at)
        except ValueError:
            errors.append(f"{label}.verified_at: must be YYYY-MM-DD or empty when not verified")

    if not str(record.get("source_url", "")).startswith(("https://", "http://")):
        errors.append(f"{label}.source_url: must be an HTTP(S) URL")
    if not str(record.get("source_name", "")):
        errors.append(f"{label}.source_name: must not be empty")
    if not str(record.get("evidence_summary", "")):
        errors.append(f"{label}.evidence_summary: must not be empty")

    if record.get("fetch_status") == "failed":
        if record.get("confidence") != "low":
            errors.append(f"{label}: failed fetch records must have confidence low")
        if not str(record.get("error_summary", "")):
            errors.append(f"{label}: failed fetch records must include error_summary")
        if record.get("is_recommended") is not False:
            errors.append(f"{label}: failed fetch records must not be recommended")
        if record.get("verification_status") not in {"stale", "unverified"}:
            errors.append(f"{label}: failed fetch records must be stale or unverified")

    if record.get("is_recommended") is True:
        if record.get("confidence") not in {"high", "medium"}:
            errors.append(f"{label}: recommended records require high or medium confidence")
        if record.get("free_type") not in RECOMMENDABLE_FREE_TYPES:
            errors.append(f"{label}: recommended records must have a real free/trial type")
        if record.get("source_type") not in RECOMMENDABLE_SOURCE_TYPES:
            errors.append(f"{label}: recommended records require official evidence source")
        if record.get("verification_status") != "active":
            errors.append(f"{label}: only active records may be recommended")
        if record.get("fetch_status") == "failed":
            errors.append(f"{label}: failed records may not be recommended")
        if not str(record.get("recommendation_reason", "")):
            errors.append(f"{label}: recommended records need recommendation_reason")

    if record_level == "model" and record.get("free_type") in {"free_model", "free_router"}:
        pricing = record.get("model_pricing", {})
        if isinstance(pricing, dict):
            for field in ("input", "output", "prompt", "completion", "image", "request", "cache_read", "cache_write", "audio", "video", "web_search"):
                if field in pricing:
                    try:
                        if Decimal(str(pricing[field])) != 0:
                            errors.append(
                                f"{label}.model_pricing.{field}: a fully free model cannot have a non-zero price"
                            )
                    except (InvalidOperation, TypeError, ValueError):
                        errors.append(
                            f"{label}.model_pricing.{field}: price must be numeric when present"
                        )

    if provider_id in PROTOCOL_REFERENCE_IDS:
        if record.get("record_level") != "provider":
            errors.append(f"{label}: protocol reference must be provider-level")
        if record.get("free_type") != "not_free_or_unverified":
            errors.append(f"{label}: protocol reference must not claim free quota")
        if record.get("is_recommended") is not False:
            errors.append(f"{label}: protocol reference must not be recommended")
        expected_reason = "protocol reference only; no verified free API quota"
        if record.get("recommendation_reason") != expected_reason:
            errors.append(f"{label}: protocol reference reason must be exact")

    return errors


def validate_snapshots(path: Path = SNAPSHOTS_PATH) -> list[str]:
    errors: list[str] = []
    snapshots = load_json(path, [])
    if not isinstance(snapshots, list):
        return [f"{path}: must contain a JSON array"]
    for index, snapshot in enumerate(snapshots):
        label = f"snapshot[{index}]"
        if not isinstance(snapshot, dict):
            errors.append(f"{label}: must be an object")
            continue
        for field in SNAPSHOT_REQUIRED_FIELDS:
            if field not in snapshot:
                errors.append(f"{label}: missing required field {field}")
        excerpt = str(snapshot.get("relevant_excerpt", ""))
        if len(excerpt) > 500:
            errors.append(f"{label}.relevant_excerpt: must be at most 500 characters")
        if "body" in snapshot or "html" in snapshot or "raw" in snapshot:
            errors.append(f"{label}: must not store full body/html/raw content")
    return errors


def validate_relationships(records: list[dict[str, Any]]) -> list[str]:
    errors: list[str] = []
    keys: dict[tuple[str, str, str, str], int] = {}
    providers: set[str] = set()
    offers: set[tuple[str, str]] = set()
    models: set[tuple[str, str]] = set()
    for index, record in enumerate(records):
        if not isinstance(record, dict):
            continue
        key = record_key(record)
        if key in keys:
            errors.append(f"record[{index}]: duplicate record key also used by record[{keys[key]}]")
        else:
            keys[key] = index
        if record.get("record_level") == "provider":
            providers.add(str(record.get("provider_id", "")))
        elif record.get("record_level") == "offer":
            offers.add((str(record.get("provider_id", "")), str(record.get("offer_id", ""))))
        elif record.get("record_level") == "model":
            models.add((str(record.get("provider_id", "")), str(record.get("model_id", ""))))

    for index, record in enumerate(records):
        if not isinstance(record, dict):
            continue
        provider_id = str(record.get("provider_id", ""))
        level = record.get("record_level")
        if level != "provider" and provider_id not in providers:
            errors.append(f"record[{index}]: provider_id {provider_id!r} has no provider record")
        offer_id = str(record.get("offer_id", ""))
        if level == "model" and offer_id and (provider_id, offer_id) not in offers:
            errors.append(f"record[{index}]: model references missing offer {provider_id}/{offer_id}")
        if level == "model" and not offer_id:
            errors.append(f"record[{index}]: model record must reference an offer_id")
        if level == "model" and offer_id and (provider_id, offer_id) in offers:
            offer = next(
                item for item in records
                if item.get("record_level") == "offer"
                and str(item.get("provider_id", "")) == provider_id
                and str(item.get("offer_id", "")) == offer_id
            )
            if record.get("is_recommended") is True:
                if offer.get("is_recommended") is not True or offer.get("verification_status") != "active":
                    errors.append(f"record[{index}]: recommended model must reference an active recommended offer")
                if record.get("free_type") != offer.get("free_type"):
                    errors.append(f"record[{index}]: recommended model free_type must match its linked offer")
                applicable_models = offer.get("applies_to_models", [])
                if applicable_models and str(record.get("model_id", "")) not in applicable_models:
                    errors.append(f"record[{index}]: recommended model is outside its linked offer's model scope")
        if level == "offer":
            for model_id in record.get("applies_to_models", []):
                if (provider_id, model_id) not in models:
                    errors.append(
                        f"record[{index}]: offer applies_to_models references missing model {provider_id}/{model_id}"
                    )
    return errors


def validate_catalog(path: Path = CATALOG_PATH) -> list[str]:
    records = load_catalog(path)
    errors: list[str] = []
    for index, record in enumerate(records):
        if not isinstance(record, dict):
            errors.append(f"record[{index}]: must be an object")
            continue
        errors.extend(validate_record(record, index))
    errors.extend(validate_relationships(records))
    errors.extend(validate_snapshots())
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate free LLM API catalog schema.")
    parser.add_argument("--catalog", type=Path, default=CATALOG_PATH)
    args = parser.parse_args()

    errors = validate_catalog(args.catalog)
    if errors:
        print("Catalog validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Catalog validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
