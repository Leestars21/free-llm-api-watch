# 免费 API 使用指南

更新时间：2026-07-21

## 推荐原则

推荐表只能展示同时满足以下条件的记录：

- 有官方证据；
- `confidence` 为 `high` 或 `medium`；
- `is_recommended` 为 `true`；
- 明确存在 API 免费额度、免费模型、免费路由或试用额度。

`confidence: low`、`not_free_or_unverified`、`protocol reference only` 的记录只能进入候补区或参考区。

## 官方免费 API 渠道

_暂无符合条件的记录。_

## 第三方免费模型

| Provider | Level | Model/Offer | Free type | Reason | Evidence |
| --- | --- | --- | --- | --- | --- |
| OpenRouter | model | cohere/north-mini-code:free | free_model | OpenRouter official models API reports zero prompt/completion price; verify rate limits and upstream terms before production use. | https://openrouter.ai/api/v1/models |
| OpenRouter | model | google/gemma-4-26b-a4b-it:free | free_model | OpenRouter official models API reports zero prompt/completion price; verify rate limits and upstream terms before production use. | https://openrouter.ai/api/v1/models |
| OpenRouter | model | google/gemma-4-31b-it:free | free_model | OpenRouter official models API reports zero prompt/completion price; verify rate limits and upstream terms before production use. | https://openrouter.ai/api/v1/models |
| OpenRouter | model | google/lyria-3-clip-preview | free_model | OpenRouter official models API reports zero prompt/completion price; verify rate limits and upstream terms before production use. | https://openrouter.ai/api/v1/models |
| OpenRouter | model | google/lyria-3-pro-preview | free_model | OpenRouter official models API reports zero prompt/completion price; verify rate limits and upstream terms before production use. | https://openrouter.ai/api/v1/models |
| OpenRouter | model | nvidia/nemotron-3-nano-30b-a3b:free | free_model | OpenRouter official models API reports zero prompt/completion price; verify rate limits and upstream terms before production use. | https://openrouter.ai/api/v1/models |
| OpenRouter | model | nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free | free_model | OpenRouter official models API reports zero prompt/completion price; verify rate limits and upstream terms before production use. | https://openrouter.ai/api/v1/models |
| OpenRouter | model | nvidia/nemotron-3-super-120b-a12b:free | free_model | OpenRouter official models API reports zero prompt/completion price; verify rate limits and upstream terms before production use. | https://openrouter.ai/api/v1/models |
| OpenRouter | model | nvidia/nemotron-3-ultra-550b-a55b:free | free_model | OpenRouter official models API reports zero prompt/completion price; verify rate limits and upstream terms before production use. | https://openrouter.ai/api/v1/models |
| OpenRouter | model | nvidia/nemotron-3.5-content-safety:free | free_model | OpenRouter official models API reports zero prompt/completion price; verify rate limits and upstream terms before production use. | https://openrouter.ai/api/v1/models |
| OpenRouter | model | nvidia/nemotron-nano-12b-v2-vl:free | free_model | OpenRouter official models API reports zero prompt/completion price; verify rate limits and upstream terms before production use. | https://openrouter.ai/api/v1/models |
| OpenRouter | model | nvidia/nemotron-nano-9b-v2:free | free_model | OpenRouter official models API reports zero prompt/completion price; verify rate limits and upstream terms before production use. | https://openrouter.ai/api/v1/models |
| OpenRouter | model | openai/gpt-oss-20b:free | free_model | OpenRouter official models API reports zero prompt/completion price; verify rate limits and upstream terms before production use. | https://openrouter.ai/api/v1/models |
| OpenRouter | model | openrouter/free | free_model | OpenRouter official models API reports zero prompt/completion price; verify rate limits and upstream terms before production use. | https://openrouter.ai/api/v1/models |
| OpenRouter | model | poolside/laguna-m.1:free | free_model | OpenRouter official models API reports zero prompt/completion price; verify rate limits and upstream terms before production use. | https://openrouter.ai/api/v1/models |
| OpenRouter | model | poolside/laguna-xs-2.1:free | free_model | OpenRouter official models API reports zero prompt/completion price; verify rate limits and upstream terms before production use. | https://openrouter.ai/api/v1/models |

## 新用户试用额度

_暂无符合条件的记录。_

## 候补待确认与参考区

| Provider | Level | Model/Offer | Free type | Reason | Evidence |
| --- | --- | --- | --- | --- | --- |
| Alibaba Cloud Model Studio / Qwen | provider | alibaba-model-studio | not_free_or_unverified | candidate source; verify credit, validity period, identity and region requirements | https://help.aliyun.com/zh/model-studio/models |
| Anthropic Claude API | provider | anthropic-api | not_free_or_unverified | protocol reference only; no verified free API quota | https://docs.anthropic.com/en/api/messages |
| Baidu Qianfan / ERNIE | provider | baidu-qianfan | not_free_or_unverified | candidate source; verify free quota, identity, region and billing rules | https://cloud.baidu.com/doc/WENXINWORKSHOP/ |
| Cerebras Inference | provider | cerebras | not_free_or_unverified | candidate source; verify free or trial quota before recommending | https://inference-docs.cerebras.ai/ |
| Cloudflare Workers AI | provider | cloudflare-workers-ai | not_free_or_unverified | candidate source; verify free allocation, account requirements, and model pricing | https://developers.cloudflare.com/workers-ai/platform/pricing/ |
| DeepSeek API | provider | deepseek | not_free_or_unverified | candidate low-cost source; do not recommend as free without official free quota evidence | https://api-docs.deepseek.com/quick_start/pricing |
| Fireworks AI | provider | fireworks-ai | not_free_or_unverified | P1 candidate source; verify trial credit and pricing | https://docs.fireworks.ai/ |
| Google Gemini API / Google AI Studio | provider | google-gemini | not_free_or_unverified | candidate source; verify official Free Tier, rate limits, region and card requirements | https://ai.google.dev/gemini-api/docs/pricing |
| GroqCloud | provider | groqcloud | not_free_or_unverified | candidate source; verify developer free limits and supported model list | https://console.groq.com/docs/rate-limits |
| Hugging Face Inference Providers | provider | huggingface-inference-providers | not_free_or_unverified | candidate source; distinguish open weights from free hosted API | https://huggingface.co/docs/inference-providers |
| Mistral La Plateforme | provider | mistral | not_free_or_unverified | candidate source; verify whether any free or trial API quota is currently available | https://docs.mistral.ai/ |
| Moonshot / Kimi API | provider | moonshot-kimi | not_free_or_unverified | candidate source; do not recommend without official free API quota evidence | https://platform.moonshot.cn/docs/pricing/chat |
| Nebius AI Studio | provider | nebius-ai | not_free_or_unverified | P1 candidate source; verify API access, credit and pricing | https://docs.nebius.com/studio/ |
| Novita | provider | novita | not_free_or_unverified | P1 candidate source; verify model pricing and credits | https://novita.ai/docs |
| NVIDIA Build / API Catalog | provider | nvidia-build | not_free_or_unverified | P1 candidate source; verify free credits, endpoint and model terms | https://build.nvidia.com/ |
| OpenAI API | provider | openai-api | not_free_or_unverified | protocol reference only; no verified free API quota | https://platform.openai.com/docs/api-reference |
| Replicate | provider | replicate | not_free_or_unverified | P1 candidate source; model pricing varies and must be checked per model | https://replicate.com/docs |
| SiliconFlow | provider | siliconflow | not_free_or_unverified | candidate source; verify official free models, trial credit and account requirements | https://docs.siliconflow.cn/ |
| Tencent Cloud TokenHub / Hunyuan | provider | tencent-tokenhub-hunyuan | not_free_or_unverified | candidate source; verify API base, compatibility, free quota and identity requirements | https://cloud.tencent.com/document/product/1729 |
| Together AI | provider | together-ai | not_free_or_unverified | P1 candidate source; verify new-user credit and low-cost models | https://docs.together.ai/ |
| Volcengine Ark / Doubao | provider | volcengine-ark | not_free_or_unverified | candidate source; verify trial/new-user credit, model IDs and endpoint | https://www.volcengine.com/docs/82379 |
| Zhipu BigModel / GLM | provider | zhipu-bigmodel | not_free_or_unverified | candidate source; do not recommend without official free API quota evidence | https://docs.bigmodel.cn/ |

## 候补监控源与人工判断备注

| Priority | Provider | Type | Status | Official source |
| --- | --- | --- | --- | --- |
| P0 | Google Gemini API / Google AI Studio | official_model_vendor | 待复核官方 Free Tier、rate limits、地区和绑卡要求；确认前不进入推荐表。 | https://ai.google.dev/gemini-api/docs/pricing |
| P0 | Mistral La Plateforme | official_model_vendor | 待复核是否仍有免费或试用 API 额度；不确定时只作为低价/候补源。 | https://docs.mistral.ai/ |
| P0 | GroqCloud | official_model_vendor | 待复核开发者免费限制、模型列表和 rate limits；有官方证据后可建 provider/offer 记录。 | https://console.groq.com/docs/rate-limits |
| P0 | Cerebras Inference | official_model_vendor | 待复核是否提供免费或试用额度；确认前不推荐。 | https://inference-docs.cerebras.ai/ |
| P0 | Cloudflare Workers AI | official_cloud_platform | 待复核免费分配、账号要求和模型计费；需区分平台免费层和模型价格。 | https://developers.cloudflare.com/workers-ai/platform/pricing/ |
| P0 | Alibaba Cloud Model Studio / Qwen | official_cloud_platform | 待复核新用户额度、有效期、实名和地区要求；确认前只作候补。 | https://help.aliyun.com/zh/model-studio/models |
| P0 | Tencent Cloud TokenHub / Hunyuan | official_cloud_platform | 待复核 API base、兼容性、免费额度和实名要求；当前信息不足。 | https://cloud.tencent.com/document/product/1729 |
| P0 | Volcengine Ark / Doubao | official_cloud_platform | 待复核试用/新用户额度、模型 ID 和 endpoint；确认前不进推荐表。 | https://www.volcengine.com/docs/82379 |
| P0 | Zhipu BigModel / GLM | official_model_vendor | 待复核官方免费 API 额度；没有证据时不得硬塞进免费表。 | https://docs.bigmodel.cn/ |
| P0 | Moonshot / Kimi API | official_model_vendor | 待复核官方免费 API 额度；没有证据时只标为候补或低价源。 | https://platform.moonshot.cn/docs/pricing/chat |
| P0 | DeepSeek API | official_model_vendor | 通常作为低价源候补；无官方免费额度证据时不得进入免费推荐表。 | https://api-docs.deepseek.com/quick_start/pricing |
| P0 | Baidu Qianfan / ERNIE | official_cloud_platform | 待复核免费额度、实名、地区和计费规则；确认前只作候补。 | https://cloud.baidu.com/doc/WENXINWORKSHOP/ |
| P0 | OpenAI API | official_model_vendor | 协议参考源；没有官方免费 API 额度时必须标为 not_free_or_unverified。 | https://platform.openai.com/docs/api-reference |
| P0 | Anthropic Claude API | official_model_vendor | 协议参考源；没有官方免费 API 额度时必须标为 not_free_or_unverified。 | https://docs.anthropic.com/en/api/messages |
| P0 | OpenRouter | third_party_router | 已接入官方 models API；只推荐 API 返回的免费模型或 :free 模型。 | https://openrouter.ai/api/v1/models |
| P0 | SiliconFlow | third_party_inference_provider | 待复核官方免费模型、试用额度和账号要求；确认前只作候补。 | https://docs.siliconflow.cn/ |
| P0 | Hugging Face Inference Providers | third_party_inference_provider | 必须区分 open_weight_only 和免费托管 API；不能把开源权重等同于免费 API。 | https://huggingface.co/docs/inference-providers |
| P1 | Together AI | third_party_inference_provider | 候补低价/新用户额度源；待官方 pricing 和 credit 证据。 | https://docs.together.ai/ |
| P1 | Fireworks AI | third_party_inference_provider | 候补试用/低价源；待官方 pricing 和 trial 证据。 | https://docs.fireworks.ai/ |
| P1 | Novita | third_party_inference_provider | 候补试用/低价源；待官方模型价格和额度证据。 | https://novita.ai/docs |
| P1 | Replicate | third_party_inference_provider | 候补推理平台；模型价格差异大，需逐模型确认。 | https://replicate.com/docs |
| P1 | Nebius AI Studio | third_party_inference_provider | 候补试用/低价源；待官方 API、credit 和 pricing 证据。 | https://docs.nebius.com/studio/ |
| P1 | NVIDIA Build / API Catalog | third_party_inference_provider | 候补 API catalog；待确认免费 credits、endpoint 和模型条款。 | https://build.nvidia.com/ |
