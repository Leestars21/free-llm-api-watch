# 提供商对比

这里只比较当前 catalog 的证据和方案记录；未核实的速率限制、兼容性或数据政策保留为 unknown。

| 平台 | Provider ID | 状态 | Offer 数 | 核心 LLM 数 | 扩展 API 数 | 免费类型 | OpenAI 兼容 | API Base | 官方来源 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AI Horde / AI Horde OpenAI API | ai-horde | 已确认免费方案（按来源所述范围） | 1 | 0 | 0 | 社区志愿算力（动态排队） | 是 | https://oai.aihorde.net/v1 | [AI Horde OpenAI API documentation](https://oai.aihorde.net/) |
| AI21 Labs | ai21-labs | 待复核 | 0 | 0 | 0 | 无已确认方案 | 否 | https://api.ai21.com/studio/v1 | [AI21 Labs follow-up review](https://docs.ai21.com/) |
| Alibaba Cloud Model Studio / Qwen | alibaba-model-studio | 已确认免费方案（按来源所述范围） | 1 | 1 | 0 | 新用户赠额 / 免费使用上限 | 是 | https://dashscope.aliyuncs.com/compatible-mode/v1 | [Model Studio new-user free quota](https://help.aliyun.com/zh/model-studio/new-free-quota/) |
| Anthropic Claude API (protocol reference) | anthropic-api | 未验证 | 0 | 0 | 0 | 无已确认方案 | 否 | https://api.anthropic.com | [Anthropic Messages API](https://docs.anthropic.com/en/api/messages) |
| Baichuan AI API | baichuan | 待复核 | 0 | 0 | 0 | 无已确认方案 | 未知 | 未知 / 原生端点 | [Baichuan follow-up review](https://platform.baichuan-ai.com/docs) |
| Baidu Qianfan / ERNIE | baidu-qianfan | 已确认免费方案（按来源所述范围） | 1 | 0 | 0 | 新用户赠额 / 免费使用上限 | 部分兼容 | https://qianfan.baidubce.com | [Baidu Qianfan product documentation](https://cloud.baidu.com/doc/Qianfan/index.html) |
| Cerebras Inference | cerebras | 已确认免费方案（按来源所述范围） | 1 | 0 | 0 | 一次性试用额度 | 是 | https://api.cerebras.ai/v1 | [Cerebras current pricing](https://www.cerebras.ai/pricing) |
| Cloudflare Workers AI | cloudflare-workers-ai | 已确认免费方案（按来源所述范围） | 1 | 2 | 0 | 长期免费层（有用量/速率限制） | 部分兼容 | https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/run | [Workers AI pricing](https://developers.cloudflare.com/workers-ai/platform/pricing/) |
| Cohere API | cohere | 已确认免费方案（按来源所述范围） | 1 | 3 | 2 | 每月免费评估额度 | 部分兼容 | https://api.cohere.com/v2 | [Cohere API rate limits](https://docs.cohere.com/v2/docs/rate-limits) |
| DeepInfra | deepinfra | 已复核：当前未确认免费 API | 0 | 0 | 0 | 无已确认方案 | 是 | https://api.deepinfra.com/v1/openai | [DeepInfra pricing and billing](https://deepinfra.com/pricing) |
| DeepSeek API | deepseek | 已复核：当前未确认免费 API | 0 | 0 | 0 | 无已确认方案 | 是 | https://api.deepseek.com | [DeepSeek API pricing](https://api-docs.deepseek.com/quick_start/pricing) |
| Fireworks AI | fireworks-ai | 待复核 | 0 | 0 | 0 | 无已确认方案 | 是 | https://api.fireworks.ai/inference/v1 | [Fireworks AI pricing](https://fireworks.ai/pricing) |
| GitHub Models (retired service) | github-models | 已停止 / 已下架 | 0 | 0 | 0 | 无已确认方案 | 未知 | 未知 / 原生端点 | [GitHub Models documentation](https://docs.github.com/en/github-models) |
| Google Gemini API / Google AI Studio | google-gemini | 已确认免费方案（按来源所述范围） | 1 | 2 | 2 | 长期免费层（有用量/速率限制） | 部分兼容 | https://generativelanguage.googleapis.com | [Gemini Developer API pricing](https://ai.google.dev/gemini-api/docs/pricing) |
| GroqCloud | groqcloud | 已确认免费方案（按来源所述范围） | 1 | 3 | 7 | 长期免费层（有用量/速率限制） | 是 | https://api.groq.com/openai/v1 | [GroqCloud models and rate limits](https://console.groq.com/docs/rate-limits) |
| Hugging Face Inference Providers | huggingface-inference-providers | 已确认免费方案（按来源所述范围） | 1 | 0 | 0 | 长期免费层（有用量/速率限制） | 是 | https://router.huggingface.co/v1 | [Inference Providers pricing](https://huggingface.co/docs/inference-providers/en/pricing) |
| Hyperbolic | hyperbolic | 待复核 | 0 | 0 | 0 | 无已确认方案 | 是 | https://api.hyperbolic.xyz/v1 | [Hyperbolic follow-up review](https://docs.hyperbolic.xyz/) |
| iFlytek Spark API | iflytek-spark | 待复核 | 0 | 0 | 0 | 无已确认方案 | 未知 | 未知 / 原生端点 | [iFlytek Spark follow-up review](https://www.xfyun.cn/doc/spark/Web.html) |
| MiniMax API | minimax | 待复核 | 0 | 0 | 0 | 无已确认方案 | 部分兼容 | https://api.minimax.chat/v1 | [MiniMax API follow-up review](https://platform.minimaxi.com/document/) |
| Mistral La Plateforme | mistral | 已确认免费方案（按来源所述范围） | 1 | 0 | 0 | 长期免费层（有用量/速率限制） | 部分兼容 | https://api.mistral.ai | [Mistral Studio quickstart and usage limits](https://docs.mistral.ai/getting-started/quickstarts/developer/first-api-request) |
| ModelScope Inference / 魔搭社区 | modelscope | 已确认免费方案（按来源所述范围） | 1 | 0 | 0 | 长期免费层（有用量/速率限制） | 是 | https://api-inference.modelscope.cn/v1 | [ModelScope MoLi points announcement](https://www.modelscope.cn/posts/435591) |
| Moonshot / Kimi API | moonshot-kimi | 已复核：当前未确认免费 API | 0 | 0 | 0 | 无已确认方案 | 是 | https://api.moonshot.cn/v1 | [Moonshot API pricing](https://platform.moonshot.cn/docs/pricing/chat) |
| Nebius AI Studio | nebius-ai | 待复核 | 0 | 0 | 0 | 无已确认方案 | 是 | https://api.studio.nebius.com/v1 | [Nebius AI Studio follow-up review](https://dev.nebius.com/) |
| Novita AI | novita | 已确认免费方案（按来源所述范围） | 4 | 5 | 0 | 指定免费模型、新用户赠额 / 免费使用上限、限时活动 | 是 | https://api.novita.ai/openai | [Novita AI model pricing and model pages](https://novita.ai/pricing) |
| NVIDIA Build / API Catalog | nvidia-build | 待复核 | 0 | 0 | 0 | 无已确认方案 | 是 | https://integrate.api.nvidia.com/v1 | [NVIDIA NIM getting started](https://docs.nvidia.com/nim/large-language-models/latest/get-started/) |
| Ollama Cloud | ollama-cloud | 已确认免费方案（按来源所述范围） | 1 | 0 | 0 | 长期免费层（有用量/速率限制） | 部分兼容 | https://ollama.com/api | [Ollama Cloud pricing](https://www.ollama.com/pricing) |
| OpenAI API (protocol reference) | openai-api | 未验证 | 0 | 0 | 0 | 无已确认方案 | 是 | https://api.openai.com/v1 | [OpenAI API reference](https://platform.openai.com/docs/api-reference) |
| OpenRouter | openrouter | 已确认免费方案（按来源所述范围） | 1 | 12 | 2 | 免费路由模型 | 是 | https://openrouter.ai/api/v1 | [OpenRouter free models and rate limits](https://openrouter.ai/collections/free-models) |
| Reka AI Vision API | reka-ai | 已确认免费方案（按来源所述范围） | 1 | 0 | 0 | 一次性试用额度 | 否 | https://vision-agent.api.reka.ai | [Reka Vision API pricing](https://docs.reka.ai/vision/pricing) |
| Replicate | replicate | 已确认免费方案（按来源所述范围） | 1 | 0 | 0 | 一次性试用额度 | 部分兼容 | https://api.replicate.com/v1 | [Replicate billing documentation](https://replicate.com/docs/topics/billing) |
| SambaNova Cloud | sambanova-cloud | 已复核：当前未确认免费 API | 0 | 0 | 0 | 无已确认方案 | 是 | https://api.sambanova.ai/v1 | [SambaCloud plans and billing](https://cloud.sambanova.ai/plans) |
| SiliconFlow | siliconflow | 已确认免费方案（按来源所述范围） | 1 | 0 | 0 | 指定免费模型 | 是 | https://api.siliconflow.cn/v1 | [SiliconFlow rate limits and free-model documentation](https://docs.siliconflow.cn/docs/userguide/faqs/rate-limit-and-upgradation) |
| Tencent Cloud TokenHub | tencent-tokenhub | 已确认免费方案（按来源所述范围） | 2 | 2 | 0 | 一次性试用额度、限时活动 | 是 | https://tokenhub.tencentmaas.com/v1 | [TokenHub free experience package](https://intl.cloud.tencent.com/zh/document/product/1300/80423) |
| Tencent Cloud Hunyuan API (legacy platform) | tencent-tokenhub-hunyuan | 历史记录 | 0 | 0 | 0 | 无已确认方案 | 未知 | 未知 / 原生端点 | [Tencent Cloud migration announcement](https://cloud.tencent.com/announce/detail/2287) |
| Together AI | together-ai | 已复核：当前未确认免费 API | 0 | 0 | 0 | 无已确认方案 | 是 | https://api.together.xyz/v1 | [Together AI free-tier and billing update](https://support.together.ai/articles/1862638756-changes-to-free-tier-and-billing-july-2025) |
| Vercel AI Gateway | vercel-ai-gateway | 已确认免费方案（按来源所述范围） | 1 | 2 | 0 | 长期免费层（有用量/速率限制） | 是 | https://ai-gateway.vercel.sh/v1 | [Vercel AI Gateway pricing and model catalog](https://vercel.com/docs/ai-gateway/pricing) |
| Volcengine Ark / Doubao | volcengine-ark | 已确认免费方案（按来源所述范围） | 1 | 0 | 0 | 新用户赠额 / 免费使用上限 | 是 | https://ark.cn-beijing.volces.com/api/v3 | [Ark free inference quota and safe experience mode](https://docs.volcengine.com/docs/ark/free-tokens-only-mode?lang=zh) |
| 01.AI Yi API | yi-api | 待复核 | 0 | 0 | 0 | 无已确认方案 | 未知 | 未知 / 原生端点 | [01.AI follow-up review](https://platform.lingyiwanwu.com/docs) |
| Zhipu BigModel / GLM | zhipu-bigmodel | 已确认免费方案（按来源所述范围） | 1 | 1 | 0 | 指定免费模型 | 部分兼容 | https://open.bigmodel.cn/api/paas/v4 | [Zhipu GLM-4.7-Flash announcement](https://www.zhipuai.cn/zh/news/148) |
