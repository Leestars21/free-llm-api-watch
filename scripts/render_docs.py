from __future__ import annotations

import json
from collections import defaultdict
from datetime import date
from decimal import Decimal, InvalidOperation
from typing import Any

from catalog_schema import PROJECT_ROOT, load_catalog


README_PATH = PROJECT_ROOT / "README.md"
README_EN_PATH = PROJECT_ROOT / "README.en.md"
FREE_GUIDE_PATH = PROJECT_ROOT / "docs" / "free-api-guide.md"
FREE_MODELS_PATH = PROJECT_ROOT / "docs" / "free-models.md"
FREE_MODELS_EN_PATH = PROJECT_ROOT / "docs" / "free-models.en.md"
PROVIDER_COMPARISON_PATH = PROJECT_ROOT / "docs" / "provider-comparison.md"
CANDIDATE_SOURCES_PATH = PROJECT_ROOT / "docs" / "candidate-sources.md"
TRANSLATIONS_ZH_PATH = PROJECT_ROOT / "data" / "translations_zh.json"
TRANSLATIONS_ZH = json.loads(TRANSLATIONS_ZH_PATH.read_text(encoding="utf-8"))

FREE_TYPE_ZH = {
    "stable_free_tier": "长期免费层（有用量/速率限制）",
    "new_user_credit": "新用户赠额 / 免费使用上限",
    "trial_credit": "一次性试用额度",
    "free_model": "指定免费模型",
    "free_router": "免费路由模型",
    "community_volunteer": "社区志愿算力（动态排队）",
    "limited_time_promotion": "限时活动",
    "open_weight_only": "仅开源权重，不计作托管免费 API",
    "not_free_or_unverified": "未确认免费 / 已停止 / 仅参考",
}
FREE_TYPE_EN = {
    "stable_free_tier": "Recurring free tier (usage/rate limits apply)",
    "new_user_credit": "New-user grant / usage cap",
    "trial_credit": "One-time trial credit",
    "free_model": "Specific free model",
    "free_router": "Free router model",
    "community_volunteer": "Volunteer community compute (dynamic queue)",
    "limited_time_promotion": "Limited-time promotion",
    "open_weight_only": "Open weights only; not hosted free API",
    "not_free_or_unverified": "Not confirmed free / retired / reference only",
}
STATUS_ZH = {
    "active": "证据范围内有效",
    "stale": "过期待复核",
    "withdrawn": "已停止 / 已下架",
    "pending": "待复核",
    "historical": "历史记录",
    "unverified": "未验证",
}
STATUS_EN = {
    "active": "Active within stated evidence scope",
    "stale": "Stale; review required",
    "withdrawn": "Withdrawn / model removed",
    "pending": "Pending review",
    "historical": "Historical",
    "unverified": "Unverified",
}
QUOTA_SCOPE_ZH = {
    "provider_shared": "平台共享",
    "account_shared": "账号共享",
    "per_model": "按模型独立",
    "per_user": "按用户",
    "one_time": "一次性",
    "unknown": "未知",
}
COMPATIBILITY_ZH = {"yes": "是", "no": "否", "partial": "部分兼容", "unknown": "未知"}
FLAG_ZH = {"yes": "是", "no": "否", "unknown": "未知"}
QUOTA_UNIT_ZH = {
    "MoLi points/day": "MoLi 积分/天",
    "Neurons/day": "Neurons/天",
    "USD": "美元",
    "USD credits/month": "美元额度/月",
    "USD per million tokens": "美元/百万 Token",
    "account_rate_limited_api_access": "账号访问（受速率限制）",
    "account_usage_budget": "账号用量预算",
    "credits (amount undisclosed)": "额度积分（数值未公开）",
    "dynamic_model_catalog": "动态型号目录",
    "free-plan access with model rate limits": "免费计划调用（受型号速率限制）",
    "model_pricing": "模型价格",
    "model_pricing_and_account_rate_limit": "模型价格与账号速率限制",
    "requests/month": "次 API 调用/月",
    "tokens/account_mode": "Token/账号模式",
    "tokens/model": "Token/模型",
    "unknown": "未知",
    "video_minutes": "视频分钟",
    "volunteer_capacity": "志愿算力容量",
}
FREE_TYPES = {
    "stable_free_tier",
    "new_user_credit",
    "trial_credit",
    "free_model",
    "free_router",
    "community_volunteer",
    "limited_time_promotion",
}


def markdown(value: Any) -> str:
    if value is None or value == "":
        return "未知"
    if isinstance(value, (dict, list)):
        import json

        value = json.dumps(value, ensure_ascii=False, sort_keys=True)
    return str(value).replace("|", "&#124;").replace("\r", " ").replace("\n", " ")


def localized(record: dict[str, Any], field: str, language: str) -> Any:
    value = record.get(field)
    if language != "zh":
        return value
    provider_id = str(record.get("provider_id", ""))
    if field == "candidate_reason":
        return TRANSLATIONS_ZH.get("providers", {}).get(provider_id, value)
    offer_id = str(record.get("offer_id", ""))
    translated = TRANSLATIONS_ZH.get("offers", {}).get(offer_id, {}).get(field)
    return translated if translated is not None else value


def formatted_rate_limits(record: dict[str, Any], language: str) -> str:
    limits = record.get("rate_limits")
    if language == "zh":
        model_limit_keys = {"rpm", "rpd", "tpm", "tpd", "ash", "asd"}
        has_model_limits = (
            record.get("record_level") == "model"
            and isinstance(limits, dict)
            and any(key in limits for key in model_limit_keys)
        )
        if has_model_limits:
            units = {
                "rpm": "RPM",
                "rpd": "RPD",
                "tpm": "TPM",
                "tpd": "TPD",
                "ash": "音频秒/小时",
                "asd": "音频秒/日",
            }
            numeric = [f"{units[key]} {value}" for key, value in limits.items() if key in units]
            return "，".join(numeric) if numeric else "未知"
        offer_id = str(record.get("offer_id", ""))
        translated = TRANSLATIONS_ZH.get("offers", {}).get(offer_id, {}).get("rate_limits")
        if translated:
            return str(translated)
    if not limits:
        return "未知" if language == "zh" else "unknown"
    return markdown(limits)


def provider_status(provider: dict[str, Any], has_free_offer: bool, language: str) -> str:
    verification_status = str(provider.get("verification_status", "unverified"))
    no_free_offer = (
        verification_status == "active"
        and provider.get("free_type") == "not_free_or_unverified"
    )
    if language == "zh":
        if has_free_offer:
            return "已确认免费方案（按来源所述范围）"
        if no_free_offer:
            return "已复核：当前未确认免费 API"
        return STATUS_ZH.get(verification_status, "未验证")
    if has_free_offer:
        return "Free offer confirmed within stated evidence scope"
    if no_free_offer:
        return "Reviewed: no current free API confirmed"
    return STATUS_EN.get(verification_status, "Unverified")


def model_type_label(value: Any, language: str) -> str:
    model_type = str(value or "unknown")
    if language == "zh":
        return TRANSLATIONS_ZH.get("model_types", {}).get(model_type, model_type)
    return model_type.replace("_", " ")


def modality_labels(values: Any, language: str) -> str:
    if not isinstance(values, list) or not values:
        return "未知" if language == "zh" else "unknown"
    if language == "zh":
        translations = TRANSLATIONS_ZH.get("modalities", {})
        return ", ".join(str(translations.get(str(value), value)) for value in values)
    return ", ".join(str(value) for value in values)


def capability_label(value: Any, language: str) -> str:
    normalized = str(value or "unknown")
    labels = {
        "supported": "支持" if language == "zh" else "supported",
        "unsupported": "不支持" if language == "zh" else "unsupported",
        "unknown": "未知" if language == "zh" else "unknown",
    }
    return labels.get(normalized, normalized)


def multimodal_label(values: Any, language: str) -> str:
    if not isinstance(values, list) or not values:
        return "未知" if language == "zh" else "unknown"
    is_multimodal = len(set(str(value) for value in values)) > 1
    if language == "zh":
        return "是" if is_multimodal else "否"
    return "yes" if is_multimodal else "no"


def context_label(value: Any, language: str) -> str:
    if not isinstance(value, int):
        return "未知" if language == "zh" else "unknown"
    unit = " Token" if language == "zh" else " tokens"
    return f"{value:,}{unit}"


def eligibility_label(record: dict[str, Any], language: str) -> str:
    card = flag_label(record.get("requires_card", "unknown"), language)
    identity = flag_label(record.get("requires_identity_verification", "unknown"), language)
    region = localized(record, "requires_phone_region", language) or (
        "未知" if language == "zh" else "unknown"
    )
    if language == "zh":
        return f"绑卡：{card}；实名：{identity}；地区：{region}"
    return f"Card: {card}; identity check: {identity}; region: {region}"


def flag_label(value: Any, language: str) -> str:
    normalized = "yes" if value is True else "no" if value is False else str(value or "unknown")
    if language == "zh":
        return FLAG_ZH.get(normalized, "未知")
    return normalized


def compatibility_label(value: Any, language: str) -> str:
    normalized = "yes" if value is True else "no" if value is False else str(value or "unknown")
    if language == "zh":
        return COMPATIBILITY_ZH.get(normalized, "未知")
    return normalized


def quota_unit_label(value: Any, language: str) -> str:
    normalized = str(value or "unknown")
    if language == "zh":
        return QUOTA_UNIT_ZH.get(normalized, normalized)
    return normalized


def md_table(rows: list[dict[str, Any]], columns: list[tuple[str, str]]) -> str:
    if not rows:
        return "（暂无记录）"
    lines = ["| " + " | ".join(label for label, _ in columns) + " |"]
    lines.append("| " + " | ".join("---" for _ in columns) + " |")
    for row in rows:
        lines.append("| " + " | ".join(markdown(row.get(key, "")) for _, key in columns) + " |")
    return "\n".join(lines)


def recommended(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [
        record
        for record in records
        if record.get("is_recommended") is True
        and record.get("verification_status") == "active"
        and record.get("confidence") in {"high", "medium"}
        and record.get("free_type") in FREE_TYPES
    ]


def latest_date(records: list[dict[str, Any]]) -> str:
    candidates = [str(row.get("verified_at") or row.get("last_checked", "")) for row in records]
    dates: list[date] = []
    for candidate in candidates:
        try:
            dates.append(date.fromisoformat(candidate))
        except ValueError:
            continue
    return max(dates).isoformat() if dates else "未知"


def free_counts(records: list[dict[str, Any]]) -> dict[str, Any]:
    selected = recommended(records)
    provider_records = [record for record in records if record.get("record_level") == "provider"]
    active_provider_ids = {
        str(record.get("provider_id", "")) for record in selected
    }
    credit_provider_ids = {
        str(record.get("provider_id", ""))
        for record in selected
        if record.get("record_level") == "offer"
        and record.get("free_type") in {"new_user_credit", "trial_credit"}
    }
    return {
        "monitored_providers": len({str(row.get("provider_id", "")) for row in provider_records}),
        "confirmed_providers": len(active_provider_ids),
        "free_models": sum(1 for row in selected if row.get("record_level") == "model"),
        "offers": sum(1 for row in selected if row.get("record_level") == "offer"),
        "credit_providers": len(credit_provider_ids),
        "zero_price_models": sum(
            1 for row in selected
            if row.get("record_level") == "model" and has_zero_input_output_price(row)
        ),
    }


def has_zero_input_output_price(record: dict[str, Any]) -> bool:
    pricing = record.get("model_pricing")
    if not isinstance(pricing, dict):
        return False
    input_price = pricing.get("input", pricing.get("prompt"))
    output_price = pricing.get("output", pricing.get("completion"))
    try:
        return Decimal(str(input_price)) == 0 and Decimal(str(output_price)) == 0
    except (InvalidOperation, TypeError, ValueError):
        return False


def group_records(records: list[dict[str, Any]]) -> dict[str, dict[str, list[dict[str, Any]]]]:
    grouped: dict[str, dict[str, list[dict[str, Any]]]] = defaultdict(
        lambda: {"provider": [], "offer": [], "model": []}
    )
    for record in records:
        level = record.get("record_level")
        provider_id = str(record.get("provider_id", ""))
        if level in {"provider", "offer", "model"}:
            grouped[provider_id][str(level)].append(record)
    return grouped


def model_ids_for(
    provider_id: str,
    entries: dict[str, list[dict[str, Any]]],
    language: str,
) -> str:
    model_rows = [
        row for row in entries["model"]
        if row.get("is_recommended") and row.get("verification_status") == "active"
    ]
    ids = sorted({str(row.get("model_id", "")) for row in model_rows if row.get("model_id")})
    if ids:
        return ", ".join(f"`{model_id}`" for model_id in ids)
    applies = sorted({
        str(model_id)
        for offer in entries["offer"]
        if offer.get("is_recommended") and offer.get("verification_status") == "active"
        for model_id in offer.get("applies_to_models", [])
        if model_id
    })
    if applies:
        return ", ".join(f"`{model_id}`" for model_id in applies)
    if any(offer.get("is_recommended") for offer in entries["offer"]):
        return (
            "型号随平台目录或账号资格变化，请查看官方链接"
            if language == "zh"
            else "Models vary by catalog/account eligibility; see official source"
        )
    return "无当前已确认免费型号" if language == "zh" else "No currently confirmed free model"


def official_link(record: dict[str, Any]) -> str:
    url = str(record.get("source_url", ""))
    name = str(record.get("source_name", "官方来源"))
    if not url.startswith(("https://", "http://")):
        return "未知"
    return f"[{markdown(name)}]({url})"


def provider_overview_rows(records: list[dict[str, Any]], language: str = "zh") -> list[dict[str, Any]]:
    grouped = group_records(records)
    rows = []
    for provider_id in sorted(grouped):
        entries = grouped[provider_id]
        provider = entries["provider"][0] if entries["provider"] else {}
        active_offers = [
            row for row in entries["offer"]
            if row.get("is_recommended") and row.get("verification_status") == "active"
        ]
        if not active_offers:
            continue
        free_types = []
        offer_descriptions = []
        for row in active_offers:
            free_type = row.get("free_type")
            type_label = (
                FREE_TYPE_ZH.get(str(free_type), str(free_type))
                if language == "zh"
                else FREE_TYPE_EN.get(str(free_type), str(free_type))
            )
            free_types.append(type_label)
            separator = "；" if language == "zh" else "; "
            colon = "：" if language == "zh" else ": "
            offer_descriptions.append(
                f"`{row.get('offer_id')}`{colon}{type_label}{separator}"
                f"{localized(row, 'free_quota', language) or ('额度未知' if language == 'zh' else 'amount unknown')}"
            )
        source = active_offers[0]
        rows.append({
            "provider": provider.get("provider", provider_id),
            "free_type": ("；" if language == "zh" else "; ").join(free_types),
            "quota": ("；" if language == "zh" else "; ").join(
                str(localized(row, "free_quota", language) or ("额度未知" if language == "zh" else "amount unknown"))
                for row in active_offers
            ),
            "models": model_ids_for(provider_id, entries, language),
            "expires": ("；" if language == "zh" else "; ").join(
                str(localized(row, "expires", language) or ("未说明" if language == "zh" else "not stated"))
                for row in active_offers
            ),
            "card": ("；" if language == "zh" else "; ").join(
                flag_label(row.get("requires_card", "unknown"), language)
                for row in active_offers
            ),
            "compat": compatibility_label(provider.get("openai_compatible", "unknown"), language),
            "status": provider_status(provider, True, language),
            "source": official_link(source),
            "offer_ids": ("；" if language == "zh" else "; ").join(str(row.get("offer_id", "")) for row in active_offers),
            "offers": ("；" if language == "zh" else "; ").join(offer_descriptions),
            "rate_limits": ("；" if language == "zh" else "; ").join(
                formatted_rate_limits(row, language) for row in active_offers
            ),
        })
    return rows


def model_rows(records: list[dict[str, Any]], language: str = "zh") -> list[dict[str, Any]]:
    provider_names = {
        str(row.get("provider_id", "")): str(row.get("provider", row.get("provider_id", "")))
        for row in records if row.get("record_level") == "provider"
    }
    return [
        {
            "provider": provider_names.get(str(row.get("provider_id", "")), row.get("provider_id", "")),
            "provider_id": row.get("provider_id", ""),
            "model_id": row.get("model_id", ""),
            "model_name": row.get("model_name", ""),
            "model_type": model_type_label(row.get("model_type", "unknown"), language),
            "offer_id": row.get("offer_id", ""),
            "free_type": (
                FREE_TYPE_ZH.get(str(row.get("free_type")), str(row.get("free_type", "")))
                if language == "zh"
                else FREE_TYPE_EN.get(str(row.get("free_type")), str(row.get("free_type", "")))
            ),
            "quota": localized(row, "free_quota", language) or (
                "按关联 Offer / 平台额度" if language == "zh" else "See linked offer / provider quota"
            ),
            "quota_unit": quota_unit_label(row.get("free_quota_unit", ""), language),
            "reset": localized(row, "quota_reset", language) or ("未知" if language == "zh" else "unknown"),
            "context": context_label(row.get("context_window"), language),
            "modalities": modality_labels(row.get("modalities"), language),
            "multimodal": multimodal_label(row.get("modalities"), language),
            "limits": formatted_rate_limits(row, language),
            "tools": capability_label(row.get("tool_calling", "unknown"), language),
            "structured": capability_label(row.get("structured_output", "unknown"), language),
            "reasoning": capability_label(row.get("reasoning", "unknown"), language),
            "web_search": capability_label(row.get("web_search", "unknown"), language),
            "eligibility": eligibility_label(row, language),
            "expires": localized(row, "expires", language) or ("未说明" if language == "zh" else "not stated"),
            "base": row.get("api_base", "") or ("平台控制台/原生 API" if language == "zh" else "Console/native API"),
            "openai": compatibility_label(row.get("openai_compatible", "unknown"), language),
            "source": official_link(row),
            "verified_at": row.get("verified_at", "") or ("未知" if language == "zh" else "unknown"),
            "confidence": row.get("confidence", "unknown"),
        }
        for row in recommended(records)
        if row.get("record_level") == "model"
    ]


def offer_rows(records: list[dict[str, Any]], language: str = "zh") -> list[dict[str, Any]]:
    provider_names = {
        str(row.get("provider_id", "")): str(row.get("provider", row.get("provider_id", "")))
        for row in records if row.get("record_level") == "provider"
    }
    selected = [row for row in recommended(records) if row.get("record_level") == "offer"]
    return [
        {
            "provider": provider_names.get(str(row.get("provider_id", "")), row.get("provider_id", "")),
            "offer_id": row.get("offer_id", ""),
            "type": (
                FREE_TYPE_ZH.get(str(row.get("free_type")), row.get("free_type", ""))
                if language == "zh"
                else FREE_TYPE_EN.get(str(row.get("free_type")), row.get("free_type", ""))
            ),
            "quota": localized(row, "free_quota", language) or ("额度未知" if language == "zh" else "amount unknown"),
            "quota_unit": quota_unit_label(row.get("free_quota_unit", ""), language),
            "models": ", ".join(row.get("applies_to_models", [])) or ("动态 / 账号内确认" if language == "zh" else "Dynamic / confirm in account"),
            "reset": localized(row, "quota_reset", language) or ("未知" if language == "zh" else "unknown"),
            "expires": localized(row, "expires", language) or ("未说明" if language == "zh" else "not stated"),
            "card": flag_label(row.get("requires_card", "unknown"), language),
            "identity": flag_label(row.get("requires_identity_verification", "unknown"), language),
            "region": localized(row, "requires_phone_region", language) or ("未知" if language == "zh" else "unknown"),
            "scope": QUOTA_SCOPE_ZH.get(str(row.get("quota_scope", "unknown")), "未知") if language == "zh" else row.get("quota_scope", "unknown"),
            "limits": formatted_rate_limits(row, language),
            "source": official_link(row),
        }
        for row in selected
    ]


def candidate_rows(records: list[dict[str, Any]], language: str = "zh") -> list[dict[str, Any]]:
    selected = recommended(records)
    active_ids = {str(row.get("provider_id", "")) for row in selected}
    rows = []
    for provider in records:
        if provider.get("record_level") != "provider":
            continue
        provider_id = str(provider.get("provider_id", ""))
        if provider_id in active_ids:
            continue
        display_status = provider_status(provider, False, language)
        rows.append({
            "provider": provider.get("provider", provider_id),
            "status": display_status,
            "source": official_link(provider),
            "reason": localized(
                {**provider, "candidate_reason": provider.get("recommendation_reason", "") or provider.get("evidence_summary", "")},
                "candidate_reason",
                language,
            ),
        })
    return rows


def render_readme(records: list[dict[str, Any]]) -> str:
    counts = free_counts(records)
    date_checked = latest_date(recommended(records))
    overview = provider_overview_rows(records, "zh")
    models = model_rows(records, "zh")
    offers = offer_rows(records, "zh")
    candidates = candidate_rows(records, "zh")
    return f"""# Free LLM API Watch

**最后核验日期：{date_checked}**

这是一个基于官方证据维护的免费/试用 LLM API 目录。目录区分零价格模型、周期性免费层、新用户赠额、一次性试用、速率限制和开源权重；具体额度和模型名单可能因账号、地区、产品批次而变动。

## 当前目录统计

| 指标 | 数量 |
| --- | ---: |
| 监控提供商 | {counts['monitored_providers']} |
| 已确认有免费 API 或试用方案的提供商 | {counts['confirmed_providers']} |
| 有明确免费访问关系的模型记录 | {counts['free_models']} |
| 已确认免费/试用 Offer | {counts['offers']} |
| 提供新用户赠额或试用额度的平台 | {counts['credit_providers']} |
| 其中明确标为输入/输出零价格的模型记录 | {counts['zero_price_models']} |

统计只计 `active`、官方来源、`medium/high` 可信度且 `is_recommended=true` 的记录。一个平台级额度若适用于多个模型，计作一个 Offer；没有固定模型清单时会标注为动态/账号内确认，不会推测型号。

## 免费平台总览

{overview_table(overview)}

## 免费模型详细列表

模型类型包括聊天、语音生成、语音识别、内容审核、Embedding、Rerank 等；`unknown` 表示官方材料未能确认，不代表不支持。额度、速率限制、资格、到期、API Base、来源和验证时间等完整字段见[免费模型明细](docs/free-models.md)。

{md_table(models, [('平台','provider'),('Model Name','model_name'),('精确 Model ID','model_id'),('类型','model_type'),('Offer ID','offer_id'),('免费范围','quota'),('上下文','context'),('模态','modalities'),('多模态','multimodal'),('速率限制','limits'),('工具调用','tools'),('结构化输出','structured'),('API Base','base'),('OpenAI 兼容','openai'),('来源','source')])}

## 新用户赠额与试用

赠额、共享余额与模型免费定价不是同一概念。下表的 `额度范围`、有效期、实名/地区要求须与账号内页面再次核对。

{md_table([row for row in offers if any(token in str(row['type']) for token in ('新用户','试用'))], [('平台','provider'),('Offer ID','offer_id'),('类型','type'),('额度','quota'),('额度单位','quota_unit'),('可用模型','models'),('重置/发放','reset'),('有效期','expires'),('绑卡','card'),('实名','identity'),('地区限制','region'),('额度范围','scope'),('速率限制（不属于赠额）','limits'),('官方来源','source')])}

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
    messages=[{{"role": "user", "content": "用两句话介绍不确定性量化。"}}],
)
print(response.choices[0].message.content)
```

例如 OpenRouter 的 Base URL 为 `https://openrouter.ai/api/v1`；每家服务商的 API Key、模型 ID、模型可用性和条款不同。不要将密钥写入仓库。

## 待复核、已停止与历史平台

下面的条目尚无足够当前官方证据，或服务已停止/迁移；不会进入当前免费推荐列表。

{md_table(candidates, [('平台','provider'),('状态','status'),('官方来源','source'),('原因/证据缺口','reason')])}

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
"""


def overview_table(rows: list[dict[str, Any]], language: str = "zh") -> str:
    if not rows:
        return "（暂无已确认 Offer）" if language == "zh" else "(No confirmed offers yet)"
    # Keep the overview scannable while retaining every offer ID and its evidence link.
    if language == "en":
        overview_columns = [
            ("Provider", "provider"), ("Free type", "free_type"), ("Free amount", "quota"),
            ("Listed models", "models"), ("Validity", "expires"), ("Card", "card"),
            ("OpenAI compatible", "compat"), ("Status", "status"), ("Official source", "source"),
        ]
        detail_columns = [
            ("Provider", "provider"), ("Offer ID", "offer_ids"), ("Offer details", "offers"),
            ("Rate limits (separate from grants)", "rate_limits"),
        ]
    else:
        overview_columns = [
            ("平台", "provider"), ("免费类型", "free_type"), ("免费额度", "quota"),
            ("已列型号", "models"), ("有效期", "expires"), ("绑卡", "card"),
            ("OpenAI 兼容", "compat"), ("状态", "status"), ("官方链接", "source"),
        ]
        detail_columns = [
            ("平台", "provider"), ("Offer ID", "offer_ids"), ("方案说明", "offers"),
            ("速率限制（独立于赠额）", "rate_limits"),
        ]
    summary = "Offer ID、速率限制与判定范围" if language == "zh" else "Offer IDs, rate limits, and scope"
    return md_table(rows, [
        *overview_columns,
    ]) + f"\n\n<details><summary>{summary}</summary>\n\n" + md_table(rows, [
        *detail_columns,
    ]) + "\n\n</details>"


def render_readme_en(records: list[dict[str, Any]]) -> str:
    counts = free_counts(records)
    date_checked = latest_date(recommended(records))
    overview = provider_overview_rows(records, "en")
    models = model_rows(records, "en")
    offers = offer_rows(records, "en")
    candidates = candidate_rows(records, "en")
    return f"""# Free LLM API Watch

**Last evidence review: {date_checked}**

An evidence-based directory of free and trial LLM API access. The catalog separates zero-priced models, recurring free tiers, new-user grants, one-time trials, rate limits, and open weights. Availability can depend on account, region, model, and product cohort.

## Current catalog statistics

| Metric | Count |
| --- | ---: |
| Monitored providers | {counts['monitored_providers']} |
| Providers with a confirmed free API or trial offer | {counts['confirmed_providers']} |
| Model records with confirmed free access | {counts['free_models']} |
| Confirmed free/trial offers | {counts['offers']} |
| Providers with a new-user grant or trial credit | {counts['credit_providers']} |
| Models explicitly listed at zero input/output price | {counts['zero_price_models']} |

Statistics include only active, recommended records supported by official sources at medium/high confidence. A shared provider credit is counted once as an offer. Dynamic model lists are labeled as such instead of being guessed.

## Free API provider overview

{overview_table(overview, "en")}

## Free model details

`unknown` means that official evidence reviewed here did not confirm the field. Full model-level quota, rate limits, eligibility, expiry, API base, source, verification date, and confidence are in the [free model detail file](docs/free-models.en.md).

{md_table(models, [('Provider','provider'),('Model name','model_name'),('Exact Model ID','model_id'),('Type','model_type'),('Offer ID','offer_id'),('Free scope','quota'),('Context','context'),('Modalities','modalities'),('Multimodal','multimodal'),('Rate limits','limits'),('Tools','tools'),('Structured output','structured'),('API Base','base'),('OpenAI compatible','openai'),('Source','source')])}

## New-user credits and trials

Credits, shared balances and zero-priced models are different kinds of free access. Check the account console for current eligibility, expiry, identity and region requirements.

{md_table(offers, [('Provider','provider'),('Offer ID','offer_id'),('Type','type'),('Amount','quota'),('Unit','quota_unit'),('Models','models'),('Reset/grant','reset'),('Validity','expires'),('Card','card'),('Identity','identity'),('Region','region'),('Scope','scope'),('Rate limits (not a grant)','limits'),('Source','source')])}

## OpenAI-compatible API example

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["LLM_API_KEY"],
    base_url=os.environ["LLM_BASE_URL"],
)
response = client.chat.completions.create(
    model=os.environ["LLM_MODEL_ID"],
    messages=[{{"role": "user", "content": "Explain uncertainty quantification in two sentences."}}],
)
print(response.choices[0].message.content)
```

For example, OpenRouter uses `https://openrouter.ai/api/v1`. Confirm compatibility, parameters, model ID, terms, and key handling for each provider. Never commit API keys.

## Candidates, retired services, and records to recheck

These providers are not in the current recommendation list because current evidence is incomplete or the service has been retired.

{md_table(candidates, [('Provider','provider'),('Status','status'),('Official source','source'),('Reason/evidence gap','reason')])}

## Data and update policy

- `data/manual_catalog.json` is the evidence-backed source for manually reviewed providers, offers, models, and official links. `data/free_api_catalog.json` is the merged output.
- `data/translations_zh.json` contains display-only Chinese text; it does not replace or alter official evidence fields.
- JSON and CSV are emitted together. Records are keyed by provider, record level, model ID, and offer ID; same-named models from different providers stay separate.
- `free_quota` records a grant or free-price scope; `rate_limits` separately records RPM, TPM, RPD and related limits.
- A model-list API proves model existence, not free access. Free recommendations require separate official pricing or policy evidence.
- Network failures retain old automatic records as `stale` and remove them from recommendations. A model is withdrawn only after a complete successful API response confirms its removal or changed pricing.
- Running the updater does not refresh the evidence date for manually reviewed policies.

## Local verification

```powershell
python scripts/update_catalog.py
python scripts/validate_catalog.py
python scripts/score_models.py
python scripts/render_docs.py
python -m unittest discover -s tests -v
```

The repository workflow `.github/workflows/update-catalog.yml` runs daily at UTC 00:00 and validates/test-gates automated updates. Manual policy evidence remains maintained in `manual_catalog.json`.

## Disclaimer and privacy

Prices, quotas, model routing, regions, rate limits, terms and data processing can change. Recheck the linked source before production use. Do not send sensitive material to a provider whose data practices you have not reviewed, and do not bypass terms, access controls, limits, identity checks or regional restrictions.

This catalog is not legal, security, procurement, privacy or compliance advice. See [privacy and risk](docs/privacy-and-risk.md), [disclaimer](docs/disclaimer.md), and the [free API guide](docs/free-api-guide.md).

## License

MIT License. See [LICENSE](LICENSE).
"""


def render_free_guide(records: list[dict[str, Any]]) -> str:
    offers = offer_rows(records)
    models = model_rows(records)
    return f"""# 免費 API 使用指南

最近證據核驗日期：{latest_date(recommended(records))}

## 如何區分免費類型

| free_type | 含義 |
| --- | --- |
| `free_model` | 官方證據確認特定模型的 API 價格為零，或明確列為免費模型。 |
| `stable_free_tier` | 平台提供持續免費層；仍可能有每月總量、RPM、TPM 或模型准入限制。 |
| `new_user_credit` | 新帳號/符合條件的模型領取免費 Token 或用量上限，常有地區與有效期限制。 |
| `trial_credit` | 一次性或限时评估；不能当作长期、无限调用。 |
| `limited_time_promotion` | 活动期免费，须明确活动时间和资格。 |
| `open_weight_only` | 可自行部署开放权重，不代表平台提供免费的托管 API。 |

## 已确认的 Offers

{md_table(offers, [('平台','provider'),('Offer ID','offer_id'),('类型','type'),('额度','quota'),('适用模型','models'),('额度范围','scope'),('重置','reset'),('有效期','expires'),('绑卡','card'),('实名','identity'),('地区/账号资格','region'),('速率限制（另计）','limits'),('来源','source')])}

## 明确型号

{md_table(models, [('平台','provider'),('Model Name','model_name'),('Model ID','model_id'),('类型','model_type'),('关联 Offer','offer_id'),('免费范围','quota'),('上下文','context'),('模态','modalities'),('速率限制','limits'),('工具调用','tools'),('API Base','base'),('OpenAI 兼容','openai'),('来源','source')])}

## 额度和速率限制

- `free_quota` 是免费总量、共享余额、免费模型价格或平台专属额度。`rate_limits` 是 RPM/TPM/RPD/TPD/并发等限流，二者不互相替代。
- 按模型赠送 Token 时查看 `quota_scope=per_model`；平台共享余额通常为 `account_shared`；一次性试用为 `one_time`。
- Account/Project RPM/TPM 可能针对每个模型单独执行，也可能共享。没有公开规则时保留为 `unknown`，不要推算请求数。
- 模型 API 返回清单只能证明型号存在。免费状态必须由独立官方价格页、免费层政策或公告确认。

## 数据状态

- `active`：来源在核验日期仍支持该范围的结论；不代表实际 API 调用成功。
- `stale`：最新自动检查失败，旧记录留存供复核，当前不推荐。
- `withdrawn`：完整且成功的官方目录检查确认型号下架或不再免费。
- `pending` / `historical` / `unverified`：证据缺口或仅有历史记录，不进入推荐表。
- `verified_at` 表示政策/型号证据实际核对日期，不会因为更新脚本运行而自动刷新。

完整统计和中英文表格见 [README](../README.md) 与 [English README](../README.en.md)。
逐型号的额度、限速、资格、API Base、来源和核验时间见[完整型号清单](free-models.md)。
"""


def render_free_models(records: list[dict[str, Any]], language: str) -> str:
    rows = model_rows(records, language)
    if language == "zh":
        columns = [
            ("提供商", "provider"), ("Provider ID", "provider_id"), ("Model Name", "model_name"),
            ("精确 Model ID", "model_id"), ("模型类型", "model_type"), ("Offer ID", "offer_id"),
            ("免费类型", "free_type"), ("免费额度/价格范围", "quota"), ("额度单位", "quota_unit"),
            ("重置周期", "reset"), ("速率限制", "limits"), ("免费资格", "eligibility"),
            ("有效期", "expires"), ("上下文窗口", "context"), ("支持模态", "modalities"),
            ("多模态", "multimodal"), ("工具调用", "tools"), ("结构化输出", "structured"),
            ("推理", "reasoning"), ("网页搜索", "web_search"), ("API Base", "base"),
            ("OpenAI 兼容", "openai"), ("官方来源", "source"), ("最近核验", "verified_at"),
            ("可信度", "confidence"),
        ]
        return f"""# 已确认免费或试用的模型明细

本页由 catalog 生成，只列出当前 `active`、有官方依据、`medium/high` 可信度且已推荐的型号，共 {len(rows)} 条记录。

免费总量与速率限制分列。多模态一栏按来源列出的模态数量派生；`unknown` 表示当前官方证据没有确认该字段。免费资格和额度可能受账号、地区、项目或模型限制，使用前请核对来源。

{md_table(rows, columns)}
"""

    columns = [
        ("Provider", "provider"), ("Provider ID", "provider_id"), ("Model name", "model_name"),
        ("Exact Model ID", "model_id"), ("Model type", "model_type"), ("Offer ID", "offer_id"),
        ("Free type", "free_type"), ("Free quota/price scope", "quota"), ("Quota unit", "quota_unit"),
        ("Reset period", "reset"), ("Rate limits", "limits"), ("Eligibility", "eligibility"),
        ("Validity", "expires"), ("Context window", "context"), ("Modalities", "modalities"),
        ("Multimodal", "multimodal"), ("Tool calling", "tools"), ("Structured output", "structured"),
        ("Reasoning", "reasoning"), ("Web search", "web_search"), ("API Base", "base"),
        ("OpenAI compatible", "openai"), ("Official source", "source"), ("Last verified", "verified_at"),
        ("Confidence", "confidence"),
    ]
    return f"""# Confirmed Free or Trial Model Details

Generated from the catalog. This page includes only active, recommended model records backed by official evidence at medium/high confidence ({len(rows)} records).

Free grants and rate limits are separate. The multimodal column is derived from the number of modalities listed in the source. `unknown` means the reviewed official evidence did not confirm that field. Check the linked source for current account, region, project, and model eligibility.

{md_table(rows, columns)}
"""


def render_provider_comparison(records: list[dict[str, Any]]) -> str:
    grouped = group_records(records)
    rows = []
    for provider_id, entries in sorted(grouped.items()):
        provider = entries["provider"][0] if entries["provider"] else {}
        active = [row for row in recommended(records) if row.get("provider_id") == provider_id]
        active_offer = any(row.get("record_level") == "offer" for row in active)
        rows.append({
            "provider": provider.get("provider", provider_id),
            "provider_id": provider_id,
            "status": provider_status(provider, active_offer, "zh"),
            "offer_count": sum(1 for row in active if row.get("record_level") == "offer"),
            "model_count": sum(1 for row in active if row.get("record_level") == "model"),
            "free_types": "、".join(sorted({FREE_TYPE_ZH.get(str(row.get("free_type", "")), str(row.get("free_type", ""))) for row in active})) or "无已确认方案",
            "openai": compatibility_label(provider.get("openai_compatible", "unknown"), "zh"),
            "api_base": provider.get("api_base", "") or "未知 / 原生端点",
            "source": official_link(provider),
        })
    return """# 提供商对比

这里只比较当前 catalog 的证据和方案记录；未核实的速率限制、兼容性或数据政策保留为 unknown。

""" + md_table(rows, [
        ("平台", "provider"), ("Provider ID", "provider_id"), ("状态", "status"),
        ("Offer 数", "offer_count"), ("型号数", "model_count"), ("免费类型", "free_types"),
        ("OpenAI 兼容", "openai"), ("API Base", "api_base"), ("官方来源", "source"),
    ]) + "\n"


def render_candidate_sources(records: list[dict[str, Any]]) -> str:
    rows = candidate_rows(records)
    return f"""# 候补与历史来源

本页由 provider-level 目录记录生成，涵盖本轮重点研究的国内外平台。候补不是免费 API 结论。只有官方政策与可用 API 型号均得到当前证据支持时，才进入推荐区。

## 尚待复核、非免费或仅有历史证据

{md_table(rows, [('平台','provider'),('状态','status'),('官方来源','source'),('原因/证据缺口','reason')])}

## 复核规则

- 旧公告不能替代当前模型 API/价格证据；`historical` 记录不进入推荐。
- 开源权重、网页聊天、合作应用的内置模型或低价 Token 不证明直接托管 API 免费。
- 动态模型广场、活动额度和账户资格不稳定时，记录明确标注“动态/账号内确认”，不猜测型号或数量。
- 当前服务已停止或迁移的记录保留供检索，但 README 当前推荐表会排除它们。
"""


def main() -> int:
    records = load_catalog()
    README_PATH.write_text(render_readme(records), encoding="utf-8")
    README_EN_PATH.write_text(render_readme_en(records), encoding="utf-8")
    FREE_GUIDE_PATH.write_text(render_free_guide(records), encoding="utf-8")
    FREE_MODELS_PATH.write_text(render_free_models(records, "zh"), encoding="utf-8")
    FREE_MODELS_EN_PATH.write_text(render_free_models(records, "en"), encoding="utf-8")
    PROVIDER_COMPARISON_PATH.write_text(render_provider_comparison(records), encoding="utf-8")
    CANDIDATE_SOURCES_PATH.write_text(render_candidate_sources(records), encoding="utf-8")
    counts = free_counts(records)
    print(
        f"Rendered bilingual README and docs from {len(records)} catalog records; "
        f"{counts['confirmed_providers']} confirmed providers, {counts['free_models']} model records, "
        f"{counts['offers']} offers"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
