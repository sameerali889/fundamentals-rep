# AI Agent Instructions for fundamentals-rep

## Repository overview
- `fundamentals-rep` is a small Python learning repository with beginner-focused script examples.
- Core content lives in `new-sessions/`.
- `python-11AM/` is included as a git submodule and should be treated as external lesson content unless the user asks to modify it.

## What an AI agent should know
- There is no formal build or test system in this repo.
- Scripts are typically executed directly with `python` or `python3`.
- Keep code simple, clear, and beginner-friendly.
- Preserve existing comments and learning-oriented style unless the user requests a refactor.
- Avoid introducing advanced frameworks, packaging, or unrelated project scaffolding.

## File and directory guidance
- `new-sessions/`: primary working area for Python examples and exercises.
- `python-11AM/`: submodule content; do not change without explicit user direction.
- `__pycache__/` and temporary files are ignored by `.gitignore`.

## When to create new files
- Add new example scripts or guide notes only when the user asks for new lessons or exercises.
- Prefer using the existing naming and comment style found in `new-sessions/`.

## Helpful behavior
- When asked to edit code, focus on correctness, readability, and educational clarity.
- When asked to explain code, keep explanations accessible to beginners.
