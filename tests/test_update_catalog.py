from __future__ import annotations

import sys
import unittest
import urllib.error
from pathlib import Path
from unittest.mock import patch


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "scripts"))

import update_catalog  # noqa: E402
from catalog_schema import load_catalog, record_key  # noqa: E402
from render_docs import model_rows  # noqa: E402
from score_models import score_records  # noqa: E402
from validate_catalog import validate_relationships  # noqa: E402


class UpdateCatalogTests(unittest.TestCase):
    def test_openrouter_free_selector_requires_every_price_dimension_to_be_zero(self) -> None:
        self.assertTrue(
            update_catalog.is_free_openrouter_model(
                {"id": "vendor/free", "pricing": {"prompt": "0", "completion": "0", "image": "0"}}
            )
        )
        self.assertFalse(
            update_catalog.is_free_openrouter_model(
                {"id": "vendor/paid", "pricing": {"prompt": "0.0001", "completion": "0"}}
            )
        )
        self.assertFalse(
            update_catalog.is_free_openrouter_model(
                {"id": "vendor/hidden-fee:free", "pricing": {"prompt": "0", "completion": "0", "request": "0.01"}}
            )
        )
        self.assertFalse(
            update_catalog.is_free_openrouter_model(
                {"id": "vendor/suffix-only:free", "pricing": {"prompt": "0", "completion": "0.001"}}
            )
        )
        self.assertFalse(
            update_catalog.is_free_openrouter_model(
                {"id": "vendor/missing-price", "pricing": {"prompt": "0"}}
            )
        )

    def test_rate_limits_are_not_used_as_a_free_quota_or_price_signal(self) -> None:
        model = {
            "id": "vendor/no-price-data",
            "rate_limits": {"requests_per_minute": 20, "tokens_per_minute": 100000},
        }
        self.assertFalse(update_catalog.is_free_openrouter_model(model))
        offers = update_catalog.build_manual_records()
        openrouter_offer = next(
            row for row in offers
            if row.get("record_level") == "offer" and row.get("provider_id") == "openrouter"
        )
        self.assertNotIn("50 requests", str(openrouter_offer.get("free_quota", "")))
        self.assertEqual(openrouter_offer["rate_limits"]["requests_per_day"], 50)

    def test_trial_and_new_user_grants_keep_their_own_types(self) -> None:
        records = update_catalog.build_manual_records()
        offer_types = {
            row.get("offer_id"): row.get("free_type")
            for row in records if row.get("record_level") == "offer"
        }
        self.assertEqual(offer_types["cohere-evaluation-key"], "trial_credit")
        self.assertEqual(offer_types["model-studio-new-user-model-quota"], "new_user_credit")
        self.assertEqual(offer_types["gemini-api-free-tier"], "stable_free_tier")

    def test_manual_records_are_preserved_when_openrouter_fetch_fails(self) -> None:
        records = update_catalog.build_manual_records()
        old_openrouter = update_catalog.build_openrouter_record(
            {"id": "vendor/old-free", "name": "Old Free", "pricing": {"prompt": "0", "completion": "0"}},
            "2026-10-20",
        )
        old_openrouter["last_checked"] = "2026-10-20"
        old_openrouter["verified_at"] = "2026-10-20"
        records.append(old_openrouter)
        with patch.object(update_catalog, "request_json", side_effect=urllib.error.URLError("offline")), patch.object(
            update_catalog, "store_snapshot"
        ):
            updated, status = update_catalog.update_openrouter(records)

        self.assertEqual(status, "failed")
        manual_model = next(
            row for row in updated
            if row.get("provider_id") == "cohere" and row.get("model_id") == "command-a-03-2025"
        )
        self.assertEqual(manual_model["verification_status"], "active")
        retained = next(row for row in updated if row.get("model_id") == "vendor/old-free")
        self.assertEqual(retained["verification_status"], "stale")
        self.assertFalse(retained["is_recommended"])
        self.assertEqual(retained["last_checked"], "2026-10-20")

    def test_successful_update_is_deduplicated_and_withdraws_changed_pricing(self) -> None:
        records = update_catalog.build_manual_records()
        old_model = update_catalog.build_openrouter_record(
            {"id": "vendor/now-paid", "name": "Now Paid", "pricing": {"prompt": "0", "completion": "0"}},
            "2026-10-20",
        )
        old_model["last_checked"] = "2026-10-20"
        old_model["verified_at"] = "2026-10-20"
        records.extend([old_model, dict(old_model)])
        payload = {
            "data": [
                {"id": "vendor/new-free", "name": "New Free", "pricing": {"prompt": "0", "completion": "0"}},
                {"id": "vendor/now-paid", "name": "Now Paid", "pricing": {"prompt": "0.01", "completion": "0.02"}},
            ]
        }
        with patch.object(update_catalog, "request_json", return_value=(payload, 200, b'{"data":[]}')), patch.object(
            update_catalog, "store_snapshot"
        ):
            updated, status = update_catalog.update_openrouter(records)

        self.assertEqual(status, "ok")
        keys = [record_key(row) for row in updated]
        self.assertEqual(len(keys), len(set(keys)))
        self.assertEqual(
            sum(1 for row in updated if row.get("model_id") == "vendor/new-free"),
            1,
        )
        paid = next(row for row in updated if row.get("model_id") == "vendor/now-paid")
        self.assertEqual(paid["verification_status"], "withdrawn")
        self.assertFalse(paid["is_recommended"])

    def test_identical_model_ids_from_different_providers_do_not_merge(self) -> None:
        records = [
            {"provider_id": "provider-a", "record_level": "model", "model_id": "same-name", "offer_id": "offer-a"},
            {"provider_id": "provider-b", "record_level": "model", "model_id": "same-name", "offer_id": "offer-b"},
        ]
        self.assertEqual(len(update_catalog.dedupe_records(records)), 2)

    def test_catalog_relationships_and_keys_are_valid(self) -> None:
        records = load_catalog()
        self.assertEqual(validate_relationships(records), [])
        keys = [record_key(row) for row in records]
        self.assertEqual(len(keys), len(set(keys)))

    def test_withdrawn_models_are_excluded_from_recommendation_rows(self) -> None:
        records = update_catalog.build_manual_records()
        withdrawn = next(row for row in records if row.get("model_id") == "glm-4.7-flash")
        withdrawn["verification_status"] = "withdrawn"
        withdrawn["is_recommended"] = False
        self.assertNotIn("glm-4.7-flash", {row["model_id"] for row in model_rows(records)})

    def test_scoring_does_not_invent_capabilities(self) -> None:
        rows = [{
            "record_level": "model",
            "coding_score_tier": "unknown",
            "reasoning_score_tier": "unknown",
            "long_context_score_tier": "unknown",
            "multimodal_score_tier": "unknown",
            "speed_tier": "unknown",
            "tool_calling": "unknown",
            "structured_output": "unknown",
            "reasoning": "unknown",
            "web_search": "unknown",
        }]
        score_records(rows)
        self.assertEqual(rows[0]["coding_score_tier"], "unknown")
        self.assertEqual(rows[0]["tool_calling"], "unknown")


if __name__ == "__main__":
    unittest.main()
