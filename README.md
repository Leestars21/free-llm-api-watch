# Free LLM API Watch

[English](README.en.md) · 项目主页：[Leestars21/free-llm-api-watch](https://github.com/Leestars21/free-llm-api-watch)

查找可以免费调用的大语言模型 API：这里整理平台、免费方式、模型和官方来源，覆盖免费层、新用户额度与限时活动。

## 从这里开始

| 平台 | 免费方式 | 额度与限制 | 核验日期 | 官方来源 |
| --- | --- | --- | --- | --- |
| Google Gemini API / Google AI Studio | 长期免费层（有用量/速率限制） | 指定模型输入/输出 Token 免费；每个项目的免费层限额按模型和账号设置；有效期 未公布固定结束日期；模型和地区资格可能变化 | 2026-11-16 | [Gemini Developer API pricing and rate limits](https://aistudio.google.com/docs/pricing) |
| GroqCloud | 长期免费层（有用量/速率限制） | Free Plan 内可免费调用列出的模型，但受每个模型的速率上限约束；没有单独赠送 Token 包；有效期 未公布固定结束日期；免费计划条款和模型可用性可能变化 | 2026-11-16 | [Groq Free Plan rate limits and supported models](https://console.groq.com/docs/rate-limits) |
| Cloudflare Workers AI | 长期免费层（有用量/速率限制） | 每天 10,000 Neurons；有效期 官方未公布固定结束日期 | 2026-11-16 | [Workers AI pricing and changelog](https://developers.cloudflare.com/workers-ai/platform/pricing/) |
| OpenRouter | 免费路由模型 | 没有 Token 赠额；仅当前 API 返回所有价格维度均为零的模型按免费路由处理；有效期 模型的免费状态可能随时变化 | 2026-11-16 | [OpenRouter free model limits](https://openrouter.ai/docs/api-reference/limits) |

以上仅是少量入口，并非排名或完整清单。免费范围、模型、地区及账号资格随时可能变化；请查看官方来源与账号控制台后再使用。各条记录的核验日期见完整目录，不应把最新日期理解为全部条目均在当天核验。

- **[查看全部平台和免费方案](docs/free-api-guide.md)**：比较额度、资格、有效期与官方来源。
- **[查看全部免费 LLM 型号](docs/free-models.md)**：精确 Model ID、API 地址、限制与逐条核验日期。
- [free-newapi 官方平台核验对照](docs/reference-platform-review.md)：16 个平台的当前政策、差异与来源。
- [平台对比](docs/provider-comparison.md) · [其他 AI API](docs/related-ai-apis.md) · [候补与历史记录](docs/candidate-sources.md)

免费层受用量和速率限制；新用户赠额与限时活动不代表长期免费。模型出现在 API 列表中也不代表调用免费。

### 🤖 让 AI 帮你找免费 API

将本仓库链接和你的使用场景发给 ChatGPT、Claude、Gemini 等 AI 助手，让它根据你的需求筛选和比较方案，省去逐个平台查看模型、额度和接口文档的时间。复制并修改下面的提示词即可：

```text
请阅读 https://github.com/Leestars21/free-llm-api-watch 的 README、免费 API 指南、免费模型清单和供应商对比文档。

我需要一个免费 API，用于 Zotero 插件中的学术论文总结，希望支持长上下文，最好兼容 OpenAI API。请根据这一用途筛选合适的方案，比较免费额度、模型能力、上下文长度、速率限制、注册条件和 OpenAI API 兼容性。

请尽可能访问供应商官方文档，核实最新免费政策和模型可用情况，并给出推荐模型的准确 Model ID、API 地址和申请入口。区分长期免费、新用户赠额和限时活动，不要将历史免费记录当作当前可用方案。无法核实的信息请明确说明，不要编造额度或可用状态。
```

AI 的推荐仅供参考；实际可用性以供应商官方文档、账号控制台及 API 测试结果为准。

## 数据与更新

目录结合官方来源和自动更新；更新失败时不会将旧数据当作最新核验。[查看更新工作流](.github/workflows/update-catalog.yml)、[变更记录](docs/changelog.md)和[隐私与风险](docs/privacy-and-risk.md)。使用前请核实条款，勿公开 API 密钥或敏感数据。

发现问题欢迎提交 Issue 或 Pull Request。MIT 许可，见 [LICENSE](LICENSE)。
