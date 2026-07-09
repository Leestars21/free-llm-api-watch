from __future__ import annotations

import sys
import unittest
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "scripts"))

from catalog_schema import ENUMS, REQUIRED_FIELDS, load_catalog  # noqa: E402
from validate_catalog import validate_catalog  # noqa: E402


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


if __name__ == "__main__":
    unittest.main()
