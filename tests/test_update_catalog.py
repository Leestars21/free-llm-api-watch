from __future__ import annotations

import os
import sys
import tempfile
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
        self.assertEqual(offer_types["cohere-evaluation-key"], "monthly_evaluation_tier")
        self.assertEqual(offer_types["model-studio-new-user-model-quota"], "new_user_credit")
        self.assertEqual(offer_types["gemini-api-free-tier"], "stable_free_tier")
        self.assertEqual(offer_types["cerebras-developer-intro-promotion"], "trial_credit")
        self.assertEqual(offer_types["tokenhub-language-model-free-package-2026"], "limited_time_promotion")

    def test_legacy_model_types_are_migrated_and_unknown_directions_are_not_guessed(self) -> None:
        records = update_catalog.build_manual_records()
        self.assertFalse(any(row.get("model_type") in {"chat", "multimodal"} for row in records))
        tts = next(row for row in records if row.get("model_id") == "gemini-3.8-flash-tts")
        self.assertEqual(tts["model_scope"], "related_ai_api")
        self.assertEqual(tts["input_modalities"], ["text"])
        self.assertEqual(tts["output_modalities"], ["audio"])
        self.assertTrue(any(row.get("model_id") == "gemini-3.1-flash-lite" for row in records))
        self.assertTrue(any(row.get("model_id") == "north-mini-code-1.0" for row in records))

    def test_openrouter_model_type_uses_metadata_not_model_names(self) -> None:
        row = update_catalog.build_openrouter_record({
            "id": "vendor/vision-audio-chat",
            "name": "Vision Audio Chat",
            "pricing": {"prompt": "0", "completion": "0"},
            "architecture": {},
        }, "2026-11-02")
        self.assertEqual(row["model_type"], "unknown")
        self.assertEqual(row["model_scope"], "unknown")
        self.assertEqual(row["input_modalities"], [])
        self.assertEqual(row["output_modalities"], [])

    def test_openrouter_explicit_direction_and_exact_overrides(self) -> None:
        row = update_catalog.build_openrouter_record({
            "id": "vendor/text-image-model",
            "name": "Any name",
            "pricing": {"prompt": "0", "completion": "0"},
            "architecture": {"input_modalities": ["text", "image"], "output_modalities": ["text"]},
            "supported_parameters": ["tools", "response_format", "reasoning"],
        }, "2026-11-02")
        self.assertEqual(row["model_type"], "multimodal_llm")
        self.assertEqual(row["model_scope"], "core_llm")
        self.assertEqual(row["input_modalities"], ["image", "text"])
        self.assertEqual(row["output_modalities"], ["text"])
        self.assertEqual(row["tool_calling"], "supported")
        self.assertEqual(row["reasoning"], "unknown")
        music = update_catalog.build_openrouter_record({
            "id": "google/lyria-3-clip-preview:free",
            "pricing": {"prompt": "0", "completion": "0"},
            "architecture": {"input_modalities": ["text"], "output_modalities": ["audio"]},
        }, "2026-11-02")
        self.assertEqual(music["model_type"], "music_generation")
        self.assertEqual(music["model_scope"], "related_ai_api")
        image = update_catalog.build_openrouter_record({
            "id": "vendor/image-api",
            "pricing": {"prompt": "0", "completion": "0"},
            "architecture": {"input_modalities": ["text"], "output_modalities": ["image"]},
        }, "2026-11-02")
        self.assertEqual(image["model_type"], "image_generation")
        video = update_catalog.build_openrouter_record({
            "id": "vendor/video-api",
            "pricing": {"prompt": "0", "completion": "0"},
            "architecture": {"input_modalities": ["text"], "output_modalities": ["video"]},
        }, "2026-11-02")
        self.assertEqual(video["model_type"], "video_generation")

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

    def test_github_output_reports_source_failures_for_commit_gate(self) -> None:
        source_text = (PROJECT_ROOT / "data" / "free_api_catalog.json").read_text(encoding="utf-8")
        scenarios = (
            ("success", "ok", [], "0"),
            ("openrouter-failed", "failed", [], "1"),
            ("optional-source-failed", "ok", ["provider: timed out"], "1"),
        )

        with tempfile.TemporaryDirectory(prefix="catalog-workflow-") as temp_dir:
            temp_root = Path(temp_dir)
            for name, status, warnings, expected_failures in scenarios:
                with self.subTest(scenario=name):
                    catalog_path = temp_root / f"catalog-{name}.json"
                    output_path = temp_root / f"github-output-{name}.txt"
                    catalog_path.write_text(source_text, encoding="utf-8")

                    def keep_records(records, offline=False):
                        return records, status

                    with patch.dict(os.environ, {"GITHUB_OUTPUT": str(output_path)}):
                        with patch.object(update_catalog, "update_openrouter", side_effect=keep_records), patch.object(
                            update_catalog, "update_optional_model_inventories", return_value=warnings
                        ):
                            self.assertEqual(
                                update_catalog.main(["--catalog", str(catalog_path)]),
                                0,
                            )

                    outputs = dict(
                        line.split("=", maxsplit=1)
                        for line in output_path.read_text(encoding="utf-8").splitlines()
                    )
                    self.assertEqual(outputs["openrouter_status"], status)
                    self.assertEqual(outputs["source_failures"], expected_failures)

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
