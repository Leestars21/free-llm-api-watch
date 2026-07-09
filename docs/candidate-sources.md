# Candidate Sources

本文件记录 P0/P1 监控源和人工复核要点。候补源不是免费 API 证据；状态列中写明“不确定”“待复核”的项目，需要用户打开官方来源自行判断。

| Priority | Provider | Type | OpenAI | Anthropic | Status / user judgement note | Official source |
| --- | --- | --- | --- | --- | --- | --- |
| P0 | Google Gemini API / Google AI Studio | official_model_vendor | partial | no | 待复核官方 Free Tier、rate limits、地区和绑卡要求；确认前不进入推荐表。 | https://ai.google.dev/gemini-api/docs/pricing |
| P0 | Mistral La Plateforme | official_model_vendor | partial | no | 待复核是否仍有免费或试用 API 额度；不确定时只作为低价/候补源。 | https://docs.mistral.ai/ |
| P0 | GroqCloud | official_model_vendor | yes | no | 待复核开发者免费限制、模型列表和 rate limits；有官方证据后可建 provider/offer 记录。 | https://console.groq.com/docs/rate-limits |
| P0 | Cerebras Inference | official_model_vendor | yes | no | 待复核是否提供免费或试用额度；确认前不推荐。 | https://inference-docs.cerebras.ai/ |
| P0 | Cloudflare Workers AI | official_cloud_platform | partial | no | 待复核免费分配、账号要求和模型计费；需区分平台免费层和模型价格。 | https://developers.cloudflare.com/workers-ai/platform/pricing/ |
| P0 | Alibaba Cloud Model Studio / Qwen | official_cloud_platform | yes | no | 待复核新用户额度、有效期、实名和地区要求；确认前只作候补。 | https://help.aliyun.com/zh/model-studio/models |
| P0 | Tencent Cloud TokenHub / Hunyuan | official_cloud_platform | unknown | unknown | 待复核 API base、兼容性、免费额度和实名要求；当前信息不足。 | https://cloud.tencent.com/document/product/1729 |
| P0 | Volcengine Ark / Doubao | official_cloud_platform | yes | no | 待复核试用/新用户额度、模型 ID 和 endpoint；确认前不进推荐表。 | https://www.volcengine.com/docs/82379 |
| P0 | Zhipu BigModel / GLM | official_model_vendor | partial | no | 待复核官方免费 API 额度；没有证据时不得硬塞进免费表。 | https://docs.bigmodel.cn/ |
| P0 | Moonshot / Kimi API | official_model_vendor | yes | no | 待复核官方免费 API 额度；没有证据时只标为候补或低价源。 | https://platform.moonshot.cn/docs/pricing/chat |
| P0 | DeepSeek API | official_model_vendor | yes | no | 通常作为低价源候补；无官方免费额度证据时不得进入免费推荐表。 | https://api-docs.deepseek.com/quick_start/pricing |
| P0 | Baidu Qianfan / ERNIE | official_cloud_platform | partial | no | 待复核免费额度、实名、地区和计费规则；确认前只作候补。 | https://cloud.baidu.com/doc/WENXINWORKSHOP/ |
| P0 | OpenAI API | official_model_vendor | yes | no | 协议参考源；没有官方免费 API 额度时必须标为 not_free_or_unverified。 | https://platform.openai.com/docs/api-reference |
| P0 | Anthropic Claude API | official_model_vendor | no | yes | 协议参考源；没有官方免费 API 额度时必须标为 not_free_or_unverified。 | https://docs.anthropic.com/en/api/messages |
| P0 | OpenRouter | third_party_router | yes | unknown | 已接入官方 models API；只推荐 API 返回的免费模型或 :free 模型。 | https://openrouter.ai/api/v1/models |
| P0 | SiliconFlow | third_party_inference_provider | yes | no | 待复核官方免费模型、试用额度和账号要求；确认前只作候补。 | https://docs.siliconflow.cn/ |
| P0 | Hugging Face Inference Providers | third_party_inference_provider | partial | no | 必须区分 open_weight_only 和免费托管 API；不能把开源权重等同于免费 API。 | https://huggingface.co/docs/inference-providers |
| P1 | Together AI | third_party_inference_provider | yes | no | 候补低价/新用户额度源；待官方 pricing 和 credit 证据。 | https://docs.together.ai/ |
| P1 | Fireworks AI | third_party_inference_provider | yes | no | 候补试用/低价源；待官方 pricing 和 trial 证据。 | https://docs.fireworks.ai/ |
| P1 | Novita | third_party_inference_provider | yes | no | 候补试用/低价源；待官方模型价格和额度证据。 | https://novita.ai/docs |
| P1 | Replicate | third_party_inference_provider | partial | no | 候补推理平台；模型价格差异大，需逐模型确认。 | https://replicate.com/docs |
| P1 | Nebius AI Studio | third_party_inference_provider | yes | no | 候补试用/低价源；待官方 API、credit 和 pricing 证据。 | https://docs.nebius.com/studio/ |
| P1 | NVIDIA Build / API Catalog | third_party_inference_provider | yes | no | 候补 API catalog；待确认免费 credits、endpoint 和模型条款。 | https://build.nvidia.com/ |

## 抓取失败处理

抓取失败时不要编造数据。失败项必须写入：

```json
{
  "fetch_status": "failed",
  "error_summary": "",
  "confidence": "low",
  "free_type": "not_free_or_unverified"
}
```

失败源需要保留在本文件或 `docs/changelog.md` 中供人工复核。
