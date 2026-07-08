# AGENTS.md

This repository is a curated catalog of Codex-native subagent definitions.

## Rules

- Keep each subagent as a valid `.toml` file.
- Add new agents under the most specific `categories/<category>/` directory.
- Update both the root `README.md` and the category `README.md` when adding, removing, renaming, or materially changing an agent.
- Preserve upstream attribution and MIT license notices.
- Validate TOML parsing and unique agent filenames before committing.

## Validation

```bash
find categories -name '*.toml' | wc -l
python3 scripts/validate_agents.py
```
