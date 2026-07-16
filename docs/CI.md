# Continuous Integration (CI)

## Overview

CosmoStream uses GitHub Actions to automatically verify code quality whenever changes are pushed to the repository or a pull request is opened.

The goal of Continuous Integration (CI) is to detect problems early by ensuring that all committed code satisfies the project's quality standards before it is merged.

---

## Workflow Location

The workflow configuration is located at:

```
.github/workflows/ci.yml
```

GitHub automatically detects workflows placed inside this directory.

---

## When the Workflow Runs

The CI workflow is triggered when:

- Code is pushed to the `main` branch.
- A Pull Request targeting the `main` branch is opened or updated.

---

## Quality Checks

The current CI pipeline performs the following checks:

### Ruff Linting

Checks the source code for common programming mistakes, style violations, and potential issues.

Command:

```bash
ruff check .
```

---

### Ruff Formatting

Verifies that all Python files follow the project's formatting rules.

Command:

```bash
ruff format --check .
```

Unlike local formatting, the CI pipeline does **not** modify files. It only reports formatting errors.

---

### Pre-commit Hooks

Runs the project's configured pre-commit hooks to ensure code quality standards are met.

Command:

```bash
pre-commit run --all-files
```

---

## Running the Checks Locally

Before pushing changes, developers should execute the same checks locally.

Using the project's Makefile:

```bash
make lint
make format
make check
```

Running these commands before every commit reduces the chances of CI failures.

---

## Current Workflow

```
Developer
    │
    ▼
Git Commit
    │
    ▼
Git Push
    │
    ▼
GitHub Actions
    │
    ▼
Checkout Repository
    │
    ▼
Setup Python
    │
    ▼
Install Development Tools
    │
    ▼
Run Ruff
    │
    ▼
Run Pre-commit
    │
    ▼
Pass ✓   or   Fail ✗
```

---

## Future Improvements

As CosmoStream evolves, the CI pipeline will be expanded to include:

- Automated unit testing
- Docker image builds
- Integration testing
- Security scanning
- Dependency vulnerability checks
- Coverage reports
- Deployment automation (CD)

---

## References

- GitHub Actions
- Ruff
- Pre-commit
