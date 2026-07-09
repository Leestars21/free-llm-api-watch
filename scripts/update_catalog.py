from __future__ import annotations

import argparse
import hashlib
import json
import os
import ssl
import urllib.error
import urllib.request
from decimal import Decimal, InvalidOperation
from typing import Any

from catalog_schema import (
    PROTOCOL_REFERENCE_IDS,
    SNAPSHOTS_PATH,
    empty_record,
    load_catalog,
    load_json,
    now_utc,
    record_key,
    today_utc,
    write_catalog,
    write_json,
)


OPENROUTER_MODELS_URL = "https://openrouter.ai/api/v1/models"

CANDIDATE_PROVIDER_SOURCES = [
    {
        "provider_id": "google-gemini",
        "provider": "Google Gemini API / Google AI Studio",
        "channel_type": "official_model_vendor",
        "country_or_region": "Global",
        "api_base": "https://generativelanguage.googleapis.com",
        "openai_compatible": "partial",
        "anthropic_compatible": "no",
        "source_name": "Google Gemini API pricing",
        "source_url": "https://ai.google.dev/gemini-api/docs/pricing",
        "note": "candidate source; verify official Free Tier, rate limits, region and card requirements",
    },
    {
        "provider_id": "mistral",
        "provider": "Mistral La Plateforme",
        "channel_type": "official_model_vendor",
        "country_or_region": "EU/Global",
        "api_base": "https://api.mistral.ai",
        "openai_compatible": "partial",
        "anthropic_compatible": "no",
        "source_name": "Mistral documentation",
        "source_url": "https://docs.mistral.ai/",
        "note": "candidate source; verify whether any free or trial API quota is currently available",
    },
    {
        "provider_id": "groqcloud",
        "provider": "GroqCloud",
        "channel_type": "official_model_vendor",
        "country_or_region": "US/Global",
        "api_base": "https://api.groq.com/openai/v1",
        "openai_compatible": "yes",
        "anthropic_compatible": "no",
        "source_name": "GroqCloud rate limits",
        "source_url": "https://console.groq.com/docs/rate-limits",
        "note": "candidate source; verify developer free limits and supported model list",
    },
    {
        "provider_id": "cerebras",
        "provider": "Cerebras Inference",
        "channel_type": "official_model_vendor",
        "country_or_region": "US/Global",
        "api_base": "https://api.cerebras.ai/v1",
        "openai_compatible": "yes",
        "anthropic_compatible": "no",
        "source_name": "Cerebras Inference docs",
        "source_url": "https://inference-docs.cerebras.ai/",
        "note": "candidate source; verify free or trial quota before recommending",
    },
    {
        "provider_id": "cloudflare-workers-ai",
        "provider": "Cloudflare Workers AI",
        "channel_type": "official_cloud_platform",
        "country_or_region": "Global",
        "api_base": "https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/run",
        "openai_compatible": "partial",
        "anthropic_compatible": "no",
        "source_name": "Cloudflare Workers AI pricing",
        "source_url": "https://developers.cloudflare.com/workers-ai/platform/pricing/",
        "note": "candidate source; verify free allocation, account requirements, and model pricing",
    },
    {
        "provider_id": "alibaba-model-studio",
        "provider": "Alibaba Cloud Model Studio / Qwen",
        "channel_type": "official_cloud_platform",
        "country_or_region": "China/Global",
        "api_base": "https://dashscope.aliyuncs.com/compatible-mode/v1",
        "openai_compatible": "yes",
        "anthropic_compatible": "no",
        "source_name": "Alibaba Cloud Model Studio models",
        "source_url": "https://help.aliyun.com/zh/model-studio/models",
        "note": "candidate source; verify credit, validity period, identity and region requirements",
    },
    {
        "provider_id": "tencent-tokenhub-hunyuan",
        "provider": "Tencent Cloud TokenHub / Hunyuan",
        "channel_type": "official_cloud_platform",
        "country_or_region": "China",
        "api_base": "",
        "openai_compatible": "unknown",
        "anthropic_compatible": "unknown",
        "source_name": "Tencent Cloud TokenHub docs",
        "source_url": "https://cloud.tencent.com/document/product/1729",
        "note": "candidate source; verify API base, compatibility, free quota and identity requirements",
    },
    {
        "provider_id": "volcengine-ark",
        "provider": "Volcengine Ark / Doubao",
        "channel_type": "official_cloud_platform",
        "country_or_region": "China",
        "api_base": "https://ark.cn-beijing.volces.com/api/v3",
        "openai_compatible": "yes",
        "anthropic_compatible": "no",
        "source_name": "Volcengine Ark docs",
        "source_url": "https://www.volcengine.com/docs/82379",
        "note": "candidate source; verify trial/new-user credit, model IDs and endpoint",
    },
    {
        "provider_id": "zhipu-bigmodel",
        "provider": "Zhipu BigModel / GLM",
        "channel_type": "official_model_vendor",
        "country_or_region": "China",
        "api_base": "https://open.bigmodel.cn/api/paas/v4",
        "openai_compatible": "partial",
        "anthropic_compatible": "no",
        "source_name": "Zhipu BigModel docs",
        "source_url": "https://docs.bigmodel.cn/",
        "note": "candidate source; do not recommend without official free API quota evidence",
    },
    {
        "provider_id": "moonshot-kimi",
        "provider": "Moonshot / Kimi API",
        "channel_type": "official_model_vendor",
        "country_or_region": "China",
        "api_base": "https://api.moonshot.cn/v1",
        "openai_compatible": "yes",
        "anthropic_compatible": "no",
        "source_name": "Moonshot pricing docs",
        "source_url": "https://platform.moonshot.cn/docs/pricing/chat",
        "note": "candidate source; do not recommend without official free API quota evidence",
    },
    {
        "provider_id": "deepseek",
        "provider": "DeepSeek API",
        "channel_type": "official_model_vendor",
        "country_or_region": "China/Global",
        "api_base": "https://api.deepseek.com",
        "openai_compatible": "yes",
        "anthropic_compatible": "no",
        "source_name": "DeepSeek pricing docs",
        "source_url": "https://api-docs.deepseek.com/quick_start/pricing",
        "note": "candidate low-cost source; do not recommend as free without official free quota evidence",
    },
    {
        "provider_id": "baidu-qianfan",
        "provider": "Baidu Qianfan / ERNIE",
        "channel_type": "official_cloud_platform",
        "country_or_region": "China",
        "api_base": "https://qianfan.baidubce.com",
        "openai_compatible": "partial",
        "anthropic_compatible": "no",
        "source_name": "Baidu Qianfan docs",
        "source_url": "https://cloud.baidu.com/doc/WENXINWORKSHOP/",
        "note": "candidate source; verify free quota, identity, region and billing rules",
    },
    {
        "provider_id": "siliconflow",
        "provider": "SiliconFlow",
        "channel_type": "third_party_inference_provider",
        "country_or_region": "China/Global",
        "api_base": "https://api.siliconflow.cn/v1",
        "openai_compatible": "yes",
        "anthropic_compatible": "no",
        "source_name": "SiliconFlow docs",
        "source_url": "https://docs.siliconflow.cn/",
        "note": "candidate source; verify official free models, trial credit and account requirements",
    },
    {
        "provider_id": "huggingface-inference-providers",
        "provider": "Hugging Face Inference Providers",
        "channel_type": "third_party_inference_provider",
        "country_or_region": "Global",
        "api_base": "https://api-inference.huggingface.co",
        "openai_compatible": "partial",
        "anthropic_compatible": "no",
        "source_name": "Hugging Face Inference Providers docs",
        "source_url": "https://huggingface.co/docs/inference-providers",
        "note": "candidate source; distinguish open weights from free hosted API",
    },
    {
        "provider_id": "together-ai",
        "provider": "Together AI",
        "channel_type": "third_party_inference_provider",
        "country_or_region": "Global",
        "api_base": "https://api.together.xyz/v1",
        "openai_compatible": "yes",
        "anthropic_compatible": "no",
        "source_name": "Together AI docs",
        "source_url": "https://docs.together.ai/",
        "note": "P1 candidate source; verify new-user credit and low-cost models",
    },
    {
        "provider_id": "fireworks-ai",
        "provider": "Fireworks AI",
        "channel_type": "third_party_inference_provider",
        "country_or_region": "Global",
        "api_base": "https://api.fireworks.ai/inference/v1",
        "openai_compatible": "yes",
        "anthropic_compatible": "no",
        "source_name": "Fireworks AI docs",
        "source_url": "https://docs.fireworks.ai/",
        "note": "P1 candidate source; verify trial credit and pricing",
    },
    {
        "provider_id": "novita",
        "provider": "Novita",
        "channel_type": "third_party_inference_provider",
        "country_or_region": "Global",
        "api_base": "https://api.novita.ai/v3/openai",
        "openai_compatible": "yes",
        "anthropic_compatible": "no",
        "source_name": "Novita docs",
        "source_url": "https://novita.ai/docs",
        "note": "P1 candidate source; verify model pricing and credits",
    },
    {
        "provider_id": "replicate",
        "provider": "Replicate",
        "channel_type": "third_party_inference_provider",
        "country_or_region": "Global",
        "api_base": "https://api.replicate.com/v1",
        "openai_compatible": "partial",
        "anthropic_compatible": "no",
        "source_name": "Replicate docs",
        "source_url": "https://replicate.com/docs",
        "note": "P1 candidate source; model pricing varies and must be checked per model",
    },
    {
        "provider_id": "nebius-ai",
        "provider": "Nebius AI Studio",
        "channel_type": "third_party_inference_provider",
        "country_or_region": "Global/EU",
        "api_base": "https://api.studio.nebius.com/v1",
        "openai_compatible": "yes",
        "anthropic_compatible": "no",
        "source_name": "Nebius AI Studio docs",
        "source_url": "https://docs.nebius.com/studio/",
        "note": "P1 candidate source; verify API access, credit and pricing",
    },
    {
        "provider_id": "nvidia-build",
        "provider": "NVIDIA Build / API Catalog",
        "channel_type": "third_party_inference_provider",
        "country_or_region": "Global",
        "api_base": "https://integrate.api.nvidia.com/v1",
        "openai_compatible": "yes",
        "anthropic_compatible": "no",
        "source_name": "NVIDIA Build",
        "source_url": "https://build.nvidia.com/",
        "note": "P1 candidate source; verify free credits, endpoint and model terms",
    },
]

CANDIDATE_PROVIDER_IDS = {source["provider_id"] for source in CANDIDATE_PROVIDER_SOURCES}


def build_https_context() -> ssl.SSLContext:
    try:
        import certifi  # type: ignore

        return ssl.create_default_context(cafile=certifi.where())
    except Exception:
        return ssl.create_default_context()


def request_json(url: str, timeout: int = 30) -> tuple[dict[str, Any], int, bytes]:
    headers = {
        "Accept": "application/json",
        "User-Agent": "free-llm-api-watch/0.1 (+https://github.com/)",
    }
    if os.getenv("HTTP_REFERER"):
        headers["HTTP-Referer"] = os.environ["HTTP_REFERER"]
    if os.getenv("X_TITLE"):
        headers["X-Title"] = os.environ["X_TITLE"]
    request = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(request, timeout=timeout, context=build_https_context()) as response:
        body = response.read()
        status = getattr(response, "status", 200)
    return json.loads(body.decode("utf-8")), int(status), body


def decimal_is_zero(value: Any) -> bool:
    try:
        return Decimal(str(value)) == Decimal("0")
    except (InvalidOperation, TypeError, ValueError):
        return False


def is_free_openrouter_model(model: dict[str, Any]) -> bool:
    model_id = str(model.get("id", ""))
    pricing = model.get("pricing") or {}
    prompt_free = decimal_is_zero(pricing.get("prompt"))
    completion_free = decimal_is_zero(pricing.get("completion"))
    return model_id.endswith(":free") or (prompt_free and completion_free)


def infer_modalities(model: dict[str, Any]) -> list[str]:
    haystack = " ".join(
        [
            str(model.get("id", "")),
            str(model.get("name", "")),
            str((model.get("architecture") or {}).get("modality", "")),
        ]
    ).lower()
    modalities = ["text"]
    if any(token in haystack for token in ["image", "vision", "multimodal"]):
        modalities.append("image")
    if "audio" in haystack:
        modalities.append("audio")
    return sorted(set(modalities))


def family_from_openrouter_id(model_id: str) -> str:
    if "/" in model_id:
        return model_id.split("/", 1)[0]
    return "unknown"


def build_openrouter_record(model: dict[str, Any], checked: str) -> dict[str, Any]:
    model_id = str(model.get("id", ""))
    pricing = model.get("pricing") or {}
    context = model.get("context_length")
    try:
        context_window = int(context) if context is not None else None
    except (TypeError, ValueError):
        context_window = None

    free_quota = "Prompt and completion pricing reported as 0 by OpenRouter models API"
    if model_id.endswith(":free"):
        free_quota += "; model id is marked with :free"

    return empty_record(
        provider="OpenRouter",
        record_level="model",
        provider_id="openrouter",
        channel_type="third_party_router",
        country_or_region="Global",
        official=False,
        api_base="https://openrouter.ai/api/v1",
        openai_compatible="yes",
        anthropic_compatible="unknown",
        free_type="free_model",
        free_quota=free_quota,
        free_quota_unit="model_pricing",
        quota_reset="unknown",
        expires="unknown",
        requires_card="unknown",
        requires_identity_verification="unknown",
        model_id=model_id,
        model_name=str(model.get("name") or model_id),
        model_family=family_from_openrouter_id(model_id),
        context_window=context_window,
        modalities=infer_modalities(model),
        privacy_notes="Third-party routing; do not send sensitive data without reviewing OpenRouter and upstream provider terms.",
        terms_risk="Free routing and rate limits may change without notice; verify before production use.",
        source_type="official_api",
        source_name="OpenRouter models API",
        source_url=OPENROUTER_MODELS_URL,
        evidence_summary=(
            "OpenRouter official models API returned this model with zero prompt/completion pricing "
            f"(prompt={pricing.get('prompt')}, completion={pricing.get('completion')})."
        ),
        last_checked=checked,
        confidence="high",
        is_recommended=True,
        recommendation_reason=(
            "OpenRouter official models API reports zero prompt/completion price; verify rate limits "
            "and upstream terms before production use."
        ),
        fetch_status="ok",
    )


def build_openrouter_failure(error: str, checked: str) -> dict[str, Any]:
    return empty_record(
        provider="OpenRouter",
        record_level="provider",
        provider_id="openrouter",
        channel_type="third_party_router",
        country_or_region="Global",
        official=False,
        api_base="https://openrouter.ai/api/v1",
        openai_compatible="yes",
        anthropic_compatible="unknown",
        free_type="not_free_or_unverified",
        source_type="official_api",
        source_name="OpenRouter models API",
        source_url=OPENROUTER_MODELS_URL,
        evidence_summary="Fetch failed; no free API claim is made for this run.",
        last_checked=checked,
        confidence="low",
        is_recommended=False,
        recommendation_reason="fetch failed; manual review required",
        fetch_status="failed",
        error_summary=error[:300],
    )


def protocol_reference_records(checked: str) -> list[dict[str, Any]]:
    reason = "protocol reference only; no verified free API quota"
    return [
        empty_record(
            provider="OpenAI API",
            record_level="provider",
            provider_id="openai-api",
            channel_type="official_model_vendor",
            country_or_region="Global",
            official=True,
            api_base="https://api.openai.com/v1",
            openai_compatible="yes",
            anthropic_compatible="no",
            free_type="not_free_or_unverified",
            source_type="official_docs",
            source_name="OpenAI API reference",
            source_url="https://platform.openai.com/docs/api-reference",
            evidence_summary="Protocol reference record only; no free API quota is claimed.",
            last_checked=checked,
            confidence="medium",
            is_recommended=False,
            recommendation_reason=reason,
            fetch_status="manual",
        ),
        empty_record(
            provider="Anthropic Claude API",
            record_level="provider",
            provider_id="anthropic-api",
            channel_type="official_model_vendor",
            country_or_region="Global",
            official=True,
            api_base="https://api.anthropic.com",
            openai_compatible="no",
            anthropic_compatible="yes",
            free_type="not_free_or_unverified",
            source_type="official_docs",
            source_name="Anthropic Messages API",
            source_url="https://docs.anthropic.com/en/api/messages",
            evidence_summary="Protocol reference record only; no free API quota is claimed.",
            last_checked=checked,
            confidence="medium",
            is_recommended=False,
            recommendation_reason=reason,
            fetch_status="manual",
        ),
    ]


def candidate_provider_records(checked: str) -> list[dict[str, Any]]:
    records = []
    for source in CANDIDATE_PROVIDER_SOURCES:
        official = str(source["channel_type"]).startswith("official_")
        records.append(
            empty_record(
                provider=source["provider"],
                record_level="provider",
                provider_id=source["provider_id"],
                channel_type=source["channel_type"],
                country_or_region=source["country_or_region"],
                official=official,
                api_base=source["api_base"],
                openai_compatible=source["openai_compatible"],
                anthropic_compatible=source["anthropic_compatible"],
                free_type="not_free_or_unverified",
                privacy_notes="Candidate source only; review provider terms and privacy policy before sending sensitive data.",
                terms_risk="Free quota, trial credit, pricing, and rate limits are unverified by automated parsing.",
                source_type="manual",
                source_name=source["source_name"],
                source_url=source["source_url"],
                evidence_summary=(
                    "Candidate source from the monitored provider list. No automated parser has verified "
                    "an official free API quota for this provider-level record."
                ),
                last_checked=checked,
                confidence="low",
                is_recommended=False,
                recommendation_reason=source["note"],
                fetch_status="manual",
            )
        )
    return records


def source_snapshot(
    *,
    source_url: str,
    status: int | str,
    body: bytes,
    parser_status: str,
    extracted_fields: dict[str, Any],
    error: str = "",
) -> dict[str, Any]:
    excerpt = (
        "Official JSON API parsed for model metadata and pricing. "
        "Only summary metadata is stored; the full response body is not committed."
    )
    if error:
        excerpt = f"Fetch or parser failure: {error[:430]}"
    return {
        "source_url": source_url,
        "fetched_at": now_utc(),
        "http_status": status,
        "page_title": "OpenRouter models API",
        "relevant_excerpt": excerpt[:500],
        "extracted_fields": extracted_fields,
        "hash": hashlib.sha256(body).hexdigest() if body else "",
        "parser_status": parser_status,
    }


def update_openrouter(records: list[dict[str, Any]], offline: bool = False) -> list[dict[str, Any]]:
    checked = today_utc()
    kept = [
        r
        for r in records
        if not (
            r.get("provider_id") == "openrouter"
            or r.get("provider_id") in PROTOCOL_REFERENCE_IDS
            or r.get("provider_id") in CANDIDATE_PROVIDER_IDS
        )
    ]
    kept.extend(protocol_reference_records(checked))
    kept.extend(candidate_provider_records(checked))

    snapshots = load_json(SNAPSHOTS_PATH, [])

    if offline:
        kept.append(build_openrouter_failure("offline mode requested", checked))
        snapshots.append(
            source_snapshot(
                source_url=OPENROUTER_MODELS_URL,
                status="offline",
                body=b"",
                parser_status="skipped",
                extracted_fields={"reason": "offline mode requested"},
                error="offline mode requested",
            )
        )
        write_json(SNAPSHOTS_PATH, snapshots[-20:])
        return dedupe_records(kept)

    try:
        payload, status, body = request_json(OPENROUTER_MODELS_URL)
        models = payload.get("data", [])
        if not isinstance(models, list):
            raise ValueError("OpenRouter response field 'data' is not a list")
        free_models = [m for m in models if isinstance(m, dict) and is_free_openrouter_model(m)]
        kept.extend(build_openrouter_record(model, checked) for model in free_models)
        snapshots.append(
            source_snapshot(
                source_url=OPENROUTER_MODELS_URL,
                status=status,
                body=body,
                parser_status="ok",
                extracted_fields={
                    "total_model_count": len(models),
                    "free_model_count": len(free_models),
                    "selector": "id suffix :free OR prompt/completion pricing equal 0",
                },
            )
        )
    except Exception as exc:
        error = f"{type(exc).__name__}: {exc}"
        kept.append(build_openrouter_failure(error, checked))
        snapshots.append(
            source_snapshot(
                source_url=OPENROUTER_MODELS_URL,
                status="failed",
                body=b"",
                parser_status="failed",
                extracted_fields={"free_model_count": 0},
                error=error,
            )
        )

    write_json(SNAPSHOTS_PATH, snapshots[-20:])
    return dedupe_records(kept)


def dedupe_records(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    result: dict[tuple[str, str, str, str], dict[str, Any]] = {}
    for record in records:
        result[record_key(record)] = record
    return list(result.values())


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Update free LLM API catalog.")
    parser.add_argument("--offline", action="store_true", help="Do not make network requests.")
    args = parser.parse_args(argv)

    records = load_catalog()
    records = update_openrouter(records, offline=args.offline)
    write_catalog(records)
    print(f"Wrote {len(records)} catalog records")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
