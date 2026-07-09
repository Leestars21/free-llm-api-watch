from __future__ import annotations

from collections import Counter, defaultdict
from typing import Any

from catalog_schema import ENUMS, PROJECT_ROOT, REQUIRED_FIELDS, load_catalog


README_PATH = PROJECT_ROOT / "README.md"
FREE_GUIDE_PATH = PROJECT_ROOT / "docs" / "free-api-guide.md"
PROVIDER_COMPARISON_PATH = PROJECT_ROOT / "docs" / "provider-comparison.md"
CANDIDATE_SOURCES_PATH = PROJECT_ROOT / "docs" / "candidate-sources.md"


CANDIDATE_SOURCES: list[dict[str, str]] = [
    {
        "priority": "P0",
        "provider": "Google Gemini API / Google AI Studio",
        "channel_type": "official_model_vendor",
        "openai": "partial",
        "anthropic": "no",
        "status": "待复核官方 Free Tier、rate limits、地区和绑卡要求；确认前不进入推荐表。",
        "source": "https://ai.google.dev/gemini-api/docs/pricing",
    },
    {
        "priority": "P0",
        "provider": "Mistral La Plateforme",
        "channel_type": "official_model_vendor",
        "openai": "partial",
        "anthropic": "no",
        "status": "待复核是否仍有免费或试用 API 额度；不确定时只作为低价/候补源。",
        "source": "https://docs.mistral.ai/",
    },
    {
        "priority": "P0",
        "provider": "GroqCloud",
        "channel_type": "official_model_vendor",
        "openai": "yes",
        "anthropic": "no",
        "status": "待复核开发者免费限制、模型列表和 rate limits；有官方证据后可建 provider/offer 记录。",
        "source": "https://console.groq.com/docs/rate-limits",
    },
    {
        "priority": "P0",
        "provider": "Cerebras Inference",
        "channel_type": "official_model_vendor",
        "openai": "yes",
        "anthropic": "no",
        "status": "待复核是否提供免费或试用额度；确认前不推荐。",
        "source": "https://inference-docs.cerebras.ai/",
    },
    {
        "priority": "P0",
        "provider": "Cloudflare Workers AI",
        "channel_type": "official_cloud_platform",
        "openai": "partial",
        "anthropic": "no",
        "status": "待复核免费分配、账号要求和模型计费；需区分平台免费层和模型价格。",
        "source": "https://developers.cloudflare.com/workers-ai/platform/pricing/",
    },
    {
        "priority": "P0",
        "provider": "Alibaba Cloud Model Studio / Qwen",
        "channel_type": "official_cloud_platform",
        "openai": "yes",
        "anthropic": "no",
        "status": "待复核新用户额度、有效期、实名和地区要求；确认前只作候补。",
        "source": "https://help.aliyun.com/zh/model-studio/models",
    },
    {
        "priority": "P0",
        "provider": "Tencent Cloud TokenHub / Hunyuan",
        "channel_type": "official_cloud_platform",
        "openai": "unknown",
        "anthropic": "unknown",
        "status": "待复核 API base、兼容性、免费额度和实名要求；当前信息不足。",
        "source": "https://cloud.tencent.com/document/product/1729",
    },
    {
        "priority": "P0",
        "provider": "Volcengine Ark / Doubao",
        "channel_type": "official_cloud_platform",
        "openai": "yes",
        "anthropic": "no",
        "status": "待复核试用/新用户额度、模型 ID 和 endpoint；确认前不进推荐表。",
        "source": "https://www.volcengine.com/docs/82379",
    },
    {
        "priority": "P0",
        "provider": "Zhipu BigModel / GLM",
        "channel_type": "official_model_vendor",
        "openai": "partial",
        "anthropic": "no",
        "status": "待复核官方免费 API 额度；没有证据时不得硬塞进免费表。",
        "source": "https://docs.bigmodel.cn/",
    },
    {
        "priority": "P0",
        "provider": "Moonshot / Kimi API",
        "channel_type": "official_model_vendor",
        "openai": "yes",
        "anthropic": "no",
        "status": "待复核官方免费 API 额度；没有证据时只标为候补或低价源。",
        "source": "https://platform.moonshot.cn/docs/pricing/chat",
    },
    {
        "priority": "P0",
        "provider": "DeepSeek API",
        "channel_type": "official_model_vendor",
        "openai": "yes",
        "anthropic": "no",
        "status": "通常作为低价源候补；无官方免费额度证据时不得进入免费推荐表。",
        "source": "https://api-docs.deepseek.com/quick_start/pricing",
    },
    {
        "priority": "P0",
        "provider": "Baidu Qianfan / ERNIE",
        "channel_type": "official_cloud_platform",
        "openai": "partial",
        "anthropic": "no",
        "status": "待复核免费额度、实名、地区和计费规则；确认前只作候补。",
        "source": "https://cloud.baidu.com/doc/WENXINWORKSHOP/",
    },
    {
        "priority": "P0",
        "provider": "OpenAI API",
        "channel_type": "official_model_vendor",
        "openai": "yes",
        "anthropic": "no",
        "status": "协议参考源；没有官方免费 API 额度时必须标为 not_free_or_unverified。",
        "source": "https://platform.openai.com/docs/api-reference",
    },
    {
        "priority": "P0",
        "provider": "Anthropic Claude API",
        "channel_type": "official_model_vendor",
        "openai": "no",
        "anthropic": "yes",
        "status": "协议参考源；没有官方免费 API 额度时必须标为 not_free_or_unverified。",
        "source": "https://docs.anthropic.com/en/api/messages",
    },
    {
        "priority": "P0",
        "provider": "OpenRouter",
        "channel_type": "third_party_router",
        "openai": "yes",
        "anthropic": "unknown",
        "status": "已接入官方 models API；只推荐 API 返回的免费模型或 :free 模型。",
        "source": "https://openrouter.ai/api/v1/models",
    },
    {
        "priority": "P0",
        "provider": "SiliconFlow",
        "channel_type": "third_party_inference_provider",
        "openai": "yes",
        "anthropic": "no",
        "status": "待复核官方免费模型、试用额度和账号要求；确认前只作候补。",
        "source": "https://docs.siliconflow.cn/",
    },
    {
        "priority": "P0",
        "provider": "Hugging Face Inference Providers",
        "channel_type": "third_party_inference_provider",
        "openai": "partial",
        "anthropic": "no",
        "status": "必须区分 open_weight_only 和免费托管 API；不能把开源权重等同于免费 API。",
        "source": "https://huggingface.co/docs/inference-providers",
    },
    {
        "priority": "P1",
        "provider": "Together AI",
        "channel_type": "third_party_inference_provider",
        "openai": "yes",
        "anthropic": "no",
        "status": "候补低价/新用户额度源；待官方 pricing 和 credit 证据。",
        "source": "https://docs.together.ai/",
    },
    {
        "priority": "P1",
        "provider": "Fireworks AI",
        "channel_type": "third_party_inference_provider",
        "openai": "yes",
        "anthropic": "no",
        "status": "候补试用/低价源；待官方 pricing 和 trial 证据。",
        "source": "https://docs.fireworks.ai/",
    },
    {
        "priority": "P1",
        "provider": "Novita",
        "channel_type": "third_party_inference_provider",
        "openai": "yes",
        "anthropic": "no",
        "status": "候补试用/低价源；待官方模型价格和额度证据。",
        "source": "https://novita.ai/docs",
    },
    {
        "priority": "P1",
        "provider": "Replicate",
        "channel_type": "third_party_inference_provider",
        "openai": "partial",
        "anthropic": "no",
        "status": "候补推理平台；模型价格差异大，需逐模型确认。",
        "source": "https://replicate.com/docs",
    },
    {
        "priority": "P1",
        "provider": "Nebius AI Studio",
        "channel_type": "third_party_inference_provider",
        "openai": "yes",
        "anthropic": "no",
        "status": "候补试用/低价源；待官方 API、credit 和 pricing 证据。",
        "source": "https://docs.nebius.com/studio/",
    },
    {
        "priority": "P1",
        "provider": "NVIDIA Build / API Catalog",
        "channel_type": "third_party_inference_provider",
        "openai": "yes",
        "anthropic": "no",
        "status": "候补 API catalog；待确认免费 credits、endpoint 和模型条款。",
        "source": "https://build.nvidia.com/",
    },
]


def md_escape(value: Any) -> str:
    text = "" if value is None else str(value)
    return text.replace("|", "\\|").replace("\n", " ")


def table(records: list[dict[str, Any]], columns: list[tuple[str, str]]) -> str:
    if not records:
        return "_暂无符合条件的记录。_"
    rows = ["| " + " | ".join(title for title, _ in columns) + " |"]
    rows.append("| " + " | ".join("---" for _ in columns) + " |")
    for record in records:
        rows.append("| " + " | ".join(md_escape(record.get(field, "")) for _, field in columns) + " |")
    return "\n".join(rows)


def latest_date(records: list[dict[str, Any]]) -> str:
    dates = sorted(str(r.get("last_checked", "")) for r in records if r.get("last_checked"))
    return dates[-1] if dates else "尚未抓取"


def count_by(records: list[dict[str, Any]], field: str) -> str:
    counts = Counter(str(record.get(field, "")) for record in records)
    return ", ".join(f"`{key}`: {value}" for key, value in sorted(counts.items()))


def model_or_offer(record: dict[str, Any]) -> str:
    return str(record.get("model_id") or record.get("offer_id") or record.get("provider_id") or "")


def build_sections(records: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    display_records = []
    for record in records:
        copy = dict(record)
        copy["model_or_offer"] = model_or_offer(record)
        display_records.append(copy)

    recommended = [
        r
        for r in display_records
        if r.get("is_recommended") is True
        and r.get("confidence") in {"high", "medium"}
        and r.get("free_type") != "not_free_or_unverified"
    ]
    sections = {
        "official_free": [
            r
            for r in recommended
            if r.get("channel_type") in {"official_model_vendor", "official_cloud_platform"}
            and r.get("record_level") in {"provider", "offer"}
        ],
        "third_party_free_models": [
            r
            for r in recommended
            if r.get("channel_type") in {"third_party_router", "third_party_inference_provider"}
            and r.get("record_level") == "model"
        ],
        "trial_offers": [
            r
            for r in recommended
            if r.get("record_level") == "offer"
            or r.get("free_type") in {"new_user_credit", "trial_credit"}
        ],
        "candidates": [
            r
            for r in display_records
            if r.get("is_recommended") is not True
            or r.get("confidence") == "low"
            or r.get("free_type") == "not_free_or_unverified"
        ],
        "protocol_refs": [
            r for r in display_records if r.get("provider_id") in {"openai-api", "anthropic-api"}
        ],
        "all": display_records,
    }
    return sections


def enum_table() -> str:
    rows = [
        {
            "field": field,
            "values": ", ".join(f"`{value}`" for value in sorted(values)),
        }
        for field, values in sorted(ENUMS.items())
    ]
    return table(rows, [("字段", "field"), ("可选值", "values")])


def required_fields_table() -> str:
    rows = [{"field": field} for field in REQUIRED_FIELDS]
    return table(rows, [("必填字段", "field")])


def render_readme(records: list[dict[str, Any]]) -> str:
    sections = build_sections(records)
    rec_columns = [
        ("Provider", "provider"),
        ("Level", "record_level"),
        ("Model/Offer", "model_or_offer"),
        ("Free type", "free_type"),
        ("OpenAI", "openai_compatible"),
        ("Anthropic", "anthropic_compatible"),
        ("Confidence", "confidence"),
        ("Checked", "last_checked"),
        ("Evidence", "source_url"),
    ]
    candidate_columns = [
        ("Provider", "provider"),
        ("Level", "record_level"),
        ("Model/Offer", "model_or_offer"),
        ("Free type", "free_type"),
        ("Confidence", "confidence"),
        ("Reason / Note", "recommendation_reason"),
        ("Checked", "last_checked"),
        ("Evidence", "source_url"),
    ]
    source_columns = [
        ("Priority", "priority"),
        ("Provider", "provider"),
        ("Type", "channel_type"),
        ("OpenAI", "openai"),
        ("Anthropic", "anthropic"),
        ("Status / user judgement note", "status"),
        ("Official source", "source"),
    ]

    return f"""# Free LLM API Watch

中文 | [English](README.en.md)

本项目持续追踪可以通过 API 调用的免费、试用或低成本前沿大模型渠道，包括官方模型厂商 API、官方云平台、第三方模型聚合平台和第三方推理平台。项目只统计可通过 API 使用的渠道，不统计单纯网页或 App 免费模型。

最近一次数据更新时间：{latest_date(records)}

当前 catalog 记录数：{len(records)}

记录层级统计：{count_by(records, "record_level") or "暂无"}

免费类型统计：{count_by(records, "free_type") or "暂无"}

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

{table(sections["official_free"], rec_columns)}

## 第三方免费模型

{table(sections["third_party_free_models"], rec_columns)}

## 新用户试用额度

{table(sections["trial_offers"], rec_columns)}

## 低价但非免费

低价但非免费记录不进入推荐表。DeepSeek、Kimi、智谱、百度千帆、Mistral、Together AI、Fireworks 等如果只有低价或未确认额度，应保留在候补区，直到官方证据证明存在免费 API 额度、免费模型、免费路由或试用额度。

## 候补待确认与参考区

{table(sections["candidates"], candidate_columns)}

## 协议参考源

{table(sections["protocol_refs"], candidate_columns)}

## 候补监控源与人工判断备注

以下条目来自 `data/providers.yaml` 的初始监控范围。它们不是免费 API 结论；如果状态列写了“待复核”，用户需要打开官方 source 自行判断，不要直接当作推荐。

{table(CANDIDATE_SOURCES, source_columns)}

## 完整字段要求

{required_fields_table()}

## 枚举值要求

{enum_table()}

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
{{
  "fetch_status": "failed",
  "error_summary": "",
  "confidence": "low",
  "free_type": "not_free_or_unverified"
}}
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
"""


def render_free_guide(records: list[dict[str, Any]]) -> str:
    sections = build_sections(records)
    rec_columns = [
        ("Provider", "provider"),
        ("Level", "record_level"),
        ("Model/Offer", "model_or_offer"),
        ("Free type", "free_type"),
        ("Reason", "recommendation_reason"),
        ("Evidence", "source_url"),
    ]
    return f"""# 免费 API 使用指南

更新时间：{latest_date(records)}

## 推荐原则

推荐表只能展示同时满足以下条件的记录：

- 有官方证据；
- `confidence` 为 `high` 或 `medium`；
- `is_recommended` 为 `true`；
- 明确存在 API 免费额度、免费模型、免费路由或试用额度。

`confidence: low`、`not_free_or_unverified`、`protocol reference only` 的记录只能进入候补区或参考区。

## 官方免费 API 渠道

{table(sections["official_free"], rec_columns)}

## 第三方免费模型

{table(sections["third_party_free_models"], rec_columns)}

## 新用户试用额度

{table(sections["trial_offers"], rec_columns)}

## 候补待确认与参考区

{table(sections["candidates"], rec_columns)}

## 候补监控源与人工判断备注

{table(CANDIDATE_SOURCES, [("Priority", "priority"), ("Provider", "provider"), ("Type", "channel_type"), ("Status", "status"), ("Official source", "source")])}
"""


def render_provider_comparison(records: list[dict[str, Any]]) -> str:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for record in records:
        grouped[str(record.get("provider_id", ""))].append(record)
    rows = []
    for provider_id, provider_records in sorted(grouped.items()):
        first = provider_records[0]
        recommended = sum(1 for r in provider_records if r.get("is_recommended"))
        rows.append(
            {
                "provider": first.get("provider", provider_id),
                "provider_id": provider_id,
                "channel_type": first.get("channel_type", ""),
                "records": len(provider_records),
                "recommended": recommended,
                "record_levels": ", ".join(sorted({str(r.get("record_level", "")) for r in provider_records})),
                "free_types": ", ".join(sorted({str(r.get("free_type", "")) for r in provider_records})),
                "openai": first.get("openai_compatible", "unknown"),
                "anthropic": first.get("anthropic_compatible", "unknown"),
            }
        )
    return "# Provider Comparison\n\n" + table(
        rows,
        [
            ("Provider", "provider"),
            ("ID", "provider_id"),
            ("Type", "channel_type"),
            ("Records", "records"),
            ("Recommended", "recommended"),
            ("Levels", "record_levels"),
            ("Free types", "free_types"),
            ("OpenAI", "openai"),
            ("Anthropic", "anthropic"),
        ],
    ) + "\n"


def render_candidate_sources() -> str:
    return f"""# Candidate Sources

本文件记录 P0/P1 监控源和人工复核要点。候补源不是免费 API 证据；状态列中写明“不确定”“待复核”的项目，需要用户打开官方来源自行判断。

{table(CANDIDATE_SOURCES, [("Priority", "priority"), ("Provider", "provider"), ("Type", "channel_type"), ("OpenAI", "openai"), ("Anthropic", "anthropic"), ("Status / user judgement note", "status"), ("Official source", "source")])}

## 抓取失败处理

抓取失败时不要编造数据。失败项必须写入：

```json
{{
  "fetch_status": "failed",
  "error_summary": "",
  "confidence": "low",
  "free_type": "not_free_or_unverified"
}}
```

失败源需要保留在本文件或 `docs/changelog.md` 中供人工复核。
"""


def main() -> int:
    records = load_catalog()
    README_PATH.write_text(render_readme(records), encoding="utf-8")
    FREE_GUIDE_PATH.write_text(render_free_guide(records), encoding="utf-8")
    PROVIDER_COMPARISON_PATH.write_text(render_provider_comparison(records), encoding="utf-8")
    CANDIDATE_SOURCES_PATH.write_text(render_candidate_sources(), encoding="utf-8")
    print(f"Rendered README and docs from {len(records)} catalog records")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
