# Changelog

## 2026-11-01

- Expanded the evidence catalog with current official free/trial offers from Gemini, Groq, Cerebras, Cloudflare Workers AI, Alibaba Model Studio, Tencent TokenHub migration, Volcengine Ark, Zhipu, SiliconFlow, ModelScope, Hugging Face, Mistral, Cohere, Vercel AI Gateway, AI Horde, Replicate and Reka Vision.
- Added exact model records where current official sources state the ID and free scope, including Gemini 3.5 Flash-Lite / 3.8 Flash TTS, Cerebras `zai-glm-4.7`, Workers AI `@cf/zai-org/glm-4.7-flash` and `@cf/google/gemma-4-26b-a4b-it`, Zhipu `glm-4.7-flash`, Alibaba `qwen3.8-max`, Cohere chat/embedding/rerank IDs, and two Vercel AI Gateway free routes. Dynamic model catalogs remain explicitly account/live-list dependent.
- Added Ollama Cloud's documented monthly starter allowance while leaving its unpublished amount and account-visible eligible model set unspecified. Added Novita's exact zero-price Ling 3.1 Flash route and marked selected Ling 3.0 / Apodex 1.1 Mini routes as time-limited promotions; recorded Novita referral credits as conditional rather than an automatic signup grant.
- Added GroqCloud's current Free Plan limit-table models with exact per-model RPM/RPD/TPM/TPD or audio-second caps; these rate limits remain separate from token grants. The free-model IDs come from official docs, while no Groq authenticated model-list API was checked in this run.
- Reviewed SambaNova Cloud and DeepInfra current pricing: their standard API requests require paid credits/card or prepayment, so they remain in the inventory as reviewed providers without a confirmed general free inference offer.
- Added a Chinese localization map for quota, expiry, region, rate-limit and candidate-reason text. README and guides now show per-model limits, free-plan versus paid status, and a generated count for providers with new-user grants/trials; the English README keeps English headers and matched statistics.
- Recorded changed/retired policies: Zhipu's `glm-4.7-flash` replaces the older `glm-4.5-flash`; Tencent's legacy Hunyuan API platform closed 2026-09-30 and the new TokenHub credit is migration-only with no public amount; GitHub Models retired 2026-07-30; Together AI currently documents no free trial; Fireworks' old $1 credit was not confirmed by its current pricing page.
- Separated `free_quota` from `rate_limits`, added `verified_at`, quota scope, model type/pricing, model-to-offer relationships, evidence status and data origin.
- Replaced destructive OpenRouter refresh with merge/update semantics: strict zero-price checks, retries/timeouts, anomaly guard, stale retention on fetch failure, and withdrawal only after a successful complete response.
- Added optional authenticated inventory checks for Gemini, Groq, SiliconFlow, ModelScope, Cloudflare Workers AI and Cohere. These record model IDs only and never infer free access from model-list responses; missing credentials simply skip the source.
- Regenerated Chinese and English README statistics and provider/model/offer tables from catalog records. Updated guide, provider comparison and candidate-source docs.
- Updated both workflow copies to run the same checks but skip automatic commits if any source check fails. Workflow credentials are optional repository secrets; no secrets are stored in the repo. No commit or push was performed in this local task.
- Added regression coverage for price classification, rate-limit separation, trial types, relationships, manual-data preservation, failure handling, deduplication, withdrawal filtering, bilingual statistics and conservative capability scoring.

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
