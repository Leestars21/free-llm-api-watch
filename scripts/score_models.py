from __future__ import annotations

from catalog_schema import load_catalog, write_catalog


SCORE_FIELDS = [
    "coding_score_tier",
    "reasoning_score_tier",
    "long_context_score_tier",
    "multimodal_score_tier",
    "speed_tier",
]

CAPABILITY_FIELDS = [
    "tool_calling",
    "structured_output",
    "reasoning",
    "web_search",
]


def score_records(records: list[dict]) -> list[dict]:
    for record in records:
        # Do not infer benchmark capability without evidence. This pass only normalizes blanks.
        for field in SCORE_FIELDS:
            if not record.get(field):
                record[field] = "unknown"
        for field in CAPABILITY_FIELDS:
            if not record.get(field):
                record[field] = "unknown"
        if record.get("record_level") != "model":
            for field in SCORE_FIELDS:
                record[field] = "unknown"
    return records


def main() -> int:
    records = score_records(load_catalog())
    write_catalog(records)
    print(f"Scored {len(records)} records conservatively")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
