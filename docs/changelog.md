# Changelog

## 2026-07-09

- Added a standalone GitHub Actions workflow for daily catalog updates after publishing this folder as its own repository.
- Added a disclaimer document and expanded README disclaimers.
- Added provider-level candidate records for monitored P0/P1 sources so uncertain providers are represented in the catalog as `not_free_or_unverified`.
- Expanded README and generated docs so recommendation tables are not truncated and uncertain P0/P1 sources are listed with user-judgement notes.
- Created the initial `free-llm-api-watch` project structure.
- Added provider/model/offer-level schema fields.
- Added enum validation to prevent template strings such as `yes/no/partial/unknown` from entering catalog data.
- Added OpenAI API and Anthropic Claude API as protocol-reference-only records in the update script.
- Added OpenRouter official models API fetcher for verified free model records.
- Added source snapshot constraints so only evidence summaries are stored.
- Added failure handling rule: no fabricated data on fetch failure.
- Added GitHub Actions workflow template under `templates/github-actions/` instead of creating root `.github/workflows/`.
