# Free LLM API Watch

An evidence-based directory of free LLM API providers, including zero-priced models, recurring allowances, new-user grants and limited-time promotions. Model eligibility and quota details follow the linked official source and account console.

**Last reviewed: 2026-11-13** · [中文](README.md)

## Catalog statistics

| Metric | Count |
| --- | ---: |
| Monitored providers | 39 |
| Providers with a verified free offer | 21 |
| Core free LLMs (unique provider + Model ID) | 36 |
| Related AI API extensions | 13 |
| Core models explicitly priced at zero | 25 |

Counts include active, recommended records backed by official sources at medium/high confidence. Each Model ID is counted once per provider. Free quotas and rate limits are shown separately.

## Quick navigation

- [Free API provider lookup](#free-api-quick-lookup)
- [Recurring free API and periodic allowances](#recurring-free-api)
- [New-user credits and one-time trials](#new-user-credits)
- [Limited-time offers](#limited-time-offers)
- [Find models by use case](#find-by-use-case)
- [Find Qwen, GLM, Gemini, and DeepSeek](#find-by-model-family)
- [API setup example](#api-setup)
- [All core models](docs/free-models.en.md) · [Related AI API extensions](docs/related-ai-apis.en.md)
- [Updates and sources](#data-and-sources)

<a id="free-api-quick-lookup"></a>
## Free API provider lookup

One row per provider; at most three verified core LLMs are shown. If a provider uses a dynamic or account-only model catalog, the table says so instead of guessing a free model ID.

| Provider | Free method | Allowance / limit / validity | Representative free LLMs | Conditions | OpenAI SDK | Official details |
| --- | --- | --- | --- | --- | --- | --- |
| AI Horde / AI Horde OpenAI API | Volunteer community compute (dynamic queue) | No fixed token/request grant; free community inference at lowest anonymous priority; valid: Pilot service; scope may change | No specific free LLM confirmed; check the live catalog/account | Card no; identity unknown; region not stated | yes | [AI Horde OpenAI API docs](https://oai.aihorde.net/) |
| Alibaba Cloud Model Studio / Qwen | New-user grant / usage cap | Typically 1,000,000 tokens per eligible model; exact amount varies by model; valid: 90 days from the applicable model activation/release/approval date; se… | `qwen3.8-max` | Card unknown; identity yes; region Beijing region in China; verify the ident… | yes | [Model Studio new-user free quota](https://help.aliyun.com/zh/model-studio/new-free-quota/) |
| Baidu Qianfan / ERNIE | New-user grant / usage cap | 20 RMB new-user coupon; current official page says no usage threshold; valid: One month from issuance | No specific free LLM confirmed; check the live catalog/account | Card unknown; identity yes; region unknown | partial | [Baidu Qianfan new-user coupon](https://cloud.baidu.com/doc/Qianfan/index.html) |
| Cerebras Inference | One-time trial credit | $5 one-time promotional credit for 30 days; valid payment method required; no automatic billing; API pauses after expiry or exhaustion unless PayGo is sep… | No specific free LLM confirmed; check the live catalog/account | Card yes; identity unknown; region unknown | yes | [Cerebras current pricing](https://www.cerebras.ai/pricing) |
| Cloudflare Workers AI | Recurring free tier (usage/rate limits apply) | 10,000 Neurons/day; valid: No fixed end date published | `@cf/google/gemma-4-26b-a4b-it`, `@cf/zai-org/glm-4.7-flash` | Card unknown; identity unknown; region not stated | partial | [Workers AI pricing and changelog](https://developers.cloudflare.com/workers-ai/platform/pricing/) |
| Cohere API | Monthly free evaluation allowance | Up to 1,000 API calls/month shared across endpoints for eligible evaluation keys; model/endpoint RPM limits also apply; valid: Evaluation-key eligibility;… | `command-a-03-2025`, `command-r7b-12-2024`, `north-mini-code-1.0` | Card unknown; identity unknown; region not stated | partial | [Cohere rate limits and model access](https://docs.cohere.com/v2/docs/rate-limits) |
| Google Gemini API / Google AI Studio | Recurring free tier (usage/rate limits apply) | Model-specific $0 input/output pricing; per-project free-tier rate limits vary by model and account; valid: No fixed end date published; model/region elig… | `gemini-3.1-flash-lite`, `gemini-3.5-flash-lite` | Card no; identity unknown; region Availability varies by country/region | partial | [Gemini Developer API pricing and rate limits](https://ai.google.dev/gemini-api/docs/pricing) |
| GroqCloud | Recurring free tier (usage/rate limits apply) | Free Plan API usage is available at no charge within per-model rate limits; no separate token grant is documented; valid: No fixed end date stated; Free P… | `openai/gpt-oss-120b`, `openai/gpt-oss-20b`, `qwen/qwen3.8-27b` | Card unknown; identity unknown; region not stated | yes | [Groq Free Plan rate limits and supported models](https://console.groq.com/docs/rate-limits) |
| Hugging Face Inference Providers | Recurring free tier (usage/rate limits apply) | $0.10 monthly inference credit for free users, subject to change; valid: Credits renew subject to current Hugging Face policy; no independent per-model qu… | No specific free LLM confirmed; check the live catalog/account | Card unknown; identity unknown; region not stated | yes | [Inference Providers pricing](https://huggingface.co/docs/inference-providers/en/pricing) |
| Mistral La Plateforme | Recurring free tier (usage/rate limits apply) | Free mode with account-specific monthly usage budget; public numeric amount not stated; valid: No fixed end date published | No specific free LLM confirmed; check the live catalog/account | Card no; identity unknown; region not stated | partial | [Mistral free mode and usage limits](https://docs.mistral.ai/admin/billing-usage/usage-limits) |
| ModelScope Inference / 魔搭社区 | Recurring free tier (usage/rate limits apply) | 200 MoLi points/day per registered account; points are shared across platform usage; valid: Daily grant; accumulated balance/expiration terms can vary | No specific free LLM confirmed; check the live catalog/account | Card no; identity unknown; region not stated | yes | [ModelScope MoLi points announcement](https://www.modelscope.cn/posts/435591) |
| Novita AI | Limited-time promotion; Specific free model; New-user grant / usage cap | Model page currently lists input and output at $0 per million tokens as a launch promotion; valid: Launch promotion; end date not stated on reviewed page;… | `apodex/apodex-1.1-mini`, `inclusionai/ling-3.0-flash-fin`, `inclusionai/ling-3.0-flash-sante`; 2 more（[全部](docs/free-models.en.md)） | Card unknown; identity unknown; region not stated | yes | [Novita Apodex 1.1 Mini launch and pricing](https://blogs.novita.ai/apodex-1-1-mini-on-novita-ai-api-quickstart-pricing/) |
| Ollama Cloud | Recurring free tier (usage/rate limits apply) | Monthly starter usage credits for a smaller set of cloud models; exact amount is not published and is shown in the account. Free plan allows one concurren… | No specific free LLM confirmed; check the live catalog/account | Card unknown; identity unknown; region not stated | partial | [Ollama Cloud pricing](https://www.ollama.com/pricing) |
| OpenRouter | Free router model | No token grant; models listed with zero prompt/completion prices are free while listed; valid: Model free status may change without notice | `apodex/apodex-1.1-mini:free`, `baidu/ernie-5.5-flash-preview:free`, `cohere/north-mini-code:free`; 12 more（[全部](docs/free-models.en.md)） | Card unknown; identity unknown; region not stated | yes | [OpenRouter free model rate limits](https://openrouter.ai/collections/free-models) |
| Reka AI Vision API | One-time trial credit | 180 indexed-video minutes for eligible new users; valid: Trial terms shown at sign-up; expiry date not stated in reviewed pricing page | No specific free LLM confirmed; check the live catalog/account | Card unknown; identity unknown; region not stated | no | [Reka Vision API pricing](https://docs.reka.ai/vision/pricing) |
| Replicate | One-time trial credit | Selected models may be run free for a short evaluation period; amount not specified; valid: Free evaluation ends when the model prompts for billing setup | No specific free LLM confirmed; check the live catalog/account | Card unknown; identity unknown; region not stated | partial | [Replicate billing documentation](https://replicate.com/docs/topics/billing) |
| SiliconFlow | Specific free model | Model-specific free entries in the live model gallery; no universal platform-wide token grant; valid: Eligibility can change with the live model catalog | No specific free LLM confirmed; check the live catalog/account | Card unknown; identity yes; region not stated | yes | [SiliconFlow rate limits and model gallery](https://docs.siliconflow.cn/docs/userguide/faqs/rate-limit-and-upgradation) |
| Tencent Cloud TokenHub | Limited-time promotion; One-time trial credit | 1,000,000 free tokens per eligible language model; freezes $10 account balance/credit per model until endpoint deletion; valid: One year after claim; camp… | `deepseek-v4-flash`, `glm-5.3-flash` | Card unknown; identity unknown; region unknown; Card unknown; identity unknown; region not sta… | yes | [TokenHub free experience package terms](https://intl.cloud.tencent.com/zh/document/product/1300/80423) |
| Vercel AI Gateway | Recurring free tier (usage/rate limits apply) | $5 AI Gateway credit/month for eligible free-tier team accounts; valid: Free monthly credit no longer applies after purchasing credits | `inclusionai/ling-3.1-flash-1019`, `nvidia/nemotron-3.5-lightning-free` | Card yes; identity unknown; region not stated | yes | [Vercel AI Gateway pricing and live model catalog](https://vercel.com/docs/ai-gateway/pricing) |
| Volcengine Ark / Doubao | New-user grant / usage cap | Up to 500,000 free tokens as a usage cap in Safe Experience mode; separate model grants may differ; valid: Eligibility is limited to accounts that have no… | No specific free LLM confirmed; check the live catalog/account | Card unknown; identity unknown; region not stated | yes | [Ark Safe Experience mode](https://docs.volcengine.com/docs/ark/free-tokens-only-mode?lang=zh) |
| Zhipu BigModel / GLM | Specific free model | API input and output token pricing reported as free for glm-4.7-flash; request limits are not specified in the announcement; valid: No fixed end date stat… | `glm-4.7-flash` | Card unknown; identity unknown; region not stated | partial | [Zhipu GLM-4.7-Flash announcement](https://www.zhipuai.cn/zh/news/148) |

Free web chat, open model weights, API model visibility, and free API inference are different things. A credit is not a permanent free tier. Free plans can require rate limits, identity verification, a payment card, or regional eligibility. Check the conditions and official source before use.

<a id="recurring-free-api"></a>
## Recurring free API and periodic allowances

This group includes zero-priced models, recurring free tiers, daily points, and monthly evaluation allowances. A provider-level allowance does not prove every catalog model is free.

| Provider | Free method | Allowance / limit / validity | Representative free LLMs | Conditions | OpenAI SDK | Official details |
| --- | --- | --- | --- | --- | --- | --- |
| AI Horde / AI Horde OpenAI API | Volunteer community compute (dynamic queue) | No fixed token/request grant; free community inference at lowest anonymous priority; valid: Pilot service; scope may change | No specific free LLM confirmed; check the live catalog/account | Card no; identity unknown; region not stated | yes | [AI Horde OpenAI API docs](https://oai.aihorde.net/) |
| Cloudflare Workers AI | Recurring free tier (usage/rate limits apply) | 10,000 Neurons/day; valid: No fixed end date published | `@cf/google/gemma-4-26b-a4b-it`, `@cf/zai-org/glm-4.7-flash` | Card unknown; identity unknown; region not stated | partial | [Workers AI pricing and changelog](https://developers.cloudflare.com/workers-ai/platform/pricing/) |
| Cohere API | Monthly free evaluation allowance | Up to 1,000 API calls/month shared across endpoints for eligible evaluation keys; model/endpoint RPM limits also apply; valid: Evaluation-key eligibility;… | `command-a-03-2025`, `command-r7b-12-2024`, `north-mini-code-1.0` | Card unknown; identity unknown; region not stated | partial | [Cohere rate limits and model access](https://docs.cohere.com/v2/docs/rate-limits) |
| Google Gemini API / Google AI Studio | Recurring free tier (usage/rate limits apply) | Model-specific $0 input/output pricing; per-project free-tier rate limits vary by model and account; valid: No fixed end date published; model/region elig… | `gemini-3.1-flash-lite`, `gemini-3.5-flash-lite` | Card no; identity unknown; region Availability varies by country/region | partial | [Gemini Developer API pricing and rate limits](https://ai.google.dev/gemini-api/docs/pricing) |
| GroqCloud | Recurring free tier (usage/rate limits apply) | Free Plan API usage is available at no charge within per-model rate limits; no separate token grant is documented; valid: No fixed end date stated; Free P… | `openai/gpt-oss-120b`, `openai/gpt-oss-20b`, `qwen/qwen3.8-27b` | Card unknown; identity unknown; region not stated | yes | [Groq Free Plan rate limits and supported models](https://console.groq.com/docs/rate-limits) |
| Hugging Face Inference Providers | Recurring free tier (usage/rate limits apply) | $0.10 monthly inference credit for free users, subject to change; valid: Credits renew subject to current Hugging Face policy; no independent per-model qu… | No specific free LLM confirmed; check the live catalog/account | Card unknown; identity unknown; region not stated | yes | [Inference Providers pricing](https://huggingface.co/docs/inference-providers/en/pricing) |
| Mistral La Plateforme | Recurring free tier (usage/rate limits apply) | Free mode with account-specific monthly usage budget; public numeric amount not stated; valid: No fixed end date published | No specific free LLM confirmed; check the live catalog/account | Card no; identity unknown; region not stated | partial | [Mistral free mode and usage limits](https://docs.mistral.ai/admin/billing-usage/usage-limits) |
| ModelScope Inference / 魔搭社区 | Recurring free tier (usage/rate limits apply) | 200 MoLi points/day per registered account; points are shared across platform usage; valid: Daily grant; accumulated balance/expiration terms can vary | No specific free LLM confirmed; check the live catalog/account | Card no; identity unknown; region not stated | yes | [ModelScope MoLi points announcement](https://www.modelscope.cn/posts/435591) |
| Novita AI | Specific free model | Current model page lists input and output at $0 per million tokens; valid: Pricing can change; recheck the model page before use | `apodex/apodex-1.1-mini`, `inclusionai/ling-3.0-flash-fin`, `inclusionai/ling-3.0-flash-sante`; 2 more（[全部](docs/free-models.en.md)） | Card unknown; identity unknown; region not stated | yes | [Novita Ling 3.1 Flash model details](https://novita.ai/models/model-detail/inclusionai-ling-3.1-flash?from=pricing) |
| Ollama Cloud | Recurring free tier (usage/rate limits apply) | Monthly starter usage credits for a smaller set of cloud models; exact amount is not published and is shown in the account. Free plan allows one concurren… | No specific free LLM confirmed; check the live catalog/account | Card unknown; identity unknown; region not stated | partial | [Ollama Cloud pricing](https://www.ollama.com/pricing) |
| OpenRouter | Free router model | No token grant; models listed with zero prompt/completion prices are free while listed; valid: Model free status may change without notice | `apodex/apodex-1.1-mini:free`, `baidu/ernie-5.5-flash-preview:free`, `cohere/north-mini-code:free`; 12 more（[全部](docs/free-models.en.md)） | Card unknown; identity unknown; region not stated | yes | [OpenRouter free model rate limits](https://openrouter.ai/collections/free-models) |
| SiliconFlow | Specific free model | Model-specific free entries in the live model gallery; no universal platform-wide token grant; valid: Eligibility can change with the live model catalog | No specific free LLM confirmed; check the live catalog/account | Card unknown; identity yes; region not stated | yes | [SiliconFlow rate limits and model gallery](https://docs.siliconflow.cn/docs/userguide/faqs/rate-limit-and-upgradation) |
| Vercel AI Gateway | Recurring free tier (usage/rate limits apply) | $5 AI Gateway credit/month for eligible free-tier team accounts; valid: Free monthly credit no longer applies after purchasing credits | `inclusionai/ling-3.1-flash-1019`, `nvidia/nemotron-3.5-lightning-free` | Card yes; identity unknown; region not stated | yes | [Vercel AI Gateway pricing and live model catalog](https://vercel.com/docs/ai-gateway/pricing) |
| Zhipu BigModel / GLM | Specific free model | API input and output token pricing reported as free for glm-4.7-flash; request limits are not specified in the announcement; valid: No fixed end date stat… | `glm-4.7-flash` | Card unknown; identity unknown; region not stated | partial | [Zhipu GLM-4.7-Flash announcement](https://www.zhipuai.cn/zh/news/148) |

<a id="new-user-credits"></a>
## New-user credits and one-time trials

These offers may have eligibility rules, claim periods, or expiry dates. Keep them separate from recurring free access.

| Provider | Free method | Allowance / limit / validity | Representative free LLMs | Conditions | OpenAI SDK | Official details |
| --- | --- | --- | --- | --- | --- | --- |
| Alibaba Cloud Model Studio / Qwen | New-user grant / usage cap | Typically 1,000,000 tokens per eligible model; exact amount varies by model; valid: 90 days from the applicable model activation/release/approval date; se… | `qwen3.8-max` | Card unknown; identity yes; region Beijing region in China; verify the ident… | yes | [Model Studio new-user free quota](https://help.aliyun.com/zh/model-studio/new-free-quota/) |
| Baidu Qianfan / ERNIE | New-user grant / usage cap | 20 RMB new-user coupon; current official page says no usage threshold; valid: One month from issuance | No specific free LLM confirmed; check the live catalog/account | Card unknown; identity yes; region unknown | partial | [Baidu Qianfan new-user coupon](https://cloud.baidu.com/doc/Qianfan/index.html) |
| Cerebras Inference | One-time trial credit | $5 one-time promotional credit for 30 days; valid payment method required; no automatic billing; API pauses after expiry or exhaustion unless PayGo is sep… | No specific free LLM confirmed; check the live catalog/account | Card yes; identity unknown; region unknown | yes | [Cerebras current pricing](https://www.cerebras.ai/pricing) |
| Novita AI | New-user grant / usage cap | US$10 credit to each side for a successful referral; referrer rewards are capped at US$500; valid: Terms and credit expiry not stated on reviewed referral… | `apodex/apodex-1.1-mini`, `inclusionai/ling-3.0-flash-fin`, `inclusionai/ling-3.0-flash-sante`; 2 more（[全部](docs/free-models.en.md)） | Card unknown; identity unknown; region not stated | yes | [Novita referral program](https://novita.ai/referral/) |
| Reka AI Vision API | One-time trial credit | 180 indexed-video minutes for eligible new users; valid: Trial terms shown at sign-up; expiry date not stated in reviewed pricing page | No specific free LLM confirmed; check the live catalog/account | Card unknown; identity unknown; region not stated | no | [Reka Vision API pricing](https://docs.reka.ai/vision/pricing) |
| Replicate | One-time trial credit | Selected models may be run free for a short evaluation period; amount not specified; valid: Free evaluation ends when the model prompts for billing setup | No specific free LLM confirmed; check the live catalog/account | Card unknown; identity unknown; region not stated | partial | [Replicate billing documentation](https://replicate.com/docs/topics/billing) |
| Tencent Cloud TokenHub | One-time trial credit | Amount not stated in public announcement; valid: Three months after claim, according to announcement | `deepseek-v4-flash`, `glm-5.3-flash` | Card unknown; identity unknown; region not stated | yes | [Tencent Cloud migration announcement](https://cloud.tencent.com/announce/detail/2287) |
| Volcengine Ark / Doubao | New-user grant / usage cap | Up to 500,000 free tokens as a usage cap in Safe Experience mode; separate model grants may differ; valid: Eligibility is limited to accounts that have no… | No specific free LLM confirmed; check the live catalog/account | Card unknown; identity unknown; region not stated | yes | [Ark Safe Experience mode](https://docs.volcengine.com/docs/ark/free-tokens-only-mode?lang=zh) |

<a id="limited-time-offers"></a>
## Limited-time offers

Campaign end dates and eligible models can change. Expired records are removed from recommendations.

| Provider | Free method | Allowance / limit / validity | Representative free LLMs | Conditions | OpenAI SDK | Official details |
| --- | --- | --- | --- | --- | --- | --- |
| Novita AI | Limited-time promotion | Model page currently lists input and output at $0 per million tokens as a launch promotion; valid: Launch promotion; end date not stated on reviewed page;… | `apodex/apodex-1.1-mini`, `inclusionai/ling-3.0-flash-fin`, `inclusionai/ling-3.0-flash-sante`; 2 more（[全部](docs/free-models.en.md)） | Card unknown; identity unknown; region not stated | yes | [Novita Apodex 1.1 Mini launch and pricing](https://blogs.novita.ai/apodex-1-1-mini-on-novita-ai-api-quickstart-pricing/) |
| Tencent Cloud TokenHub | Limited-time promotion | 1,000,000 free tokens per eligible language model; freezes $10 account balance/credit per model until endpoint deletion; valid: One year after claim; camp… | `deepseek-v4-flash`, `glm-5.3-flash` | Card unknown; identity unknown; region unknown | yes | [TokenHub free experience package terms](https://intl.cloud.tencent.com/zh/document/product/1300/80423) |

<a id="find-by-use-case"></a>
## Find models by use case

Candidates are filtered using recorded official capability fields, modalities, and context windows. This is not a performance ranking. The long-context filter requires a documented context window of at least 100K tokens.

| Use case | Verified candidates |
| --- | --- |
| General text generation | [Model Studio new-user free quota example](https://help.aliyun.com/zh/model-studio/new-free-quota/) `qwen3.8-max`; [Cloudflare Workers AI model catalog](https://developers.cloudflare.com/workers-ai/models/) `@cf/google/gemma-4-26b-a4b-it`; [Workers AI GLM-4.7-Flash model page](https://developers.cloudflare.com/workers-ai/models/glm-4.7-flash/) `@cf/zai-org/glm-4.7-flash`; [Cohere models catalog](https://docs.cohere.com/v1/docs/models) `command-a-03-2025`; [Cohere models catalog](https://docs.cohere.com/v1/docs/models) `command-r7b-12-2024` |
| Reasoning | [Gemini 3.1 Flash-Lite model and pricing](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite) `gemini-3.1-flash-lite`; [Gemini 3.5 Flash-Lite model and pricing](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite) `gemini-3.5-flash-lite`; [Novita Apodex 1.1 Mini model details](https://novita.ai/models/model-detail/apodex-apodex-1.1-mini?from=pricing) `apodex/apodex-1.1-mini`; [Novita Ling 3.0 Flash Fin model details](https://novita.ai/models/model-detail/inclusionai-ling-3.0-flash-fin) `inclusionai/ling-3.0-flash-fin`; [Novita Ling 3.0 Flash Sante model details](https://novita.ai/models/model-detail/inclusionai-ling-3.0-flash-sante?from=pricing) `inclusionai/ling-3.0-flash-sante` |
| Code generation | [Cohere North Mini Code model](https://docs.cohere.com/docs/north-mini-code-1.0) `north-mini-code-1.0` |
| Tool use / agent workflows | [Workers AI GLM-4.7-Flash model page](https://developers.cloudflare.com/workers-ai/models/glm-4.7-flash/) `@cf/zai-org/glm-4.7-flash`; [Cohere North Mini Code model](https://docs.cohere.com/docs/north-mini-code-1.0) `north-mini-code-1.0`; [Gemini 3.1 Flash-Lite model and pricing](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite) `gemini-3.1-flash-lite`; [Gemini 3.5 Flash-Lite model and pricing](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite) `gemini-3.5-flash-lite`; [Groq Free Plan limits and supported models](https://console.groq.com/docs/rate-limits) `openai/gpt-oss-120b` |
| Long context (≥100K) | [Cohere North Mini Code model](https://docs.cohere.com/docs/north-mini-code-1.0) `north-mini-code-1.0`; [Gemini 3.1 Flash-Lite model and pricing](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite) `gemini-3.1-flash-lite`; [Gemini 3.5 Flash-Lite model and pricing](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite) `gemini-3.5-flash-lite`; [Groq Free Plan limits and supported models](https://console.groq.com/docs/rate-limits) `openai/gpt-oss-120b`; [Groq Free Plan limits and supported models](https://console.groq.com/docs/rate-limits) `openai/gpt-oss-20b` |
| Image understanding | [Gemini 3.1 Flash-Lite model and pricing](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite) `gemini-3.1-flash-lite`; [Gemini 3.5 Flash-Lite model and pricing](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite) `gemini-3.5-flash-lite`; [Novita Ling 3.0 Flash VL model details](https://novita.ai/models/model-detail/inclusionai-ling-3.0-flash-vl) `inclusionai/ling-3.0-flash-vl`; [OpenRouter models API](https://openrouter.ai/api/v1/models) `dots-studio/dots-3-note-preview:free`; [OpenRouter models API](https://openrouter.ai/api/v1/models) `google/gemma-4-26b-a4b-it:free` |
| Higher-volume use (published rate limits) | [Cohere North Mini Code model](https://docs.cohere.com/docs/north-mini-code-1.0) `north-mini-code-1.0` (RPM 20); [Groq Free Plan limits and supported models](https://console.groq.com/docs/rate-limits) `openai/gpt-oss-120b` (RPM 30, RPD 1000, TPM 8000, TPD 200000); [Groq Free Plan limits and supported models](https://console.groq.com/docs/rate-limits) `openai/gpt-oss-20b` (RPM 30, RPD 1000, TPM 8000, TPD 200000); [Groq Free Plan limits and supported models](https://console.groq.com/docs/rate-limits) `qwen/qwen3.8-27b` (RPM 30, RPD 1000, TPM 8000, TPD 200000) |

<a id="find-by-model-family"></a>
## Find Qwen, GLM, Gemini, and DeepSeek

Only models with a confirmed current free-access relationship appear here. Similar names or third-party availability do not establish free access.

| Provider | Exact Model ID | Model type | Free method | Free scope | Official source |
| --- | --- | --- | --- | --- | --- |
| Alibaba Cloud Model Studio / Qwen | qwen3.8-max | Text LLM | New-user grant / usage cap | Typically 1,000,000 tokens per eligible model; exact amount varies by model | [Model Studio new-user free quota example](https://help.aliyun.com/zh/model-studio/new-free-quota/) |
| Cloudflare Workers AI | @cf/zai-org/glm-4.7-flash | Text LLM | Recurring free tier (usage/rate limits apply) | 10,000 Neurons/day | [Workers AI GLM-4.7-Flash model page](https://developers.cloudflare.com/workers-ai/models/glm-4.7-flash/) |
| Google Gemini API / Google AI Studio | gemini-3.1-flash-lite | Multimodal LLM | Recurring free tier (usage/rate limits apply) | Model-specific $0 input/output pricing; per-project free-tier rate limits vary by model and account | [Gemini 3.1 Flash-Lite model and pricing](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite) |
| Google Gemini API / Google AI Studio | gemini-3.5-flash-lite | Multimodal LLM | Recurring free tier (usage/rate limits apply) | Model-specific $0 input/output pricing; per-project free-tier rate limits vary by model and account | [Gemini 3.5 Flash-Lite model and pricing](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite) |
| GroqCloud | qwen/qwen3.8-27b | Text LLM | Recurring free tier (usage/rate limits apply) | Free Plan API usage is available at no charge within per-model rate limits; no separate token grant is documented | [Groq Free Plan limits and supported models](https://console.groq.com/docs/rate-limits) |
| Tencent Cloud TokenHub | deepseek-v4-flash | Text LLM | Limited-time promotion | 1,000,000 tokens per model for one year after claim | [Tencent TokenHub DeepSeek V4 model guide](https://cloud.tencent.com/document/product/1823/132248) |
| Tencent Cloud TokenHub | glm-5.3-flash | Text LLM | Limited-time promotion | 1,000,000 tokens per model for one year after claim | [Tencent TokenHub model inventory](https://cloud.tencent.com/document/product/1823/130078) |
| Zhipu BigModel / GLM | glm-4.7-flash | Text LLM | Specific free model | API input and output token pricing reported as free for glm-4.7-flash; request limits are not specified in the announcement | [Zhipu GLM-4.7-Flash announcement](https://www.zhipuai.cn/zh/news/148) |

<a id="api-setup"></a>
## OpenAI-compatible API example

The [full core model directory](docs/free-models.en.md) lists exact API bases, compatibility, modalities, tool support, rate limits, and sources. Use the OpenAI SDK directly only where compatibility is marked “yes”; “partial” may not support every parameter.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["LLM_API_KEY"],
    base_url=os.environ["LLM_BASE_URL"],
)
response = client.chat.completions.create(
    model=os.environ["LLM_MODEL_ID"],
    messages=[{"role": "user", "content": "Explain uncertainty quantification in two sentences."}],
)
print(response.choices[0].message.content)
```

Use each provider's own API key, base URL, and exact Model ID. Never commit API keys. See the [API setup guide](docs/free-api-guide.md) for more details.

<a id="data-and-sources"></a>
## Updates and sources

- [Full core free model list](docs/free-models.en.md): exact IDs, access terms, rate limits, context, input/output modalities, capabilities, API base, sources, and review date.
- [Related AI API extensions](docs/related-ai-apis.en.md): embeddings, reranking, ASR, TTS, moderation, and image/video/music generation; excluded from core LLM counts.
- [Provider comparison](docs/provider-comparison.md) · [Candidate and historical sources](docs/candidate-sources.md) · [Changelog](docs/changelog.md) · [API guide](docs/free-api-guide.md)
- `data/manual_catalog.json` stores manually verified policy and model evidence; `data/free_api_catalog.json` is generated. A model-list endpoint proves existence, not free access.
- Failed updates retain automatic records for review and do not refresh manual policy dates. Automatic recommendations are withdrawn only after a successful complete response confirms removal or a paid price.
- [GitHub Actions workflow](.github/workflows/update-catalog.yml) runs updates, validation, scoring, documentation generation, and tests daily at 00:00 UTC. It skips automatic commits if any source check fails.

## Disclaimer and privacy

Prices, quotas, model routing, regions, rate limits, terms and data processing can change. Recheck the linked source before production use. Do not send sensitive material to a provider whose data practices you have not reviewed, and do not bypass terms, access controls, limits, identity checks or regional restrictions.

This catalog is not legal, security, procurement, privacy or compliance advice. See [privacy and risk](docs/privacy-and-risk.md), [disclaimer](docs/disclaimer.md), and the [free API guide](docs/free-api-guide.md).

## License

MIT License. See [LICENSE](LICENSE).
