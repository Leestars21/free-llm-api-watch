from __future__ import annotations

import sys
import unittest
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "scripts"))

from catalog_schema import REQUIRED_FIELDS, SNAPSHOTS_PATH, load_catalog, load_json  # noqa: E402


class RequiredFieldsTests(unittest.TestCase):
    def test_all_records_have_required_fields(self) -> None:
        for index, record in enumerate(load_catalog()):
            missing = [field for field in REQUIRED_FIELDS if field not in record]
            self.assertEqual(missing, [], msg=f"record[{index}] missing fields")

    def test_recommended_records_are_not_low_confidence(self) -> None:
        for record in load_catalog():
            if record.get("is_recommended"):
                self.assertIn(record.get("confidence"), {"high", "medium"})
                self.assertNotEqual(record.get("free_type"), "not_free_or_unverified")

    def test_source_snapshots_are_summaries_only(self) -> None:
        for index, snapshot in enumerate(load_json(SNAPSHOTS_PATH, [])):
            self.assertLessEqual(
                len(str(snapshot.get("relevant_excerpt", ""))),
                500,
                msg=f"snapshot[{index}] excerpt too long",
            )
            forbidden = {"body", "html", "raw"}
            self.assertTrue(
                forbidden.isdisjoint(snapshot.keys()),
                msg=f"snapshot[{index}] stores raw content",
            )


if __name__ == "__main__":
    unittest.main()
