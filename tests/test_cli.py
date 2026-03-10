from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
POLICY = ROOT / "examples" / "policies" / "default-policy.json"


def run_cli(request_file: Path) -> dict[str, object]:
    completed = subprocess.run(
        [
            sys.executable,
            "-m",
            "god_spear_mcp_gate.cli",
            "--policy",
            str(POLICY),
            "--request",
            str(request_file),
        ],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return json.loads(completed.stdout)


def test_safe_read_returns_allow() -> None:
    request_file = ROOT / "examples" / "requests" / "safe-read.json"
    decision = run_cli(request_file)

    assert decision["decision"] == "allow"
    assert decision["requested_action"] == "read_file"
    assert decision["target"] == "workspace/docs/approved-vendors.md"


def test_outside_root_write_returns_deny() -> None:
    request_file = ROOT / "examples" / "requests" / "outside-root-write.json"
    decision = run_cli(request_file)

    assert decision["decision"] == "deny"
    assert decision["requested_action"] == "write_file"
    assert "outside allowed roots" in str(decision["reason"]).lower()
