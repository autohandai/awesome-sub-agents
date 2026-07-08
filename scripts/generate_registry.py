#!/usr/bin/env python3
"""Generate the Autohand sub-agent registry from catalog markdown files."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CATEGORIES = ROOT / "categories"
REGISTRY_PATH = ROOT / "registry.json"
REPOSITORY_URL = "https://github.com/autohandai/awesome-sub-agents"


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        raise ValueError("missing frontmatter")
    end = text.find("\n---", 4)
    if end < 0:
        raise ValueError("missing closing frontmatter")
    raw = text[4:end]
    meta: dict[str, str] = {}
    for line in raw.splitlines():
        if not line.strip():
            continue
        if ":" not in line:
            raise ValueError(f"invalid frontmatter line: {line}")
        key, value = line.split(":", 1)
        meta[key.strip()] = value.strip()
    return meta


def build_registry() -> dict[str, Any]:
    agents: list[dict[str, Any]] = []
    for path in sorted(CATEGORIES.rglob("*.md")):
        if path.name == "README.md":
            continue
        meta = parse_frontmatter(path.read_text(encoding="utf-8"))
        relative_path = path.relative_to(ROOT).as_posix()
        tools = [tool.strip() for tool in meta.get("tools", "").split(",") if tool.strip()]
        agent: dict[str, Any] = {
            "name": path.stem,
            "description": meta.get("description", ""),
            "category": path.parent.name,
            "path": relative_path,
            "tools": tools,
        }
        model = meta.get("model")
        if model:
            agent["model"] = model
        agents.append(agent)

    return {
        "schemaVersion": 1,
        "repository": REPOSITORY_URL,
        "agents": agents,
    }


def format_registry(registry: dict[str, Any]) -> str:
    return json.dumps(registry, indent=2, ensure_ascii=False) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Fail if registry.json is missing or stale")
    args = parser.parse_args()

    expected = format_registry(build_registry())
    if args.check:
        if not REGISTRY_PATH.exists():
            print("registry.json is missing; run scripts/generate_registry.py", file=sys.stderr)
            return 1
        actual = REGISTRY_PATH.read_text(encoding="utf-8")
        if actual != expected:
            print("registry.json is stale; run scripts/generate_registry.py", file=sys.stderr)
            return 1
        print("registry.json is up to date.")
        return 0

    REGISTRY_PATH.write_text(expected, encoding="utf-8")
    print("Generated registry.json.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
