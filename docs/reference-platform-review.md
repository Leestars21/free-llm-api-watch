# 官方平台核验对照

[English](reference-platform-review.en.md) · [免费 API 指南](free-api-guide.md) · [免费 LLM 型号](free-models.md)

核验日期：2026-11-16。本次参考 [free-newapi 的官方免费额度平台清单](https://github.com/kirito8/free-newapi/blob/7d74d2340de3bd82f211574631fa1c4f5e736a0c/README.md)，逐一复核其中的国内 8 个、海外 8 个平台。参考清单用于发现平台，入库政策和模型资格依据下表中的供应商官方资料。

平台政策的复核日期与型号的复核日期分别记录。本次保留已有型号各自的核验日期；OpenRouter 模型清单仍为 2026-11-16 的 API 快照。来源摘要、核验字段和所读页面文本的哈希保存在 [source_snapshots.json](../data/source_snapshots.json)。

## 国内平台

| 平台 | 当前官方政策与条件 | 本次目录处理 | 官方来源 |
| --- | --- | --- | --- |
| SiliconFlow / 硅基流动 | 实名后可调用广场中标为免费的模型；限流按账号和模型设置，多个 Key 共享。动态限流模型随负载变化。 | 更新免费模型资格与动态限流说明，具体免费 ID 仍需查看实时广场。 | [限流与免费模型](https://docs.siliconflow.cn/docs/userguide/faqs/rate-limit-and-upgradation) |
| 火山方舟 / 豆包 | 新用户免费在线推理额度按模型独立计算，同一模型的主/子账号及基础/精调模型共享；实际余额与有效期见控制台。安心体验模式是账号开关，使用同一赠额。 | 修正共享范围，移除统一 50 万 Token 上限的说法；该数字在额度页中是计算示例。 | [免费推理额度](https://docs.volcengine.com/docs/ark/free-inference-quota?lang=zh)、[安心体验模式](https://docs.volcengine.com/docs/ark/free-tokens-only-mode?lang=zh) |
| 阿里云百炼 / Model Studio | 北京地域、符合资格并实名；通常每模型 100 万 Token，90 天有效，从适用开通、发布、审批日期中的最晚日期起算；同模型主/RAM 用户共享。 | 更新资格、起算日与额度用完即停默认关闭的说明。 | [新用户免费额度](https://help.aliyun.com/zh/model-studio/new-free-quota/) |
| 百度千帆 | 实名新用户 20 元代金券，有效期一个月。 | 更新方案核验日期，未从该方案确认精确免费模型 ID。 | [千帆产品文档](https://cloud.baidu.com/doc/Qianfan/index.html) |
| 智谱 BigModel / GLM | 当前价格表与型号指南确认 GLM-4.7-Flash、GLM-4.6V-Flash 输入/输出免费，仍有账号并发限制。 | 新增 `glm-4.6v-flash`，补齐 `glm-4.7-flash` 的 200K 上下文、思考、工具和结构化输出；保留退役型号的排除。 | [当前定价](https://docs.bigmodel.cn/cn/guide/start/pricing)、[4.7 指南](https://docs.bigmodel.cn/cn/guide/models/free/glm-4.7-flash)、[4.6V 指南](https://docs.bigmodel.cn/cn/guide/models/free/glm-4.6v-flash) |
| ModelScope / 魔搭 | 每日登录领 200 魔粒，绑定阿里云后每日再领 50；使用前需完善信息并验证邮箱。短期魔粒 24 小时、长期 90 天；API 消耗以型号详情页为准。 | 更新领取条件、绑定增额与到期规则，移除旧的统一每次调用积分估算。 | [2026-11-12 更新的官方公告](https://www.modelscope.cn/posts/435591) |
| 美团 LongCat | LongCat-2.5 标准 API 当前付费：限时输入 2 元、缓存输入 0.04 元、输出 8 元/百万 Token；购买的资源包 30 天有效。活动/邀请赠额的通用金额、资格和有效期未确认。 | 新增平台与官方接口地址，归入“已复核但未确认通用免费 API”，不建立已确认免费方案。 | [按量定价](https://longcat.chat/platform/docs/zh/api-pay-as-you-go)、[资源包](https://longcat.chat/platform/docs/zh/token-pack)、[接入文档](https://longcat.chat/platform/docs/zh) |
| 商汤 SenseNova | Token Plan 公测 ¥0/月。通用池为滚动 5 小时 120,000 积分、滚动周 1,200,000；Flash-Lite 专属池分别为 60,000 和 600,000。两层窗口同时限制。 | 新增平台、两类公测方案及 `sensenova-6.8-flash`、`sensenova-6.8-flash-lite`。按限时公测权益记录。 | [公测方案](https://www.sensenova.cn/token-plan)、[API 与积分规则](https://platform.sensenova.cn/docs) |

## 海外平台

| 平台 | 当前官方政策与条件 | 本次目录处理 | 官方来源 |
| --- | --- | --- | --- |
| Google Gemini API / AI Studio | 指定模型 Standard Free Tier 输入/输出免费；限额按项目和模型设置。此次核验的文本模型免费层不提供 Google Search/Maps grounding；免费层内容可用于改进产品。 | 新增 `gemini-4-hydrogen`、`gemini-3.8-flash`，补齐上下文和能力；更新重定向后的定价地址。 | [当前定价](https://aistudio.google.com/docs/pricing)、[Hydrogen](https://aistudio.google.com/docs/models/gemini-4-hydrogen)、[3.8 Flash](https://aistudio.google.com/docs/models/gemini-3.8-flash) |
| GroqCloud | 当前 Free Plan 表列出 10 个精确 ID；请求、Token 或音频秒限额按组织和模型设置。 | 复核现有型号资格与限速表，保留各型号原有详细能力核验日期。 | [Free Plan 限额](https://console.groq.com/docs/rate-limits) |
| Cerebras | 一次性 5 美元推广额度，激活后 30 天有效，需有效付款方式；不自动收费，耗尽/到期后暂停，另购 PayGo 后才继续付费使用。 | 保留一次性推广方案；旧 0 美元 Free Tier 与现行资料的差异仍待核验，不恢复旧型号推荐。 | [当前定价](https://www.cerebras.ai/pricing) |
| Cohere | 评估 Key 每月共享最多 1,000 次调用，文档列出的 Chat 接口为 20 RPM；生产 Key 条件另列。 | 复核每月评估方案，保持与一次性试用赠额的区分。 | [评估 Key 限额](https://docs.cohere.com/v2/docs/rate-limits) |
| Cloudflare Workers AI | 每日 10,000 Neurons，00:00 UTC 重置；部分模型需要付费方案或预付 AI Gateway credits。 | 复核每日分配与付费模型例外，保留 Neurons 单位。 | [价格及付费模型范围](https://developers.cloudflare.com/workers-ai/platform/pricing/) |
| OpenRouter | 免费模型 20 RPM；累计购买少于 10 credits 为 50 RPD，达到门槛后为 1,000 RPD；FAQ 说明 9 credits 可按取整宽限生效，实际以 Key 返回限额为准。 | 更新平台限额说明；模型清单仍保留 2026-11-16 的 17 个零价模型快照。 | [免费模型限额](https://openrouter.ai/docs/api-reference/limits) |
| NVIDIA Build / NIM | 开发者会员可免费调用指定托管端点，用于原型、研究、开发和测试；生产使用需要另行许可。未确认统一数字额度或 RPM。 | 从待核验改为已确认开发者免费端点，新增 `deepseek-ai/deepseek-v4.1-flash`、`nvidia/nemotron-3.5-lightning-30b-a3b`。 | [会员与用途](https://docs.api.nvidia.com/nim/docs/product)、[DeepSeek 免费端点](https://build.nvidia.com/deepseek-ai/deepseek-v4.1-flash)、[Nemotron 免费端点](https://build.nvidia.com/nvidia/nemotron-3.5-lightning-30b-a3b) |
| SambaNova Cloud | 当前 Free 方案可浏览控制台；发起 API 请求需添加付款方式并购买额度。 | 保持“已复核但未确认通用免费推理”，不将方案名称当作免费调用依据。 | [当前方案](https://cloud.sambanova.ai/plans) |

## 使用时需要保留的条件

- 商汤两层滚动积分上限同时生效，不能相加为固定 Token 赠额。Flash-Lite 专属池用完可消耗可用通用积分；消费返赠活动已于 2026-10-27 下线，旧返赠保留原有效期。
- Gemini 4 Hydrogen 的 1,048,576 Token 上下文由输入和输出共享，默认同步输出上限为 65,536；3.8 Flash 的输入上限为 1,048,576、输出上限为 65,536。
- GLM-4.6V-Flash 支持文件、视频、图像输入，但官方指南说明不能在同一请求中同时理解这三类输入。商汤 Flash Lite 的未确认上下文与能力字段保留为未知。
- 本次核验的 NVIDIA 托管模型页面说明会记录输入/输出，用于改进 NVIDIA 产品及 AI 模型。开发者用途限制和数据使用条款需要同时考虑。
- 本次工作核验公开官方页面，并生成目录；未使用供应商账号进行实际推理调用。领取资格、实际余额和请求成功情况仍由账号控制台及 API 测试确认。
