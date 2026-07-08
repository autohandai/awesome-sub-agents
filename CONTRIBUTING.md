# Contributing to Awesome Sub-Agents

Thanks for contributing.

This repository is an Autohand-curated collection of Autohand Code sub-agents (`.md` files). Contributions should prioritize practical usefulness, clear scope, and compatibility with Autohand Code behavior.

## How to Contribute

### Add a New Subagent

1. Choose the correct category under `categories/`.
2. Add one `.md` file for the new agent.
3. Update both:
   - `README.md` (main category listing)
   - `categories/<category>/README.md` (linked bullet + short description)
4. Keep agent names sorted alphabetically where possible.
5. Open a PR with the use case and why this agent is distinct.

### Improve an Existing Subagent

1. Keep the role bounded (avoid broad persona text).
2. Preserve Autohand markdown format.
3. Update relevant README descriptions if behavior or intent changed.
4. Include before/after rationale in your PR.

## Required Agent Format

Each agent must be a valid Autohand markdown file and include frontmatter:

- `description`
- `tools`

Common optional fields:

- `model`

The markdown body is the agent prompt.

## Authoring Quality Bar

The prompt body should be concrete and task-shaped. Use this structure:

- `Working mode`
- `Focus on`
- `Quality checks`
- `Return`
- `Do not ... unless explicitly requested by the parent agent.`

Avoid:

- Unsupported tool/platform assumptions
- Generic roleplay text with no output contract
- Scope creep instructions ("always do everything")

## Model and Sandbox Guidance

- Prefer `gpt-5.4` for complex reasoning/review roles.
- Prefer `gpt-5.3-codex-spark` for lighter search/synthesis roles.
- Use read-only tools by default for review/research agents.
- Use write-capable tools only when the agent must implement changes.

## Validation Checklist (Before PR)

- All links in `README.md` and category READMEs resolve.
- New/edited `.md` files parse correctly.
- Agent `name` is unique across repository.
- Main and category READMEs include the new agent.
- Descriptions stay concise and accurate to current behavior.

## Pull Request Checklist

- [ ] Added/updated agent markdown file(s)
- [ ] Updated main `README.md`
- [ ] Updated category `README.md`
- [ ] Verified links and markdown agent validity
- [ ] Included clear PR description and motivation

## Style Notes

- Keep documentation in English.
- Prefer precise, practical wording over marketing language.
- Keep descriptions short; keep instructions high-signal.

## License

By contributing, you agree your contributions are provided under the repository license terms.
