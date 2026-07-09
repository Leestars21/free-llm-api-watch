from __future__ import annotations

import sys
import unittest
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "scripts"))

from catalog_schema import load_catalog  # noqa: E402


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

    def test_standalone_workflow_exists(self) -> None:
        workflow = PROJECT_ROOT / ".github" / "workflows" / "update-catalog.yml"
        self.assertTrue(workflow.exists())
        text = workflow.read_text(encoding="utf-8")
        self.assertIn('cron: "0 0 * * *"', text)
        self.assertIn("python scripts/update_catalog.py", text)


if __name__ == "__main__":
    unittest.main()
