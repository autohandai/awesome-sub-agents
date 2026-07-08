# AGENTS.md

This repository is a curated catalog of Autohand Code sub-agent definitions.

## Rules

- Keep each subagent as a valid Autohand markdown agent file.
- Add new agents under the most specific `categories/<category>/` directory.
- Update both the root `README.md` and the category `README.md` when adding, removing, renaming, or materially changing an agent.
- Preserve upstream attribution and MIT license notices.
- Validate frontmatter, prompt bodies, and unique agent filenames before committing.

## Validation

```bash
find categories -name '*.md' ! -name README.md | wc -l
python3 scripts/validate_agents.py
```
