# Free LLM API Watch

[中文](README.md) | English

This project tracks free, trial, and low-cost frontier LLM channels that are usable through APIs. It covers official model-vendor APIs, official cloud model platforms, third-party model routers, and third-party inference providers. It does not track web-only or app-only free models unless they also provide API access.

## Core Rules

- Use official docs, official pricing pages, official rate-limit pages, official model-list APIs, official changelogs, or other first-party evidence for final catalog records.
- Third-party posts are leads only and must not enter recommendation tables without official evidence.
- Free quota records are separated into `provider`, `model`, and `offer` levels.
- Enum examples such as `yes/no/partial/unknown` are not data values; catalog records must use one concrete value.
- OpenAI API and Anthropic Claude API are protocol references only unless a verified official free API quota exists.
- `source_snapshots.json` stores short evidence summaries only, not full web pages or full pricing-page text.
- Fetch failures must not fabricate data.

## Local Update

```powershell
python scripts/update_catalog.py
python scripts/validate_catalog.py
python scripts/score_models.py
python scripts/render_docs.py
python -m unittest discover -s tests -v
```

## GitHub Actions

The workflow is provided as a template at:

```text
templates/github-actions/update-catalog.yml
```

It only runs after a user copies it to the repository root as `.github/workflows/update-catalog.yml`. If this project is used as a subdirectory in a larger repository, keep `PROJECT_DIR=free-llm-api-watch` or run `cd free-llm-api-watch` before executing the scripts.

## License

MIT License. See `LICENSE`.
