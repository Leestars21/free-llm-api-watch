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
    "model_family",
    "context_window",
    "modalities",
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
    "confidence",
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
        "new_user_credit",
        "trial_credit",
        "free_model",
        "free_router",
        "open_weight_only",
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
        "independent_benchmark",
        "manual",
    },
    "confidence": {"high", "medium", "low"},
    "fetch_status": {"ok", "failed", "manual", "pending"},
}

RECOMMENDABLE_FREE_TYPES = {
    "stable_free_tier",
    "new_user_credit",
    "trial_credit",
    "free_model",
    "free_router",
}

RECOMMENDABLE_SOURCE_TYPES = {
    "official_docs",
    "official_api",
    "official_pricing",
    "official_changelog",
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
        writer = csv.DictWriter(f, fieldnames=REQUIRED_FIELDS, extrasaction="ignore")
        writer.writeheader()
        for record in records:
            row = dict(record)
            if isinstance(row.get("modalities"), list):
                row["modalities"] = "|".join(str(v) for v in row["modalities"])
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
        "model_family": "",
        "context_window": None,
        "modalities": [],
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
        "confidence": "low",
        "is_recommended": False,
        "recommendation_reason": "",
        "fetch_status": "pending",
        "error_summary": "",
    }
    record.update(overrides)
    return record


def record_key(record: dict[str, Any]) -> tuple[str, str, str, str]:
    return (
        str(record.get("provider_id", "")),
        str(record.get("record_level", "")),
        str(record.get("model_id", "")),
        str(record.get("offer_id", "")),
    )
