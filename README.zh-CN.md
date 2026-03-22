<!-- language-switch:start -->
[English](./README.md) | [中文](./README.zh-CN.md)
<!-- language-switch:end -->

# 神枪MCP门

针对 MCP 式工具请求的低入侵预检信任门控。

智能体运行时安全工具包的一部分。
此仓库展示了如何在 MCP 风格的工具执行之前放置可移动的边界检查。

## 定位

这是一个最小的 MCP 式预检信任门。
它位于小型运行时控制链中的工具执行之前。
它不是完整的 MCP 服务器平台。

## 这是什么

- 文档优先且最小的可运行演示。
- 一个读取策略 JSON 和请求 JSON 的小型 CLI。
- 用于 MCP 式工具请求的可拆卸预检门。
- 可以位于工具执行前面的瘦适配器模式。

## 这不是什么

- 不是完整的 MCP 服务器。
- 不是一个完整的代理框架。
- 不是官方 MCP 标准扩展。
- 不是深层的运行时执行层。

## 快速入门

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
python -m pip install -e ".[test]"

python -m god_spear_mcp_gate.cli \
  --policy examples/policies/default-policy.json \
  --request examples/requests/safe-read.json

pytest
```

## 演示资产

- [演示](docs/demo.md)
- [集成模式](docs/integration-pattern.md)
- [默认策略](examples/policies/default-policy.json)
- [安全读取请求](examples/requests/safe-read.json)
- [外部根写请求](examples/requests/outside-root-write.json)
- [安全读取决策](examples/results/safe-read.decision.json)
- [外部根写入决策](examples/results/outside-root-write.decision.json)
- [运行时控制链概述](https://github.com/joy7758/token-governor/blob/main/docs/outreach/runtime-control-chain-overview.md)

## 决策模型

- 如果 `requested_action` 在 `denied_actions` 中列出，则门返回 `deny`。
- 如果 `target` 在 `allowed_roots` 之外，则门返回 `deny`。
- 如果 `requested_action` 在 `review_actions` 中列出，则门返回 `review`。
- 如果 `requested_action` 列在 `allowed_actions` 中，并且 `target` 保留在 `allowed_roots` 中，则门返回 `allow`。
- 其他一切都回到 `review`。

## 相关项目

- [神枪](https://github.com/joy7758/god-spear)
- [代币调控器](https://github.com/joy7758/token-governor)
- [ARO审核](https://github.com/joy7758/aro-audit)
