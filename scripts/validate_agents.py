#!/usr/bin/env python3
"""Validate Autohand markdown agent files and duplicate names."""

from __future__ import annotations

import sys
from pathlib import Path

from generate_registry import build_registry, format_registry

ROOT = Path(__file__).resolve().parents[1]
CATEGORIES = ROOT / "categories"
REGISTRY_PATH = ROOT / "registry.json"


def parse_frontmatter(text: str) -> tuple[dict[str, str], str] | None:
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end < 0:
        return None
    raw = text[4:end]
    body = text[end + 4 :].strip()
    meta: dict[str, str] = {}
    for line in raw.splitlines():
        if not line.strip():
            continue
        if ":" not in line:
            return None
        key, value = line.split(":", 1)
        meta[key.strip()] = value.strip()
    return meta, body


def main() -> int:
    seen: dict[str, Path] = {}
    errors: list[str] = []

    toml_files = sorted(CATEGORIES.rglob("*.toml"))
    if toml_files:
        for path in toml_files:
            errors.append(f"{path.relative_to(ROOT)}: catalog agents must be Autohand markdown, not TOML")

    for path in sorted(CATEGORIES.rglob("*.md")):
        if path.name == "README.md":
            continue

        parsed = parse_frontmatter(path.read_text(encoding="utf-8"))
        if parsed is None:
            errors.append(f"{path.relative_to(ROOT)}: missing frontmatter")
            continue
        meta, body = parsed

        name = path.stem
        description = meta.get("description")
        tools = meta.get("tools")
        if not description:
            errors.append(f"{path.relative_to(ROOT)}: missing description")
        if not tools:
            errors.append(f"{path.relative_to(ROOT)}: missing tools")
        if not body:
            errors.append(f"{path.relative_to(ROOT)}: missing prompt body")

        previous = seen.get(name)
        if previous:
            errors.append(
                f"{path.relative_to(ROOT)}: duplicate name {name!r}; first seen in {previous.relative_to(ROOT)}"
            )
        else:
            seen[name] = path

    expected_registry = format_registry(build_registry())
    if not REGISTRY_PATH.exists():
        errors.append("registry.json is missing; run scripts/generate_registry.py")
    elif REGISTRY_PATH.read_text(encoding="utf-8") != expected_registry:
        errors.append("registry.json is stale; run scripts/generate_registry.py")

    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    print(f"Validated {len(seen)} Autohand markdown agents.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
