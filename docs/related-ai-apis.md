# 相关 AI API 扩展资源

这些 API 可用于生成、检索或安全任务，但不是核心文本/多模态 LLM。它们单独列出，不计入 README 的核心模型数量。当前有 13 个已核实的扩展型号。

| 平台 | 精确 Model ID | 扩展类型 | 免费类型 | 额度/范围 | 速率限制 | API Base | OpenAI 兼容 | 官方来源 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Cohere API | embed-v4.0 | Embedding 向量 | 每月免费评估额度 | 符合条件的评估 Key 每月最多 1,000 次 API 调用，多个端点共享；另有端点/型号 RPM 限制。 | 聊天模型常见限制为 20 RPM；实际端点与型号限制以官方表格为准。 | https://api.cohere.com/v2 | 部分兼容 | [Cohere models catalog](https://docs.cohere.com/v1/docs/models) |
| Cohere API | rerank-v4.0-fast | Rerank 重排 | 每月免费评估额度 | 符合条件的评估 Key 每月最多 1,000 次 API 调用，多个端点共享；另有端点/型号 RPM 限制。 | 聊天模型常见限制为 20 RPM；实际端点与型号限制以官方表格为准。 | https://api.cohere.com/v2 | 部分兼容 | [Cohere models catalog](https://docs.cohere.com/v1/docs/models) |
| Google Gemini API / Google AI Studio | gemini-3.8-flash-lite-tts | 语音生成 | 长期免费层（有用量/速率限制） | 指定模型输入/输出价格为 $0；每个项目的免费层限额按模型和账号而异 | RPM / TPM / RPD 依项目与模型而变；请查 AI Studio 控制台 | https://generativelanguage.googleapis.com | 部分兼容 | [Gemini Developer API pricing](https://ai.google.dev/gemini-api/docs/pricing) |
| Google Gemini API / Google AI Studio | gemini-3.8-flash-tts | 语音生成 | 长期免费层（有用量/速率限制） | 指定模型输入/输出价格为 $0；每个项目的免费层限额按模型和账号而异 | RPM / TPM / RPD 依项目与模型而变；请查 AI Studio 控制台 | https://generativelanguage.googleapis.com | 部分兼容 | [Gemini Developer API pricing](https://ai.google.dev/gemini-api/docs/pricing) |
| GroqCloud | canopylabs/orpheus-arabic-saudi | 语音生成 | 长期免费层（有用量/速率限制） | Free Plan 内可免费调用列出的模型，但受每个模型的速率上限约束；没有单独赠送 Token 包 | RPM 10，RPD 100，TPM 1200，TPD 3600 | https://api.groq.com/openai/v1 | 是 | [Groq Free Plan limits and supported models](https://console.groq.com/docs/rate-limits) |
| GroqCloud | canopylabs/orpheus-v1-english | 语音生成 | 长期免费层（有用量/速率限制） | Free Plan 内可免费调用列出的模型，但受每个模型的速率上限约束；没有单独赠送 Token 包 | RPM 10，RPD 100，TPM 1200，TPD 3600 | https://api.groq.com/openai/v1 | 是 | [Groq Free Plan limits and supported models](https://console.groq.com/docs/rate-limits) |
| GroqCloud | meta-llama/llama-prompt-guard-2-22m | 内容安全 / 审核 | 长期免费层（有用量/速率限制） | Free Plan 内可免费调用列出的模型，但受每个模型的速率上限约束；没有单独赠送 Token 包 | RPM 30，RPD 14400，TPM 15000，TPD 500000 | https://api.groq.com/openai/v1 | 是 | [Groq Free Plan limits and supported models](https://console.groq.com/docs/rate-limits) |
| GroqCloud | meta-llama/llama-prompt-guard-2-86m | 内容安全 / 审核 | 长期免费层（有用量/速率限制） | Free Plan 内可免费调用列出的模型，但受每个模型的速率上限约束；没有单独赠送 Token 包 | RPM 30，RPD 14400，TPM 15000，TPD 500000 | https://api.groq.com/openai/v1 | 是 | [Groq Free Plan limits and supported models](https://console.groq.com/docs/rate-limits) |
| GroqCloud | openai/gpt-oss-safeguard-20b | 内容安全 / 审核 | 长期免费层（有用量/速率限制） | Free Plan 内可免费调用列出的模型，但受每个模型的速率上限约束；没有单独赠送 Token 包 | RPM 3，RPD 1000，TPM 2000，TPD 200000 | https://api.groq.com/openai/v1 | 是 | [Groq Free Plan limits and supported models](https://console.groq.com/docs/rate-limits) |
| GroqCloud | whisper-large-v3 | 语音识别 | 长期免费层（有用量/速率限制） | Free Plan 内可免费调用列出的模型，但受每个模型的速率上限约束；没有单独赠送 Token 包 | RPM 20，RPD 2000，音频秒/小时 7200，音频秒/日 28800 | https://api.groq.com/openai/v1 | 是 | [Groq Free Plan limits and supported models](https://console.groq.com/docs/rate-limits) |
| GroqCloud | whisper-large-v3-turbo | 语音识别 | 长期免费层（有用量/速率限制） | Free Plan 内可免费调用列出的模型，但受每个模型的速率上限约束；没有单独赠送 Token 包 | RPM 20，RPD 2000，音频秒/小时 7200，音频秒/日 28800 | https://api.groq.com/openai/v1 | 是 | [Groq Free Plan limits and supported models](https://console.groq.com/docs/rate-limits) |
| OpenRouter | google/lyria-3-clip-preview | 音乐生成 | 免费路由模型 | 没有 Token 赠额；仅当前 API 返回所有价格维度均为零的模型按免费路由处理 | 免费账号当前通常为 20 RPM、50 RPD；累计购买额度满 $10 的账号适用更高每日额度 | https://openrouter.ai/api/v1 | 是 | [OpenRouter models API](https://openrouter.ai/api/v1/models) |
| OpenRouter | google/lyria-3-pro-preview | 音乐生成 | 免费路由模型 | 没有 Token 赠额；仅当前 API 返回所有价格维度均为零的模型按免费路由处理 | 免费账号当前通常为 20 RPM、50 RPD；累计购买额度满 $10 的账号适用更高每日额度 | https://openrouter.ai/api/v1 | 是 | [OpenRouter models API](https://openrouter.ai/api/v1/models) |

## 输入/输出与能力详情

| 平台 / Model ID | 输入模态 | 输出模态 | 能力标签 | 工具调用 | 结构化输出 | 资格 | 有效期 | 核验日期 | 来源 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Cohere API / `embed-v4.0` | 图像, 文本 | 向量 | 未确认 | 未知 | 未知 | 绑卡：未知；实名：未知；地区：未知 | 评估 Key 资格；生产用途需申请 Production Key。 | 2026-11-01 | [Cohere models catalog](https://docs.cohere.com/v1/docs/models) |
| Cohere API / `rerank-v4.0-fast` | 文本 | 相关性分数 | 未确认 | 未知 | 未知 | 绑卡：未知；实名：未知；地区：未知 | 评估 Key 资格；生产用途需申请 Production Key。 | 2026-11-01 | [Cohere models catalog](https://docs.cohere.com/v1/docs/models) |
| Google Gemini API / Google AI Studio / `gemini-3.8-flash-lite-tts` | 文本 | 音频 | 未确认 | 未知 | 未知 | 绑卡：否；实名：未知；地区：可用国家 / 地区因模型和账号而异 | 未公布固定结束日期；模型和地区资格可能变化 | 2026-11-02 | [Gemini Developer API pricing](https://ai.google.dev/gemini-api/docs/pricing) |
| Google Gemini API / Google AI Studio / `gemini-3.8-flash-tts` | 文本 | 音频 | 未确认 | 未知 | 未知 | 绑卡：否；实名：未知；地区：可用国家 / 地区因模型和账号而异 | 未公布固定结束日期；模型和地区资格可能变化 | 2026-11-02 | [Gemini Developer API pricing](https://ai.google.dev/gemini-api/docs/pricing) |
| GroqCloud / `canopylabs/orpheus-arabic-saudi` | 文本 | 音频 | 未确认 | 未知 | 未知 | 绑卡：未知；实名：未知；地区：未知 | 未公布固定结束日期；免费计划条款和模型可用性可能变化 | 2026-11-01 | [Groq Free Plan limits and supported models](https://console.groq.com/docs/rate-limits) |
| GroqCloud / `canopylabs/orpheus-v1-english` | 文本 | 音频 | 未确认 | 未知 | 未知 | 绑卡：未知；实名：未知；地区：未知 | 未公布固定结束日期；免费计划条款和模型可用性可能变化 | 2026-11-01 | [Groq Free Plan limits and supported models](https://console.groq.com/docs/rate-limits) |
| GroqCloud / `meta-llama/llama-prompt-guard-2-22m` | 文本 | 类别标签 | 未确认 | 未知 | 未知 | 绑卡：未知；实名：未知；地区：未知 | 未公布固定结束日期；免费计划条款和模型可用性可能变化 | 2026-11-01 | [Groq Free Plan limits and supported models](https://console.groq.com/docs/rate-limits) |
| GroqCloud / `meta-llama/llama-prompt-guard-2-86m` | 文本 | 类别标签 | 未确认 | 未知 | 未知 | 绑卡：未知；实名：未知；地区：未知 | 未公布固定结束日期；免费计划条款和模型可用性可能变化 | 2026-11-01 | [Groq Free Plan limits and supported models](https://console.groq.com/docs/rate-limits) |
| GroqCloud / `openai/gpt-oss-safeguard-20b` | 文本 | 类别标签 | 未确认 | 未知 | 未知 | 绑卡：未知；实名：未知；地区：未知 | 未公布固定结束日期；免费计划条款和模型可用性可能变化 | 2026-11-01 | [Groq Free Plan limits and supported models](https://console.groq.com/docs/rate-limits) |
| GroqCloud / `whisper-large-v3` | 音频 | 文本 | 未确认 | 未知 | 未知 | 绑卡：未知；实名：未知；地区：未知 | 未公布固定结束日期；免费计划条款和模型可用性可能变化 | 2026-11-01 | [Groq Free Plan limits and supported models](https://console.groq.com/docs/rate-limits) |
| GroqCloud / `whisper-large-v3-turbo` | 音频 | 文本 | 未确认 | 未知 | 未知 | 绑卡：未知；实名：未知；地区：未知 | 未公布固定结束日期；免费计划条款和模型可用性可能变化 | 2026-11-01 | [Groq Free Plan limits and supported models](https://console.groq.com/docs/rate-limits) |
| OpenRouter / `google/lyria-3-clip-preview` | 图像, 文本 | 音频, 文本 | 未确认 | 未知 | 支持 | 绑卡：否；实名：未知；地区：未知 | 模型的免费状态可能随时变化 | 2026-11-14 | [OpenRouter models API](https://openrouter.ai/api/v1/models) |
| OpenRouter / `google/lyria-3-pro-preview` | 图像, 文本 | 音频, 文本 | 未确认 | 未知 | 支持 | 绑卡：否；实名：未知；地区：未知 | 模型的免费状态可能随时变化 | 2026-11-14 | [OpenRouter models API](https://openrouter.ai/api/v1/models) |

未列型号不代表平台没有该类 API；只有当前免费方案和型号关系均有官方证据时才纳入本页。
