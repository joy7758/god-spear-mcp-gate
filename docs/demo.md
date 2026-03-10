# Demo

## Scenario

This demo places a small preflight gate in front of MCP-style tool execution. A request is checked against a compact policy before any tool action is allowed to run.

## Policy

The example policy keeps the control removable and low intrusion. It declares allowed actions, denied actions, review actions, and approved target roots.

- [default-policy.json](../examples/policies/default-policy.json)

## Safe Path

The safe path is a read request aimed at an approved workspace document. The request stays inside the allowed roots and uses an allowed action.

- [safe-read.json](../examples/requests/safe-read.json)
- [safe-read.decision.json](../examples/results/safe-read.decision.json)

## Blocked Path

The blocked path is a write request aimed outside the approved roots. The gate denies it before execution and returns a clear reason.

- [outside-root-write.json](../examples/requests/outside-root-write.json)
- [outside-root-write.decision.json](../examples/results/outside-root-write.decision.json)

## Why this matters

The point of the demo is not deep enforcement. It shows a removable, low-intrusion boundary check before execution so teams can make preflight trust decisions with a small amount of code.
