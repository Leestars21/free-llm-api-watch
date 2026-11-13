from __future__ import annotations

import json
from collections import defaultdict
from datetime import date
from decimal import Decimal, InvalidOperation
from typing import Any

from catalog_schema import CORE_LLM_TYPES, PROJECT_ROOT, RELATED_AI_TYPES, load_catalog


README_PATH = PROJECT_ROOT / "README.md"
README_EN_PATH = PROJECT_ROOT / "README.en.md"
FREE_GUIDE_PATH = PROJECT_ROOT / "docs" / "free-api-guide.md"
FREE_MODELS_PATH = PROJECT_ROOT / "docs" / "free-models.md"
FREE_MODELS_EN_PATH = PROJECT_ROOT / "docs" / "free-models.en.md"
PROVIDER_COMPARISON_PATH = PROJECT_ROOT / "docs" / "provider-comparison.md"
CANDIDATE_SOURCES_PATH = PROJECT_ROOT / "docs" / "candidate-sources.md"
RELATED_AI_PATH = PROJECT_ROOT / "docs" / "related-ai-apis.md"
RELATED_AI_EN_PATH = PROJECT_ROOT / "docs" / "related-ai-apis.en.md"
TRANSLATIONS_ZH_PATH = PROJECT_ROOT / "data" / "translations_zh.json"
TRANSLATIONS_ZH = json.loads(TRANSLATIONS_ZH_PATH.read_text(encoding="utf-8"))

FREE_TYPE_ZH = {
    "stable_free_tier": "长期免费层（有用量/速率限制）",
    "monthly_evaluation_tier": "每月免费评估额度",
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
    "monthly_evaluation_tier": "Monthly free evaluation allowance",
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
    "CNY": "人民币",
    "RMB": "人民币",
    "USD credit": "美元抵扣额",
    "model calls/month": "次模型调用/月",
    "tokens/model": "Token/模型",
}
FREE_TYPES = {
    "stable_free_tier",
    "monthly_evaluation_tier",
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
    else:
        model_limit_keys = {"rpm", "rpd", "tpm", "tpd", "ash", "asd"}
        if record.get("record_level") == "model" and isinstance(limits, dict) and any(key in limits for key in model_limit_keys):
            units = {"rpm": "RPM", "rpd": "RPD", "tpm": "TPM", "tpd": "TPD", "ash": "audio seconds/hour", "asd": "audio seconds/day"}
            return ", ".join(f"{units[key]} {value}" for key, value in limits.items() if key in units) or "unknown"
    if not limits:
        return "未知" if language == "zh" else "unknown"
    if isinstance(limits, dict):
        separator = "；" if language == "zh" else "; "
        return separator.join(f"{key.replace('_', ' ')}: {markdown(value)}" for key, value in limits.items())
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
    return {
        "text_llm": "Text LLM",
        "multimodal_llm": "Multimodal LLM",
        "speech_recognition": "Speech recognition",
        "speech_generation": "Speech generation",
        "image_generation": "Image generation",
        "video_generation": "Video generation",
        "music_generation": "Music generation",
        "content_moderation": "Content moderation",
        "routing_alias": "Routing alias",
    }.get(model_type, model_type.replace("_", " "))


def capability_tags(values: Any, language: str) -> str:
    if not isinstance(values, list) or not values:
        return "未确认" if language == "zh" else "not confirmed"
    zh_labels = {
        "reasoning": "推理",
        "code_generation": "代码生成",
        "long_context": "长上下文",
        "image_understanding": "图像理解",
        "agent_workflows": "Agent 工作流",
    }
    en_labels = {
        "reasoning": "reasoning",
        "code_generation": "code generation",
        "long_context": "long context",
        "image_understanding": "image understanding",
        "agent_workflows": "agent workflows",
    }
    labels = zh_labels if language == "zh" else en_labels
    return ", ".join(labels.get(str(value), str(value)) for value in values)


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
    selected_models = [row for row in selected if row.get("record_level") == "model"]
    core_model_keys = {
        (str(row.get("provider_id", "")), str(row.get("model_id", "")))
        for row in selected_models
        if row.get("model_scope") == "core_llm"
    }
    related_model_keys = {
        (str(row.get("provider_id", "")), str(row.get("model_id", "")))
        for row in selected_models
        if row.get("model_scope") == "related_ai_api"
    }
    router_keys = {
        (str(row.get("provider_id", "")), str(row.get("model_id", "")))
        for row in selected_models
        if row.get("model_type") == "routing_alias"
    }
    model_by_key = {
        (str(row.get("provider_id", "")), str(row.get("model_id", ""))): row
        for row in selected_models
        if row.get("model_scope") == "core_llm"
    }
    return {
        "monitored_providers": len({str(row.get("provider_id", "")) for row in provider_records}),
        "confirmed_providers": len(active_provider_ids),
        "free_models": len(core_model_keys),
        "core_llm_models": len(core_model_keys),
        "related_ai_models": len(related_model_keys - router_keys),
        "routing_aliases": len(router_keys),
        "offers": sum(1 for row in selected if row.get("record_level") == "offer"),
        "credit_providers": len(credit_provider_ids),
        "zero_price_models": sum(
            1 for row in model_by_key.values() if has_zero_input_output_price(row)
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
        if row.get("is_recommended")
        and row.get("verification_status") == "active"
        and row.get("model_scope") == "core_llm"
    ]
    ids = sorted({str(row.get("model_id", "")) for row in model_rows if row.get("model_id")})
    if ids:
        shown = ", ".join(f"`{model_id}`" for model_id in ids[:3])
        if len(ids) > 3:
            suffix = "；" if language == "zh" else "; "
            more = f"另有 {len(ids) - 3} 个" if language == "zh" else f"{len(ids) - 3} more"
            link = "docs/free-models.md" if language == "zh" else "docs/free-models.en.md"
            shown += f"{suffix}{more}（[全部]({link})）"
        return shown
    if any(
        offer.get("is_recommended") and offer.get("verification_status") == "active"
        for offer in entries["offer"]
    ):
        return (
            "具体型号需在平台目录或账号内确认；此处不推测"
            if language == "zh"
            else "No specific free LLM confirmed; check the live catalog/account"
        )
    return "无当前已确认免费型号" if language == "zh" else "No currently confirmed free model"


def official_link(record: dict[str, Any]) -> str:
    url = str(record.get("source_url", ""))
    name = str(record.get("source_name", "官方来源"))
    if not url.startswith(("https://", "http://")):
        return "未知"
    return f"[{markdown(name)}]({url})"


def shorten(value: Any, limit: int, language: str) -> str:
    text = str(value or "")
    if len(text) <= limit:
        return text
    marker = "…" if language == "zh" else "…"
    return text[: limit - 1].rstrip() + marker


def eligibility_summary(record: dict[str, Any], language: str) -> str:
    card = flag_label(record.get("requires_card", "unknown"), language)
    identity = flag_label(record.get("requires_identity_verification", "unknown"), language)
    region = localized(record, "requires_phone_region", language)
    region = str(region) if region else ("未说明" if language == "zh" else "not stated")
    if language == "zh":
        return f"绑卡 {card}；实名 {identity}；地区 {shorten(region, 42, language)}"
    return f"Card {card}; identity {identity}; region {shorten(region, 42, language)}"


def provider_overview_rows(
    records: list[dict[str, Any]],
    language: str = "zh",
    selected_free_types: set[str] | None = None,
) -> list[dict[str, Any]]:
    grouped = group_records(records)
    rows = []
    for provider_id in sorted(grouped):
        entries = grouped[provider_id]
        provider = entries["provider"][0] if entries["provider"] else {}
        active_offers = [
            row for row in entries["offer"]
            if row in recommended(records)
            and (selected_free_types is None or row.get("free_type") in selected_free_types)
        ]
        if not active_offers:
            continue
        type_labels = []
        offer_descriptions = []
        for row in active_offers:
            free_type = row.get("free_type")
            type_label = (
                FREE_TYPE_ZH.get(str(free_type), str(free_type))
                if language == "zh"
                else FREE_TYPE_EN.get(str(free_type), str(free_type))
            )
            type_labels.append(type_label)
            colon = "：" if language == "zh" else ": "
            offer_descriptions.append(f"{type_label}{colon}{localized(row, 'free_quota', language) or ('额度未知' if language == 'zh' else 'amount unknown')}")
        source = active_offers[0]
        expiry_label = "有效期" if language == "zh" else "valid"
        quota_items = []
        for row in active_offers:
            quota = str(localized(row, "free_quota", language) or ("额度未知" if language == "zh" else "amount unknown"))
            expiry = str(localized(row, "expires", language) or ("未说明" if language == "zh" else "not stated"))
            quota = quota.strip().rstrip(" .;；。")
            expiry = expiry.strip().rstrip(" .;；。")
            quota_items.append(f"{quota}；{expiry_label} {expiry}" if language == "zh" else f"{quota}; {expiry_label}: {expiry}")
        other_offer_count = max(0, len(quota_items) - 2)
        quota_items = quota_items[:2]
        if other_offer_count:
            quota_items.append(f"另有 {other_offer_count} 个方案" if language == "zh" else f"{other_offer_count} more offers")
        eligibility = list(dict.fromkeys(eligibility_summary(row, language) for row in active_offers))
        modes = list(dict.fromkeys(FREE_TYPE_ZH.get(str(row.get("free_type")), str(row.get("free_type"))) if language == "zh" else FREE_TYPE_EN.get(str(row.get("free_type")), str(row.get("free_type"))) for row in active_offers))
        rows.append({
            "provider": provider.get("provider", provider_id),
            "provider_id": provider_id,
            "free_type": ("；" if language == "zh" else "; ").join(modes),
            "quota": shorten(("；" if language == "zh" else "; ").join(quota_items), 155, language),
            "models": model_ids_for(provider_id, entries, language),
            "eligibility": shorten(("；" if language == "zh" else "; ").join(eligibility), 95, language),
            "compat": compatibility_label(provider.get("openai_compatible", "unknown"), language),
            "source": official_link(source),
            "offer_ids": ("；" if language == "zh" else "; ").join(str(row.get("offer_id", "")) for row in active_offers),
            "offers": ("；" if language == "zh" else "; ").join(offer_descriptions[:2]),
            "rate_limits": ("；" if language == "zh" else "; ").join(
                formatted_rate_limits(row, language) for row in active_offers
            ),
            "expires": shorten(("；" if language == "zh" else "; ").join(str(localized(row, "expires", language) or ("未说明" if language == "zh" else "not stated")) for row in active_offers), 70, language),
        })
    return rows


def model_rows(
    records: list[dict[str, Any]],
    language: str = "zh",
    model_scope: str = "core_llm",
) -> list[dict[str, Any]]:
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
            "model_scope": row.get("model_scope", "unknown"),
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
            "input_modalities": modality_labels(row.get("input_modalities"), language),
            "output_modalities": modality_labels(row.get("output_modalities"), language),
            "capabilities": capability_tags(row.get("capabilities"), language),
            "capabilities_source": official_link({**row, "source_url": row.get("capabilities_source_url") or row.get("source_url"), "source_name": "能力依据" if language == "zh" else "Capability evidence"}),
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
        if row.get("record_level") == "model" and row.get("model_scope") == model_scope
    ]


def use_case_rows(records: list[dict[str, Any]], language: str) -> list[dict[str, Any]]:
    rows = model_rows(records, language, "core_llm")
    raw_models = {
        (str(row.get("provider_id", "")), str(row.get("model_id", ""))): row
        for row in recommended(records)
        if row.get("record_level") == "model" and row.get("model_scope") == "core_llm"
    }
    definitions = [
        ("普通文本生成" if language == "zh" else "General text generation", lambda row: True),
        ("推理" if language == "zh" else "Reasoning", lambda row: row.get("reasoning") == "supported" or "reasoning" in row.get("capabilities", [])),
        ("代码生成" if language == "zh" else "Code generation", lambda row: "code_generation" in row.get("capabilities", [])),
        ("工具调用 / Agent" if language == "zh" else "Tool use / agent workflows", lambda row: row.get("tool_calling") == "supported" or "agent_workflows" in row.get("capabilities", [])),
        ("长上下文（≥100K）" if language == "zh" else "Long context (≥100K)", lambda row: isinstance(row.get("context_window"), int) and row.get("context_window") >= 100_000),
        ("图像理解" if language == "zh" else "Image understanding", lambda row: "image" in row.get("input_modalities", []) and "text" in row.get("output_modalities", [])),
        ("高频调用（公布了速率限制）" if language == "zh" else "Higher-volume use (published rate limits)", lambda row: isinstance(row.get("rate_limits"), dict) and any(key in row["rate_limits"] for key in ("rpm", "rpd", "tpm", "tpd"))),
    ]
    result = []
    for label, predicate in definitions:
        candidates = []
        for display in rows:
            source = raw_models.get((str(display["provider_id"]), str(display["model_id"])), {})
            if predicate(source):
                detail = f"`{display['model_id']}`"
                if label.endswith("rate limits)") or label.endswith("速率限制）"):
                    detail += f" ({display['limits']})"
                candidates.append(f"{official_link(source)} {detail}")
        result.append({
            "use_case": label,
            "candidates": ("、" if language == "zh" else "; ").join(candidates[:5]) or ("暂无已核实型号" if language == "zh" else "No verified model listed"),
        })
    return result


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
            "eligibility": eligibility_summary(row, language),
            "scope": QUOTA_SCOPE_ZH.get(str(row.get("quota_scope", "unknown")), "未知") if language == "zh" else row.get("quota_scope", "unknown"),
            "limits": formatted_rate_limits(row, language),
            "verified_at": row.get("verified_at") or row.get("last_checked") or "unknown",
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


def featured_rows(records: list[dict[str, Any]], language: str) -> list[dict[str, Any]]:
    """Show a small, evidence-backed selection; omit unavailable offers."""
    names = ("Google Gemini API", "GroqCloud", "Cloudflare Workers AI", "OpenRouter")
    eligible = provider_overview_rows(records, language, {"stable_free_tier", "free_router"})
    rows = [row for name in names for row in eligible if name in str(row["provider"])][:4]
    for row in rows:
        offer_ids = {part.strip() for part in str(row["offer_ids"]).replace("；", ";").split(";")}
        dates = sorted({str(offer.get("verified_at") or offer.get("last_checked") or "unknown")
                        for offer in recommended(records)
                        if offer.get("record_level") == "offer"
                        and offer.get("provider_id") == row["provider_id"]
                        and str(offer.get("offer_id", "")) in offer_ids})
        row["verified_at"] = ", ".join(dates) or "unknown"
    return rows


def render_readme(records: list[dict[str, Any]]) -> str:
    rows = featured_rows(records, "zh")
    table = md_table(rows, [("平台", "provider"), ("免费方式", "free_type"), ("额度与限制", "quota"), ("核验日期", "verified_at"), ("官方来源", "source")])
    return f"""# Free LLM API Watch

[English](README.en.md) · 项目主页：[Leestars21/free-llm-api-watch](https://github.com/Leestars21/free-llm-api-watch)

查找可以免费调用的大语言模型 API：这里整理平台、免费方式、模型和官方来源，覆盖免费层、新用户额度与限时活动。

## 从这里开始

{table}

以上仅是少量入口，并非排名或完整清单。免费范围、模型、地区及账号资格随时可能变化；请查看官方来源与账号控制台后再使用。各条记录的核验日期见完整目录，不应把最新日期理解为全部条目均在当天核验。

- **[查看全部平台和免费方案](docs/free-api-guide.md)**：比较额度、资格、有效期与官方来源。
- **[查看全部免费 LLM 型号](docs/free-models.md)**：精确 Model ID、API 地址、限制与逐条核验日期。
- [平台对比](docs/provider-comparison.md) · [其他 AI API](docs/related-ai-apis.md) · [候补与历史记录](docs/candidate-sources.md)

免费层受用量和速率限制；新用户赠额与限时活动不代表长期免费。模型出现在 API 列表中也不代表调用免费。

## 数据与更新

目录结合官方来源和自动更新；更新失败时不会将旧数据当作最新核验。[查看更新工作流](.github/workflows/update-catalog.yml)、[变更记录](docs/changelog.md)和[隐私与风险](docs/privacy-and-risk.md)。使用前请核实条款，勿公开 API 密钥或敏感数据。

发现问题欢迎提交 Issue 或 Pull Request。MIT 许可，见 [LICENSE](LICENSE)。
"""


def overview_table(rows: list[dict[str, Any]], language: str = "zh") -> str:
    if not rows:
        return "（暂无已确认 Offer）" if language == "zh" else "(No confirmed offers yet)"
    if language == "en":
        columns = [
            ("Provider", "provider"), ("Free method", "free_type"), ("Allowance / limit / validity", "quota"),
            ("Representative free LLMs", "models"), ("Conditions", "eligibility"),
            ("OpenAI SDK", "compat"), ("Official details", "source"),
        ]
    else:
        columns = [
            ("平台", "provider"), ("免费方式", "free_type"), ("额度 / 限制 / 有效期", "quota"),
            ("代表性免费 LLM", "models"), ("使用条件", "eligibility"),
            ("OpenAI SDK", "compat"), ("官方详情", "source"),
        ]
    return md_table(rows, columns)


def render_readme_en(records: list[dict[str, Any]]) -> str:
    rows = featured_rows(records, "en")
    table = md_table(rows, [("Provider", "provider"), ("Free offer", "free_type"), ("Allowance and limits", "quota"), ("Verified", "verified_at"), ("Official source", "source")])
    return f"""# Free LLM API Watch

[中文](README.md) · Project: [Leestars21/free-llm-api-watch](https://github.com/Leestars21/free-llm-api-watch)

Find LLM APIs with free access. This directory tracks providers, free offers, models and official evidence, including recurring tiers, new-user credits and promotions.

## Start here

{table}

These are selected starting points, not a ranking or a complete list. Offers, models, regions and account eligibility can change; check the official source and your account. Review dates are recorded per entry in the full directory; the latest date does not mean every entry was reviewed then.

- **[All providers and free offers](docs/free-api-guide.md)**: allowances, eligibility, expiry and official sources.
- **[All free LLM models](docs/free-models.en.md)**: exact Model IDs, API endpoints, limits and individual review dates.
- [Provider comparison](docs/provider-comparison.md) · [Other AI APIs](docs/related-ai-apis.en.md) · [Candidate and historical records](docs/candidate-sources.md)

Free tiers have usage and rate limits. New-user credits and promotions are not permanent free access; a model appearing in an API list does not prove free use. The offers guide and provider comparison are currently in Chinese.

## Data and updates

The catalog combines official sources and automated updates; failed checks do not refresh old evidence. See the [update workflow](.github/workflows/update-catalog.yml), [changelog](docs/changelog.md) and [privacy and risk](docs/privacy-and-risk.md). Verify terms before use and never publish API keys or sensitive data.

Issues and pull requests are welcome. MIT license; see [LICENSE](LICENSE).
"""


def render_free_guide(records: list[dict[str, Any]]) -> str:
    offers = offer_rows(records)
    models = model_rows(records)
    return f"""# 免費 API 使用指南

最近一条证据核验日期：{latest_date(recommended(records))}；各记录的核验日期可能不同。

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

{md_table(offers, [('平台','provider'),('类型','type'),('额度','quota'),('单位','quota_unit'),('适用范围','scope'),('有效期','expires'),('绑卡/实名/地区','eligibility'),('核验日期','verified_at'),('官方来源','source')])}

## 核心 LLM

模型类型与使用能力分开记录。`text_llm` 是文本 LLM；`multimodal_llm` 同时支持文本交互和至少一种非文本模态。模型清单可证明型号存在，只有独立免费政策或官方价格才能证明免费。

### 型号、方案与接入

{md_table(models, [('平台','provider'),('精确 Model ID','model_id'),('类型','model_type'),('Offer ID','offer_id'),('免费类型','free_type'),('额度范围','quota'),('API Base','base'),('OpenAI 兼容','openai'),('来源','source')])}

### 模态、能力与限速

{md_table(models, [('平台','provider'),('Model ID','model_id'),('输入模态','input_modalities'),('输出模态','output_modalities'),('能力标签','capabilities'),('工具调用','tools'),('结构化输出','structured'),('推理','reasoning'),('上下文','context'),('速率限制','limits'),('免费资格','eligibility'),('核验日期','verified_at'),('能力依据','capabilities_source')])}

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
"""


def render_free_models(records: list[dict[str, Any]], language: str) -> str:
    rows = model_rows(records, language)
    detailed_rows = [{**row, "model": f"{row['provider']} / `{row['model_id']}`"} for row in rows]
    if language == "zh":
        connection_columns = [
            ("提供商", "provider"), ("精确 Model ID", "model_id"), ("模型类型", "model_type"),
            ("关联 Offer", "offer_id"), ("免费类型", "free_type"), ("免费额度/范围", "quota"),
            ("额度单位", "quota_unit"), ("API Base", "base"), ("OpenAI 兼容", "openai"),
            ("官方来源", "source"),
        ]
        capability_columns = [
            ("平台 / Model ID", "model"), ("输入模态", "input_modalities"), ("输出模态", "output_modalities"),
            ("能力标签", "capabilities"), ("工具调用", "tools"), ("结构化输出", "structured"),
            ("推理", "reasoning"), ("上下文窗口", "context"), ("速率限制", "limits"),
            ("资格", "eligibility"), ("有效期", "expires"), ("最近核验", "verified_at"),
            ("可信度", "confidence"), ("能力依据", "capabilities_source"),
        ]
        return f"""# 已确认免费或试用的核心 LLM

本页由目录生成，只列出当前 `active`、有官方依据、中/高可信度且已推荐的核心模型，共 {len(rows)} 个按平台和 Model ID 去重的型号。扩展资源见[相关 AI API 目录](related-ai-apis.md)。

免费额度与速率限制分列；未知字段表示已审阅的官方来源没有确认该项。模型免费资格可能受账号、地区、项目或型号限制。

## 免费方案和接入

{md_table(rows, connection_columns)}

## 输入/输出模态、能力和限制

{md_table(detailed_rows, capability_columns)}
"""

    connection_columns = [
        ("Provider", "provider"), ("Exact Model ID", "model_id"), ("Model type", "model_type"),
        ("Linked offer", "offer_id"), ("Free type", "free_type"), ("Free quota/scope", "quota"),
        ("Quota unit", "quota_unit"), ("API Base", "base"), ("OpenAI compatible", "openai"),
        ("Official source", "source"),
    ]
    capability_columns = [
        ("Provider / Model ID", "model"), ("Input modalities", "input_modalities"),
        ("Output modalities", "output_modalities"), ("Capability tags", "capabilities"),
        ("Tool calling", "tools"), ("Structured output", "structured"), ("Reasoning", "reasoning"),
        ("Context window", "context"), ("Rate limits", "limits"), ("Eligibility", "eligibility"),
        ("Validity", "expires"), ("Last verified", "verified_at"), ("Confidence", "confidence"),
        ("Capability evidence", "capabilities_source"),
    ]
    return f"""# Confirmed free or trial core LLMs

Generated from the catalog. This page includes active, recommended core models backed by official evidence at medium/high confidence ({len(rows)} unique provider + Model ID pairs). See the [related AI API directory](related-ai-apis.en.md) for extensions.

Free quota and rate limits are separate. `unknown` means the reviewed official source did not confirm the field. Eligibility may depend on account, region, project, and model.

## Free access and connection

{md_table(rows, connection_columns)}

## Input/output modalities, capabilities, and limits

{md_table(detailed_rows, capability_columns)}
"""


def render_related_ai(records: list[dict[str, Any]], language: str) -> str:
    rows = [row for row in model_rows(records, language, "related_ai_api") if row.get("model_type") != model_type_label("routing_alias", language)]
    detailed_rows = [{**row, "model": f"{row['provider']} / `{row['model_id']}`"} for row in rows]
    if language == "zh":
        return f"""# 相关 AI API 扩展资源

这些 API 可用于生成、检索或安全任务，但不是核心文本/多模态 LLM。它们单独列出，不计入 README 的核心模型数量。当前有 {len(rows)} 个已核实的扩展型号。

{md_table(rows, [('平台','provider'),('精确 Model ID','model_id'),('扩展类型','model_type'),('免费类型','free_type'),('额度/范围','quota'),('速率限制','limits'),('API Base','base'),('OpenAI 兼容','openai'),('官方来源','source')])}

## 输入/输出与能力详情

{md_table(detailed_rows, [('平台 / Model ID','model'),('输入模态','input_modalities'),('输出模态','output_modalities'),('能力标签','capabilities'),('工具调用','tools'),('结构化输出','structured'),('资格','eligibility'),('有效期','expires'),('核验日期','verified_at'),('来源','source')])}

未列型号不代表平台没有该类 API；只有当前免费方案和型号关系均有官方证据时才纳入本页。
"""
    return f"""# Related AI API extensions

These APIs support generation, retrieval, or safety tasks but are not core text/multimodal LLMs. They are listed separately and excluded from the README core model count. There are {len(rows)} verified extension model records.

{md_table(rows, [('Provider','provider'),('Exact Model ID','model_id'),('Extension type','model_type'),('Free type','free_type'),('Quota/scope','quota'),('Rate limits','limits'),('API Base','base'),('OpenAI compatible','openai'),('Official source','source')])}

## Input/output and capability details

{md_table(detailed_rows, [('Provider / Model ID','model'),('Input modalities','input_modalities'),('Output modalities','output_modalities'),('Capability tags','capabilities'),('Tool calling','tools'),('Structured output','structured'),('Eligibility','eligibility'),('Validity','expires'),('Last verified','verified_at'),('Source','source')])}

An omitted model does not mean a provider lacks that API category. Include a record only when both the current free offer and model relationship have official evidence.
"""


def render_provider_comparison(records: list[dict[str, Any]]) -> str:
    grouped = group_records(records)
    rows = []
    for provider_id, entries in sorted(grouped.items()):
        provider = entries["provider"][0] if entries["provider"] else {}
        active = [row for row in recommended(records) if row.get("provider_id") == provider_id]
        active_offer = any(row.get("record_level") == "offer" for row in active)
        core_models = {
            str(row.get("model_id", "")) for row in active
            if row.get("record_level") == "model" and row.get("model_scope") == "core_llm"
        }
        related_models = {
            str(row.get("model_id", "")) for row in active
            if row.get("record_level") == "model" and row.get("model_scope") == "related_ai_api"
            and row.get("model_type") != "routing_alias"
        }
        rows.append({
            "provider": provider.get("provider", provider_id),
            "provider_id": provider_id,
            "status": provider_status(provider, active_offer, "zh"),
            "offer_count": sum(1 for row in active if row.get("record_level") == "offer"),
            "model_count": len(core_models),
            "related_model_count": len(related_models),
            "free_types": "、".join(sorted({FREE_TYPE_ZH.get(str(row.get("free_type", "")), str(row.get("free_type", ""))) for row in active})) or "无已确认方案",
            "openai": compatibility_label(provider.get("openai_compatible", "unknown"), "zh"),
            "api_base": provider.get("api_base", "") or "未知 / 原生端点",
            "source": official_link(provider),
        })
    return """# 提供商对比

这里只比较当前 catalog 的证据和方案记录；未核实的速率限制、兼容性或数据政策保留为 unknown。

""" + md_table(rows, [
        ("平台", "provider"), ("Provider ID", "provider_id"), ("状态", "status"),
        ("Offer 数", "offer_count"), ("核心 LLM 数", "model_count"), ("扩展 API 数", "related_model_count"), ("免费类型", "free_types"),
        ("OpenAI 兼容", "openai"), ("API Base", "api_base"), ("官方来源", "source"),
    ]) + "\n"


def render_candidate_sources(records: list[dict[str, Any]]) -> str:
    rows = candidate_rows(records)
    provider_names = {
        str(row.get("provider_id", "")): str(row.get("provider", row.get("provider_id", "")))
        for row in records if row.get("record_level") == "provider"
    }
    core_provider_ids = {
        str(row.get("provider_id", "")) for row in recommended(records)
        if row.get("record_level") == "model" and row.get("model_scope") == "core_llm"
    }
    dynamic_rows = []
    for offer in recommended(records):
        if offer.get("record_level") != "offer" or str(offer.get("provider_id", "")) in core_provider_ids:
            continue
        dynamic_rows.append({
            "provider": provider_names.get(str(offer.get("provider_id", "")), offer.get("provider_id", "")),
            "type": FREE_TYPE_ZH.get(str(offer.get("free_type", "")), str(offer.get("free_type", ""))),
            "quota": localized(offer, "free_quota", "zh"),
            "eligibility": eligibility_summary(offer, "zh"),
            "source": official_link(offer),
        })
    return f"""# 候补与历史来源

本页由 provider-level 目录记录生成，涵盖本轮重点研究的国内外平台。候补不是免费 API 结论。只有官方政策与可用 API 型号均得到当前证据支持时，才进入推荐区。

## 尚待复核、非免费或仅有历史证据

{md_table(rows, [('平台','provider'),('状态','status'),('官方来源','source'),('原因/证据缺口','reason')])}

## 已确认免费方案，但未确认具体核心 LLM 型号

以下平台确有官方免费方案，但公开来源没有列出稳定、明确适用的核心 LLM ID，或者型号资格只在动态目录/账号中显示。README 不会因此推荐未验证的具体模型。

{md_table(dynamic_rows, [('平台','provider'),('免费方式','type'),('额度/限制','quota'),('账号条件与有效期','eligibility'),('官方来源','source')])}

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
    RELATED_AI_PATH.write_text(render_related_ai(records, "zh"), encoding="utf-8")
    RELATED_AI_EN_PATH.write_text(render_related_ai(records, "en"), encoding="utf-8")
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
