from __future__ import annotations

import csv
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"
CATALOG_PATH = DATA_DIR / "free_api_catalog.json"
CATALOG_CSV_PATH = DATA_DIR / "free_api_catalog.csv"
SNAPSHOTS_PATH = DATA_DIR / "source_snapshots.json"

REQUIRED_FIELDS = [
    "provider",
    "record_level",
    "provider_id",
    "offer_id",
    "channel_type",
    "country_or_region",
    "official",
    "api_base",
    "openai_compatible",
    "anthropic_compatible",
    "free_type",
    "free_quota",
    "free_quota_unit",
    "quota_reset",
    "expires",
    "requires_card",
    "requires_identity_verification",
    "requires_phone_region",
    "model_id",
    "model_name",
    "model_scope",
    "model_type",
    "model_family",
    "context_window",
    "modalities",
    "input_modalities",
    "output_modalities",
    "capabilities",
    "capabilities_source_url",
    "model_pricing",
    "rate_limits",
    "quota_scope",
    "applies_to_models",
    "tool_calling",
    "structured_output",
    "reasoning",
    "web_search",
    "coding_score_tier",
    "reasoning_score_tier",
    "long_context_score_tier",
    "multimodal_score_tier",
    "speed_tier",
    "privacy_notes",
    "data_training_policy",
    "terms_risk",
    "source_type",
    "source_name",
    "source_url",
    "evidence_summary",
    "last_checked",
    "verified_at",
    "confidence",
    "verification_status",
    "data_origin",
    "is_recommended",
    "recommendation_reason",
    "fetch_status",
    "error_summary",
]

ENUMS = {
    "record_level": {"provider", "model", "offer"},
    "channel_type": {
        "official_model_vendor",
        "official_cloud_platform",
        "third_party_router",
        "third_party_inference_provider",
        "shadow_or_untrusted_api",
    },
    "openai_compatible": {"yes", "no", "partial", "unknown"},
    "anthropic_compatible": {"yes", "no", "partial", "unknown"},
    "free_type": {
        "stable_free_tier",
        "monthly_evaluation_tier",
        "new_user_credit",
        "trial_credit",
        "free_model",
        "free_router",
        "community_volunteer",
        "open_weight_only",
        "limited_time_promotion",
        "not_free_or_unverified",
    },
    "requires_card": {"yes", "no", "unknown"},
    "requires_identity_verification": {"yes", "no", "unknown"},
    "tool_calling": {"supported", "unsupported", "unknown"},
    "structured_output": {"supported", "unsupported", "unknown"},
    "reasoning": {"supported", "unsupported", "unknown"},
    "web_search": {"supported", "unsupported", "unknown"},
    "coding_score_tier": {"S", "S-", "A+", "A", "B", "unknown"},
    "reasoning_score_tier": {"S", "S-", "A+", "A", "B", "unknown"},
    "long_context_score_tier": {"S", "S-", "A+", "A", "B", "unknown"},
    "multimodal_score_tier": {"S", "S-", "A+", "A", "B", "unknown"},
    "speed_tier": {"fast", "medium", "slow", "unknown"},
    "data_training_policy": {"yes", "no", "opt_out", "unknown"},
    "source_type": {
        "official_docs",
        "official_api",
        "official_pricing",
        "official_changelog",
        "official_announcement",
        "independent_benchmark",
        "manual",
    },
    "confidence": {"high", "medium", "low"},
    "fetch_status": {"ok", "failed", "manual", "pending"},
    "verification_status": {"active", "stale", "withdrawn", "pending", "historical", "unverified"},
    "data_origin": {"manual", "official_api"},
    "quota_scope": {"provider_shared", "account_shared", "per_model", "per_user", "one_time", "unknown"},
    "model_scope": {"core_llm", "related_ai_api", "unknown"},
}

MODEL_TYPES = {
    "text_llm",
    "multimodal_llm",
    "embedding",
    "rerank",
    "speech_recognition",
    "speech_generation",
    "image_generation",
    "video_generation",
    "music_generation",
    "content_moderation",
    "classification",
    "routing_alias",
    "unknown",
}
CORE_LLM_TYPES = {"text_llm", "multimodal_llm"}
RELATED_AI_TYPES = MODEL_TYPES - CORE_LLM_TYPES - {"unknown"}
MODEL_CAPABILITIES = {
    "reasoning",
    "code_generation",
    "long_context",
    "image_understanding",
    "agent_workflows",
}
MODALITY_TYPES = {"text", "image", "audio", "video", "pdf", "embedding", "score", "label"}

RECOMMENDABLE_FREE_TYPES = {
    "stable_free_tier",
    "monthly_evaluation_tier",
    "new_user_credit",
    "trial_credit",
    "free_model",
    "free_router",
    "community_volunteer",
    "limited_time_promotion",
}

RECOMMENDABLE_SOURCE_TYPES = {
    "official_docs",
    "official_api",
    "official_pricing",
    "official_changelog",
    "official_announcement",
}

PROTOCOL_REFERENCE_IDS = {"openai-api", "anthropic-api"}

SNAPSHOT_REQUIRED_FIELDS = [
    "source_url",
    "fetched_at",
    "http_status",
    "page_title",
    "relevant_excerpt",
    "extracted_fields",
    "hash",
    "parser_status",
]


def today_utc() -> str:
    return datetime.now(timezone.utc).date().isoformat()


def now_utc() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def load_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    text = path.read_text(encoding="utf-8")
    if not text.strip():
        return default
    return json.loads(text)


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def load_catalog(path: Path = CATALOG_PATH) -> list[dict[str, Any]]:
    value = load_json(path, [])
    if not isinstance(value, list):
        raise ValueError(f"{path} must contain a JSON array")
    return value


def write_catalog(records: list[dict[str, Any]], path: Path = CATALOG_PATH) -> None:
    records = sorted(
        records,
        key=lambda r: (
            str(r.get("provider_id", "")),
            str(r.get("record_level", "")),
            str(r.get("model_id", "")),
            str(r.get("offer_id", "")),
        ),
    )
    write_json(path, records)
    write_catalog_csv(records)


def write_catalog_csv(
    records: list[dict[str, Any]], path: Path = CATALOG_CSV_PATH
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=REQUIRED_FIELDS,
            extrasaction="ignore",
            lineterminator="\n",
        )
        writer.writeheader()
        for record in records:
            row = dict(record)
            if isinstance(row.get("modalities"), list):
                row["modalities"] = "|".join(str(v) for v in row["modalities"])
            for field in ("model_pricing", "rate_limits", "applies_to_models"):
                if isinstance(row.get(field), (dict, list)):
                    row[field] = json.dumps(row[field], ensure_ascii=False, sort_keys=True)
            writer.writerow(row)


def empty_record(**overrides: Any) -> dict[str, Any]:
    record: dict[str, Any] = {
        "provider": "",
        "record_level": "provider",
        "provider_id": "",
        "offer_id": "",
        "channel_type": "third_party_inference_provider",
        "country_or_region": "",
        "official": False,
        "api_base": "",
        "openai_compatible": "unknown",
        "anthropic_compatible": "unknown",
        "free_type": "not_free_or_unverified",
        "free_quota": "",
        "free_quota_unit": "",
        "quota_reset": "",
        "expires": "",
        "requires_card": "unknown",
        "requires_identity_verification": "unknown",
        "requires_phone_region": "",
        "model_id": "",
        "model_name": "",
        "model_scope": "unknown",
        "model_type": "unknown",
        "model_family": "",
        "context_window": None,
        "modalities": [],
        "input_modalities": [],
        "output_modalities": [],
        "capabilities": [],
        "capabilities_source_url": "",
        "model_pricing": {},
        "rate_limits": {},
        "quota_scope": "unknown",
        "applies_to_models": [],
        "tool_calling": "unknown",
        "structured_output": "unknown",
        "reasoning": "unknown",
        "web_search": "unknown",
        "coding_score_tier": "unknown",
        "reasoning_score_tier": "unknown",
        "long_context_score_tier": "unknown",
        "multimodal_score_tier": "unknown",
        "speed_tier": "unknown",
        "privacy_notes": "",
        "data_training_policy": "unknown",
        "terms_risk": "",
        "source_type": "manual",
        "source_name": "",
        "source_url": "",
        "evidence_summary": "",
        "last_checked": today_utc(),
        "verified_at": today_utc(),
        "confidence": "low",
        "verification_status": "unverified",
        "data_origin": "manual",
        "is_recommended": False,
        "recommendation_reason": "",
        "fetch_status": "pending",
        "error_summary": "",
    }
    record.update(overrides)
    return record


def migrate_model_metadata(record: dict[str, Any]) -> dict[str, Any]:
    """Upgrade legacy model labels while preserving their model IDs."""
    if record.get("record_level") != "model":
        return record

    legacy_modalities = record.get("modalities")
    if not isinstance(legacy_modalities, list):
        legacy_modalities = []
    legacy_modalities = sorted({str(value).lower() for value in legacy_modalities})
    input_modalities = record.get("input_modalities")
    output_modalities = record.get("output_modalities")

    model_type = str(record.get("model_type") or "unknown")
    if model_type == "chat":
        # Legacy chat records with another modality do not say whether that
        # modality is input or output. Keep them unknown until source data is
        # reviewed instead of silently treating them as text-only LLMs.
        model_type = "unknown" if set(legacy_modalities) - {"text"} else "text_llm"
    elif model_type == "multimodal":
        # The legacy union field loses direction; a fresh source check must
        # supply input_modalities and output_modalities before promotion.
        model_type = "unknown"
    if model_type not in MODEL_TYPES:
        model_type = "unknown"

    record["model_type"] = model_type
    if model_type in CORE_LLM_TYPES:
        record["model_scope"] = "core_llm"
    elif model_type in RELATED_AI_TYPES:
        record["model_scope"] = "related_ai_api"
    else:
        record["model_scope"] = "unknown"

    if not isinstance(input_modalities, list) or not isinstance(output_modalities, list):
        input_modalities = input_modalities if isinstance(input_modalities, list) else []
        output_modalities = output_modalities if isinstance(output_modalities, list) else []
    if model_type in CORE_LLM_TYPES | RELATED_AI_TYPES and (
        not input_modalities or not output_modalities
    ):
        directions: tuple[list[str], list[str]] = ([], [])
        if model_type == "text_llm":
            directions = (["text"], ["text"])
        elif model_type == "multimodal_llm":
            directions = ([], [])
        elif model_type == "speech_recognition":
            directions = (["audio"], ["text"])
        elif model_type == "speech_generation":
            directions = (["text"], ["audio"])
        elif model_type == "embedding":
            directions = ([value for value in legacy_modalities if value in {"text", "image"}] or ["text"], ["embedding"])
        elif model_type == "rerank":
            directions = (["text"], ["score"])
        elif model_type == "content_moderation":
            directions = (["text"], ["label"])
        elif model_type == "music_generation":
            directions = (["text"], ["audio"])
        if not input_modalities:
            input_modalities = directions[0]
        if not output_modalities:
            output_modalities = directions[1]

    record["input_modalities"] = sorted({str(value).lower() for value in input_modalities})
    record["output_modalities"] = sorted({str(value).lower() for value in output_modalities})
    directional_union = set(record["input_modalities"]) | set(record["output_modalities"])
    record["modalities"] = sorted(directional_union or set(legacy_modalities))

    capabilities = record.get("capabilities")
    if not isinstance(capabilities, list):
        capabilities = []
    record["capabilities"] = sorted({str(value) for value in capabilities})
    record.setdefault("capabilities_source_url", "")
    return record


def record_key(record: dict[str, Any]) -> tuple[str, str, str, str]:
    return (
        str(record.get("provider_id", "")),
        str(record.get("record_level", "")),
        str(record.get("model_id", "")),
        str(record.get("offer_id", "")),
    )
