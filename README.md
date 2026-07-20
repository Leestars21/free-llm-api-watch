# Free LLM API Watch

中文 | [English](README.en.md)

本项目持续追踪可以通过 API 调用的免费、试用或低成本前沿大模型渠道，包括官方模型厂商 API、官方云平台、第三方模型聚合平台和第三方推理平台。项目只统计可通过 API 使用的渠道，不统计单纯网页或 App 免费模型。

最近一次数据更新时间：2026-07-20

当前 catalog 记录数：39

记录层级统计：`model`: 17, `provider`: 22

免费类型统计：`free_model`: 17, `not_free_or_unverified`: 22

## 结论先读

- 当前已验证进入推荐表的记录全部来自 OpenRouter 官方 models API，均为 `model` 级免费模型记录。
- 暂无已经验证的官方 provider 级免费 API 渠道记录；Gemini、Groq、Cloudflare Workers AI 等已列为 P0 复核源。
- OpenAI API 与 Anthropic Claude API 只作为协议兼容性参考源；没有官方免费 API 额度时，不得进入免费推荐表。
- 所有不确定来源都写在本文的“候补监控源与人工判断备注”中，用户应按备注自行复核。

## 数据原则

- 只用官方文档、官方 pricing 页面、官方 rate limit 页面、官方模型列表 API、官方 changelog 或可追溯的一手资料作为最终证据。
- 第三方博客、论坛、自媒体只能作为线索，不能作为推荐表证据。
- 免费额度分为 `provider`、`model`、`offer` 三层，不把平台免费层、模型免费价格和新用户试用额度混成同一类。
- 示例 JSON 中的 `yes/no/partial/unknown`、`S/S-/A+/A/B/unknown` 等只是枚举说明；实际数据只能填写一个具体值，不能把整个枚举字符串写进 catalog。
- `source_snapshots.json` 只保存证据摘要，不保存完整网页、pricing 页面正文或完整 API 响应。
- 抓取失败时不编造数据，失败项必须标为 `confidence: low` 和 `free_type: not_free_or_unverified`。

## 免责声明

- 本项目只是信息目录，不构成法律、财务、安全、采购、隐私或合规建议。
- 免费额度、模型路由、价格、模型可用性、账号要求、地区限制和服务条款都可能变化；使用前必须打开 `source_url` 复核官方来源。
- `confidence: low`、`free_type: not_free_or_unverified`、`fetch_status: failed`、`protocol reference only` 的记录不是推荐，只是候补或协议参考。
- 不要用本项目绕过服务条款、访问控制、rate limit、付费墙、实名要求、地区限制或账号要求。
- 本项目故意排除共享 API key、逆向网页接口、拼车账号、cookie/session token 中转和匿名“无限 API”网关。
- 用户需要自行评估服务条款、隐私政策、数据留存、可接受使用政策和当地法律要求。

## 数据层级

| record_level | 含义 | 示例 |
| --- | --- | --- |
| provider | 渠道级记录，说明某个平台或 API 是否存在官方免费层 | Google Gemini API 是否有 Free Tier |
| model | 模型级记录，说明某个平台上的具体模型是否免费 | OpenRouter 上某个 `:free` 模型 |
| offer | 免费额度、试用额度、活动额度记录 | 新用户 90 天 token credit |

每条记录必须包含 `record_level`、`provider_id`、`offer_id`、`is_recommended`、`recommendation_reason`。如果不确定，应明确写入 `confidence: low`、`is_recommended: false`，并把判断依据或缺口写入备注。

## 官方免费 API 渠道

_暂无符合条件的记录。_

## 第三方免费模型

| Provider | Level | Model/Offer | Free type | OpenAI | Anthropic | Confidence | Checked | Evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| OpenRouter | model | cohere/north-mini-code:free | free_model | yes | unknown | high | 2026-07-20 | https://openrouter.ai/api/v1/models |
| OpenRouter | model | google/gemma-4-26b-a4b-it:free | free_model | yes | unknown | high | 2026-07-20 | https://openrouter.ai/api/v1/models |
| OpenRouter | model | google/gemma-4-31b-it:free | free_model | yes | unknown | high | 2026-07-20 | https://openrouter.ai/api/v1/models |
| OpenRouter | model | google/lyria-3-clip-preview | free_model | yes | unknown | high | 2026-07-20 | https://openrouter.ai/api/v1/models |
| OpenRouter | model | google/lyria-3-pro-preview | free_model | yes | unknown | high | 2026-07-20 | https://openrouter.ai/api/v1/models |
| OpenRouter | model | nvidia/nemotron-3-nano-30b-a3b:free | free_model | yes | unknown | high | 2026-07-20 | https://openrouter.ai/api/v1/models |
| OpenRouter | model | nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free | free_model | yes | unknown | high | 2026-07-20 | https://openrouter.ai/api/v1/models |
| OpenRouter | model | nvidia/nemotron-3-super-120b-a12b:free | free_model | yes | unknown | high | 2026-07-20 | https://openrouter.ai/api/v1/models |
| OpenRouter | model | nvidia/nemotron-3-ultra-550b-a55b:free | free_model | yes | unknown | high | 2026-07-20 | https://openrouter.ai/api/v1/models |
| OpenRouter | model | nvidia/nemotron-3.5-content-safety:free | free_model | yes | unknown | high | 2026-07-20 | https://openrouter.ai/api/v1/models |
| OpenRouter | model | nvidia/nemotron-nano-12b-v2-vl:free | free_model | yes | unknown | high | 2026-07-20 | https://openrouter.ai/api/v1/models |
| OpenRouter | model | nvidia/nemotron-nano-9b-v2:free | free_model | yes | unknown | high | 2026-07-20 | https://openrouter.ai/api/v1/models |
| OpenRouter | model | openai/gpt-oss-20b:free | free_model | yes | unknown | high | 2026-07-20 | https://openrouter.ai/api/v1/models |
| OpenRouter | model | openrouter/free | free_model | yes | unknown | high | 2026-07-20 | https://openrouter.ai/api/v1/models |
| OpenRouter | model | poolside/laguna-m.1:free | free_model | yes | unknown | high | 2026-07-20 | https://openrouter.ai/api/v1/models |
| OpenRouter | model | poolside/laguna-xs-2.1:free | free_model | yes | unknown | high | 2026-07-20 | https://openrouter.ai/api/v1/models |
| OpenRouter | model | tencent/hy3:free | free_model | yes | unknown | high | 2026-07-20 | https://openrouter.ai/api/v1/models |

## 新用户试用额度

_暂无符合条件的记录。_

## 低价但非免费

低价但非免费记录不进入推荐表。DeepSeek、Kimi、智谱、百度千帆、Mistral、Together AI、Fireworks 等如果只有低价或未确认额度，应保留在候补区，直到官方证据证明存在免费 API 额度、免费模型、免费路由或试用额度。

## 候补待确认与参考区

| Provider | Level | Model/Offer | Free type | Confidence | Reason / Note | Checked | Evidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Alibaba Cloud Model Studio / Qwen | provider | alibaba-model-studio | not_free_or_unverified | low | candidate source; verify credit, validity period, identity and region requirements | 2026-07-20 | https://help.aliyun.com/zh/model-studio/models |
| Anthropic Claude API | provider | anthropic-api | not_free_or_unverified | medium | protocol reference only; no verified free API quota | 2026-07-20 | https://docs.anthropic.com/en/api/messages |
| Baidu Qianfan / ERNIE | provider | baidu-qianfan | not_free_or_unverified | low | candidate source; verify free quota, identity, region and billing rules | 2026-07-20 | https://cloud.baidu.com/doc/WENXINWORKSHOP/ |
| Cerebras Inference | provider | cerebras | not_free_or_unverified | low | candidate source; verify free or trial quota before recommending | 2026-07-20 | https://inference-docs.cerebras.ai/ |
| Cloudflare Workers AI | provider | cloudflare-workers-ai | not_free_or_unverified | low | candidate source; verify free allocation, account requirements, and model pricing | 2026-07-20 | https://developers.cloudflare.com/workers-ai/platform/pricing/ |
| DeepSeek API | provider | deepseek | not_free_or_unverified | low | candidate low-cost source; do not recommend as free without official free quota evidence | 2026-07-20 | https://api-docs.deepseek.com/quick_start/pricing |
| Fireworks AI | provider | fireworks-ai | not_free_or_unverified | low | P1 candidate source; verify trial credit and pricing | 2026-07-20 | https://docs.fireworks.ai/ |
| Google Gemini API / Google AI Studio | provider | google-gemini | not_free_or_unverified | low | candidate source; verify official Free Tier, rate limits, region and card requirements | 2026-07-20 | https://ai.google.dev/gemini-api/docs/pricing |
| GroqCloud | provider | groqcloud | not_free_or_unverified | low | candidate source; verify developer free limits and supported model list | 2026-07-20 | https://console.groq.com/docs/rate-limits |
| Hugging Face Inference Providers | provider | huggingface-inference-providers | not_free_or_unverified | low | candidate source; distinguish open weights from free hosted API | 2026-07-20 | https://huggingface.co/docs/inference-providers |
| Mistral La Plateforme | provider | mistral | not_free_or_unverified | low | candidate source; verify whether any free or trial API quota is currently available | 2026-07-20 | https://docs.mistral.ai/ |
| Moonshot / Kimi API | provider | moonshot-kimi | not_free_or_unverified | low | candidate source; do not recommend without official free API quota evidence | 2026-07-20 | https://platform.moonshot.cn/docs/pricing/chat |
| Nebius AI Studio | provider | nebius-ai | not_free_or_unverified | low | P1 candidate source; verify API access, credit and pricing | 2026-07-20 | https://docs.nebius.com/studio/ |
| Novita | provider | novita | not_free_or_unverified | low | P1 candidate source; verify model pricing and credits | 2026-07-20 | https://novita.ai/docs |
| NVIDIA Build / API Catalog | provider | nvidia-build | not_free_or_unverified | low | P1 candidate source; verify free credits, endpoint and model terms | 2026-07-20 | https://build.nvidia.com/ |
| OpenAI API | provider | openai-api | not_free_or_unverified | medium | protocol reference only; no verified free API quota | 2026-07-20 | https://platform.openai.com/docs/api-reference |
| Replicate | provider | replicate | not_free_or_unverified | low | P1 candidate source; model pricing varies and must be checked per model | 2026-07-20 | https://replicate.com/docs |
| SiliconFlow | provider | siliconflow | not_free_or_unverified | low | candidate source; verify official free models, trial credit and account requirements | 2026-07-20 | https://docs.siliconflow.cn/ |
| Tencent Cloud TokenHub / Hunyuan | provider | tencent-tokenhub-hunyuan | not_free_or_unverified | low | candidate source; verify API base, compatibility, free quota and identity requirements | 2026-07-20 | https://cloud.tencent.com/document/product/1729 |
| Together AI | provider | together-ai | not_free_or_unverified | low | P1 candidate source; verify new-user credit and low-cost models | 2026-07-20 | https://docs.together.ai/ |
| Volcengine Ark / Doubao | provider | volcengine-ark | not_free_or_unverified | low | candidate source; verify trial/new-user credit, model IDs and endpoint | 2026-07-20 | https://www.volcengine.com/docs/82379 |
| Zhipu BigModel / GLM | provider | zhipu-bigmodel | not_free_or_unverified | low | candidate source; do not recommend without official free API quota evidence | 2026-07-20 | https://docs.bigmodel.cn/ |

## 协议参考源

| Provider | Level | Model/Offer | Free type | Confidence | Reason / Note | Checked | Evidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Anthropic Claude API | provider | anthropic-api | not_free_or_unverified | medium | protocol reference only; no verified free API quota | 2026-07-20 | https://docs.anthropic.com/en/api/messages |
| OpenAI API | provider | openai-api | not_free_or_unverified | medium | protocol reference only; no verified free API quota | 2026-07-20 | https://platform.openai.com/docs/api-reference |

## 候补监控源与人工判断备注

以下条目来自 `data/providers.yaml` 的初始监控范围。它们不是免费 API 结论；如果状态列写了“待复核”，用户需要打开官方 source 自行判断，不要直接当作推荐。

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

## 完整字段要求

| 必填字段 |
| --- |
| provider |
| record_level |
| provider_id |
| offer_id |
| channel_type |
| country_or_region |
| official |
| api_base |
| openai_compatible |
| anthropic_compatible |
| free_type |
| free_quota |
| free_quota_unit |
| quota_reset |
| expires |
| requires_card |
| requires_identity_verification |
| requires_phone_region |
| model_id |
| model_name |
| model_family |
| context_window |
| modalities |
| tool_calling |
| structured_output |
| reasoning |
| web_search |
| coding_score_tier |
| reasoning_score_tier |
| long_context_score_tier |
| multimodal_score_tier |
| speed_tier |
| privacy_notes |
| data_training_policy |
| terms_risk |
| source_type |
| source_name |
| source_url |
| evidence_summary |
| last_checked |
| confidence |
| is_recommended |
| recommendation_reason |
| fetch_status |
| error_summary |

## 枚举值要求

| 字段 | 可选值 |
| --- | --- |
| anthropic_compatible | `no`, `partial`, `unknown`, `yes` |
| channel_type | `official_cloud_platform`, `official_model_vendor`, `shadow_or_untrusted_api`, `third_party_inference_provider`, `third_party_router` |
| coding_score_tier | `A`, `A+`, `B`, `S`, `S-`, `unknown` |
| confidence | `high`, `low`, `medium` |
| data_training_policy | `no`, `opt_out`, `unknown`, `yes` |
| fetch_status | `failed`, `manual`, `ok`, `pending` |
| free_type | `free_model`, `free_router`, `new_user_credit`, `not_free_or_unverified`, `open_weight_only`, `stable_free_tier`, `trial_credit` |
| long_context_score_tier | `A`, `A+`, `B`, `S`, `S-`, `unknown` |
| multimodal_score_tier | `A`, `A+`, `B`, `S`, `S-`, `unknown` |
| openai_compatible | `no`, `partial`, `unknown`, `yes` |
| reasoning | `supported`, `unknown`, `unsupported` |
| reasoning_score_tier | `A`, `A+`, `B`, `S`, `S-`, `unknown` |
| record_level | `model`, `offer`, `provider` |
| requires_card | `no`, `unknown`, `yes` |
| requires_identity_verification | `no`, `unknown`, `yes` |
| source_type | `independent_benchmark`, `manual`, `official_api`, `official_changelog`, `official_docs`, `official_pricing` |
| speed_tier | `fast`, `medium`, `slow`, `unknown` |
| structured_output | `supported`, `unknown`, `unsupported` |
| tool_calling | `supported`, `unknown`, `unsupported` |
| web_search | `supported`, `unknown`, `unsupported` |

## source_snapshots.json 约束

`data/source_snapshots.json` 不要保存完整网页正文、pricing 页面全文或完整 API 响应。只允许保存：

- `source_url`
- `fetched_at`
- `http_status`
- `page_title`
- `relevant_excerpt`，最多 500 字
- `extracted_fields`
- `hash`
- `parser_status`

## 抓取失败处理

抓取失败时不要编造数据。失败项应写入：

```json
{
  "fetch_status": "failed",
  "error_summary": "",
  "confidence": "low",
  "free_type": "not_free_or_unverified"
}
```

失败源需要在 `docs/candidate-sources.md` 或 `docs/changelog.md` 中标注需要人工复核。

## 推荐表约束

README 的推荐表只能展示同时满足以下条件的记录：

- 有官方证据；
- `confidence` 为 `high` 或 `medium`；
- `is_recommended` 为 `true`；
- 明确存在 API 免费额度、免费模型、免费路由或试用额度。

`confidence: low`、`not_free_or_unverified`、`protocol reference only` 的记录只能进入候补区或参考区。

## 用户决策建议

1. 先看 `free_type`：长期免费层优先于新用户信用额度；模型级免费要额外确认速率限制。
2. 再看 `record_level`：不要把 provider 级额度、model 级免费价格和 offer 级试用额度混为一谈。
3. 再看 `channel_type`：官方渠道适合更稳定的实验，第三方路由适合快速试用但要承担上游和路由层双重变更风险。
4. 检查 `openai_compatible` 和 `anthropic_compatible`：只在明确为 `yes` 或可接受 `partial` 时复用现有客户端。
5. `confidence: low`、`not_free_or_unverified`、`protocol reference only` 的记录只能当线索或协议参考，不能当免费 API 推荐。

## OpenAI-Compatible 配置模板

```env
OPENAI_API_KEY=your-provider-key
OPENAI_BASE_URL=https://openrouter.ai/api/v1
OPENAI_MODEL=provider/model:free
```

## Anthropic Messages API 配置模板

```env
ANTHROPIC_API_KEY=your-anthropic-key
ANTHROPIC_BASE_URL=https://api.anthropic.com
ANTHROPIC_MODEL=claude-model-id
```

Anthropic Claude API 在本项目中是协议参考源；除非官方免费 API 额度被验证，否则不会出现在免费推荐表。

## 本地更新

```powershell
python scripts/update_catalog.py
python scripts/validate_catalog.py
python scripts/score_models.py
python scripts/render_docs.py
python -m unittest discover -s tests -v
```

## GitHub Actions

如果 `free-llm-api-watch/` 作为独立 GitHub 仓库发布，仓库内已经包含真实工作流：

```text
.github/workflows/update-catalog.yml
```

该工作流每天 UTC 00:00 运行一次，也支持手动触发。它会执行 `update_catalog.py`、`validate_catalog.py`、`score_models.py`、`render_docs.py` 和单元测试；有变化时自动提交 `data/`、`docs/` 和 `README.md`。

如果本项目作为大仓库子目录使用，不要在父仓库根目录直接生成 workflow。可复制模板：

```text
templates/github-actions/update-catalog.yml
```

只有当用户把该模板复制到父仓库根目录 `.github/workflows/update-catalog.yml` 后，父仓库的 GitHub Actions 才会运行。模板会在根目录 checkout 后进入 `free-llm-api-watch` 再运行脚本。

## 项目结构

```text
free-llm-api-watch/
  .github/
    workflows/
      update-catalog.yml
  README.md
  README.en.md
  docs/
    free-api-guide.md
    codex-usage.md
    privacy-and-risk.md
    disclaimer.md
    provider-comparison.md
    candidate-sources.md
    changelog.md
  data/
    providers.yaml
    free_api_catalog.json
    free_api_catalog.csv
    source_snapshots.json
  scripts/
    catalog_schema.py
    update_catalog.py
    validate_catalog.py
    score_models.py
    render_docs.py
  tests/
    test_schema.py
    test_required_fields.py
  templates/github-actions/
    update-catalog.yml
  .env.example
  .gitignore
  requirements.txt
  LICENSE
```

## 风险提示

免费 API 和免费模型会频繁变化。使用前请复核 `last_checked`、`confidence`、`source_url` 和服务条款。不要把私有代码、商业数据、个人信息、密钥或受限数据发给不可信第三方路由。

更完整的免责声明见 `docs/disclaimer.md`。

## License

MIT License. See `LICENSE`.
