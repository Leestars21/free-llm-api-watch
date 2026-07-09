from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
from typing import Any

from catalog_schema import (
    CATALOG_PATH,
    ENUMS,
    PROTOCOL_REFERENCE_IDS,
    RECOMMENDABLE_FREE_TYPES,
    RECOMMENDABLE_SOURCE_TYPES,
    REQUIRED_FIELDS,
    SNAPSHOT_REQUIRED_FIELDS,
    SNAPSHOTS_PATH,
    load_catalog,
    load_json,
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
    if not isinstance(record.get("modalities"), list):
        errors.append(f"{label}.modalities: must be a list")

    context_window = record.get("context_window")
    if context_window is not None and not isinstance(context_window, int):
        errors.append(f"{label}.context_window: must be integer or null")

    provider_id = str(record.get("provider_id", ""))
    if not provider_id:
        errors.append(f"{label}.provider_id: must not be empty")

    record_level = record.get("record_level")
    if record_level == "model" and not str(record.get("model_id", "")):
        errors.append(f"{label}.model_id: model-level records must set model_id")
    if record_level == "offer" and not str(record.get("offer_id", "")):
        errors.append(f"{label}.offer_id: offer-level records must set offer_id")

    last_checked = str(record.get("last_checked", ""))
    try:
        date.fromisoformat(last_checked)
    except ValueError:
        errors.append(f"{label}.last_checked: must be YYYY-MM-DD")

    if not str(record.get("source_url", "")).startswith(("https://", "http://")):
        errors.append(f"{label}.source_url: must be an HTTP(S) URL")
    if not str(record.get("source_name", "")):
        errors.append(f"{label}.source_name: must not be empty")
    if not str(record.get("evidence_summary", "")):
        errors.append(f"{label}.evidence_summary: must not be empty")

    if record.get("fetch_status") == "failed":
        if record.get("confidence") != "low":
            errors.append(f"{label}: failed fetch records must have confidence low")
        if record.get("free_type") != "not_free_or_unverified":
            errors.append(
                f"{label}: failed fetch records must use free_type not_free_or_unverified"
            )
        if not str(record.get("error_summary", "")):
            errors.append(f"{label}: failed fetch records must include error_summary")

    if record.get("is_recommended") is True:
        if record.get("confidence") not in {"high", "medium"}:
            errors.append(f"{label}: recommended records require high or medium confidence")
        if record.get("free_type") not in RECOMMENDABLE_FREE_TYPES:
            errors.append(f"{label}: recommended records must have a real free/trial type")
        if record.get("source_type") not in RECOMMENDABLE_SOURCE_TYPES:
            errors.append(f"{label}: recommended records require official evidence source")
        if not str(record.get("recommendation_reason", "")):
            errors.append(f"{label}: recommended records need recommendation_reason")

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


def validate_catalog(path: Path = CATALOG_PATH) -> list[str]:
    records = load_catalog(path)
    errors: list[str] = []
    for index, record in enumerate(records):
        if not isinstance(record, dict):
            errors.append(f"record[{index}]: must be an object")
            continue
        errors.extend(validate_record(record, index))
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
