from __future__ import annotations

import sys
import unittest
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "scripts"))

from catalog_schema import ENUMS, REQUIRED_FIELDS, load_catalog, migrate_model_metadata  # noqa: E402
from validate_catalog import validate_catalog, validate_record  # noqa: E402


class CatalogSchemaTests(unittest.TestCase):
    def test_catalog_passes_validator(self) -> None:
        self.assertEqual(validate_catalog(), [])

    def test_required_fields_are_unique(self) -> None:
        self.assertEqual(len(REQUIRED_FIELDS), len(set(REQUIRED_FIELDS)))

    def test_enum_fields_do_not_store_template_strings(self) -> None:
        records = load_catalog()
        for index, record in enumerate(records):
            for field in ENUMS:
                value = record.get(field)
                self.assertNotIsInstance(
                    value if isinstance(value, str) and "/" in value else None,
                    str,
                    msg=f"record[{index}].{field} uses template string {value!r}",
                )

    def test_legacy_text_chat_migrates_without_changing_model_id(self) -> None:
        record = migrate_model_metadata({
            "record_level": "model",
            "model_id": "vendor/exact-id",
            "model_type": "chat",
            "modalities": ["text"],
        })
        self.assertEqual(record["model_id"], "vendor/exact-id")
        self.assertEqual(record["model_type"], "text_llm")
        self.assertEqual(record["model_scope"], "core_llm")
        self.assertEqual(record["input_modalities"], ["text"])
        self.assertEqual(record["output_modalities"], ["text"])

    def test_ambiguous_legacy_modalities_remain_unknown(self) -> None:
        record = migrate_model_metadata({
            "record_level": "model",
            "model_id": "vendor/uncertain",
            "model_type": "multimodal",
            "modalities": ["image", "text"],
        })
        self.assertEqual(record["model_type"], "unknown")
        self.assertEqual(record["model_scope"], "unknown")
        self.assertEqual(record["input_modalities"], [])
        self.assertEqual(record["output_modalities"], [])
        self.assertEqual(record["modalities"], ["image", "text"])

    def test_model_type_and_capability_tags_are_independent(self) -> None:
        records = load_catalog()
        north = next(row for row in records if row.get("model_id") == "north-mini-code-1.0")
        self.assertEqual(north["model_type"], "text_llm")
        self.assertEqual(set(north["capabilities"]), {"agent_workflows", "code_generation", "long_context"})

    def test_zero_price_model_rejects_nonzero_price_dimensions(self) -> None:
        records = load_catalog()
        free_model = next(row for row in records if row.get("record_level") == "model" and row.get("free_type") == "free_model")
        broken = dict(free_model)
        broken["model_pricing"] = {"input": "0", "output": "0.0001"}
        errors = validate_record(broken, 999)
        self.assertTrue(any("model_pricing.output" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
