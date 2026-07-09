# Codex 使用说明

## 本地更新流程

在 `free-llm-api-watch/` 目录中运行：

```powershell
python scripts/update_catalog.py
python scripts/validate_catalog.py
python scripts/score_models.py
python scripts/render_docs.py
python -m unittest discover -s tests -v
```

## 只处理项目目录

如果本项目位于更大的管理目录或 monorepo 中，所有命令都应先进入 `free-llm-api-watch/` 后执行。不要在父级目录创建 catalog、抓取输出或 GitHub Actions。

## GitHub Actions 模板

如果 `free-llm-api-watch/` 作为独立 GitHub 仓库发布，仓库内的 `.github/workflows/update-catalog.yml` 会每天 UTC 00:00 自动运行，也支持手动触发。

如果本项目仍作为大仓库子目录使用，不要直接修改父仓库根目录 `.github/workflows/`。模板位于：

```text
templates/github-actions/update-catalog.yml
```

要在父仓库启用自动更新，需要由用户把模板复制到父仓库根目录：

```text
.github/workflows/update-catalog.yml
```

如果本项目作为大仓库子目录使用，模板中的 `PROJECT_DIR` 应保持为 `free-llm-api-watch`，workflow 会在根目录 checkout 后进入该目录运行脚本。

## OpenAI-Compatible 配置模板

```env
OPENAI_API_KEY=your-provider-key
OPENAI_BASE_URL=https://openrouter.ai/api/v1
OPENAI_MODEL=provider/model:free
```

只有 `openai_compatible` 为 `yes` 或可接受 `partial` 的记录才适合直接使用 OpenAI-compatible 客户端。

## Anthropic Messages API 配置模板

```env
ANTHROPIC_API_KEY=your-anthropic-key
ANTHROPIC_BASE_URL=https://api.anthropic.com
ANTHROPIC_MODEL=claude-model-id
```

Anthropic Claude API 是协议参考源。没有官方免费 API 额度时，它应保持：

```json
{
  "free_type": "not_free_or_unverified",
  "record_level": "provider",
  "is_recommended": false,
  "recommendation_reason": "protocol reference only; no verified free API quota"
}
```
