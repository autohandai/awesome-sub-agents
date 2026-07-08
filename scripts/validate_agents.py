#!/usr/bin/env python3
"""Validate agent TOML files and duplicate names."""

from __future__ import annotations

import sys
import tomllib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CATEGORIES = ROOT / "categories"


def main() -> int:
    seen: dict[str, Path] = {}
    errors: list[str] = []

    for path in sorted(CATEGORIES.rglob("*.toml")):
        try:
            data = tomllib.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:  # noqa: BLE001 - report every TOML parse failure.
            errors.append(f"{path.relative_to(ROOT)}: invalid TOML: {exc}")
            continue

        name = data.get("name")
        if not isinstance(name, str) or not name.strip():
            errors.append(f"{path.relative_to(ROOT)}: missing string name")
            continue

        previous = seen.get(name)
        if previous:
            errors.append(
                f"{path.relative_to(ROOT)}: duplicate name {name!r}; first seen in {previous.relative_to(ROOT)}"
            )
        else:
            seen[name] = path

    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    print(f"Validated {len(seen)} agents.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
