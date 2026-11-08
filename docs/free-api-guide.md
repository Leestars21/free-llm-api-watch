# 免費 API 使用指南

最近證據核驗日期：2026-11-08

## 免費方式

| 類型 | 含義 |
| --- | --- |
| `free_model` | 官方資料確認特定模型 API 價格為零，或明確列為免費模型。 |
| `stable_free_tier` | 持續免費層；仍可能有額度、RPM、TPM 或模型准入限制。 |
| `monthly_evaluation_tier` | 每月重置的評估额度；例如共享的月度 API 調用次數。 |
| `new_user_credit` | 符合條件的新用户可领取的 Token 或用量上限，常有地区与有效期限制。 |
| `trial_credit` | 一次性或限时评估额度，不代表长期免费。 |
| `limited_time_promotion` | 明确限定活动时间和资格的免费方案。 |
| `community_volunteer` | 依赖志愿算力，模型、排队时间和吞吐量会动态变化。 |

## 已确认方案

| 平台 | 类型 | 额度 | 单位 | 适用范围 | 有效期 | 绑卡/实名/地区 | 官方来源 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AI Horde / AI Horde OpenAI API | 社区志愿算力（动态排队） | 没有固定 Token / 请求赠额；匿名访问可使用社区志愿算力，排队优先级最低 | 志愿算力容量 | 平台共享 | 试运行服务，范围可能调整 | 绑卡 否；实名 未知；地区 未说明 | [AI Horde OpenAI API docs](https://oai.aihorde.net/) |
| Alibaba Cloud Model Studio / Qwen | 新用户赠额 / 免费使用上限 | 符合条件的新账号通常每个模型获得约 100 万 Token；具体额度因模型而异 | Token/模型 | 按模型独立 | 按模型激活、发布或审批时间起算 90 天；以控制台为准 | 绑卡 未知；实名 是；地区 仅限中国北京地域且账号符合资格 | [Model Studio new-user free quota](https://help.aliyun.com/zh/model-studio/new-free-quota/) |
| Baidu Qianfan / ERNIE | 新用户赠额 / 免费使用上限 | 新用户 20 元优惠券；官方产品页未列出具体免费 API 型号。 | 人民币 | 一次性 | 发放后一个月。 | 绑卡 未知；实名 是；地区 账号地区与手机号要求待核对。 | [Baidu Qianfan new-user coupon](https://cloud.baidu.com/doc/Qianfan/index.html) |
| Cerebras Inference | 一次性试用额度 | 一次性 5 美元推广额度，有效 30 天；需有效支付方式，不会自动扣款；到期或用尽后 API 暂停，除非另购 PayGo。 | 美元抵扣额 | 一次性 | 激活后 30 天；定价页未公布单独活动截止日。 | 绑卡 是；实名 未知；地区 未知 | [Cerebras current pricing](https://www.cerebras.ai/pricing) |
| Cloudflare Workers AI | 长期免费层（有用量/速率限制） | 每天 10,000 Neurons | Neurons/天 | 账号共享 | 官方未公布固定结束日期 | 绑卡 未知；实名 未知；地区 未说明 | [Workers AI pricing and changelog](https://developers.cloudflare.com/workers-ai/platform/pricing/) |
| Cohere API | 每月免费评估额度 | 符合条件的评估 Key 每月最多 1,000 次 API 调用，多个端点共享；另有端点/型号 RPM 限制。 | 次模型调用/月 | 账号共享 | 评估 Key 资格；生产用途需申请 Production Key。 | 绑卡 未知；实名 未知；地区 未说明 | [Cohere rate limits and model access](https://docs.cohere.com/v2/docs/rate-limits) |
| Google Gemini API / Google AI Studio | 长期免费层（有用量/速率限制） | 指定模型输入/输出价格为 $0；每个项目的免费层限额按模型和账号而异 | 模型价格与账号速率限制 | 按模型独立 | 未公布固定结束日期；模型和地区资格可能变化 | 绑卡 否；实名 未知；地区 可用国家 / 地区因模型和账号而异 | [Gemini Developer API pricing and rate limits](https://ai.google.dev/gemini-api/docs/pricing) |
| GroqCloud | 长期免费层（有用量/速率限制） | Free Plan 内可免费调用列出的模型，但受每个模型的速率上限约束；没有单独赠送 Token 包 | 免费计划调用（受型号速率限制） | 账号共享 | 未公布固定结束日期；免费计划条款和模型可用性可能变化 | 绑卡 未知；实名 未知；地区 未说明 | [Groq Free Plan rate limits and supported models](https://console.groq.com/docs/rate-limits) |
| Hugging Face Inference Providers | 长期免费层（有用量/速率限制） | 免费账号每月共享 $0.10 推理额度；政策可能调整 | 美元额度/月 | 账号共享 | 按 Hugging Face 当前政策续发；各模型没有独立固定额度 | 绑卡 未知；实名 未知；地区 未说明 | [Inference Providers pricing](https://huggingface.co/docs/inference-providers/en/pricing) |
| Mistral La Plateforme | 长期免费层（有用量/速率限制） | Free 模式提供账号级月度用量预算；公开文档没有给出统一数值 | 账号用量预算 | 账号共享 | 官方未公布固定结束日期 | 绑卡 否；实名 未知；地区 未说明 | [Mistral free mode and usage limits](https://docs.mistral.ai/admin/billing-usage/usage-limits) |
| ModelScope Inference / 魔搭社区 | 长期免费层（有用量/速率限制） | 注册账号每日 200 MoLi 积分，平台内多种推理/训练任务共享。 | MoLi 积分/天 | 账号共享 | 每日额度及累计积分有效期以当前积分规则为准 | 绑卡 否；实名 未知；地区 未说明 | [ModelScope MoLi points announcement](https://www.modelscope.cn/posts/435591) |
| Novita AI | 限时活动 | 当前模型页显示输入和输出均为每百万 Token $0，属于上线促销 | 美元/百万 Token | 按模型独立 | 上线促销；已核对页面未注明结束日期 | 绑卡 未知；实名 未知；地区 未说明 | [Novita Apodex 1.1 Mini launch and pricing](https://blogs.novita.ai/apodex-1-1-mini-on-novita-ai-api-quickstart-pricing/) |
| Novita AI | 限时活动 | 部分 Ling 3.0 型号当前显示输入/输出 $0；目录将其标记为限时免费 | 美元/百万 Token | 按模型独立 | 限时活动；已核对页面未注明结束日期 | 绑卡 未知；实名 未知；地区 未说明 | [Novita Ling 3.0 model details](https://novita.ai/pricing) |
| Novita AI | 指定免费模型 | 当前模型页显示输入和输出均为每百万 Token $0 | 美元/百万 Token | 按模型独立 | 价格可能变化；使用前请复核模型页 | 绑卡 未知；实名 未知；地区 未说明 | [Novita Ling 3.1 Flash model details](https://novita.ai/models/model-detail/inclusionai-ling-3.1-flash?from=pricing) |
| Novita AI | 新用户赠额 / 免费使用上限 | 成功邀请后，邀请人与受邀人各得 $10；邀请人奖励累计上限 $500 | 美元 | 按用户 | 已核对的邀请页面未说明条款和额度有效期 | 绑卡 未知；实名 未知；地区 未说明 | [Novita referral program](https://novita.ai/referral/) |
| Ollama Cloud | 长期免费层（有用量/速率限制） | Free 方案每月包含部分云端模型的起步用量；额度数值未公开，在账号内显示；最多 1 个并发请求 | 额度积分（数值未公开） | 账号共享 | 每月额度；具体规则以账号页面为准 | 绑卡 未知；实名 未知；地区 未说明 | [Ollama Cloud pricing](https://www.ollama.com/pricing) |
| OpenRouter | 免费路由模型 | 没有 Token 赠额；仅当前 API 返回所有价格维度均为零的模型按免费路由处理 | 模型价格 | 账号共享 | 模型的免费状态可能随时变化 | 绑卡 未知；实名 未知；地区 未说明 | [OpenRouter free model rate limits](https://openrouter.ai/collections/free-models) |
| Reka AI Vision API | 一次性试用额度 | 符合条件的新用户可试用 180 分钟视频索引 | 视频分钟 | 一次性 | 注册时显示试用条款；已核对定价页未写明到期日 | 绑卡 未知；实名 未知；地区 未说明 | [Reka Vision API pricing](https://docs.reka.ai/vision/pricing) |
| Replicate | 一次性试用额度 | 部分模型可在短期评估期间免费运行；未公布统一额度 | 未知 | 一次性 | 模型要求设置账单时，免费评估即结束 | 绑卡 未知；实名 未知；地区 未说明 | [Replicate billing documentation](https://replicate.com/docs/topics/billing) |
| SiliconFlow | 指定免费模型 | 实时模型广场中部分型号调用价为零；没有统一的平台 Token 赠额 | 动态型号目录 | 按模型独立 | 型号资格随实时模型目录变化 | 绑卡 未知；实名 是；地区 未说明 | [SiliconFlow rate limits and model gallery](https://docs.siliconflow.cn/docs/userguide/faqs/rate-limit-and-upgradation) |
| Tencent Cloud TokenHub | 限时活动 | 适用语言模型每个型号 100 万 Token；每个型号需冻结 10 美元账户余额/额度，删除端点后返还。 | Token/模型 | 按模型独立 | 领取后一年；活动截止 2026-12-31。 | 绑卡 未知；实名 未知；地区 账号地区及资格请在 TokenHub 控制台核对。 | [TokenHub free experience package terms](https://intl.cloud.tencent.com/zh/document/product/1300/80423) |
| Tencent Cloud TokenHub | 一次性试用额度 | 公告未公布额度；仅符合条件的旧平台迁移用户可领取。 | 未知 | 一次性 | 公告称领取后 3 个月。 | 绑卡 未知；实名 未知；地区 以迁移用户账号资格为准。 | [Tencent Cloud migration announcement](https://cloud.tencent.com/announce/detail/2287) |
| Vercel AI Gateway | 长期免费层（有用量/速率限制） | 符合条件的 Free 团队账号每月有 $5 AI Gateway 额度 | 美元额度/月 | 账号共享 | 购买额度后不再享有免费月额度 | 绑卡 是；实名 未知；地区 未说明 | [Vercel AI Gateway pricing and live model catalog](https://vercel.com/docs/ai-gateway/pricing) |
| Volcengine Ark / Doubao | 新用户赠额 / 免费使用上限 | 符合条件的账号在安全体验模式下最多可用 500,000 Token；各模型另有额度 | Token/账号模式 | 账号共享 | 仅限此前未开通模型服务或未使用过安全体验模式的账号 | 绑卡 未知；实名 未知；地区 未说明 | [Ark Safe Experience mode](https://docs.volcengine.com/docs/ark/free-tokens-only-mode?lang=zh) |
| Zhipu BigModel / GLM | 指定免费模型 | 官方公告称 GLM-4.7-Flash API 输入和输出 Token 免费；公告未说明请求上限 | 模型价格 | 按模型独立 | 公告未注明固定结束日期 | 绑卡 未知；实名 未知；地区 未说明 | [Zhipu GLM-4.7-Flash announcement](https://www.zhipuai.cn/zh/news/148) |

## 核心 LLM

模型类型与使用能力分开记录。`text_llm` 是文本 LLM；`multimodal_llm` 同时支持文本交互和至少一种非文本模态。模型清单可证明型号存在，只有独立免费政策或官方价格才能证明免费。

### 型号、方案与接入

| 平台 | 精确 Model ID | 类型 | Offer ID | 免费类型 | 额度范围 | API Base | OpenAI 兼容 | 来源 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Alibaba Cloud Model Studio / Qwen | qwen3.8-max | 文本大语言模型 | model-studio-new-user-model-quota | 新用户赠额 / 免费使用上限 | 符合条件的新账号通常每个模型获得约 100 万 Token；具体额度因模型而异 | https://dashscope.aliyuncs.com/compatible-mode/v1 | 是 | [Model Studio new-user free quota example](https://help.aliyun.com/zh/model-studio/new-free-quota/) |
| Cloudflare Workers AI | @cf/google/gemma-4-26b-a4b-it | 文本大语言模型 | workers-ai-daily-neurons | 长期免费层（有用量/速率限制） | 每天 10,000 Neurons | https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/run | 部分兼容 | [Cloudflare Workers AI model catalog](https://developers.cloudflare.com/workers-ai/models/) |
| Cloudflare Workers AI | @cf/zai-org/glm-4.7-flash | 文本大语言模型 | workers-ai-daily-neurons | 长期免费层（有用量/速率限制） | 每天 10,000 Neurons | https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/run | 部分兼容 | [Workers AI GLM-4.7-Flash model page](https://developers.cloudflare.com/workers-ai/models/glm-4.7-flash/) |
| Cohere API | command-a-03-2025 | 文本大语言模型 | cohere-evaluation-key | 每月免费评估额度 | 符合条件的评估 Key 每月最多 1,000 次 API 调用，多个端点共享；另有端点/型号 RPM 限制。 | https://api.cohere.com/v2 | 部分兼容 | [Cohere models catalog](https://docs.cohere.com/v1/docs/models) |
| Cohere API | command-r7b-12-2024 | 文本大语言模型 | cohere-evaluation-key | 每月免费评估额度 | 符合条件的评估 Key 每月最多 1,000 次 API 调用，多个端点共享；另有端点/型号 RPM 限制。 | https://api.cohere.com/v2 | 部分兼容 | [Cohere models catalog](https://docs.cohere.com/v1/docs/models) |
| Cohere API | north-mini-code-1.0 | 文本大语言模型 | cohere-evaluation-key | 每月免费评估额度 | 符合条件的评估 Key 每月最多 1,000 次 API 调用，多个端点共享；另有端点/型号 RPM 限制。 | https://api.cohere.com/v2 | 部分兼容 | [Cohere North Mini Code model](https://docs.cohere.com/docs/north-mini-code-1.0) |
| Google Gemini API / Google AI Studio | gemini-3.1-flash-lite | 多模态大语言模型 | gemini-api-free-tier | 长期免费层（有用量/速率限制） | 指定模型输入/输出价格为 $0；每个项目的免费层限额按模型和账号而异 | https://generativelanguage.googleapis.com | 部分兼容 | [Gemini 3.1 Flash-Lite model and pricing](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite) |
| Google Gemini API / Google AI Studio | gemini-3.5-flash-lite | 多模态大语言模型 | gemini-api-free-tier | 长期免费层（有用量/速率限制） | 指定模型输入/输出价格为 $0；每个项目的免费层限额按模型和账号而异 | https://generativelanguage.googleapis.com | 部分兼容 | [Gemini 3.5 Flash-Lite model and pricing](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite) |
| GroqCloud | openai/gpt-oss-120b | 文本大语言模型 | groqcloud-free-plan | 长期免费层（有用量/速率限制） | Free Plan 内可免费调用列出的模型，但受每个模型的速率上限约束；没有单独赠送 Token 包 | https://api.groq.com/openai/v1 | 是 | [Groq Free Plan limits and supported models](https://console.groq.com/docs/rate-limits) |
| GroqCloud | openai/gpt-oss-20b | 文本大语言模型 | groqcloud-free-plan | 长期免费层（有用量/速率限制） | Free Plan 内可免费调用列出的模型，但受每个模型的速率上限约束；没有单独赠送 Token 包 | https://api.groq.com/openai/v1 | 是 | [Groq Free Plan limits and supported models](https://console.groq.com/docs/rate-limits) |
| GroqCloud | qwen/qwen3.8-27b | 文本大语言模型 | groqcloud-free-plan | 长期免费层（有用量/速率限制） | Free Plan 内可免费调用列出的模型，但受每个模型的速率上限约束；没有单独赠送 Token 包 | https://api.groq.com/openai/v1 | 是 | [Groq Free Plan limits and supported models](https://console.groq.com/docs/rate-limits) |
| Novita AI | apodex/apodex-1.1-mini | 文本大语言模型 | novita-apodex-1-1-mini-launch-promotion | 限时活动 | 当前模型页显示输入和输出均为每百万 Token $0，属于上线促销 | https://api.novita.ai/openai | 是 | [Novita Apodex 1.1 Mini model details](https://novita.ai/models/model-detail/apodex-apodex-1.1-mini?from=pricing) |
| Novita AI | inclusionai/ling-3.0-flash-fin | 文本大语言模型 | novita-ling-3-0-limited-promotion | 限时活动 | 部分 Ling 3.0 型号当前显示输入/输出 $0；目录将其标记为限时免费 | https://api.novita.ai/openai | 是 | [Novita Ling 3.0 Flash Fin model details](https://novita.ai/models/model-detail/inclusionai-ling-3.0-flash-fin) |
| Novita AI | inclusionai/ling-3.0-flash-sante | 文本大语言模型 | novita-ling-3-0-limited-promotion | 限时活动 | 部分 Ling 3.0 型号当前显示输入/输出 $0；目录将其标记为限时免费 | https://api.novita.ai/openai | 是 | [Novita Ling 3.0 Flash Sante model details](https://novita.ai/models/model-detail/inclusionai-ling-3.0-flash-sante?from=pricing) |
| Novita AI | inclusionai/ling-3.0-flash-vl | 多模态大语言模型 | novita-ling-3-0-limited-promotion | 限时活动 | 部分 Ling 3.0 型号当前显示输入/输出 $0；目录将其标记为限时免费 | https://api.novita.ai/openai | 是 | [Novita Ling 3.0 Flash VL model details](https://novita.ai/models/model-detail/inclusionai-ling-3.0-flash-vl) |
| Novita AI | inclusionai/ling-3.1-flash | 文本大语言模型 | novita-ling-3-1-flash-free | 指定免费模型 | 当前模型页显示输入和输出均为每百万 Token $0 | https://api.novita.ai/openai | 是 | [Novita Ling 3.1 Flash model details](https://novita.ai/models/model-detail/inclusionai-ling-3.1-flash?from=pricing) |
| OpenRouter | cohere/north-mini-code:free | 文本大语言模型 | openrouter-free-model-route | 免费路由模型 | 没有 Token 赠额；仅当前 API 返回所有价格维度均为零的模型按免费路由处理 | https://openrouter.ai/api/v1 | 是 | [OpenRouter models API](https://openrouter.ai/api/v1/models) |
| OpenRouter | dots-studio/dots-3-note-preview:free | 多模态大语言模型 | openrouter-free-model-route | 免费路由模型 | 没有 Token 赠额；仅当前 API 返回所有价格维度均为零的模型按免费路由处理 | https://openrouter.ai/api/v1 | 是 | [OpenRouter models API](https://openrouter.ai/api/v1/models) |
| OpenRouter | google/gemma-4-26b-a4b-it:free | 多模态大语言模型 | openrouter-free-model-route | 免费路由模型 | 没有 Token 赠额；仅当前 API 返回所有价格维度均为零的模型按免费路由处理 | https://openrouter.ai/api/v1 | 是 | [OpenRouter models API](https://openrouter.ai/api/v1/models) |
| OpenRouter | google/gemma-4-31b-it:free | 多模态大语言模型 | openrouter-free-model-route | 免费路由模型 | 没有 Token 赠额；仅当前 API 返回所有价格维度均为零的模型按免费路由处理 | https://openrouter.ai/api/v1 | 是 | [OpenRouter models API](https://openrouter.ai/api/v1/models) |
| OpenRouter | liquid/lfm-2.5-2.6b:free | 文本大语言模型 | openrouter-free-model-route | 免费路由模型 | 没有 Token 赠额；仅当前 API 返回所有价格维度均为零的模型按免费路由处理 | https://openrouter.ai/api/v1 | 是 | [OpenRouter models API](https://openrouter.ai/api/v1/models) |
| OpenRouter | liquid/lfm-3-1.7b:free | 文本大语言模型 | openrouter-free-model-route | 免费路由模型 | 没有 Token 赠额；仅当前 API 返回所有价格维度均为零的模型按免费路由处理 | https://openrouter.ai/api/v1 | 是 | [OpenRouter models API](https://openrouter.ai/api/v1/models) |
| OpenRouter | nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free | 多模态大语言模型 | openrouter-free-model-route | 免费路由模型 | 没有 Token 赠额；仅当前 API 返回所有价格维度均为零的模型按免费路由处理 | https://openrouter.ai/api/v1 | 是 | [OpenRouter models API](https://openrouter.ai/api/v1/models) |
| OpenRouter | nvidia/nemotron-3-ultra-550b-a55b:free | 文本大语言模型 | openrouter-free-model-route | 免费路由模型 | 没有 Token 赠额；仅当前 API 返回所有价格维度均为零的模型按免费路由处理 | https://openrouter.ai/api/v1 | 是 | [OpenRouter models API](https://openrouter.ai/api/v1/models) |
| OpenRouter | nvidia/nemotron-3.5-lightning:free | 文本大语言模型 | openrouter-free-model-route | 免费路由模型 | 没有 Token 赠额；仅当前 API 返回所有价格维度均为零的模型按免费路由处理 | https://openrouter.ai/api/v1 | 是 | [OpenRouter models API](https://openrouter.ai/api/v1/models) |
| OpenRouter | nvidia/nemotron-3.5-super-vl:free | 多模态大语言模型 | openrouter-free-model-route | 免费路由模型 | 没有 Token 赠额；仅当前 API 返回所有价格维度均为零的模型按免费路由处理 | https://openrouter.ai/api/v1 | 是 | [OpenRouter models API](https://openrouter.ai/api/v1/models) |
| OpenRouter | recursive/flint-v1.0:free | 文本大语言模型 | openrouter-free-model-route | 免费路由模型 | 没有 Token 赠额；仅当前 API 返回所有价格维度均为零的模型按免费路由处理 | https://openrouter.ai/api/v1 | 是 | [OpenRouter models API](https://openrouter.ai/api/v1/models) |
| OpenRouter | stealth/crouton-alpha | 多模态大语言模型 | openrouter-free-model-route | 免费路由模型 | 没有 Token 赠额；仅当前 API 返回所有价格维度均为零的模型按免费路由处理 | https://openrouter.ai/api/v1 | 是 | [OpenRouter models API](https://openrouter.ai/api/v1/models) |
| OpenRouter | xingchen-agi/xing4.0-29b-a4b:free | 文本大语言模型 | openrouter-free-model-route | 免费路由模型 | 没有 Token 赠额；仅当前 API 返回所有价格维度均为零的模型按免费路由处理 | https://openrouter.ai/api/v1 | 是 | [OpenRouter models API](https://openrouter.ai/api/v1/models) |
| Tencent Cloud TokenHub | deepseek-v4-flash | 文本大语言模型 | tokenhub-language-model-free-package-2026 | 限时活动 | 适用语言模型每个型号 100 万 Token；每个型号需冻结 10 美元账户余额/额度，删除端点后返还。 | https://tokenhub.tencentmaas.com/v1 | 是 | [Tencent TokenHub DeepSeek V4 model guide](https://cloud.tencent.com/document/product/1823/132248) |
| Tencent Cloud TokenHub | glm-5.3-flash | 文本大语言模型 | tokenhub-language-model-free-package-2026 | 限时活动 | 适用语言模型每个型号 100 万 Token；每个型号需冻结 10 美元账户余额/额度，删除端点后返还。 | https://tokenhub.tencentmaas.com/v1 | 是 | [Tencent TokenHub model inventory](https://cloud.tencent.com/document/product/1823/130078) |
| Vercel AI Gateway | inclusionai/ling-3.1-flash-1019 | 文本大语言模型 | vercel-ai-gateway-monthly-credit | 长期免费层（有用量/速率限制） | 符合条件的 Free 团队账号每月有 $5 AI Gateway 额度 | https://ai-gateway.vercel.sh/v1 | 是 | [Vercel AI Gateway model catalog](https://vercel.com/ai-gateway/models?features=free) |
| Vercel AI Gateway | nvidia/nemotron-3.5-lightning-free | 文本大语言模型 | vercel-ai-gateway-monthly-credit | 长期免费层（有用量/速率限制） | 符合条件的 Free 团队账号每月有 $5 AI Gateway 额度 | https://ai-gateway.vercel.sh/v1 | 是 | [Vercel AI Gateway model catalog](https://vercel.com/ai-gateway/models?features=free) |
| Zhipu BigModel / GLM | glm-4.7-flash | 文本大语言模型 | bigmodel-glm-4.7-flash-free | 指定免费模型 | 官方公告称 GLM-4.7-Flash API 输入和输出 Token 免费；公告未说明请求上限 | https://open.bigmodel.cn/api/paas/v4 | 部分兼容 | [Zhipu GLM-4.7-Flash announcement](https://www.zhipuai.cn/zh/news/148) |

### 模态、能力与限速

| 平台 | Model ID | 输入模态 | 输出模态 | 能力标签 | 工具调用 | 结构化输出 | 推理 | 上下文 | 速率限制 | 免费资格 | 核验日期 | 能力依据 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Alibaba Cloud Model Studio / Qwen | qwen3.8-max | 文本 | 文本 | 未确认 | 未知 | 未知 | 未知 | 未知 | 速率限制与赠送 Token 分开；请在控制台查看 | 绑卡：未知；实名：是；地区：仅限中国北京地域且账号符合资格 | 2026-11-01 | [能力依据](https://help.aliyun.com/zh/model-studio/new-free-quota/) |
| Cloudflare Workers AI | @cf/google/gemma-4-26b-a4b-it | 文本 | 文本 | 未确认 | 未知 | 未知 | 未知 | 未知 | 另有模型级限制；部分模型不适用免费额度，请查 Workers AI 型号目录 | 绑卡：未知；实名：未知；地区：未知 | 2026-11-02 | [能力依据](https://developers.cloudflare.com/workers-ai/models/) |
| Cloudflare Workers AI | @cf/zai-org/glm-4.7-flash | 文本 | 文本 | Agent 工作流 | 支持 | 未知 | 未知 | 未知 | 另有模型级限制；部分模型不适用免费额度，请查 Workers AI 型号目录 | 绑卡：未知；实名：未知；地区：未知 | 2026-11-02 | [能力依据](https://developers.cloudflare.com/workers-ai/models/glm-4.7-flash/) |
| Cohere API | command-a-03-2025 | 文本 | 文本 | 未确认 | 未知 | 未知 | 未知 | 未知 | 聊天模型常见限制为 20 RPM；实际端点与型号限制以官方表格为准。 | 绑卡：未知；实名：未知；地区：未知 | 2026-11-01 | [能力依据](https://docs.cohere.com/v1/docs/models) |
| Cohere API | command-r7b-12-2024 | 文本 | 文本 | 未确认 | 未知 | 未知 | 未知 | 未知 | 聊天模型常见限制为 20 RPM；实际端点与型号限制以官方表格为准。 | 绑卡：未知；实名：未知；地区：未知 | 2026-11-01 | [能力依据](https://docs.cohere.com/v1/docs/models) |
| Cohere API | north-mini-code-1.0 | 文本 | 文本 | Agent 工作流, 代码生成, 长上下文 | 支持 | 支持 | 未知 | 256,000 Token | RPM 20 | 绑卡：未知；实名：未知；地区：未知 | 2026-11-02 | [能力依据](https://docs.cohere.com/docs/north-mini-code-1.0) |
| Google Gemini API / Google AI Studio | gemini-3.1-flash-lite | 音频, 图像, PDF, 文本, 视频 | 文本 | Agent 工作流, 图像理解, 长上下文, 推理 | 支持 | 支持 | 支持 | 1,048,576 Token | RPM / TPM / RPD 依项目与模型而变；请查 AI Studio 控制台 | 绑卡：否；实名：未知；地区：可用国家 / 地区因模型和账号而异 | 2026-11-02 | [能力依据](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite) |
| Google Gemini API / Google AI Studio | gemini-3.5-flash-lite | 音频, 图像, PDF, 文本, 视频 | 文本 | Agent 工作流, 图像理解, 长上下文, 推理 | 支持 | 支持 | 支持 | 1,048,576 Token | RPM / TPM / RPD 依项目与模型而变；请查 AI Studio 控制台 | 绑卡：否；实名：未知；地区：可用国家 / 地区因模型和账号而异 | 2026-11-02 | [能力依据](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite) |
| GroqCloud | openai/gpt-oss-120b | 文本 | 文本 | Agent 工作流 | 支持 | 支持 | 未知 | 131,072 Token | RPM 30，RPD 1000，TPM 8000，TPD 200000 | 绑卡：未知；实名：未知；地区：未知 | 2026-11-02 | [能力依据](https://console.groq.com/docs/tool-use/overview) |
| GroqCloud | openai/gpt-oss-20b | 文本 | 文本 | Agent 工作流 | 支持 | 支持 | 未知 | 131,072 Token | RPM 30，RPD 1000，TPM 8000，TPD 200000 | 绑卡：未知；实名：未知；地区：未知 | 2026-11-02 | [能力依据](https://console.groq.com/docs/tool-use/overview) |
| GroqCloud | qwen/qwen3.8-27b | 文本 | 文本 | Agent 工作流 | 支持 | 支持 | 未知 | 131,072 Token | RPM 30，RPD 1000，TPM 8000，TPD 200000 | 绑卡：未知；实名：未知；地区：未知 | 2026-11-02 | [能力依据](https://console.groq.com/docs/tool-use/overview) |
| Novita AI | apodex/apodex-1.1-mini | 文本 | 文本 | 未确认 | 支持 | 支持 | 支持 | 256,000 Token | 模型页未说明固定速率限制 | 绑卡：未知；实名：未知；地区：未知 | 2026-11-01 | [能力依据](https://novita.ai/models/model-detail/apodex-apodex-1.1-mini?from=pricing) |
| Novita AI | inclusionai/ling-3.0-flash-fin | 文本 | 文本 | 未确认 | 支持 | 未知 | 支持 | 256,000 Token | 模型页未说明固定速率限制 | 绑卡：未知；实名：未知；地区：未知 | 2026-11-01 | [能力依据](https://novita.ai/models/model-detail/inclusionai-ling-3.0-flash-fin) |
| Novita AI | inclusionai/ling-3.0-flash-sante | 文本 | 文本 | 未确认 | 支持 | 未知 | 支持 | 256,000 Token | 模型页未说明固定速率限制 | 绑卡：未知；实名：未知；地区：未知 | 2026-11-01 | [能力依据](https://novita.ai/models/model-detail/inclusionai-ling-3.0-flash-sante?from=pricing) |
| Novita AI | inclusionai/ling-3.0-flash-vl | 图像, 文本, 视频 | 文本 | 图像理解 | 支持 | 未知 | 支持 | 256,000 Token | 模型页未说明固定速率限制 | 绑卡：未知；实名：未知；地区：未知 | 2026-11-02 | [能力依据](https://novita.ai/models/model-detail/inclusionai-ling-3.0-flash-vl) |
| Novita AI | inclusionai/ling-3.1-flash | 文本 | 文本 | 未确认 | 支持 | 未知 | 支持 | 256,000 Token | 模型页未说明固定速率限制 | 绑卡：未知；实名：未知；地区：未知 | 2026-11-01 | [能力依据](https://novita.ai/models/model-detail/inclusionai-ling-3.1-flash?from=pricing) |
| OpenRouter | cohere/north-mini-code:free | 文本 | 文本 | Agent 工作流 | 支持 | 未知 | 未知 | 256,000 Token | 免费账号当前通常为 20 RPM、50 RPD；累计购买额度满 $10 的账号适用更高每日额度 | 绑卡：否；实名：未知；地区：未知 | 2026-11-08 | [能力依据](https://openrouter.ai/api/v1/models) |
| OpenRouter | dots-studio/dots-3-note-preview:free | 图像, 文本 | 文本 | Agent 工作流 | 支持 | 支持 | 未知 | 512,000 Token | 免费账号当前通常为 20 RPM、50 RPD；累计购买额度满 $10 的账号适用更高每日额度 | 绑卡：否；实名：未知；地区：未知 | 2026-11-08 | [能力依据](https://openrouter.ai/api/v1/models) |
| OpenRouter | google/gemma-4-26b-a4b-it:free | 图像, 文本, 视频 | 文本 | Agent 工作流 | 支持 | 支持 | 未知 | 262,144 Token | 免费账号当前通常为 20 RPM、50 RPD；累计购买额度满 $10 的账号适用更高每日额度 | 绑卡：否；实名：未知；地区：未知 | 2026-11-08 | [能力依据](https://openrouter.ai/api/v1/models) |
| OpenRouter | google/gemma-4-31b-it:free | 图像, 文本, 视频 | 文本 | Agent 工作流 | 支持 | 支持 | 未知 | 262,144 Token | 免费账号当前通常为 20 RPM、50 RPD；累计购买额度满 $10 的账号适用更高每日额度 | 绑卡：否；实名：未知；地区：未知 | 2026-11-08 | [能力依据](https://openrouter.ai/api/v1/models) |
| OpenRouter | liquid/lfm-2.5-2.6b:free | 文本 | 文本 | Agent 工作流 | 支持 | 支持 | 未知 | 65,536 Token | 免费账号当前通常为 20 RPM、50 RPD；累计购买额度满 $10 的账号适用更高每日额度 | 绑卡：否；实名：未知；地区：未知 | 2026-11-08 | [能力依据](https://openrouter.ai/api/v1/models) |
| OpenRouter | liquid/lfm-3-1.7b:free | 文本 | 文本 | Agent 工作流 | 支持 | 支持 | 未知 | 262,144 Token | 免费账号当前通常为 20 RPM、50 RPD；累计购买额度满 $10 的账号适用更高每日额度 | 绑卡：否；实名：未知；地区：未知 | 2026-11-08 | [能力依据](https://openrouter.ai/api/v1/models) |
| OpenRouter | nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free | 音频, 图像, 文本, 视频 | 文本 | Agent 工作流 | 支持 | 未知 | 未知 | 256,000 Token | 免费账号当前通常为 20 RPM、50 RPD；累计购买额度满 $10 的账号适用更高每日额度 | 绑卡：否；实名：未知；地区：未知 | 2026-11-08 | [能力依据](https://openrouter.ai/api/v1/models) |
| OpenRouter | nvidia/nemotron-3-ultra-550b-a55b:free | 文本 | 文本 | Agent 工作流 | 支持 | 未知 | 未知 | 1,000,000 Token | 免费账号当前通常为 20 RPM、50 RPD；累计购买额度满 $10 的账号适用更高每日额度 | 绑卡：否；实名：未知；地区：未知 | 2026-11-08 | [能力依据](https://openrouter.ai/api/v1/models) |
| OpenRouter | nvidia/nemotron-3.5-lightning:free | 文本 | 文本 | Agent 工作流 | 支持 | 未知 | 未知 | 1,000,000 Token | 免费账号当前通常为 20 RPM、50 RPD；累计购买额度满 $10 的账号适用更高每日额度 | 绑卡：否；实名：未知；地区：未知 | 2026-11-08 | [能力依据](https://openrouter.ai/api/v1/models) |
| OpenRouter | nvidia/nemotron-3.5-super-vl:free | 图像, 文本, 视频 | 文本 | Agent 工作流 | 支持 | 支持 | 未知 | 1,000,000 Token | 免费账号当前通常为 20 RPM、50 RPD；累计购买额度满 $10 的账号适用更高每日额度 | 绑卡：否；实名：未知；地区：未知 | 2026-11-08 | [能力依据](https://openrouter.ai/api/v1/models) |
| OpenRouter | recursive/flint-v1.0:free | 文本 | 文本 | Agent 工作流 | 支持 | 支持 | 未知 | 262,144 Token | 免费账号当前通常为 20 RPM、50 RPD；累计购买额度满 $10 的账号适用更高每日额度 | 绑卡：否；实名：未知；地区：未知 | 2026-11-08 | [能力依据](https://openrouter.ai/api/v1/models) |
| OpenRouter | stealth/crouton-alpha | 音频, 文件, 图像, 文本, 视频 | 文本 | Agent 工作流 | 支持 | 支持 | 未知 | 1,048,576 Token | 免费账号当前通常为 20 RPM、50 RPD；累计购买额度满 $10 的账号适用更高每日额度 | 绑卡：否；实名：未知；地区：未知 | 2026-11-08 | [能力依据](https://openrouter.ai/api/v1/models) |
| OpenRouter | xingchen-agi/xing4.0-29b-a4b:free | 文本 | 文本 | Agent 工作流 | 支持 | 支持 | 未知 | 262,144 Token | 免费账号当前通常为 20 RPM、50 RPD；累计购买额度满 $10 的账号适用更高每日额度 | 绑卡：否；实名：未知；地区：未知 | 2026-11-08 | [能力依据](https://openrouter.ai/api/v1/models) |
| Tencent Cloud TokenHub | deepseek-v4-flash | 文本 | 文本 | Agent 工作流, 长上下文, 推理 | 支持 | 未知 | 支持 | 1,000,000 Token | 速率限制另行适用，未在该赠额说明中给出。 | 绑卡：未知；实名：未知；地区：账号地区及资格请在 TokenHub 控制台核对。 | 2026-11-02 | [能力依据](https://cloud.tencent.com/document/product/1823/132248) |
| Tencent Cloud TokenHub | glm-5.3-flash | 文本 | 文本 | 未确认 | 未知 | 未知 | 未知 | 未知 | 速率限制另行适用，未在该赠额说明中给出。 | 绑卡：未知；实名：未知；地区：账号地区及资格请在 TokenHub 控制台核对。 | 2026-11-02 | [能力依据](https://cloud.tencent.com/document/product/1823/130078) |
| Vercel AI Gateway | inclusionai/ling-3.1-flash-1019 | 文本 | 文本 | 未确认 | 未知 | 未知 | 未知 | 未知 | 上游服务商和模型自身的免费层速率限制仍然适用 | 绑卡：是；实名：未知；地区：未知 | 2026-11-01 | [能力依据](https://vercel.com/ai-gateway/models?features=free) |
| Vercel AI Gateway | nvidia/nemotron-3.5-lightning-free | 文本 | 文本 | 未确认 | 未知 | 未知 | 未知 | 未知 | 上游服务商和模型自身的免费层速率限制仍然适用 | 绑卡：是；实名：未知；地区：未知 | 2026-11-01 | [能力依据](https://vercel.com/ai-gateway/models?features=free) |
| Zhipu BigModel / GLM | glm-4.7-flash | 文本 | 文本 | 未确认 | 未知 | 未知 | 未知 | 未知 | 当前请求限制请在 BigModel 控制台查看 | 绑卡：未知；实名：未知；地区：未知 | 2026-11-01 | [能力依据](https://www.zhipuai.cn/zh/news/148) |

## 额度与速率限制

- `free_quota` 记录免费总量、共享余额或模型价格；`rate_limits` 单独记录 RPM、TPM、RPD、TPD 和并发上限。
- `quota_scope=per_model` 表示按型号发放；`account_shared` 表示账号共享；`one_time` 表示一次性方案。
- 若限速在平台控制台按账号或型号变化，目录不推算请求数或 Token 额度。
- `unknown` 表示当前官方证据无法确认；能力标签只有在有官方来源时才显示。

## 数据状态和接入

- `active` 表示来源在核验日期支持所述结论，不等于本项目实际发起了 API 调用。
- `stale` 表示最新自动检查失败，旧自动数据保留供复核，当前不推荐。
- `withdrawn` 表示成功的完整来源检查确认型号下架或价格不再免费。
- `verified_at` 是政策或型号证据实际核对日期，不会随自动目录抓取更新。

完整首页见 [中文 README](../README.md) 与 [English README](../README.en.md)。扩展模型见[相关 AI API 目录](related-ai-apis.md)。
