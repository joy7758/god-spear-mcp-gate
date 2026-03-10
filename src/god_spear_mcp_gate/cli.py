"""Command-line interface for the minimal MCP gate demo."""

from __future__ import annotations

import argparse
import json
import sys

from .policy import evaluate_request, load_json


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Evaluate a minimal MCP-style request against a trust-gate policy."
    )
    parser.add_argument("--policy", required=True, help="Path to a policy JSON file.")
    parser.add_argument("--request", required=True, help="Path to a request JSON file.")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    policy = load_json(args.policy)
    request = load_json(args.request)
    decision = evaluate_request(policy, request)

    json.dump(decision, sys.stdout, indent=2)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
