# Free LLM API Watch

[中文](README.md) · Project: [Leestars21/free-llm-api-watch](https://github.com/Leestars21/free-llm-api-watch)

Find LLM APIs with free access. This directory tracks providers, free offers, models and official evidence, including recurring tiers, new-user credits and promotions.

## Start here

| Provider | Free offer | Allowance and limits | Verified | Official source |
| --- | --- | --- | --- | --- |
| Google Gemini API / Google AI Studio | Recurring free tier (usage/rate limits apply) | Model-specific $0 input/output pricing; per-project free-tier rate limits vary by model and account; valid: No fixed end date published; model/region elig… | 2026-11-02 | [Gemini Developer API pricing and rate limits](https://ai.google.dev/gemini-api/docs/pricing) |
| GroqCloud | Recurring free tier (usage/rate limits apply) | Free Plan API usage is available at no charge within per-model rate limits; no separate token grant is documented; valid: No fixed end date stated; Free P… | 2026-11-01 | [Groq Free Plan rate limits and supported models](https://console.groq.com/docs/rate-limits) |
| Cloudflare Workers AI | Recurring free tier (usage/rate limits apply) | 10,000 Neurons/day; valid: No fixed end date published | 2026-11-02 | [Workers AI pricing and changelog](https://developers.cloudflare.com/workers-ai/platform/pricing/) |
| OpenRouter | Free router model | No token grant; models listed with zero prompt/completion prices are free while listed; valid: Model free status may change without notice | 2026-11-01 | [OpenRouter free model rate limits](https://openrouter.ai/collections/free-models) |

These are selected starting points, not a ranking or a complete list. Offers, models, regions and account eligibility can change; check the official source and your account. Review dates are recorded per entry in the full directory; the latest date does not mean every entry was reviewed then.

- **[All providers and free offers](docs/free-api-guide.md)**: allowances, eligibility, expiry and official sources.
- **[All free LLM models](docs/free-models.en.md)**: exact Model IDs, API endpoints, limits and individual review dates.
- [Provider comparison](docs/provider-comparison.md) · [Other AI APIs](docs/related-ai-apis.en.md) · [Candidate and historical records](docs/candidate-sources.md)

Free tiers have usage and rate limits. New-user credits and promotions are not permanent free access; a model appearing in an API list does not prove free use. The offers guide and provider comparison are currently in Chinese.

### 🤖 Let AI help you find a free API

Share this repository and your use case with an AI assistant such as ChatGPT, Claude or Gemini. It can help you filter and compare options for your needs, saving you from checking each provider's models, allowances and API documentation yourself. Copy and adapt this prompt:

```text
Please read the README, free API guide, free models list and provider comparison at https://github.com/Leestars21/free-llm-api-watch.

I need a free API to summarize academic papers in a Zotero plugin. I would like a long context window and, ideally, OpenAI API compatibility. Please find suitable options for this use case and compare their free allowances, model capabilities, context lengths, rate limits, registration requirements and OpenAI API compatibility.

Where possible, consult official provider documentation to verify current free policies and model availability. Give the exact Model ID, API endpoint and sign-up link for each recommended model. Distinguish recurring free access, new-user credits and limited-time promotions; do not treat historical free offers as currently available. Clearly identify anything you cannot verify, and do not invent allowances or availability.
```

AI recommendations are for reference only. Actual availability should be confirmed against the provider's official documentation, account console and API test results.

## Data and updates

The catalog combines official sources and automated updates; failed checks do not refresh old evidence. See the [update workflow](.github/workflows/update-catalog.yml), [changelog](docs/changelog.md) and [privacy and risk](docs/privacy-and-risk.md). Verify terms before use and never publish API keys or sensitive data.

Issues and pull requests are welcome. MIT license; see [LICENSE](LICENSE).
