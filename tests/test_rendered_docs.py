from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "scripts"))

from catalog_schema import load_catalog  # noqa: E402
from render_docs import free_counts  # noqa: E402


class RenderedDocsTests(unittest.TestCase):
    def test_readme_lists_every_recommended_record(self) -> None:
        readme = (PROJECT_ROOT / "README.md").read_text(encoding="utf-8")
        self.assertNotIn("仅显示前", readme)
        self.assertNotIn("完整数据见", readme)
        for record in load_catalog():
            if record.get("is_recommended"):
                marker = record.get("model_id") or record.get("offer_id") or record.get("provider_id")
                self.assertIn(str(marker), readme)

    def test_readme_lists_candidate_sources(self) -> None:
        readme = (PROJECT_ROOT / "README.md").read_text(encoding="utf-8")
        for provider in [
            "Google Gemini API / Google AI Studio",
            "GroqCloud",
            "Anthropic Claude API",
            "NVIDIA Build / API Catalog",
        ]:
            self.assertIn(provider, readme)

    def test_readme_contains_disclaimer_and_automation(self) -> None:
        readme = (PROJECT_ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("## 免责声明", readme)
        self.assertIn(".github/workflows/update-catalog.yml", readme)
        self.assertIn("每天 UTC 00:00", readme)

    def test_bilingual_readme_statistics_match_catalog(self) -> None:
        records = load_catalog()
        counts = free_counts(records)
        readme_zh = (PROJECT_ROOT / "README.md").read_text(encoding="utf-8")
        readme_en = (PROJECT_ROOT / "README.en.md").read_text(encoding="utf-8")
        self.assertIn(f"| 监控提供商 | {counts['monitored_providers']} |", readme_zh)
        self.assertIn(
            f"| 已确认有免费 API 或试用方案的提供商 | {counts['confirmed_providers']} |",
            readme_zh,
        )
        self.assertIn(
            f"| 提供新用户赠额或试用额度的平台 | {counts['credit_providers']} |",
            readme_zh,
        )
        self.assertIn(
            f"| Providers with a confirmed free API or trial offer | {counts['confirmed_providers']} |",
            readme_en,
        )
        self.assertIn(
            f"| Providers with a new-user grant or trial credit | {counts['credit_providers']} |",
            readme_en,
        )
        self.assertIn(
            f"| Model records with confirmed free access | {counts['free_models']} |",
            readme_en,
        )

    def test_offer_translations_and_bilingual_tables_are_complete(self) -> None:
        records = load_catalog()
        translations = json.loads(
            (PROJECT_ROOT / "data" / "translations_zh.json").read_text(encoding="utf-8")
        )
        active_offer_ids = {
            str(record.get("offer_id"))
            for record in records
            if record.get("record_level") == "offer"
            and record.get("is_recommended")
            and record.get("verification_status") == "active"
        }
        self.assertLessEqual(active_offer_ids, set(translations["offers"]))

        readme_zh = (PROJECT_ROOT / "README.md").read_text(encoding="utf-8")
        readme_en = (PROJECT_ROOT / "README.en.md").read_text(encoding="utf-8")
        models_zh_path = PROJECT_ROOT / "docs" / "free-models.md"
        models_en_path = PROJECT_ROOT / "docs" / "free-models.en.md"
        self.assertTrue(models_zh_path.exists())
        self.assertTrue(models_en_path.exists())
        models_zh = models_zh_path.read_text(encoding="utf-8")
        models_en = models_en_path.read_text(encoding="utf-8")
        self.assertEqual(readme_zh.count("| 平台 | 免费类型 |"), 1)
        self.assertEqual(readme_en.count("| Provider | Free type |"), 1)
        self.assertIn("Orpheus Arabic Saudi", readme_en)
        self.assertIn("音频秒/小时", readme_zh)
        self.assertNotIn("Monthly starter usage credits", readme_zh)
        for record in load_catalog():
            if record.get("record_level") == "model" and record.get("is_recommended"):
                self.assertIn(str(record["model_id"]), models_zh)
                self.assertIn(str(record["model_id"]), models_en)
        self.assertIn("免费资格", models_zh)
        self.assertIn("Quota unit", models_en)
        self.assertNotIn("free-plan access with model rate limits", models_zh)

    def test_standalone_workflow_exists(self) -> None:
        workflow = PROJECT_ROOT / ".github" / "workflows" / "update-catalog.yml"
        self.assertTrue(workflow.exists())
        text = workflow.read_text(encoding="utf-8")
        self.assertIn('cron: "0 0 * * *"', text)
        self.assertIn("python scripts/update_catalog.py", text)


if __name__ == "__main__":
    unittest.main()
