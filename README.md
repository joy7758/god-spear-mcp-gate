<!-- language-switch:start -->
<p>
  <a href="./README.md">
    <img src="https://img.shields.io/badge/English-Current-1f883d?style=for-the-badge" alt="English">
  </a>
  <a href="./README.zh-CN.md">
    <img src="https://img.shields.io/badge/Chinese-Switch-0f172a?style=for-the-badge" alt="Chinese">
  </a>
</p>
<!-- language-switch:end -->

# God Spear MCP Gate

Low-intrusion preflight trust gating for MCP-style tool requests.

Part of the Agent Runtime Safety Kit.  
This repo shows how to place a removable boundary check in front of MCP-style tool execution.

## Positioning

This is a minimal MCP-style preflight trust gate.
It sits before tool execution in a small runtime control chain.
It is not a full MCP server platform.

## What this is

- A docs-first and minimal runnable demo.
- A small CLI that reads a policy JSON and a request JSON.
- A removable preflight gate for MCP-style tool requests.
- A thin adapter pattern that can sit in front of tool execution.

## What this is not

- Not a full MCP server.
- Not a full agent framework.
- Not an official MCP standard extension.
- Not a deep runtime enforcement layer.

## Quickstart

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

## Demo Assets

- [Demo](docs/demo.md)
- [Integration Pattern](docs/integration-pattern.md)
- [Default Policy](examples/policies/default-policy.json)
- [Safe Read Request](examples/requests/safe-read.json)
- [Outside Root Write Request](examples/requests/outside-root-write.json)
- [Safe Read Decision](examples/results/safe-read.decision.json)
- [Outside Root Write Decision](examples/results/outside-root-write.decision.json)
- [Runtime Control Chain Overview](https://github.com/joy7758/token-governor/blob/main/docs/outreach/runtime-control-chain-overview.md)

## Decision Model

- If `requested_action` is listed in `denied_actions`, the gate returns `deny`.
- If `target` is outside `allowed_roots`, the gate returns `deny`.
- If `requested_action` is listed in `review_actions`, the gate returns `review`.
- If `requested_action` is listed in `allowed_actions` and `target` stays inside `allowed_roots`, the gate returns `allow`.
- Everything else falls back to `review`.

## Related Projects

- [God Spear](https://github.com/joy7758/god-spear)
- [Token Governor](https://github.com/joy7758/token-governor)
- [ARO Audit](https://github.com/joy7758/aro-audit)
