# Free LLM API Watch

整理国内外可通过 API 免费调用大语言模型的服务商，覆盖指定免费模型、周期性免费额度、新用户赠额和限时活动。模型资格与额度以官方来源和账号内显示为准。

**最近核验：2026-11-10** · [English](README.en.md)

## 目录统计

| 指标 | 数量 |
| --- | ---: |
| 监控提供商 | 39 |
| 有已核实免费方案的平台 | 21 |
| 核心免费 LLM（按平台 + Model ID 去重） | 34 |
| 相关 AI API 扩展 | 13 |
| 核心模型明确列为零价格 | 23 |

只统计 `active`、有官方证据、可信度为中/高且标记推荐的记录。同一个平台上的一个 Model ID 只计一次。速率限制和免费总额度分开记录。

## 快速导航

- [免费 API 平台速查](#free-api-quick-lookup)
- [长期免费与周期额度](#recurring-free-api)
- [新用户赠额与一次性试用](#new-user-credits)
- [限时活动](#limited-time-offers)
- [按用途寻找模型](#find-by-use-case)
- [按 Qwen、GLM、Gemini、DeepSeek 查找](#find-by-model-family)
- [API 接入示例](#api-setup)
- [全部核心模型](docs/free-models.md) · [相关 AI API 扩展](docs/related-ai-apis.md)
- [数据更新和来源](#data-and-sources)

<a id="free-api-quick-lookup"></a>
## 免费 API 平台速查

每家平台一行；型号只列最多 3 个已核实的核心 LLM。没有公开具体型号的动态/账号内目录会明确说明，不用平台级额度推测模型资格。

| 平台 | 免费方式 | 额度 / 限制 / 有效期 | 代表性免费 LLM | 使用条件 | OpenAI SDK | 官方详情 |
| --- | --- | --- | --- | --- | --- | --- |
| AI Horde / AI Horde OpenAI API | 社区志愿算力（动态排队） | 没有固定 Token / 请求赠额；匿名访问可使用社区志愿算力，排队优先级最低；有效期 试运行服务，范围可能调整 | 具体型号需在平台目录或账号内确认；此处不推测 | 绑卡 否；实名 未知；地区 未说明 | 是 | [AI Horde OpenAI API docs](https://oai.aihorde.net/) |
| Alibaba Cloud Model Studio / Qwen | 新用户赠额 / 免费使用上限 | 符合条件的新账号通常每个模型获得约 100 万 Token；具体额度因模型而异；有效期 按模型激活、发布或审批时间起算 90 天；以控制台为准 | `qwen3.8-max` | 绑卡 未知；实名 是；地区 仅限中国北京地域且账号符合资格 | 是 | [Model Studio new-user free quota](https://help.aliyun.com/zh/model-studio/new-free-quota/) |
| Baidu Qianfan / ERNIE | 新用户赠额 / 免费使用上限 | 新用户 20 元优惠券；官方产品页未列出具体免费 API 型号；有效期 发放后一个月 | 具体型号需在平台目录或账号内确认；此处不推测 | 绑卡 未知；实名 是；地区 账号地区与手机号要求待核对。 | 部分兼容 | [Baidu Qianfan new-user coupon](https://cloud.baidu.com/doc/Qianfan/index.html) |
| Cerebras Inference | 一次性试用额度 | 一次性 5 美元推广额度，有效 30 天；需有效支付方式，不会自动扣款；到期或用尽后 API 暂停，除非另购 PayGo；有效期 激活后 30 天；定价页未公布单独活动截止日 | 具体型号需在平台目录或账号内确认；此处不推测 | 绑卡 是；实名 未知；地区 未知 | 是 | [Cerebras current pricing](https://www.cerebras.ai/pricing) |
| Cloudflare Workers AI | 长期免费层（有用量/速率限制） | 每天 10,000 Neurons；有效期 官方未公布固定结束日期 | `@cf/google/gemma-4-26b-a4b-it`, `@cf/zai-org/glm-4.7-flash` | 绑卡 未知；实名 未知；地区 未说明 | 部分兼容 | [Workers AI pricing and changelog](https://developers.cloudflare.com/workers-ai/platform/pricing/) |
| Cohere API | 每月免费评估额度 | 符合条件的评估 Key 每月最多 1,000 次 API 调用，多个端点共享；另有端点/型号 RPM 限制；有效期 评估 Key 资格；生产用途需申请 Production Key | `command-a-03-2025`, `command-r7b-12-2024`, `north-mini-code-1.0` | 绑卡 未知；实名 未知；地区 未说明 | 部分兼容 | [Cohere rate limits and model access](https://docs.cohere.com/v2/docs/rate-limits) |
| Google Gemini API / Google AI Studio | 长期免费层（有用量/速率限制） | 指定模型输入/输出价格为 $0；每个项目的免费层限额按模型和账号而异；有效期 未公布固定结束日期；模型和地区资格可能变化 | `gemini-3.1-flash-lite`, `gemini-3.5-flash-lite` | 绑卡 否；实名 未知；地区 可用国家 / 地区因模型和账号而异 | 部分兼容 | [Gemini Developer API pricing and rate limits](https://ai.google.dev/gemini-api/docs/pricing) |
| GroqCloud | 长期免费层（有用量/速率限制） | Free Plan 内可免费调用列出的模型，但受每个模型的速率上限约束；没有单独赠送 Token 包；有效期 未公布固定结束日期；免费计划条款和模型可用性可能变化 | `openai/gpt-oss-120b`, `openai/gpt-oss-20b`, `qwen/qwen3.8-27b` | 绑卡 未知；实名 未知；地区 未说明 | 是 | [Groq Free Plan rate limits and supported models](https://console.groq.com/docs/rate-limits) |
| Hugging Face Inference Providers | 长期免费层（有用量/速率限制） | 免费账号每月共享 $0.10 推理额度；政策可能调整；有效期 按 Hugging Face 当前政策续发；各模型没有独立固定额度 | 具体型号需在平台目录或账号内确认；此处不推测 | 绑卡 未知；实名 未知；地区 未说明 | 是 | [Inference Providers pricing](https://huggingface.co/docs/inference-providers/en/pricing) |
| Mistral La Plateforme | 长期免费层（有用量/速率限制） | Free 模式提供账号级月度用量预算；公开文档没有给出统一数值；有效期 官方未公布固定结束日期 | 具体型号需在平台目录或账号内确认；此处不推测 | 绑卡 否；实名 未知；地区 未说明 | 部分兼容 | [Mistral free mode and usage limits](https://docs.mistral.ai/admin/billing-usage/usage-limits) |
| ModelScope Inference / 魔搭社区 | 长期免费层（有用量/速率限制） | 注册账号每日 200 MoLi 积分，平台内多种推理/训练任务共享；有效期 每日额度及累计积分有效期以当前积分规则为准 | 具体型号需在平台目录或账号内确认；此处不推测 | 绑卡 否；实名 未知；地区 未说明 | 是 | [ModelScope MoLi points announcement](https://www.modelscope.cn/posts/435591) |
| Novita AI | 限时活动；指定免费模型；新用户赠额 / 免费使用上限 | 当前模型页显示输入和输出均为每百万 Token $0，属于上线促销；有效期 上线促销；已核对页面未注明结束日期；部分 Ling 3.0 型号当前显示输入/输出 $0；目录将其标记为限时免费；有效期 限时活动；已核对页面未注明结束日期；另有 2 个方案 | `apodex/apodex-1.1-mini`, `inclusionai/ling-3.0-flash-fin`, `inclusionai/ling-3.0-flash-sante`；另有 2 个（[全部](docs/free-models.md)） | 绑卡 未知；实名 未知；地区 未说明 | 是 | [Novita Apodex 1.1 Mini launch and pricing](https://blogs.novita.ai/apodex-1-1-mini-on-novita-ai-api-quickstart-pricing/) |
| Ollama Cloud | 长期免费层（有用量/速率限制） | Free 方案每月包含部分云端模型的起步用量；额度数值未公开，在账号内显示；最多 1 个并发请求；有效期 每月额度；具体规则以账号页面为准 | 具体型号需在平台目录或账号内确认；此处不推测 | 绑卡 未知；实名 未知；地区 未说明 | 部分兼容 | [Ollama Cloud pricing](https://www.ollama.com/pricing) |
| OpenRouter | 免费路由模型 | 没有 Token 赠额；仅当前 API 返回所有价格维度均为零的模型按免费路由处理；有效期 模型的免费状态可能随时变化 | `cohere/north-mini-code:free`, `dots-studio/dots-3-note-preview:free`, `google/gemma-4-26b-a4b-it:free`；另有 10 个（[全部](docs/free-models.md)） | 绑卡 未知；实名 未知；地区 未说明 | 是 | [OpenRouter free model rate limits](https://openrouter.ai/collections/free-models) |
| Reka AI Vision API | 一次性试用额度 | 符合条件的新用户可试用 180 分钟视频索引；有效期 注册时显示试用条款；已核对定价页未写明到期日 | 具体型号需在平台目录或账号内确认；此处不推测 | 绑卡 未知；实名 未知；地区 未说明 | 否 | [Reka Vision API pricing](https://docs.reka.ai/vision/pricing) |
| Replicate | 一次性试用额度 | 部分模型可在短期评估期间免费运行；未公布统一额度；有效期 模型要求设置账单时，免费评估即结束 | 具体型号需在平台目录或账号内确认；此处不推测 | 绑卡 未知；实名 未知；地区 未说明 | 部分兼容 | [Replicate billing documentation](https://replicate.com/docs/topics/billing) |
| SiliconFlow | 指定免费模型 | 实时模型广场中部分型号调用价为零；没有统一的平台 Token 赠额；有效期 型号资格随实时模型目录变化 | 具体型号需在平台目录或账号内确认；此处不推测 | 绑卡 未知；实名 是；地区 未说明 | 是 | [SiliconFlow rate limits and model gallery](https://docs.siliconflow.cn/docs/userguide/faqs/rate-limit-and-upgradation) |
| Tencent Cloud TokenHub | 限时活动；一次性试用额度 | 适用语言模型每个型号 100 万 Token；每个型号需冻结 10 美元账户余额/额度，删除端点后返还；有效期 领取后一年；活动截止 2026-12-31；公告未公布额度；仅符合条件的旧平台迁移用户可领取；有效期 公告称领取后 3 个月 | `deepseek-v4-flash`, `glm-5.3-flash` | 绑卡 未知；实名 未知；地区 账号地区及资格请在 TokenHub 控制台核对。；绑卡 未知；实名 未知；地区 以迁移用户账号资格为准。 | 是 | [TokenHub free experience package terms](https://intl.cloud.tencent.com/zh/document/product/1300/80423) |
| Vercel AI Gateway | 长期免费层（有用量/速率限制） | 符合条件的 Free 团队账号每月有 $5 AI Gateway 额度；有效期 购买额度后不再享有免费月额度 | `inclusionai/ling-3.1-flash-1019`, `nvidia/nemotron-3.5-lightning-free` | 绑卡 是；实名 未知；地区 未说明 | 是 | [Vercel AI Gateway pricing and live model catalog](https://vercel.com/docs/ai-gateway/pricing) |
| Volcengine Ark / Doubao | 新用户赠额 / 免费使用上限 | 符合条件的账号在安全体验模式下最多可用 500,000 Token；各模型另有额度；有效期 仅限此前未开通模型服务或未使用过安全体验模式的账号 | 具体型号需在平台目录或账号内确认；此处不推测 | 绑卡 未知；实名 未知；地区 未说明 | 是 | [Ark Safe Experience mode](https://docs.volcengine.com/docs/ark/free-tokens-only-mode?lang=zh) |
| Zhipu BigModel / GLM | 指定免费模型 | 官方公告称 GLM-4.7-Flash API 输入和输出 Token 免费；公告未说明请求上限；有效期 公告未注明固定结束日期 | `glm-4.7-flash` | 绑卡 未知；实名 未知；地区 未说明 | 部分兼容 | [Zhipu GLM-4.7-Flash announcement](https://www.zhipuai.cn/zh/news/148) |

免费网页聊天、开源模型权重、模型 API 可见和免费 API 调用是不同概念。赠额不等于永久免费；免费层也可能有调用限制、实名、信用卡或地区要求。使用前请查看“条件”和官方详情。

<a id="recurring-free-api"></a>
## 长期免费与周期额度

包含零价格型号、持续免费层、每日积分和按月评估额度。平台级额度不保证所有目录型号都免费。

| 平台 | 免费方式 | 额度 / 限制 / 有效期 | 代表性免费 LLM | 使用条件 | OpenAI SDK | 官方详情 |
| --- | --- | --- | --- | --- | --- | --- |
| AI Horde / AI Horde OpenAI API | 社区志愿算力（动态排队） | 没有固定 Token / 请求赠额；匿名访问可使用社区志愿算力，排队优先级最低；有效期 试运行服务，范围可能调整 | 具体型号需在平台目录或账号内确认；此处不推测 | 绑卡 否；实名 未知；地区 未说明 | 是 | [AI Horde OpenAI API docs](https://oai.aihorde.net/) |
| Cloudflare Workers AI | 长期免费层（有用量/速率限制） | 每天 10,000 Neurons；有效期 官方未公布固定结束日期 | `@cf/google/gemma-4-26b-a4b-it`, `@cf/zai-org/glm-4.7-flash` | 绑卡 未知；实名 未知；地区 未说明 | 部分兼容 | [Workers AI pricing and changelog](https://developers.cloudflare.com/workers-ai/platform/pricing/) |
| Cohere API | 每月免费评估额度 | 符合条件的评估 Key 每月最多 1,000 次 API 调用，多个端点共享；另有端点/型号 RPM 限制；有效期 评估 Key 资格；生产用途需申请 Production Key | `command-a-03-2025`, `command-r7b-12-2024`, `north-mini-code-1.0` | 绑卡 未知；实名 未知；地区 未说明 | 部分兼容 | [Cohere rate limits and model access](https://docs.cohere.com/v2/docs/rate-limits) |
| Google Gemini API / Google AI Studio | 长期免费层（有用量/速率限制） | 指定模型输入/输出价格为 $0；每个项目的免费层限额按模型和账号而异；有效期 未公布固定结束日期；模型和地区资格可能变化 | `gemini-3.1-flash-lite`, `gemini-3.5-flash-lite` | 绑卡 否；实名 未知；地区 可用国家 / 地区因模型和账号而异 | 部分兼容 | [Gemini Developer API pricing and rate limits](https://ai.google.dev/gemini-api/docs/pricing) |
| GroqCloud | 长期免费层（有用量/速率限制） | Free Plan 内可免费调用列出的模型，但受每个模型的速率上限约束；没有单独赠送 Token 包；有效期 未公布固定结束日期；免费计划条款和模型可用性可能变化 | `openai/gpt-oss-120b`, `openai/gpt-oss-20b`, `qwen/qwen3.8-27b` | 绑卡 未知；实名 未知；地区 未说明 | 是 | [Groq Free Plan rate limits and supported models](https://console.groq.com/docs/rate-limits) |
| Hugging Face Inference Providers | 长期免费层（有用量/速率限制） | 免费账号每月共享 $0.10 推理额度；政策可能调整；有效期 按 Hugging Face 当前政策续发；各模型没有独立固定额度 | 具体型号需在平台目录或账号内确认；此处不推测 | 绑卡 未知；实名 未知；地区 未说明 | 是 | [Inference Providers pricing](https://huggingface.co/docs/inference-providers/en/pricing) |
| Mistral La Plateforme | 长期免费层（有用量/速率限制） | Free 模式提供账号级月度用量预算；公开文档没有给出统一数值；有效期 官方未公布固定结束日期 | 具体型号需在平台目录或账号内确认；此处不推测 | 绑卡 否；实名 未知；地区 未说明 | 部分兼容 | [Mistral free mode and usage limits](https://docs.mistral.ai/admin/billing-usage/usage-limits) |
| ModelScope Inference / 魔搭社区 | 长期免费层（有用量/速率限制） | 注册账号每日 200 MoLi 积分，平台内多种推理/训练任务共享；有效期 每日额度及累计积分有效期以当前积分规则为准 | 具体型号需在平台目录或账号内确认；此处不推测 | 绑卡 否；实名 未知；地区 未说明 | 是 | [ModelScope MoLi points announcement](https://www.modelscope.cn/posts/435591) |
| Novita AI | 指定免费模型 | 当前模型页显示输入和输出均为每百万 Token $0；有效期 价格可能变化；使用前请复核模型页 | `apodex/apodex-1.1-mini`, `inclusionai/ling-3.0-flash-fin`, `inclusionai/ling-3.0-flash-sante`；另有 2 个（[全部](docs/free-models.md)） | 绑卡 未知；实名 未知；地区 未说明 | 是 | [Novita Ling 3.1 Flash model details](https://novita.ai/models/model-detail/inclusionai-ling-3.1-flash?from=pricing) |
| Ollama Cloud | 长期免费层（有用量/速率限制） | Free 方案每月包含部分云端模型的起步用量；额度数值未公开，在账号内显示；最多 1 个并发请求；有效期 每月额度；具体规则以账号页面为准 | 具体型号需在平台目录或账号内确认；此处不推测 | 绑卡 未知；实名 未知；地区 未说明 | 部分兼容 | [Ollama Cloud pricing](https://www.ollama.com/pricing) |
| OpenRouter | 免费路由模型 | 没有 Token 赠额；仅当前 API 返回所有价格维度均为零的模型按免费路由处理；有效期 模型的免费状态可能随时变化 | `cohere/north-mini-code:free`, `dots-studio/dots-3-note-preview:free`, `google/gemma-4-26b-a4b-it:free`；另有 10 个（[全部](docs/free-models.md)） | 绑卡 未知；实名 未知；地区 未说明 | 是 | [OpenRouter free model rate limits](https://openrouter.ai/collections/free-models) |
| SiliconFlow | 指定免费模型 | 实时模型广场中部分型号调用价为零；没有统一的平台 Token 赠额；有效期 型号资格随实时模型目录变化 | 具体型号需在平台目录或账号内确认；此处不推测 | 绑卡 未知；实名 是；地区 未说明 | 是 | [SiliconFlow rate limits and model gallery](https://docs.siliconflow.cn/docs/userguide/faqs/rate-limit-and-upgradation) |
| Vercel AI Gateway | 长期免费层（有用量/速率限制） | 符合条件的 Free 团队账号每月有 $5 AI Gateway 额度；有效期 购买额度后不再享有免费月额度 | `inclusionai/ling-3.1-flash-1019`, `nvidia/nemotron-3.5-lightning-free` | 绑卡 是；实名 未知；地区 未说明 | 是 | [Vercel AI Gateway pricing and live model catalog](https://vercel.com/docs/ai-gateway/pricing) |
| Zhipu BigModel / GLM | 指定免费模型 | 官方公告称 GLM-4.7-Flash API 输入和输出 Token 免费；公告未说明请求上限；有效期 公告未注明固定结束日期 | `glm-4.7-flash` | 绑卡 未知；实名 未知；地区 未说明 | 部分兼容 | [Zhipu GLM-4.7-Flash announcement](https://www.zhipuai.cn/zh/news/148) |

<a id="new-user-credits"></a>
## 新用户赠额与一次性试用

这类额度通常有资格、领取期限或有效期；请把它与长期免费方案分开看。

| 平台 | 免费方式 | 额度 / 限制 / 有效期 | 代表性免费 LLM | 使用条件 | OpenAI SDK | 官方详情 |
| --- | --- | --- | --- | --- | --- | --- |
| Alibaba Cloud Model Studio / Qwen | 新用户赠额 / 免费使用上限 | 符合条件的新账号通常每个模型获得约 100 万 Token；具体额度因模型而异；有效期 按模型激活、发布或审批时间起算 90 天；以控制台为准 | `qwen3.8-max` | 绑卡 未知；实名 是；地区 仅限中国北京地域且账号符合资格 | 是 | [Model Studio new-user free quota](https://help.aliyun.com/zh/model-studio/new-free-quota/) |
| Baidu Qianfan / ERNIE | 新用户赠额 / 免费使用上限 | 新用户 20 元优惠券；官方产品页未列出具体免费 API 型号；有效期 发放后一个月 | 具体型号需在平台目录或账号内确认；此处不推测 | 绑卡 未知；实名 是；地区 账号地区与手机号要求待核对。 | 部分兼容 | [Baidu Qianfan new-user coupon](https://cloud.baidu.com/doc/Qianfan/index.html) |
| Cerebras Inference | 一次性试用额度 | 一次性 5 美元推广额度，有效 30 天；需有效支付方式，不会自动扣款；到期或用尽后 API 暂停，除非另购 PayGo；有效期 激活后 30 天；定价页未公布单独活动截止日 | 具体型号需在平台目录或账号内确认；此处不推测 | 绑卡 是；实名 未知；地区 未知 | 是 | [Cerebras current pricing](https://www.cerebras.ai/pricing) |
| Novita AI | 新用户赠额 / 免费使用上限 | 成功邀请后，邀请人与受邀人各得 $10；邀请人奖励累计上限 $500；有效期 已核对的邀请页面未说明条款和额度有效期 | `apodex/apodex-1.1-mini`, `inclusionai/ling-3.0-flash-fin`, `inclusionai/ling-3.0-flash-sante`；另有 2 个（[全部](docs/free-models.md)） | 绑卡 未知；实名 未知；地区 未说明 | 是 | [Novita referral program](https://novita.ai/referral/) |
| Reka AI Vision API | 一次性试用额度 | 符合条件的新用户可试用 180 分钟视频索引；有效期 注册时显示试用条款；已核对定价页未写明到期日 | 具体型号需在平台目录或账号内确认；此处不推测 | 绑卡 未知；实名 未知；地区 未说明 | 否 | [Reka Vision API pricing](https://docs.reka.ai/vision/pricing) |
| Replicate | 一次性试用额度 | 部分模型可在短期评估期间免费运行；未公布统一额度；有效期 模型要求设置账单时，免费评估即结束 | 具体型号需在平台目录或账号内确认；此处不推测 | 绑卡 未知；实名 未知；地区 未说明 | 部分兼容 | [Replicate billing documentation](https://replicate.com/docs/topics/billing) |
| Tencent Cloud TokenHub | 一次性试用额度 | 公告未公布额度；仅符合条件的旧平台迁移用户可领取；有效期 公告称领取后 3 个月 | `deepseek-v4-flash`, `glm-5.3-flash` | 绑卡 未知；实名 未知；地区 以迁移用户账号资格为准。 | 是 | [Tencent Cloud migration announcement](https://cloud.tencent.com/announce/detail/2287) |
| Volcengine Ark / Doubao | 新用户赠额 / 免费使用上限 | 符合条件的账号在安全体验模式下最多可用 500,000 Token；各模型另有额度；有效期 仅限此前未开通模型服务或未使用过安全体验模式的账号 | 具体型号需在平台目录或账号内确认；此处不推测 | 绑卡 未知；实名 未知；地区 未说明 | 是 | [Ark Safe Experience mode](https://docs.volcengine.com/docs/ark/free-tokens-only-mode?lang=zh) |

<a id="limited-time-offers"></a>
## 限时活动

活动结束时间和可用范围会变化；过期记录不会进入推荐表。

| 平台 | 免费方式 | 额度 / 限制 / 有效期 | 代表性免费 LLM | 使用条件 | OpenAI SDK | 官方详情 |
| --- | --- | --- | --- | --- | --- | --- |
| Novita AI | 限时活动 | 当前模型页显示输入和输出均为每百万 Token $0，属于上线促销；有效期 上线促销；已核对页面未注明结束日期；部分 Ling 3.0 型号当前显示输入/输出 $0；目录将其标记为限时免费；有效期 限时活动；已核对页面未注明结束日期 | `apodex/apodex-1.1-mini`, `inclusionai/ling-3.0-flash-fin`, `inclusionai/ling-3.0-flash-sante`；另有 2 个（[全部](docs/free-models.md)） | 绑卡 未知；实名 未知；地区 未说明 | 是 | [Novita Apodex 1.1 Mini launch and pricing](https://blogs.novita.ai/apodex-1-1-mini-on-novita-ai-api-quickstart-pricing/) |
| Tencent Cloud TokenHub | 限时活动 | 适用语言模型每个型号 100 万 Token；每个型号需冻结 10 美元账户余额/额度，删除端点后返还；有效期 领取后一年；活动截止 2026-12-31 | `deepseek-v4-flash`, `glm-5.3-flash` | 绑卡 未知；实名 未知；地区 账号地区及资格请在 TokenHub 控制台核对。 | 是 | [TokenHub free experience package terms](https://intl.cloud.tencent.com/zh/document/product/1300/80423) |

<a id="find-by-use-case"></a>
## 按用途寻找模型

下表只依据模型记录中的官方能力字段、模态和上下文长度筛选；不提供未经验证的性能排名。长上下文筛选阈值为已记录的上下文窗口至少 100K Token。

| 用途 | 已核实候选 |
| --- | --- |
| 普通文本生成 | [Model Studio new-user free quota example](https://help.aliyun.com/zh/model-studio/new-free-quota/) `qwen3.8-max`、[Cloudflare Workers AI model catalog](https://developers.cloudflare.com/workers-ai/models/) `@cf/google/gemma-4-26b-a4b-it`、[Workers AI GLM-4.7-Flash model page](https://developers.cloudflare.com/workers-ai/models/glm-4.7-flash/) `@cf/zai-org/glm-4.7-flash`、[Cohere models catalog](https://docs.cohere.com/v1/docs/models) `command-a-03-2025`、[Cohere models catalog](https://docs.cohere.com/v1/docs/models) `command-r7b-12-2024` |
| 推理 | [Gemini 3.1 Flash-Lite model and pricing](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite) `gemini-3.1-flash-lite`、[Gemini 3.5 Flash-Lite model and pricing](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite) `gemini-3.5-flash-lite`、[Novita Apodex 1.1 Mini model details](https://novita.ai/models/model-detail/apodex-apodex-1.1-mini?from=pricing) `apodex/apodex-1.1-mini`、[Novita Ling 3.0 Flash Fin model details](https://novita.ai/models/model-detail/inclusionai-ling-3.0-flash-fin) `inclusionai/ling-3.0-flash-fin`、[Novita Ling 3.0 Flash Sante model details](https://novita.ai/models/model-detail/inclusionai-ling-3.0-flash-sante?from=pricing) `inclusionai/ling-3.0-flash-sante` |
| 代码生成 | [Cohere North Mini Code model](https://docs.cohere.com/docs/north-mini-code-1.0) `north-mini-code-1.0` |
| 工具调用 / Agent | [Workers AI GLM-4.7-Flash model page](https://developers.cloudflare.com/workers-ai/models/glm-4.7-flash/) `@cf/zai-org/glm-4.7-flash`、[Cohere North Mini Code model](https://docs.cohere.com/docs/north-mini-code-1.0) `north-mini-code-1.0`、[Gemini 3.1 Flash-Lite model and pricing](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite) `gemini-3.1-flash-lite`、[Gemini 3.5 Flash-Lite model and pricing](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite) `gemini-3.5-flash-lite`、[Groq Free Plan limits and supported models](https://console.groq.com/docs/rate-limits) `openai/gpt-oss-120b` |
| 长上下文（≥100K） | [Cohere North Mini Code model](https://docs.cohere.com/docs/north-mini-code-1.0) `north-mini-code-1.0`、[Gemini 3.1 Flash-Lite model and pricing](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite) `gemini-3.1-flash-lite`、[Gemini 3.5 Flash-Lite model and pricing](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite) `gemini-3.5-flash-lite`、[Groq Free Plan limits and supported models](https://console.groq.com/docs/rate-limits) `openai/gpt-oss-120b`、[Groq Free Plan limits and supported models](https://console.groq.com/docs/rate-limits) `openai/gpt-oss-20b` |
| 图像理解 | [Gemini 3.1 Flash-Lite model and pricing](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite) `gemini-3.1-flash-lite`、[Gemini 3.5 Flash-Lite model and pricing](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite) `gemini-3.5-flash-lite`、[Novita Ling 3.0 Flash VL model details](https://novita.ai/models/model-detail/inclusionai-ling-3.0-flash-vl) `inclusionai/ling-3.0-flash-vl`、[OpenRouter models API](https://openrouter.ai/api/v1/models) `dots-studio/dots-3-note-preview:free`、[OpenRouter models API](https://openrouter.ai/api/v1/models) `google/gemma-4-26b-a4b-it:free` |
| 高频调用（公布了速率限制） | [Cohere North Mini Code model](https://docs.cohere.com/docs/north-mini-code-1.0) `north-mini-code-1.0` (RPM 20)、[Groq Free Plan limits and supported models](https://console.groq.com/docs/rate-limits) `openai/gpt-oss-120b` (RPM 30，RPD 1000，TPM 8000，TPD 200000)、[Groq Free Plan limits and supported models](https://console.groq.com/docs/rate-limits) `openai/gpt-oss-20b` (RPM 30，RPD 1000，TPM 8000，TPD 200000)、[Groq Free Plan limits and supported models](https://console.groq.com/docs/rate-limits) `qwen/qwen3.8-27b` (RPM 30，RPD 1000，TPM 8000，TPD 200000) |

<a id="find-by-model-family"></a>
## 按 Qwen、GLM、Gemini、DeepSeek 查找

这里只列当前免费关系已核实的对应模型；名字相似或第三方可调用不表示免费。

| 平台 | 精确 Model ID | 模型类型 | 免费类型 | 免费范围 | 官方来源 |
| --- | --- | --- | --- | --- | --- |
| Alibaba Cloud Model Studio / Qwen | qwen3.8-max | 文本大语言模型 | 新用户赠额 / 免费使用上限 | 符合条件的新账号通常每个模型获得约 100 万 Token；具体额度因模型而异 | [Model Studio new-user free quota example](https://help.aliyun.com/zh/model-studio/new-free-quota/) |
| Cloudflare Workers AI | @cf/zai-org/glm-4.7-flash | 文本大语言模型 | 长期免费层（有用量/速率限制） | 每天 10,000 Neurons | [Workers AI GLM-4.7-Flash model page](https://developers.cloudflare.com/workers-ai/models/glm-4.7-flash/) |
| Google Gemini API / Google AI Studio | gemini-3.1-flash-lite | 多模态大语言模型 | 长期免费层（有用量/速率限制） | 指定模型输入/输出价格为 $0；每个项目的免费层限额按模型和账号而异 | [Gemini 3.1 Flash-Lite model and pricing](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite) |
| Google Gemini API / Google AI Studio | gemini-3.5-flash-lite | 多模态大语言模型 | 长期免费层（有用量/速率限制） | 指定模型输入/输出价格为 $0；每个项目的免费层限额按模型和账号而异 | [Gemini 3.5 Flash-Lite model and pricing](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite) |
| GroqCloud | qwen/qwen3.8-27b | 文本大语言模型 | 长期免费层（有用量/速率限制） | Free Plan 内可免费调用列出的模型，但受每个模型的速率上限约束；没有单独赠送 Token 包 | [Groq Free Plan limits and supported models](https://console.groq.com/docs/rate-limits) |
| Tencent Cloud TokenHub | deepseek-v4-flash | 文本大语言模型 | 限时活动 | 适用语言模型每个型号 100 万 Token；每个型号需冻结 10 美元账户余额/额度，删除端点后返还。 | [Tencent TokenHub DeepSeek V4 model guide](https://cloud.tencent.com/document/product/1823/132248) |
| Tencent Cloud TokenHub | glm-5.3-flash | 文本大语言模型 | 限时活动 | 适用语言模型每个型号 100 万 Token；每个型号需冻结 10 美元账户余额/额度，删除端点后返还。 | [Tencent TokenHub model inventory](https://cloud.tencent.com/document/product/1823/130078) |
| Zhipu BigModel / GLM | glm-4.7-flash | 文本大语言模型 | 指定免费模型 | 官方公告称 GLM-4.7-Flash API 输入和输出 Token 免费；公告未说明请求上限 | [Zhipu GLM-4.7-Flash announcement](https://www.zhipuai.cn/zh/news/148) |

<a id="api-setup"></a>
## OpenAI-Compatible API 配置示例

具体模型的 API Base、兼容性、模态、工具调用、速率限制和官方来源见[完整核心模型目录](docs/free-models.md)。仅对标记为“是”的端点直接套用；“部分兼容”可能不支持全部 OpenAI 参数。

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

每家服务商都需使用自己的 API Key、Base URL 和精确 Model ID。不要将密钥写入仓库。完整请求参数见[API 使用指南](docs/free-api-guide.md)。

<a id="data-and-sources"></a>
## 数据更新与来源

- [完整核心免费模型目录](docs/free-models.md)：精确 ID、免费方案、限速、上下文、输入/输出模态、能力、API Base、来源和核验日期。
- [相关 AI API 扩展](docs/related-ai-apis.md)：Embedding、Rerank、ASR、TTS、内容审核及图像/视频/音乐生成，不计入核心 LLM 数量。
- [平台对比](docs/provider-comparison.md) · [候补与历史来源](docs/candidate-sources.md) · [变更记录](docs/changelog.md) · [API 使用指南](docs/free-api-guide.md)
- `data/manual_catalog.json` 保留人工核实的政策与型号；`data/free_api_catalog.json` 是合并后的输出。模型清单 API 只证明型号存在，不证明免费。
- 网络更新失败会保留旧自动记录并标记待复核；仅在成功完整响应确认下架或变为付费后撤销自动推荐。自动抓取不会刷新人工政策核验日期。
- [GitHub Actions 工作流](.github/workflows/update-catalog.yml) 每日 UTC 00:00 执行更新、验证、评分、文档生成和测试；来源检查失败时不会自动提交变更。

## 免责声明与隐私提醒

免费额度、价格、模型路由、可用区域、速率限制、服务条款和数据处理方式都可能变化。生产调用前请打开来源链接复核。不要将个人数据、私有代码、密钥或受限数据发送给不了解的数据处理方；不要绕过服务条款、访问控制、速率限制、实名要求或地区限制。

本目录不是法律、安全、采购、隐私或合规建议。详见 [免责声明](docs/disclaimer.md)、[隐私与风险说明](docs/privacy-and-risk.md) 和 [免费 API 指南](docs/free-api-guide.md)。

## License

MIT License. See [LICENSE](LICENSE).
