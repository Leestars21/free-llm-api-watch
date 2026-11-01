from __future__ import annotations

import copy
import re
import sys
import unittest
from pathlib import Path
from urllib.parse import urlsplit


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "scripts"))

from catalog_schema import load_catalog  # noqa: E402
from render_docs import free_counts, render_readme, render_readme_en  # noqa: E402


class RenderedDocsTests(unittest.TestCase):
    def test_readme_is_navigation_not_a_full_model_dump(self) -> None:
        readme = (PROJECT_ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("#free-api-quick-lookup", readme)
        self.assertIn("#recurring-free-api", readme)
        self.assertIn("#new-user-credits", readme)
        self.assertIn("#limited-time-offers", readme)
        self.assertIn("#find-by-use-case", readme)
        self.assertIn("#find-by-model-family", readme)
        self.assertNotIn("whisper-large-v3", readme)
        self.assertNotIn("rerank-v4.0-fast", readme)
        self.assertNotIn("embed-v4.0", readme)
        self.assertNotIn("。；有效期", readme)
        self.assertIn("docs/related-ai-apis.md", readme)
        self.assertIn("docs/free-models.md", readme)
        self.assertLess(len(readme.splitlines()), 250)

    def test_all_local_readme_links_and_anchors_resolve(self) -> None:
        for readme_path in (PROJECT_ROOT / "README.md", PROJECT_ROOT / "README.en.md"):
            with self.subTest(readme=readme_path.name):
                readme = readme_path.read_text(encoding="utf-8")
                anchors = set(re.findall(r'<a\s+id="([^"]+)"', readme))
                links = re.findall(r"\[[^\]]+\]\(([^)]+)\)", readme)
                self.assertTrue(links)
                for raw_target in links:
                    target = raw_target.strip("<>")
                    parsed = urlsplit(target)
                    if parsed.scheme or target.startswith("//"):
                        continue
                    if not parsed.path:
                        self.assertIn(parsed.fragment, anchors, msg=f"Missing {readme_path.name} anchor: {target}")
                        continue
                    local_path = (PROJECT_ROOT / parsed.path).resolve()
                    self.assertTrue(local_path.is_relative_to(PROJECT_ROOT.resolve()), msg=target)
                    self.assertTrue(local_path.exists(), msg=f"Missing link from {readme_path.name}: {target}")

    def test_readme_statistics_match_core_and_extension_records(self) -> None:
        records = load_catalog()
        counts = free_counts(records)
        readme_zh = (PROJECT_ROOT / "README.md").read_text(encoding="utf-8")
        readme_en = (PROJECT_ROOT / "README.en.md").read_text(encoding="utf-8")
        self.assertIn(f"| 核心免费 LLM（按平台 + Model ID 去重） | {counts['core_llm_models']} |", readme_zh)
        self.assertIn(f"| 相关 AI API 扩展 | {counts['related_ai_models']} |", readme_zh)
        self.assertIn(f"| Core free LLMs (unique provider + Model ID) | {counts['core_llm_models']} |", readme_en)
        self.assertIn(f"| Related AI API extensions | {counts['related_ai_models']} |", readme_en)
        self.assertIn("每月免费评估额度", readme_zh)
        self.assertIn("Monthly free evaluation allowance", readme_en)

    def test_bilingual_navigation_and_full_model_directories_match(self) -> None:
        readme_zh = (PROJECT_ROOT / "README.md").read_text(encoding="utf-8")
        readme_en = (PROJECT_ROOT / "README.en.md").read_text(encoding="utf-8")
        core_zh = (PROJECT_ROOT / "docs" / "free-models.md").read_text(encoding="utf-8")
        core_en = (PROJECT_ROOT / "docs" / "free-models.en.md").read_text(encoding="utf-8")
        extensions_zh = (PROJECT_ROOT / "docs" / "related-ai-apis.md").read_text(encoding="utf-8")
        extensions_en = (PROJECT_ROOT / "docs" / "related-ai-apis.en.md").read_text(encoding="utf-8")
        self.assertIn("#free-api-quick-lookup", readme_zh)
        self.assertIn("#free-api-quick-lookup", readme_en)
        for record in load_catalog():
            if record.get("record_level") != "model" or not record.get("is_recommended"):
                continue
            model_id = str(record["model_id"])
            if record.get("model_scope") == "core_llm":
                self.assertIn(model_id, core_zh)
                self.assertIn(model_id, core_en)
            elif record.get("model_scope") == "related_ai_api" and record.get("model_type") != "routing_alias":
                self.assertIn(model_id, extensions_zh)
                self.assertIn(model_id, extensions_en)
        self.assertNotIn("whisper-large-v3", core_zh)
        self.assertIn("whisper-large-v3", extensions_zh)
        self.assertIn("embed-v4.0", extensions_en)

    def test_capability_tags_do_not_duplicate_core_model_counts(self) -> None:
        records = load_catalog()
        before = free_counts(records)["core_llm_models"]
        model = next(row for row in records if row.get("record_level") == "model" and row.get("model_scope") == "core_llm")
        duplicate = copy.deepcopy(model)
        duplicate["capabilities"] = list(model.get("capabilities", [])) + ["reasoning", "code_generation"]
        after = free_counts(records + [duplicate])["core_llm_models"]
        self.assertEqual(before, after)

    def test_repository_workflow_is_linked_and_failure_gated(self) -> None:
        readme = (PROJECT_ROOT / "README.md").read_text(encoding="utf-8")
        workflow = PROJECT_ROOT / ".github" / "workflows" / "update-catalog.yml"
        self.assertIn(".github/workflows/update-catalog.yml", readme)
        self.assertTrue(workflow.exists())
        text = workflow.read_text(encoding="utf-8")
        updater = (PROJECT_ROOT / "scripts" / "update_catalog.py").read_text(encoding="utf-8")
        self.assertIn('cron: "0 0 * * *"', text)
        self.assertIn("python scripts/update_catalog.py", text)
        self.assertIn("steps.update.outputs.source_failures == '0'", text)
        self.assertIn("steps.update.outputs.source_failures != '0'", text)
        self.assertIn("GITHUB_OUTPUT", updater)
        self.assertIn('source_failures={len(optional_warnings) + (openrouter_status == \'failed\')}', updater)

    def test_readme_rendering_is_deterministic(self) -> None:
        records = load_catalog()
        self.assertEqual(render_readme(records), render_readme(records))
        self.assertEqual(render_readme_en(records), render_readme_en(records))


if __name__ == "__main__":
    unittest.main()
