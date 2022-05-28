<h1>notification-gateway-lite</h1>

# 简介

notification-gateway-lite 是一个非常轻量的通知网关，可以聚合各种推送渠道，使用 Serverless 部署，几乎零成本运行。

# 特性

- 支持各种常见的推送渠道，如Bark、企业微信等
- 支持部署成腾讯云Serverless，几乎零成本运行
- 解决因为群晖DSM奇怪的webhook设置方式而无法接入一些推送渠道的问题

## 目前支持的通知方式

- [Bark](https://github.com/Finb/Bark)
- [企业微信应用消息](https://developer.work.weixin.qq.com/document/path/90236)
- [企业微信机器人webhook](https://developer.work.weixin.qq.com/document/path/91770)

### 可能会支持的推送方式
- [ ] 钉钉
- [ ] pushplus
- [ ] ...

> 如果有需要的通知方式，请提交issue


# 部署方式

- [腾讯云Serverless](docs/TencentcloudServerless.md)
- [Docker](docs/Docker.md)

# 接口文档

见 [接口文档](docs/Api.md)

# 示例应用

- [使用 notification-gateway-lite 接收群晖DSM推送](docs/example/DSM.md)
