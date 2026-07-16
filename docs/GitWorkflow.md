# Git Workflow

## Branch Strategy

main
feature/<feature-name>
experiment/<topic>

## Commit Convention

feat:
fix:
docs:
build:
refactor:
test:
chore:

## Development Workflow

1. Create a feature branch
2. Develop
3. Run quality checks
4. Commit
5. Merge into main

## Pre-commit Hooks

Automatically runs:

- Ruff Check
- Ruff Format

## Useful Commands

git status
git log --oneline --decorate --graph
git switch
git switch -c
git restore
git reset --soft HEAD~1
git stash

## Before Every Commit

make lint
make format
make check
