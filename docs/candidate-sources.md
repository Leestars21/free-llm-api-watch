# 候补与历史来源

本页由 provider-level 目录记录生成，涵盖本轮重点研究的国内外平台。候补不是免费 API 结论。只有官方政策与可用 API 型号均得到当前证据支持时，才进入推荐区。

## 尚待复核、非免费或仅有历史证据

| 平台 | 状态 | 官方来源 | 原因/证据缺口 |
| --- | --- | --- | --- |
| AI21 Labs | 待复核 | [AI21 Labs follow-up review](https://docs.ai21.com/) | 本轮未能从当前官方定价资料确认 API 免费额度、试用金或适用模型 ID。 |
| Anthropic Claude API (protocol reference) | 未验证 | [Anthropic Messages API](https://docs.anthropic.com/en/api/messages) | 此项仅作为 API 协议参考；本目录未确认 Claude API 的通用免费额度。 |
| Baichuan AI API | 待复核 | [Baichuan follow-up review](https://platform.baichuan-ai.com/docs) | 本轮未能从当前官方 API/模型目录确认免费政策；历史或活动页面还需对照当前接口复核。 |
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

## 已确认免费方案，但未确认具体核心 LLM 型号

以下平台确有官方免费方案，但公开来源没有列出稳定、明确适用的核心 LLM ID，或者型号资格只在动态目录/账号中显示。README 不会因此推荐未验证的具体模型。

| 平台 | 免费方式 | 额度/限制 | 账号条件与有效期 | 官方来源 |
| --- | --- | --- | --- | --- |
| AI Horde / AI Horde OpenAI API | 社区志愿算力（动态排队） | 没有固定 Token / 请求赠额；匿名访问可使用社区志愿算力，排队优先级最低 | 绑卡 否；实名 未知；地区 未说明 | [AI Horde OpenAI API docs](https://oai.aihorde.net/) |
| Baidu Qianfan / ERNIE | 新用户赠额 / 免费使用上限 | 新用户 20 元优惠券；官方产品页未列出具体免费 API 型号。 | 绑卡 未知；实名 是；地区 账号地区与手机号要求待核对。 | [Baidu Qianfan new-user coupon](https://cloud.baidu.com/doc/Qianfan/index.html) |
| Cerebras Inference | 一次性试用额度 | 一次性 5 美元推广额度，有效 30 天；需有效支付方式，不会自动扣款；到期或用尽后 API 暂停，除非另购 PayGo。 | 绑卡 是；实名 未知；地区 未知 | [Cerebras current pricing](https://www.cerebras.ai/pricing) |
| Hugging Face Inference Providers | 长期免费层（有用量/速率限制） | 免费账号每月共享 $0.10 推理额度；政策可能调整 | 绑卡 未知；实名 未知；地区 未说明 | [Inference Providers pricing](https://huggingface.co/docs/inference-providers/en/pricing) |
| Mistral La Plateforme | 长期免费层（有用量/速率限制） | Free 模式提供账号级月度用量预算；公开文档没有给出统一数值 | 绑卡 否；实名 未知；地区 未说明 | [Mistral free mode and usage limits](https://docs.mistral.ai/admin/billing-usage/usage-limits) |
| ModelScope Inference / 魔搭社区 | 长期免费层（有用量/速率限制） | 注册账号每日 200 MoLi 积分，平台内多种推理/训练任务共享。 | 绑卡 否；实名 未知；地区 未说明 | [ModelScope MoLi points announcement](https://www.modelscope.cn/posts/435591) |
| Ollama Cloud | 长期免费层（有用量/速率限制） | Free 方案每月包含部分云端模型的起步用量；额度数值未公开，在账号内显示；最多 1 个并发请求 | 绑卡 未知；实名 未知；地区 未说明 | [Ollama Cloud pricing](https://www.ollama.com/pricing) |
| Reka AI Vision API | 一次性试用额度 | 符合条件的新用户可试用 180 分钟视频索引 | 绑卡 未知；实名 未知；地区 未说明 | [Reka Vision API pricing](https://docs.reka.ai/vision/pricing) |
| Replicate | 一次性试用额度 | 部分模型可在短期评估期间免费运行；未公布统一额度 | 绑卡 未知；实名 未知；地区 未说明 | [Replicate billing documentation](https://replicate.com/docs/topics/billing) |
| SiliconFlow | 指定免费模型 | 实时模型广场中部分型号调用价为零；没有统一的平台 Token 赠额 | 绑卡 未知；实名 是；地区 未说明 | [SiliconFlow rate limits and model gallery](https://docs.siliconflow.cn/docs/userguide/faqs/rate-limit-and-upgradation) |
| Volcengine Ark / Doubao | 新用户赠额 / 免费使用上限 | 符合条件的账号在安全体验模式下最多可用 500,000 Token；各模型另有额度 | 绑卡 未知；实名 未知；地区 未说明 | [Ark Safe Experience mode](https://docs.volcengine.com/docs/ark/free-tokens-only-mode?lang=zh) |

## 复核规则

- 旧公告不能替代当前模型 API/价格证据；`historical` 记录不进入推荐。
- 开源权重、网页聊天、合作应用的内置模型或低价 Token 不证明直接托管 API 免费。
- 动态模型广场、活动额度和账户资格不稳定时，记录明确标注“动态/账号内确认”，不猜测型号或数量。
- 当前服务已停止或迁移的记录保留供检索，但 README 当前推荐表会排除它们。
