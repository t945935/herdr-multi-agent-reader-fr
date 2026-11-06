#!/usr/bin/env python3
"""Dispatch to an already-started idle agent; verify a task-specific receipt."""
import argparse
import json
import os
import subprocess
import uuid
from pathlib import Path


def call(*args, timeout=310):
    done = subprocess.run(["herdr", *args], text=True, capture_output=True, timeout=timeout)
    if done.returncode:
        raise RuntimeError(done.stderr or done.stdout)
    return json.loads(done.stdout)["result"]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("target")
    parser.add_argument("prompt", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if os.environ.get("HERDR_ENV") != "1":
        raise SystemExit("Run inside Herdr")
    agent = call("agent", "get", args.target)["agent"]
    if agent["agent_status"] not in {"idle", "done"}:
        raise SystemExit("Agent must be idle/done before this task starts")
    path = args.output.resolve()
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        raise SystemExit("Choose a new receipt path; do not reuse an earlier task")
    task_id = uuid.uuid4().hex
    prompt = args.prompt.read_text() + (
        f"\n\nCe task_id={task_id}\ncompletion_path={path}\n"
        'Effectuez réellement la tâche, puis écrivez le JSON : {"task_id":"l’identifiant ci-dessus","status":"completed",'
        '"summary":"livrables précis et vérification","artifacts":["chemins réels des artefacts"]}。'
        "Si vous ne pouvez pas terminer, utilisez status=blocked et expliquez pourquoi dans summary. Ne démarrez pas d’autres agents."
    )
    settled = call("agent", "prompt", args.target, prompt, "--wait", "--timeout", "300000")
    state = settled["agent"]["agent_status"]
    if state not in {"idle", "done"} or not path.is_file():
        raise SystemExit("Agent settled without an accepted receipt; inspect agent get/read")
    receipt = json.loads(path.read_text())
    if receipt.get("task_id") != task_id or receipt.get("status") != "completed" or not receipt.get("summary"):
        raise SystemExit("Receipt does not accept this task")
    for artifact in receipt.get("artifacts", []):
        candidate = Path(artifact)
        if not candidate.is_absolute():
            candidate = Path.cwd() / candidate
        if not candidate.is_file():
            raise SystemExit(f"Missing artifact: {artifact}")
    print(json.dumps(receipt, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
