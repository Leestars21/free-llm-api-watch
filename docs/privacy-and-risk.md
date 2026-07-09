# Privacy and Risk Notes

## 排除项

本项目不收录以下渠道：

- 共享 API key；
- 逆向网页接口；
- 盗用账号、拼车账号或 cookie/session token 中转；
- 声称无限 GPT/Claude/Gemini 的非官方中转；
- 无公开主体、无服务条款、无隐私政策的 API；
- 要求用户上传账号密码、cookie、session token 的服务。

## 第三方路由风险

第三方路由和推理平台可能带来额外风险：

- 请求和响应会经过路由平台；
- 上游模型、价格、速率限制可能随时变化；
- 数据训练、日志保留、滥用审核策略可能与官方模型厂商不同；
- 免费模型可能有低速率、队列、上下文、地区或账号限制。

使用前必须复核 `source_url`、服务条款、隐私政策和 `last_checked`。

## Source snapshot 约束

`data/source_snapshots.json` 不保存完整网页正文，只保存：

- `source_url`
- `fetched_at`
- `http_status`
- `page_title`
- `relevant_excerpt`，最多 500 字
- `extracted_fields`
- `hash`
- `parser_status`

不要把大段官方文档、pricing 页面全文或完整 API 响应复制进仓库。
