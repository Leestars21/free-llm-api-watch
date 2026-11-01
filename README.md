# Free LLM API Watch

**最后核验日期：2026-11-01**

这是一个基于官方证据维护的免费/试用 LLM API 目录。目录区分零价格模型、周期性免费层、新用户赠额、一次性试用、速率限制和开源权重；具体额度和模型名单可能因账号、地区、产品批次而变动。

## 当前目录统计

| 指标 | 数量 |
| --- | ---: |
| 监控提供商 | 39 |
| 已确认有免费 API 或试用方案的提供商 | 20 |
| 有明确免费访问关系的模型记录 | 46 |
| 已确认免费/试用 Offer | 23 |
| 提供新用户赠额或试用额度的平台 | 7 |
| 其中明确标为输入/输出零价格的模型记录 | 29 |

统计只计 `active`、官方来源、`medium/high` 可信度且 `is_recommended=true` 的记录。一个平台级额度若适用于多个模型，计作一个 Offer；没有固定模型清单时会标注为动态/账号内确认，不会推测型号。

## 免费平台总览

| 平台 | 免费类型 | 免费额度 | 已列型号 | 有效期 | 绑卡 | OpenAI 兼容 | 状态 | 官方链接 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AI Horde / AI Horde OpenAI API | 社区志愿算力（动态排队） | 没有固定 Token / 请求赠额；匿名访问可使用社区志愿算力，排队优先级最低 | 型号随平台目录或账号资格变化，请查看官方链接 | 试运行服务，范围可能调整 | 否 | 是 | 已确认免费方案（按来源所述范围） | [AI Horde OpenAI API docs](https://oai.aihorde.net/) |
| Alibaba Cloud Model Studio / Qwen | 新用户赠额 / 免费使用上限 | 符合条件的新账号通常每个模型获得约 100 万 Token；具体额度因模型而异 | `qwen3.8-max` | 按模型激活、发布或审批时间起算 90 天；以控制台为准 | 未知 | 是 | 已确认免费方案（按来源所述范围） | [Model Studio new-user free quota](https://help.aliyun.com/zh/model-studio/new-free-quota/) |
| Cerebras Inference | 长期免费层（有用量/速率限制） | 提供 $0 免费层；公开页面未列出适用于所有账号/模型的统一数字额度 | `zai-glm-4.7` | 官方未公布固定结束日期 | 未知 | 是 | 已确认免费方案（按来源所述范围） | [Cerebras pricing and GLM 4.7 model page](https://inference-docs.cerebras.ai/support/pricing) |
| Cloudflare Workers AI | 长期免费层（有用量/速率限制） | 每天 10,000 Neurons | `@cf/google/gemma-4-26b-a4b-it`, `@cf/zai-org/glm-4.7-flash` | 官方未公布固定结束日期 | 未知 | 部分兼容 | 已确认免费方案（按来源所述范围） | [Workers AI pricing and changelog](https://developers.cloudflare.com/workers-ai/platform/pricing/) |
| Cohere API | 一次性试用额度 | 评估 Key 每月共 1,000 次 API 调用，多个端点共享 | `command-a-03-2025`, `command-r7b-12-2024`, `embed-v4.0`, `rerank-v4.0-fast` | 评估 Key 使用；生产环境需申请生产 Key | 未知 | 部分兼容 | 已确认免费方案（按来源所述范围） | [Cohere rate limits and models](https://docs.cohere.com/v2/docs/rate-limits) |
| Google Gemini API / Google AI Studio | 长期免费层（有用量/速率限制） | 指定模型输入/输出价格为 $0；每个项目的免费层限额按模型和账号而异 | `gemini-3.5-flash-lite`, `gemini-3.8-flash-lite-tts`, `gemini-3.8-flash-tts` | 未公布固定结束日期；模型和地区资格可能变化 | 否 | 部分兼容 | 已确认免费方案（按来源所述范围） | [Gemini Developer API pricing and rate limits](https://ai.google.dev/gemini-api/docs/pricing) |
| GroqCloud | 长期免费层（有用量/速率限制） | Free Plan 内可免费调用列出的模型，但受每个模型的速率上限约束；没有单独赠送 Token 包 | `canopylabs/orpheus-arabic-saudi`, `canopylabs/orpheus-v1-english`, `meta-llama/llama-prompt-guard-2-22m`, `meta-llama/llama-prompt-guard-2-86m`, `openai/gpt-oss-120b`, `openai/gpt-oss-20b`, `openai/gpt-oss-safeguard-20b`, `qwen/qwen3.8-27b`, `whisper-large-v3`, `whisper-large-v3-turbo` | 未公布固定结束日期；免费计划条款和模型可用性可能变化 | 未知 | 是 | 已确认免费方案（按来源所述范围） | [Groq Free Plan rate limits and supported models](https://console.groq.com/docs/rate-limits) |
| Hugging Face Inference Providers | 长期免费层（有用量/速率限制） | 免费账号每月共享 $0.10 推理额度；政策可能调整 | 型号随平台目录或账号资格变化，请查看官方链接 | 按 Hugging Face 当前政策续发；各模型没有独立固定额度 | 未知 | 是 | 已确认免费方案（按来源所述范围） | [Inference Providers pricing](https://huggingface.co/docs/inference-providers/en/pricing) |
| Mistral La Plateforme | 长期免费层（有用量/速率限制） | Free 模式提供账号级月度用量预算；公开文档没有给出统一数值 | 型号随平台目录或账号资格变化，请查看官方链接 | 官方未公布固定结束日期 | 否 | 部分兼容 | 已确认免费方案（按来源所述范围） | [Mistral free mode and usage limits](https://docs.mistral.ai/admin/billing-usage/usage-limits) |
| ModelScope Inference / 魔搭社区 | 长期免费层（有用量/速率限制） | 注册账号每天 200 MoLi 积分；绑定阿里云账号后每天再加 50 分 | 型号随平台目录或账号资格变化，请查看官方链接 | 每日额度及累计积分有效期以当前积分规则为准 | 否 | 是 | 已确认免费方案（按来源所述范围） | [ModelScope MoLi points announcement](https://www.modelscope.cn/posts/435591) |
| Novita AI | 限时活动；限时活动；指定免费模型；新用户赠额 / 免费使用上限 | 当前模型页显示输入和输出均为每百万 Token $0，属于上线促销；部分 Ling 3.0 型号当前显示输入/输出 $0；目录将其标记为限时免费；当前模型页显示输入和输出均为每百万 Token $0；成功邀请后，邀请人与受邀人各得 $10；邀请人奖励累计上限 $500 | `apodex/apodex-1.1-mini`, `inclusionai/ling-3.0-flash-fin`, `inclusionai/ling-3.0-flash-sante`, `inclusionai/ling-3.0-flash-vl`, `inclusionai/ling-3.1-flash` | 上线促销；已核对页面未注明结束日期；限时活动；已核对页面未注明结束日期；价格可能变化；使用前请复核模型页；已核对的邀请页面未说明条款和额度有效期 | 未知；未知；未知；未知 | 是 | 已确认免费方案（按来源所述范围） | [Novita Apodex 1.1 Mini launch and pricing](https://blogs.novita.ai/apodex-1-1-mini-on-novita-ai-api-quickstart-pricing/) |
| Ollama Cloud | 长期免费层（有用量/速率限制） | Free 方案每月包含部分云端模型的起步用量；额度数值未公开，在账号内显示；最多 1 个并发请求 | 型号随平台目录或账号资格变化，请查看官方链接 | 每月额度；具体规则以账号页面为准 | 未知 | 部分兼容 | 已确认免费方案（按来源所述范围） | [Ollama Cloud pricing](https://www.ollama.com/pricing) |
| OpenRouter | 免费路由模型 | 没有 Token 赠额；仅当前 API 返回所有价格维度均为零的模型按免费路由处理 | `cohere/north-mini-code:free`, `dots-studio/dots-3-note-preview:free`, `google/gemma-4-26b-a4b-it:free`, `google/gemma-4-31b-it:free`, `google/lyria-3-clip-preview`, `google/lyria-3-pro-preview`, `liquid/lfm-2.5-2.6b:free`, `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free`, `nvidia/nemotron-3-ultra-550b-a55b:free`, `nvidia/nemotron-3.5-content-safety:free`, `nvidia/nemotron-3.5-lightning:free`, `nvidia/nemotron-3.5-super-vl:free`, `openrouter/free`, `recursive/flint-v1.0:free`, `thinkingmachines/inkling-small:free`, `thinkingmachines/inkling:free`, `xingchen-agi/xing4.0-29b-a4b:free` | 模型的免费状态可能随时变化 | 未知 | 是 | 已确认免费方案（按来源所述范围） | [OpenRouter free model rate limits](https://openrouter.ai/collections/free-models) |
| Reka AI Vision API | 一次性试用额度 | 符合条件的新用户可试用 180 分钟视频索引 | 型号随平台目录或账号资格变化，请查看官方链接 | 注册时显示试用条款；已核对定价页未写明到期日 | 未知 | 否 | 已确认免费方案（按来源所述范围） | [Reka Vision API pricing](https://docs.reka.ai/vision/pricing) |
| Replicate | 一次性试用额度 | 部分模型可在短期评估期间免费运行；未公布统一额度 | 型号随平台目录或账号资格变化，请查看官方链接 | 模型要求设置账单时，免费评估即结束 | 未知 | 部分兼容 | 已确认免费方案（按来源所述范围） | [Replicate billing documentation](https://replicate.com/docs/topics/billing) |
| SiliconFlow | 指定免费模型 | 实时模型广场中部分型号调用价为零；没有统一的平台 Token 赠额 | 型号随平台目录或账号资格变化，请查看官方链接 | 型号资格随实时模型目录变化 | 未知 | 是 | 已确认免费方案（按来源所述范围） | [SiliconFlow rate limits and model gallery](https://docs.siliconflow.cn/docs/userguide/faqs/rate-limit-and-upgradation) |
| Tencent Cloud TokenHub (migration offer) | 一次性试用额度 | 公告未公布额度金额；仅符合条件的旧平台迁移用户可领取 | 型号随平台目录或账号资格变化，请查看官方链接 | 公告称领取后 3 个月 | 未知 | 未知 | 已确认免费方案（按来源所述范围） | [Tencent Cloud migration announcement](https://cloud.tencent.com/announce/detail/2287) |
| Vercel AI Gateway | 长期免费层（有用量/速率限制） | 符合条件的 Free 团队账号每月有 $5 AI Gateway 额度 | `inclusionai/ling-3.1-flash-1019`, `nvidia/nemotron-3.5-lightning-free` | 购买额度后不再享有免费月额度 | 是 | 是 | 已确认免费方案（按来源所述范围） | [Vercel AI Gateway pricing and live model catalog](https://vercel.com/docs/ai-gateway/pricing) |
| Volcengine Ark / Doubao | 新用户赠额 / 免费使用上限 | 符合条件的账号在安全体验模式下最多可用 500,000 Token；各模型另有额度 | 型号随平台目录或账号资格变化，请查看官方链接 | 仅限此前未开通模型服务或未使用过安全体验模式的账号 | 未知 | 是 | 已确认免费方案（按来源所述范围） | [Ark Safe Experience mode](https://docs.volcengine.com/docs/ark/free-tokens-only-mode?lang=zh) |
| Zhipu BigModel / GLM | 指定免费模型 | 官方公告称 GLM-4.7-Flash API 输入和输出 Token 免费；公告未说明请求上限 | `glm-4.7-flash` | 公告未注明固定结束日期 | 未知 | 部分兼容 | 已确认免费方案（按来源所述范围） | [Zhipu GLM-4.7-Flash announcement](https://www.zhipuai.cn/zh/news/148) |

<details><summary>Offer ID、速率限制与判定范围</summary>

| 平台 | Offer ID | 方案说明 | 速率限制（独立于赠额） |
| --- | --- | --- | --- |
| AI Horde / AI Horde OpenAI API | ai-horde-volunteer-inference | `ai-horde-volunteer-inference`：社区志愿算力（动态排队）；没有固定 Token / 请求赠额；匿名访问可使用社区志愿算力，排队优先级最低 | 没有固定数字限速；匿名 Key 优先级最低，等待时间取决于志愿者和队列 |
| Alibaba Cloud Model Studio / Qwen | model-studio-new-user-model-quota | `model-studio-new-user-model-quota`：新用户赠额 / 免费使用上限；符合条件的新账号通常每个模型获得约 100 万 Token；具体额度因模型而异 | 速率限制与赠送 Token 分开；请在控制台查看 |
| Cerebras Inference | cerebras-free-tier | `cerebras-free-tier`：长期免费层（有用量/速率限制）；提供 $0 免费层；公开页面未列出适用于所有账号/模型的统一数字额度 | 免费层速率较低；具体限值随账号和模型变化，公开定价页未给出统一数字 |
| Cloudflare Workers AI | workers-ai-daily-neurons | `workers-ai-daily-neurons`：长期免费层（有用量/速率限制）；每天 10,000 Neurons | 另有模型级限制；部分模型不适用免费额度，请查 Workers AI 型号目录 |
| Cohere API | cohere-evaluation-key | `cohere-evaluation-key`：一次性试用额度；评估 Key 每月共 1,000 次 API 调用，多个端点共享 | 文档所列部分聊天模型为 20 RPM；其他端点和模型限制不同 |
| Google Gemini API / Google AI Studio | gemini-api-free-tier | `gemini-api-free-tier`：长期免费层（有用量/速率限制）；指定模型输入/输出价格为 $0；每个项目的免费层限额按模型和账号而异 | RPM / TPM / RPD 依项目与模型而变；请查 AI Studio 控制台 |
| GroqCloud | groqcloud-free-plan | `groqcloud-free-plan`：长期免费层（有用量/速率限制）；Free Plan 内可免费调用列出的模型，但受每个模型的速率上限约束；没有单独赠送 Token 包 | 官方 Free Plan 限额表列出逐模型 RPM / RPD / TPM / TPD 或音频秒限值；账号实际限值可能不同 |
| Hugging Face Inference Providers | hf-monthly-inference-credit | `hf-monthly-inference-credit`：长期免费层（有用量/速率限制）；免费账号每月共享 $0.10 推理额度；政策可能调整 | 限制由推理服务商和模型决定；请查当前 Router 文档 |
| Mistral La Plateforme | mistral-studio-free-mode | `mistral-studio-free-mode`：长期免费层（有用量/速率限制）；Free 模式提供账号级月度用量预算；公开文档没有给出统一数值 | 月度预算之外还会受组织与模型级限制 |
| ModelScope Inference / 魔搭社区 | modelscope-daily-moli-points | `modelscope-daily-moli-points`：长期免费层（有用量/速率限制）；注册账号每天 200 MoLi 积分；绑定阿里云账号后每天再加 50 分 | API-Inference 调用通常按模型大小消耗约 0.5 / 1 / 2 分；其他任务也会共用积分 |
| Novita AI | novita-apodex-1-1-mini-launch-promotion；novita-ling-3-0-limited-promotion；novita-ling-3-1-flash-free；novita-referral-credit | `novita-apodex-1-1-mini-launch-promotion`：限时活动；当前模型页显示输入和输出均为每百万 Token $0，属于上线促销；`novita-ling-3-0-limited-promotion`：限时活动；部分 Ling 3.0 型号当前显示输入/输出 $0；目录将其标记为限时免费；`novita-ling-3-1-flash-free`：指定免费模型；当前模型页显示输入和输出均为每百万 Token $0；`novita-referral-credit`：新用户赠额 / 免费使用上限；成功邀请后，邀请人与受邀人各得 $10；邀请人奖励累计上限 $500 | 模型页未说明固定速率限制；模型页未说明固定速率限制；模型页未说明固定速率限制；邀请奖励需满足邀请条件，不是自动注册赠额 |
| Ollama Cloud | ollama-cloud-free-starter-usage | `ollama-cloud-free-starter-usage`：长期免费层（有用量/速率限制）；Free 方案每月包含部分云端模型的起步用量；额度数值未公开，在账号内显示；最多 1 个并发请求 | 免费方案同时最多处理 1 个请求 |
| OpenRouter | openrouter-free-model-route | `openrouter-free-model-route`：免费路由模型；没有 Token 赠额；仅当前 API 返回所有价格维度均为零的模型按免费路由处理 | 免费账号当前通常为 20 RPM、50 RPD；累计购买额度满 $10 的账号适用更高每日额度 |
| Reka AI Vision API | reka-vision-new-user-trial | `reka-vision-new-user-trial`：一次性试用额度；符合条件的新用户可试用 180 分钟视频索引 | 仅适用于 Vision API 视频处理，不适用于 Reka Chat Token API |
| Replicate | replicate-model-evaluation-run | `replicate-model-evaluation-run`：一次性试用额度；部分模型可在短期评估期间免费运行；未公布统一额度 | 可用模型与试用限制以 Replicate 当前界面为准 |
| SiliconFlow | siliconflow-live-free-model-catalog | `siliconflow-live-free-model-catalog`：指定免费模型；实时模型广场中部分型号调用价为零；没有统一的平台 Token 赠额 | 官方范围：聊天 1,000–10,000 RPM / 50,000–5,000,000 TPM；Embedding 2,000–10,000 RPM / 500,000–10,000,000 TPM；重排 2,000 RPM / 500,000 TPM；图像 2 IPM / 400 IPD |
| Tencent Cloud TokenHub (migration offer) | tokenhub-migration-experience-credit | `tokenhub-migration-experience-credit`：一次性试用额度；公告未公布额度金额；仅符合条件的旧平台迁移用户可领取 | 具体额度和可用模型需在用户控制台确认 |
| Vercel AI Gateway | vercel-ai-gateway-monthly-credit | `vercel-ai-gateway-monthly-credit`：长期免费层（有用量/速率限制）；符合条件的 Free 团队账号每月有 $5 AI Gateway 额度 | 上游服务商和模型自身的免费层速率限制仍然适用 |
| Volcengine Ark / Doubao | ark-safe-experience-mode | `ark-safe-experience-mode`：新用户赠额 / 免费使用上限；符合条件的账号在安全体验模式下最多可用 500,000 Token；各模型另有额度 | 模型另有独立速率限制；插件、知识库、批处理可能另行计费 |
| Zhipu BigModel / GLM | bigmodel-glm-4.7-flash-free | `bigmodel-glm-4.7-flash-free`：指定免费模型；官方公告称 GLM-4.7-Flash API 输入和输出 Token 免费；公告未说明请求上限 | 当前请求限制请在 BigModel 控制台查看 |

</details>

## 免费模型详细列表

模型类型包括聊天、语音生成、语音识别、内容审核、Embedding、Rerank 等；`unknown` 表示官方材料未能确认，不代表不支持。额度、速率限制、资格、到期、API Base、来源和验证时间等完整字段见[免费模型明细](docs/free-models.md)。

| 平台 | Model Name | 精确 Model ID | 类型 | Offer ID | 免费范围 | 上下文 | 模态 | 多模态 | 速率限制 | 工具调用 | 结构化输出 | API Base | OpenAI 兼容 | 来源 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Alibaba Cloud Model Studio / Qwen | Qwen 3.8 Max | qwen3.8-max | 聊天 | model-studio-new-user-model-quota | 符合条件的新账号通常每个模型获得约 100 万 Token；具体额度因模型而异 | 未知 | 文本 | 否 | 速率限制与赠送 Token 分开；请在控制台查看 | 未知 | 未知 | https://dashscope.aliyuncs.com/compatible-mode/v1 | 是 | [Model Studio new-user free quota example](https://help.aliyun.com/zh/model-studio/new-free-quota/) |
| Cerebras Inference | Z.ai GLM 4.7 on Cerebras | zai-glm-4.7 | 聊天 | cerebras-free-tier | 提供 $0 免费层；公开页面未列出适用于所有账号/模型的统一数字额度 | 未知 | 文本 | 否 | 免费层速率较低；具体限值随账号和模型变化，公开定价页未给出统一数字 | 支持 | 未知 | https://api.cerebras.ai/v1 | 是 | [Cerebras Z.ai GLM 4.7 model page](https://inference-docs.cerebras.ai/models/zai-glm-47) |
| Cloudflare Workers AI | Gemma 4 26B A4B IT on Workers AI | @cf/google/gemma-4-26b-a4b-it | 聊天 | workers-ai-daily-neurons | 每天 10,000 Neurons | 未知 | 文本 | 否 | 另有模型级限制；部分模型不适用免费额度，请查 Workers AI 型号目录 | 未知 | 未知 | https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/run | 部分兼容 | [Cloudflare Workers AI model catalog](https://developers.cloudflare.com/workers-ai/models/) |
| Cloudflare Workers AI | GLM-4.7-Flash on Workers AI | @cf/zai-org/glm-4.7-flash | 聊天 | workers-ai-daily-neurons | 每天 10,000 Neurons | 未知 | 文本 | 否 | 另有模型级限制；部分模型不适用免费额度，请查 Workers AI 型号目录 | 未知 | 未知 | https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/run | 部分兼容 | [Cloudflare Workers AI model catalog](https://developers.cloudflare.com/workers-ai/models/) |
| Cohere API | Command A | command-a-03-2025 | 聊天 | cohere-evaluation-key | 评估 Key 每月共 1,000 次 API 调用，多个端点共享 | 未知 | 文本 | 否 | 文档所列部分聊天模型为 20 RPM；其他端点和模型限制不同 | 未知 | 未知 | https://api.cohere.com/v2 | 部分兼容 | [Cohere models catalog](https://docs.cohere.com/v1/docs/models) |
| Cohere API | Command R7B | command-r7b-12-2024 | 聊天 | cohere-evaluation-key | 评估 Key 每月共 1,000 次 API 调用，多个端点共享 | 未知 | 文本 | 否 | 文档所列部分聊天模型为 20 RPM；其他端点和模型限制不同 | 未知 | 未知 | https://api.cohere.com/v2 | 部分兼容 | [Cohere models catalog](https://docs.cohere.com/v1/docs/models) |
| Cohere API | Embed 4.0 | embed-v4.0 | Embedding 向量 | cohere-evaluation-key | 评估 Key 每月共 1,000 次 API 调用，多个端点共享 | 未知 | 文本, 图像 | 是 | 文档所列部分聊天模型为 20 RPM；其他端点和模型限制不同 | 未知 | 未知 | https://api.cohere.com/v2 | 部分兼容 | [Cohere models catalog](https://docs.cohere.com/v1/docs/models) |
| Cohere API | Rerank 4.0 Fast | rerank-v4.0-fast | Rerank 重排 | cohere-evaluation-key | 评估 Key 每月共 1,000 次 API 调用，多个端点共享 | 未知 | 文本 | 否 | 文档所列部分聊天模型为 20 RPM；其他端点和模型限制不同 | 未知 | 未知 | https://api.cohere.com/v2 | 部分兼容 | [Cohere models catalog](https://docs.cohere.com/v1/docs/models) |
| Google Gemini API / Google AI Studio | Gemini 3.5 Flash-Lite | gemini-3.5-flash-lite | 聊天 | gemini-api-free-tier | 指定模型输入/输出价格为 $0；每个项目的免费层限额按模型和账号而异 | 未知 | 文本, 图像, 音频, 视频 | 是 | RPM / TPM / RPD 依项目与模型而变；请查 AI Studio 控制台 | 未知 | 未知 | https://generativelanguage.googleapis.com | 部分兼容 | [Gemini Developer API pricing](https://ai.google.dev/gemini-api/docs/pricing) |
| Google Gemini API / Google AI Studio | Gemini 3.8 Flash-Lite TTS | gemini-3.8-flash-lite-tts | 语音生成 | gemini-api-free-tier | 指定模型输入/输出价格为 $0；每个项目的免费层限额按模型和账号而异 | 未知 | 文本, 音频 | 是 | RPM / TPM / RPD 依项目与模型而变；请查 AI Studio 控制台 | 未知 | 未知 | https://generativelanguage.googleapis.com | 部分兼容 | [Gemini Developer API pricing](https://ai.google.dev/gemini-api/docs/pricing) |
| Google Gemini API / Google AI Studio | Gemini 3.8 Flash TTS | gemini-3.8-flash-tts | 语音生成 | gemini-api-free-tier | 指定模型输入/输出价格为 $0；每个项目的免费层限额按模型和账号而异 | 未知 | 文本, 音频 | 是 | RPM / TPM / RPD 依项目与模型而变；请查 AI Studio 控制台 | 未知 | 未知 | https://generativelanguage.googleapis.com | 部分兼容 | [Gemini Developer API pricing](https://ai.google.dev/gemini-api/docs/pricing) |
| GroqCloud | Orpheus Arabic Saudi | canopylabs/orpheus-arabic-saudi | 语音生成 | groqcloud-free-plan | Free Plan 内可免费调用列出的模型，但受每个模型的速率上限约束；没有单独赠送 Token 包 | 4,000 Token | 文本, 音频 | 是 | RPM 10，RPD 100，TPM 1200，TPD 3600 | 未知 | 未知 | https://api.groq.com/openai/v1 | 是 | [Groq Free Plan limits and supported models](https://console.groq.com/docs/rate-limits) |
| GroqCloud | Orpheus V1 English | canopylabs/orpheus-v1-english | 语音生成 | groqcloud-free-plan | Free Plan 内可免费调用列出的模型，但受每个模型的速率上限约束；没有单独赠送 Token 包 | 4,000 Token | 文本, 音频 | 是 | RPM 10，RPD 100，TPM 1200，TPD 3600 | 未知 | 未知 | https://api.groq.com/openai/v1 | 是 | [Groq Free Plan limits and supported models](https://console.groq.com/docs/rate-limits) |
| GroqCloud | Llama Prompt Guard 2 22M | meta-llama/llama-prompt-guard-2-22m | 内容安全 / 审核 | groqcloud-free-plan | Free Plan 内可免费调用列出的模型，但受每个模型的速率上限约束；没有单独赠送 Token 包 | 512 Token | 文本 | 否 | RPM 30，RPD 14400，TPM 15000，TPD 500000 | 未知 | 未知 | https://api.groq.com/openai/v1 | 是 | [Groq Free Plan limits and supported models](https://console.groq.com/docs/rate-limits) |
| GroqCloud | Llama Prompt Guard 2 86M | meta-llama/llama-prompt-guard-2-86m | 内容安全 / 审核 | groqcloud-free-plan | Free Plan 内可免费调用列出的模型，但受每个模型的速率上限约束；没有单独赠送 Token 包 | 512 Token | 文本 | 否 | RPM 30，RPD 14400，TPM 15000，TPD 500000 | 未知 | 未知 | https://api.groq.com/openai/v1 | 是 | [Groq Free Plan limits and supported models](https://console.groq.com/docs/rate-limits) |
| GroqCloud | GPT OSS 120B | openai/gpt-oss-120b | 聊天 | groqcloud-free-plan | Free Plan 内可免费调用列出的模型，但受每个模型的速率上限约束；没有单独赠送 Token 包 | 131,072 Token | 文本 | 否 | RPM 30，RPD 1000，TPM 8000，TPD 200000 | 未知 | 未知 | https://api.groq.com/openai/v1 | 是 | [Groq Free Plan limits and supported models](https://console.groq.com/docs/rate-limits) |
| GroqCloud | GPT OSS 20B | openai/gpt-oss-20b | 聊天 | groqcloud-free-plan | Free Plan 内可免费调用列出的模型，但受每个模型的速率上限约束；没有单独赠送 Token 包 | 131,072 Token | 文本 | 否 | RPM 30，RPD 1000，TPM 8000，TPD 200000 | 未知 | 未知 | https://api.groq.com/openai/v1 | 是 | [Groq Free Plan limits and supported models](https://console.groq.com/docs/rate-limits) |
| GroqCloud | GPT OSS Safeguard 20B | openai/gpt-oss-safeguard-20b | 内容安全 / 审核 | groqcloud-free-plan | Free Plan 内可免费调用列出的模型，但受每个模型的速率上限约束；没有单独赠送 Token 包 | 131,072 Token | 文本 | 否 | RPM 3，RPD 1000，TPM 2000，TPD 200000 | 未知 | 未知 | https://api.groq.com/openai/v1 | 是 | [Groq Free Plan limits and supported models](https://console.groq.com/docs/rate-limits) |
| GroqCloud | Qwen 3.8 27B | qwen/qwen3.8-27b | 聊天 | groqcloud-free-plan | Free Plan 内可免费调用列出的模型，但受每个模型的速率上限约束；没有单独赠送 Token 包 | 131,072 Token | 文本 | 否 | RPM 30，RPD 1000，TPM 8000，TPD 200000 | 未知 | 未知 | https://api.groq.com/openai/v1 | 是 | [Groq Free Plan limits and supported models](https://console.groq.com/docs/rate-limits) |
| GroqCloud | Whisper Large V3 | whisper-large-v3 | 语音识别 | groqcloud-free-plan | Free Plan 内可免费调用列出的模型，但受每个模型的速率上限约束；没有单独赠送 Token 包 | 未知 | 音频, 文本 | 是 | RPM 20，RPD 2000，音频秒/小时 7200，音频秒/日 28800 | 未知 | 未知 | https://api.groq.com/openai/v1 | 是 | [Groq Free Plan limits and supported models](https://console.groq.com/docs/rate-limits) |
| GroqCloud | Whisper Large V3 Turbo | whisper-large-v3-turbo | 语音识别 | groqcloud-free-plan | Free Plan 内可免费调用列出的模型，但受每个模型的速率上限约束；没有单独赠送 Token 包 | 未知 | 音频, 文本 | 是 | RPM 20，RPD 2000，音频秒/小时 7200，音频秒/日 28800 | 未知 | 未知 | https://api.groq.com/openai/v1 | 是 | [Groq Free Plan limits and supported models](https://console.groq.com/docs/rate-limits) |
| Novita AI | Apodex 1.1 Mini | apodex/apodex-1.1-mini | 聊天 | novita-apodex-1-1-mini-launch-promotion | 当前模型页显示输入和输出均为每百万 Token $0，属于上线促销 | 256,000 Token | 文本 | 否 | 模型页未说明固定速率限制 | 支持 | 支持 | https://api.novita.ai/openai | 是 | [Novita Apodex 1.1 Mini model details](https://novita.ai/models/model-detail/apodex-apodex-1.1-mini?from=pricing) |
| Novita AI | InclusionAI Ling 3.0 Flash Fin | inclusionai/ling-3.0-flash-fin | 聊天 | novita-ling-3-0-limited-promotion | 部分 Ling 3.0 型号当前显示输入/输出 $0；目录将其标记为限时免费 | 256,000 Token | 文本 | 否 | 模型页未说明固定速率限制 | 支持 | 未知 | https://api.novita.ai/openai | 是 | [Novita Ling 3.0 Flash Fin model details](https://novita.ai/models/model-detail/inclusionai-ling-3.0-flash-fin) |
| Novita AI | InclusionAI Ling 3.0 Flash Sante | inclusionai/ling-3.0-flash-sante | 聊天 | novita-ling-3-0-limited-promotion | 部分 Ling 3.0 型号当前显示输入/输出 $0；目录将其标记为限时免费 | 256,000 Token | 文本 | 否 | 模型页未说明固定速率限制 | 支持 | 未知 | https://api.novita.ai/openai | 是 | [Novita Ling 3.0 Flash Sante model details](https://novita.ai/models/model-detail/inclusionai-ling-3.0-flash-sante?from=pricing) |
| Novita AI | InclusionAI Ling 3.0 Flash VL | inclusionai/ling-3.0-flash-vl | 聊天 | novita-ling-3-0-limited-promotion | 部分 Ling 3.0 型号当前显示输入/输出 $0；目录将其标记为限时免费 | 256,000 Token | 文本, 图像, 视频 | 是 | 模型页未说明固定速率限制 | 支持 | 未知 | https://api.novita.ai/openai | 是 | [Novita Ling 3.0 Flash VL model details](https://novita.ai/models/model-detail/inclusionai-ling-3.0-flash-vl) |
| Novita AI | InclusionAI Ling 3.1 Flash | inclusionai/ling-3.1-flash | 聊天 | novita-ling-3-1-flash-free | 当前模型页显示输入和输出均为每百万 Token $0 | 256,000 Token | 文本 | 否 | 模型页未说明固定速率限制 | 支持 | 未知 | https://api.novita.ai/openai | 是 | [Novita Ling 3.1 Flash model details](https://novita.ai/models/model-detail/inclusionai-ling-3.1-flash?from=pricing) |
| OpenRouter | Cohere: North Mini Code (free) | cohere/north-mini-code:free | 聊天 | openrouter-free-model-route | 没有 Token 赠额；仅当前 API 返回所有价格维度均为零的模型按免费路由处理 | 256,000 Token | 文本 | 否 | 免费账号当前通常为 20 RPM、50 RPD；累计购买额度满 $10 的账号适用更高每日额度 | 未知 | 未知 | https://openrouter.ai/api/v1 | 是 | [OpenRouter models API](https://openrouter.ai/api/v1/models) |
| OpenRouter | Dots Studio: Dots3-Note Preview (free) | dots-studio/dots-3-note-preview:free | 多模态 | openrouter-free-model-route | 没有 Token 赠额；仅当前 API 返回所有价格维度均为零的模型按免费路由处理 | 512,000 Token | 图像, 文本 | 是 | 免费账号当前通常为 20 RPM、50 RPD；累计购买额度满 $10 的账号适用更高每日额度 | 未知 | 未知 | https://openrouter.ai/api/v1 | 是 | [OpenRouter models API](https://openrouter.ai/api/v1/models) |
| OpenRouter | Google: Gemma 4 26B A4B  (free) | google/gemma-4-26b-a4b-it:free | 多模态 | openrouter-free-model-route | 没有 Token 赠额；仅当前 API 返回所有价格维度均为零的模型按免费路由处理 | 262,144 Token | 图像, 文本, 视频 | 是 | 免费账号当前通常为 20 RPM、50 RPD；累计购买额度满 $10 的账号适用更高每日额度 | 未知 | 未知 | https://openrouter.ai/api/v1 | 是 | [OpenRouter models API](https://openrouter.ai/api/v1/models) |
| OpenRouter | Google: Gemma 4 31B (free) | google/gemma-4-31b-it:free | 多模态 | openrouter-free-model-route | 没有 Token 赠额；仅当前 API 返回所有价格维度均为零的模型按免费路由处理 | 262,144 Token | 图像, 文本, 视频 | 是 | 免费账号当前通常为 20 RPM、50 RPD；累计购买额度满 $10 的账号适用更高每日额度 | 未知 | 未知 | https://openrouter.ai/api/v1 | 是 | [OpenRouter models API](https://openrouter.ai/api/v1/models) |
| OpenRouter | Google: Lyria 3 Clip Preview | google/lyria-3-clip-preview | 多模态 | openrouter-free-model-route | 没有 Token 赠额；仅当前 API 返回所有价格维度均为零的模型按免费路由处理 | 1,048,576 Token | 音频, 图像, 文本 | 是 | 免费账号当前通常为 20 RPM、50 RPD；累计购买额度满 $10 的账号适用更高每日额度 | 未知 | 未知 | https://openrouter.ai/api/v1 | 是 | [OpenRouter models API](https://openrouter.ai/api/v1/models) |
| OpenRouter | Google: Lyria 3 Pro Preview | google/lyria-3-pro-preview | 多模态 | openrouter-free-model-route | 没有 Token 赠额；仅当前 API 返回所有价格维度均为零的模型按免费路由处理 | 1,048,576 Token | 音频, 图像, 文本 | 是 | 免费账号当前通常为 20 RPM、50 RPD；累计购买额度满 $10 的账号适用更高每日额度 | 未知 | 未知 | https://openrouter.ai/api/v1 | 是 | [OpenRouter models API](https://openrouter.ai/api/v1/models) |
| OpenRouter | LiquidAI: LFM2.5-2.6B (free) | liquid/lfm-2.5-2.6b:free | 聊天 | openrouter-free-model-route | 没有 Token 赠额；仅当前 API 返回所有价格维度均为零的模型按免费路由处理 | 65,536 Token | 文本 | 否 | 免费账号当前通常为 20 RPM、50 RPD；累计购买额度满 $10 的账号适用更高每日额度 | 未知 | 未知 | https://openrouter.ai/api/v1 | 是 | [OpenRouter models API](https://openrouter.ai/api/v1/models) |
| OpenRouter | NVIDIA: Nemotron 3 Nano Omni (free) | nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free | 多模态 | openrouter-free-model-route | 没有 Token 赠额；仅当前 API 返回所有价格维度均为零的模型按免费路由处理 | 256,000 Token | 音频, 图像, 文本, 视频 | 是 | 免费账号当前通常为 20 RPM、50 RPD；累计购买额度满 $10 的账号适用更高每日额度 | 未知 | 未知 | https://openrouter.ai/api/v1 | 是 | [OpenRouter models API](https://openrouter.ai/api/v1/models) |
| OpenRouter | NVIDIA: Nemotron 3 Ultra (free) | nvidia/nemotron-3-ultra-550b-a55b:free | 聊天 | openrouter-free-model-route | 没有 Token 赠额；仅当前 API 返回所有价格维度均为零的模型按免费路由处理 | 1,000,000 Token | 文本 | 否 | 免费账号当前通常为 20 RPM、50 RPD；累计购买额度满 $10 的账号适用更高每日额度 | 未知 | 未知 | https://openrouter.ai/api/v1 | 是 | [OpenRouter models API](https://openrouter.ai/api/v1/models) |
| OpenRouter | NVIDIA: Nemotron 3.5 Content Safety (free) | nvidia/nemotron-3.5-content-safety:free | 多模态 | openrouter-free-model-route | 没有 Token 赠额；仅当前 API 返回所有价格维度均为零的模型按免费路由处理 | 128,000 Token | 图像, 文本 | 是 | 免费账号当前通常为 20 RPM、50 RPD；累计购买额度满 $10 的账号适用更高每日额度 | 未知 | 未知 | https://openrouter.ai/api/v1 | 是 | [OpenRouter models API](https://openrouter.ai/api/v1/models) |
| OpenRouter | NVIDIA: Nemotron 3.5 Lightning (free) | nvidia/nemotron-3.5-lightning:free | 聊天 | openrouter-free-model-route | 没有 Token 赠额；仅当前 API 返回所有价格维度均为零的模型按免费路由处理 | 1,000,000 Token | 文本 | 否 | 免费账号当前通常为 20 RPM、50 RPD；累计购买额度满 $10 的账号适用更高每日额度 | 未知 | 未知 | https://openrouter.ai/api/v1 | 是 | [OpenRouter models API](https://openrouter.ai/api/v1/models) |
| OpenRouter | NVIDIA: Nemotron 3.5 Super VL (free) | nvidia/nemotron-3.5-super-vl:free | 多模态 | openrouter-free-model-route | 没有 Token 赠额；仅当前 API 返回所有价格维度均为零的模型按免费路由处理 | 1,000,000 Token | 图像, 文本, 视频 | 是 | 免费账号当前通常为 20 RPM、50 RPD；累计购买额度满 $10 的账号适用更高每日额度 | 未知 | 未知 | https://openrouter.ai/api/v1 | 是 | [OpenRouter models API](https://openrouter.ai/api/v1/models) |
| OpenRouter | Free Models Router | openrouter/free | 多模态 | openrouter-free-model-route | 没有 Token 赠额；仅当前 API 返回所有价格维度均为零的模型按免费路由处理 | 200,000 Token | 图像, 文本 | 是 | 免费账号当前通常为 20 RPM、50 RPD；累计购买额度满 $10 的账号适用更高每日额度 | 未知 | 未知 | https://openrouter.ai/api/v1 | 是 | [OpenRouter models API](https://openrouter.ai/api/v1/models) |
| OpenRouter | Recursive: Flint (free) | recursive/flint-v1.0:free | 聊天 | openrouter-free-model-route | 没有 Token 赠额；仅当前 API 返回所有价格维度均为零的模型按免费路由处理 | 262,144 Token | 文本 | 否 | 免费账号当前通常为 20 RPM、50 RPD；累计购买额度满 $10 的账号适用更高每日额度 | 未知 | 未知 | https://openrouter.ai/api/v1 | 是 | [OpenRouter models API](https://openrouter.ai/api/v1/models) |
| OpenRouter | Thinking Machines: Inkling Small (free) | thinkingmachines/inkling-small:free | 多模态 | openrouter-free-model-route | 没有 Token 赠额；仅当前 API 返回所有价格维度均为零的模型按免费路由处理 | 1,048,576 Token | 音频, 图像, 文本 | 是 | 免费账号当前通常为 20 RPM、50 RPD；累计购买额度满 $10 的账号适用更高每日额度 | 未知 | 未知 | https://openrouter.ai/api/v1 | 是 | [OpenRouter models API](https://openrouter.ai/api/v1/models) |
| OpenRouter | Thinking Machines: Inkling (free) | thinkingmachines/inkling:free | 多模态 | openrouter-free-model-route | 没有 Token 赠额；仅当前 API 返回所有价格维度均为零的模型按免费路由处理 | 1,048,576 Token | 音频, 图像, 文本 | 是 | 免费账号当前通常为 20 RPM、50 RPD；累计购买额度满 $10 的账号适用更高每日额度 | 未知 | 未知 | https://openrouter.ai/api/v1 | 是 | [OpenRouter models API](https://openrouter.ai/api/v1/models) |
| OpenRouter | XingChen: Xing4.0 29B A4B (free) | xingchen-agi/xing4.0-29b-a4b:free | 聊天 | openrouter-free-model-route | 没有 Token 赠额；仅当前 API 返回所有价格维度均为零的模型按免费路由处理 | 262,144 Token | 文本 | 否 | 免费账号当前通常为 20 RPM、50 RPD；累计购买额度满 $10 的账号适用更高每日额度 | 未知 | 未知 | https://openrouter.ai/api/v1 | 是 | [OpenRouter models API](https://openrouter.ai/api/v1/models) |
| Vercel AI Gateway | InclusionAI Ling 3.1 Flash 1019 (Vercel AI Gateway route) | inclusionai/ling-3.1-flash-1019 | 聊天 | vercel-ai-gateway-monthly-credit | 符合条件的 Free 团队账号每月有 $5 AI Gateway 额度 | 未知 | 文本 | 否 | 上游服务商和模型自身的免费层速率限制仍然适用 | 未知 | 未知 | https://ai-gateway.vercel.sh/v1 | 是 | [Vercel AI Gateway model catalog](https://vercel.com/ai-gateway/models?features=free) |
| Vercel AI Gateway | NVIDIA Nemotron 3.5 Lightning Free (Vercel AI Gateway route) | nvidia/nemotron-3.5-lightning-free | 聊天 | vercel-ai-gateway-monthly-credit | 符合条件的 Free 团队账号每月有 $5 AI Gateway 额度 | 未知 | 文本 | 否 | 上游服务商和模型自身的免费层速率限制仍然适用 | 未知 | 未知 | https://ai-gateway.vercel.sh/v1 | 是 | [Vercel AI Gateway model catalog](https://vercel.com/ai-gateway/models?features=free) |
| Zhipu BigModel / GLM | GLM-4.7-Flash | glm-4.7-flash | 聊天 | bigmodel-glm-4.7-flash-free | 官方公告称 GLM-4.7-Flash API 输入和输出 Token 免费；公告未说明请求上限 | 未知 | 文本 | 否 | 当前请求限制请在 BigModel 控制台查看 | 未知 | 未知 | https://open.bigmodel.cn/api/paas/v4 | 部分兼容 | [Zhipu GLM-4.7-Flash announcement](https://www.zhipuai.cn/zh/news/148) |

## 新用户赠额与试用

赠额、共享余额与模型免费定价不是同一概念。下表的 `额度范围`、有效期、实名/地区要求须与账号内页面再次核对。

| 平台 | Offer ID | 类型 | 额度 | 额度单位 | 可用模型 | 重置/发放 | 有效期 | 绑卡 | 实名 | 地区限制 | 额度范围 | 速率限制（不属于赠额） | 官方来源 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Alibaba Cloud Model Studio / Qwen | model-studio-new-user-model-quota | 新用户赠额 / 免费使用上限 | 符合条件的新账号通常每个模型获得约 100 万 Token；具体额度因模型而异 | Token/模型 | qwen3.8-max | 符合资格后按模型发放一次；主账号与 RAM 子账号共享 | 按模型激活、发布或审批时间起算 90 天；以控制台为准 | 未知 | 是 | 仅限中国北京地域且账号符合资格 | 按模型独立 | 速率限制与赠送 Token 分开；请在控制台查看 | [Model Studio new-user free quota](https://help.aliyun.com/zh/model-studio/new-free-quota/) |
| Cohere API | cohere-evaluation-key | 一次性试用额度 | 评估 Key 每月共 1,000 次 API 调用，多个端点共享 | 次 API 调用/月 | command-a-03-2025, command-r7b-12-2024, rerank-v4.0-fast, embed-v4.0 | 按月重置 | 评估 Key 使用；生产环境需申请生产 Key | 未知 | 未知 | 未知 | 账号共享 | 文档所列部分聊天模型为 20 RPM；其他端点和模型限制不同 | [Cohere rate limits and models](https://docs.cohere.com/v2/docs/rate-limits) |
| Novita AI | novita-referral-credit | 新用户赠额 / 免费使用上限 | 成功邀请后，邀请人与受邀人各得 $10；邀请人奖励累计上限 $500 | 美元 | 动态 / 账号内确认 | 每次成功邀请发放；未说明周期性重置 | 已核对的邀请页面未说明条款和额度有效期 | 未知 | 未知 | 未知 | 按用户 | 邀请奖励需满足邀请条件，不是自动注册赠额 | [Novita referral program](https://novita.ai/referral/) |
| Reka AI Vision API | reka-vision-new-user-trial | 一次性试用额度 | 符合条件的新用户可试用 180 分钟视频索引 | 视频分钟 | 动态 / 账号内确认 | 新用户一次性试用 | 注册时显示试用条款；已核对定价页未写明到期日 | 未知 | 未知 | 未知 | 一次性 | 仅适用于 Vision API 视频处理，不适用于 Reka Chat Token API | [Reka Vision API pricing](https://docs.reka.ai/vision/pricing) |
| Replicate | replicate-model-evaluation-run | 一次性试用额度 | 部分模型可在短期评估期间免费运行；未公布统一额度 | 未知 | 动态 / 账号内确认 | 按模型和账号的一次性评估 | 模型要求设置账单时，免费评估即结束 | 未知 | 未知 | 未知 | 一次性 | 可用模型与试用限制以 Replicate 当前界面为准 | [Replicate billing documentation](https://replicate.com/docs/topics/billing) |
| Tencent Cloud TokenHub (migration offer) | tokenhub-migration-experience-credit | 一次性试用额度 | 公告未公布额度金额；仅符合条件的旧平台迁移用户可领取 | 未知 | 动态 / 账号内确认 | 符合资格的迁移用户可领取一次 | 公告称领取后 3 个月 | 未知 | 未知 | 未知 | 一次性 | 具体额度和可用模型需在用户控制台确认 | [Tencent Cloud migration announcement](https://cloud.tencent.com/announce/detail/2287) |
| Volcengine Ark / Doubao | ark-safe-experience-mode | 新用户赠额 / 免费使用上限 | 符合条件的账号在安全体验模式下最多可用 500,000 Token；各模型另有额度 | Token/账号模式 | 动态 / 账号内确认 | 符合条件的账号一次性启用；达到上限后暂停 | 仅限此前未开通模型服务或未使用过安全体验模式的账号 | 未知 | 未知 | 未知 | 账号共享 | 模型另有独立速率限制；插件、知识库、批处理可能另行计费 | [Ark Safe Experience mode](https://docs.volcengine.com/docs/ark/free-tokens-only-mode?lang=zh) |

## OpenAI-Compatible API 配置示例

将 API Key 放在环境变量中，替换 Base URL 和 Model ID。仅对标记为 `yes` 的端点直接套用；`partial` 可能不支持全部 OpenAI 参数。原生协议平台应使用各自 SDK/文档。

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["LLM_API_KEY"],
    base_url=os.environ["LLM_BASE_URL"],
)

response = client.chat.completions.create(
    model=os.environ["LLM_MODEL_ID"],
    messages=[{"role": "user", "content": "用两句话介绍不确定性量化。"}],
)
print(response.choices[0].message.content)
```

例如 OpenRouter 的 Base URL 为 `https://openrouter.ai/api/v1`；每家服务商的 API Key、模型 ID、模型可用性和条款不同。不要将密钥写入仓库。

## 待复核、已停止与历史平台

下面的条目尚无足够当前官方证据，或服务已停止/迁移；不会进入当前免费推荐列表。

| 平台 | 状态 | 官方来源 | 原因/证据缺口 |
| --- | --- | --- | --- |
| AI21 Labs | 待复核 | [AI21 Labs follow-up review](https://docs.ai21.com/) | 本轮未能从当前官方定价资料确认 API 免费额度、试用金或适用模型 ID。 |
| Anthropic Claude API (protocol reference) | 未验证 | [Anthropic Messages API](https://docs.anthropic.com/en/api/messages) | 此项仅作为 API 协议参考；本目录未确认 Claude API 的通用免费额度。 |
| Baichuan AI API | 待复核 | [Baichuan follow-up review](https://platform.baichuan-ai.com/docs) | 本轮未能从当前官方 API/模型目录确认免费政策；历史或活动页面还需对照当前接口复核。 |
| Baidu Qianfan / ERNIE | 历史记录 | [Baidu historical free-model announcement](https://cloud.baidu.com/news/news_c7a145b9-5c99-4870-939f-e09ba506aab3) | 可查到 2024 年官方免费公告，但当前资料未能确认相应模型 API 仍可用；暂保留为历史线索。 |
| DeepInfra | 已复核：当前未确认免费 API | [DeepInfra pricing and billing](https://deepinfra.com/pricing) | 当前官方定价列出付费价格，API 调用需要绑卡或预付费；未确认通用免费额度。 |
| DeepSeek API | 已复核：当前未确认免费 API | [DeepSeek API pricing](https://api-docs.deepseek.com/quick_start/pricing) | 当前官方 API 定价为按量收费；未确认通用免费额度。开源权重和第三方托管不计入官方 API 免费。 |
| Fireworks AI | 待复核 | [Fireworks AI pricing](https://fireworks.ai/pricing) | 当前定价页未确认免费余额；旧的 $1 赠额资料可能已经过期，需继续复核。 |
| GitHub Models (retired service) | 已停止 / 已下架 | [GitHub Models documentation](https://docs.github.com/en/github-models) | GitHub Models 已于 2026-07-30 停止；保留此条仅作历史记录。 |
| Hyperbolic | 待复核 | [Hyperbolic follow-up review](https://docs.hyperbolic.xyz/) | 当前官方资料中未找到免费托管 API 额度、试用金额或免费模型名单。 |
| iFlytek Spark API | 待复核 | [iFlytek Spark follow-up review](https://www.xfyun.cn/doc/spark/Web.html) | 本轮未能确认当前 API 免费额度、适用模型 ID 或有效期。 |
| MiniMax API | 待复核 | [MiniMax API follow-up review](https://platform.minimaxi.com/document/) | 本轮未能从当前官方页面确认 API 价格和免费赠额；资格可能随地区或账号变化。 |
| Moonshot / Kimi API | 已复核：当前未确认免费 API | [Moonshot API pricing](https://platform.moonshot.cn/docs/pricing/chat) | 当前官方 API 按模型和 Token 计费；未确认通用免费 API 赠额。 |
| Nebius AI Studio | 待复核 | [Nebius AI Studio follow-up review](https://dev.nebius.com/) | 有开发者计划优惠的线索，但未找到当前 API 赠额金额、资格、有效期和适用模型。 |
| NVIDIA Build / API Catalog | 待复核 | [NVIDIA NIM getting started](https://docs.nvidia.com/nim/large-language-models/latest/get-started/) | 官方资料支持试用托管 NIM，但未确认特定模型可用的稳定免费 API 额度；免费开发者会员和自行部署不计入。 |
| OpenAI API (protocol reference) | 未验证 | [OpenAI API reference](https://platform.openai.com/docs/api-reference) | 此项仅作为 API 协议参考；本目录未确认 OpenAI API 的通用免费额度。 |
| SambaNova Cloud | 已复核：当前未确认免费 API | [SambaCloud plans and billing](https://cloud.sambanova.ai/plans) | 当前 Free 方案可浏览控制台，但调用 API 需要添加付款方式并购买额度；不计作免费推理。 |
| Tencent Cloud Hunyuan API (legacy platform) | 历史记录 | [Tencent Cloud migration announcement](https://cloud.tencent.com/announce/detail/2287) | 旧混元 API 平台已于 2026-09-30 停止；迁移用户可领取独立的 TokenHub 体验额度。 |
| Together AI | 已复核：当前未确认免费 API | [Together AI free-tier and billing update](https://support.together.ai/articles/1862638756-changes-to-free-tier-and-billing-july-2025) | 官方支持文章称当前没有免费试用，API 使用需先购买最低额度；低价或开源权重不算免费托管 API。 |
| 01.AI Yi API | 待复核 | [01.AI follow-up review](https://platform.lingyiwanwu.com/docs) | 本轮未能从当前公开官方页面确认免费 API 价格或额度；开源权重不代表托管 API 免费。 |

## 数据和更新规则

- `data/manual_catalog.json` 保存人工核实的提供商、Offer、型号及官方证据；`data/free_api_catalog.json` 是合并后的输出。
- `data/translations_zh.json` 只负责中文显示文本，不替代或改变官方证据字段。
- `data/free_api_catalog.csv` 与 JSON 由同一次更新生成；模型记录按 `provider_id + model_id + offer_id` 去重，不能跨平台合并同名模型。
- `free_quota` 表示免费总量、赠额或模型价格；`rate_limits` 单独记录 RPM、TPM、RPD 等速率/并发限制。
- 模型清单 API 只证明模型存在；只有官方价格或官方免费政策证据才能把它列为免费。
- 网络失败会保留旧自动记录并标记为 `stale`，不进入推荐表；完整 API 成功确认模型消失或价格变化后才会标记 `withdrawn`。
- 自动目录抓取不会将抓取日期当成每个平台的政策验证日期；人工记录的 `verified_at` 只在核对证据后修改。

## 本地验证

```powershell
python scripts/update_catalog.py
python scripts/validate_catalog.py
python scripts/score_models.py
python scripts/render_docs.py
python -m unittest discover -s tests -v
```

仓库中的 `.github/workflows/update-catalog.yml` 每天 UTC 00:00 运行，执行验证和测试后才允许生成自动更新提交。该工作流只对模型目录进行自动化检查，人工政策条目仍以 `manual_catalog.json` 的官方证据和复核日期为准。

## 免责声明与隐私提醒

免费额度、价格、模型路由、可用区域、速率限制、服务条款和数据处理方式都可能变化。生产调用前请打开来源链接复核。不要将个人数据、私有代码、密钥或受限数据发送给不了解的数据处理方；不要绕过服务条款、访问控制、速率限制、实名要求或地区限制。

本目录不是法律、安全、采购、隐私或合规建议。详见 [免责声明](docs/disclaimer.md)、[隐私与风险说明](docs/privacy-and-risk.md) 和 [免费 API 指南](docs/free-api-guide.md)。

## License

MIT License. See [LICENSE](LICENSE).
