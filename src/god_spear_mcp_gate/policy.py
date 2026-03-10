"""Minimal policy evaluation helpers for MCP-style preflight checks."""

from __future__ import annotations

import json
import posixpath
from pathlib import Path
from typing import Any


def load_json(path: str | Path) -> dict[str, Any]:
    with Path(path).open("r", encoding="utf-8") as handle:
        return json.load(handle)


def normalize_path(value: str) -> str:
    return posixpath.normpath(value.replace("\\", "/"))


def target_in_allowed_roots(target: str, allowed_roots: list[str]) -> bool:
    normalized_target = normalize_path(target)
    for root in allowed_roots:
        normalized_root = normalize_path(root).rstrip("/")
        if normalized_target == normalized_root:
            return True
        if normalized_target.startswith(normalized_root + "/"):
            return True
    return False


def build_decision(
    request: dict[str, Any],
    decision: str,
    reason: str,
    policy_refs: list[str],
) -> dict[str, Any]:
    return {
        "request_id": request.get("request_id", "unknown"),
        "requested_action": request.get("requested_action", ""),
        "target": request.get("target", ""),
        "decision": decision,
        "reason": reason,
        "policy_refs": policy_refs,
    }


def evaluate_request(policy: dict[str, Any], request: dict[str, Any]) -> dict[str, Any]:
    action = request.get("requested_action", "")
    target = request.get("target", "")

    denied_actions = policy.get("denied_actions", [])
    review_actions = policy.get("review_actions", [])
    allowed_actions = policy.get("allowed_actions", [])
    allowed_roots = policy.get("allowed_roots", [])

    if action in denied_actions:
        return build_decision(
            request,
            "deny",
            "Requested action is explicitly denied by policy.",
            ["denied_actions"],
        )

    if not target_in_allowed_roots(target, allowed_roots):
        return build_decision(
            request,
            "deny",
            "Target is outside allowed roots.",
            ["allowed_roots"],
        )

    if action in review_actions:
        return build_decision(
            request,
            "review",
            "Requested action requires review before execution.",
            ["review_actions", "allowed_roots"],
        )

    if action in allowed_actions:
        return build_decision(
            request,
            "allow",
            "Requested action is allowed within approved roots.",
            ["allowed_actions", "allowed_roots"],
        )

    return build_decision(
        request,
        "review",
        "Requested action is not explicitly classified by policy.",
        ["allowed_actions", "review_actions", "allowed_roots"],
    )
