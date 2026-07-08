#!/usr/bin/env python3
"""Convert Codex TOML subagents into Autohand markdown agents."""

from __future__ import annotations

import tomllib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CATEGORIES = ROOT / "categories"

READ_ONLY_TOOLS = ["read_file", "fff_grep", "fff_find"]
WORKSPACE_WRITE_TOOLS = [
    "read_file",
    "fff_grep",
    "fff_find",
    "apply_patch",
    "search_replace",
    "run_command",
]


def frontmatter_value(value: str) -> str:
    return value.replace("\n", " ").strip()


def tools_for_sandbox(sandbox_mode: str) -> list[str]:
    if sandbox_mode == "workspace-write":
        return WORKSPACE_WRITE_TOOLS
    return READ_ONLY_TOOLS


def convert_file(path: Path) -> Path:
    data = tomllib.loads(path.read_text(encoding="utf-8"))
    name = data.get("name")
    description = data.get("description")
    instructions = data.get("developer_instructions")

    if not isinstance(name, str) or not name.strip():
        raise ValueError(f"{path}: missing string name")
    if not isinstance(description, str) or not description.strip():
        raise ValueError(f"{path}: missing string description")
    if not isinstance(instructions, str) or not instructions.strip():
        raise ValueError(f"{path}: missing developer_instructions")

    sandbox_mode = str(data.get("sandbox_mode") or "read-only")
    model = data.get("model")
    tools = tools_for_sandbox(sandbox_mode)

    lines = [
        "---",
        f"description: {frontmatter_value(description)}",
        f"tools: {', '.join(tools)}",
    ]
    if isinstance(model, str) and model.strip():
        lines.append(f"model: {frontmatter_value(model)}")
    lines.extend([
        "---",
        "",
        instructions.strip(),
        "",
    ])

    target = path.with_suffix(".md")
    target.write_text("\n".join(lines), encoding="utf-8")
    path.unlink()
    return target


def update_links(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    text = text.replace(".toml)", ".md)")
    text = text.replace("valid `.toml` file", "valid `.md` file")
    text = text.replace("`.toml` files", "`.md` files")
    text = text.replace("TOML file", "markdown file")
    path.write_text(text, encoding="utf-8")


def main() -> int:
    converted = [convert_file(path) for path in sorted(CATEGORIES.rglob("*.toml"))]

    for path in [ROOT / "README.md", ROOT / "CONTRIBUTING.md", *CATEGORIES.glob("*/README.md")]:
        update_links(path)

    print(f"Converted {len(converted)} agents to Autohand markdown.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
