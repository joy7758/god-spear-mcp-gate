# Integration Pattern

This repository shows a minimal pattern for placing a preflight trust gate in front of MCP-style tool execution. It is a demo pattern, not an official MCP standard extension.

```text
MCP-style request
  -> preflight gate
  -> allowed tool execution
  -> optional ARO receipt
  -> optional Token Governor cost hook
```

In the smallest integration, a request payload is checked against a local policy before the tool layer runs. If the request is allowed, the tool executes. Teams can optionally attach an ARO Audit receipt after execution and a Token Governor cost hook around the run.
