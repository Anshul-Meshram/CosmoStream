# VS Code Setup

This document describes the recommended Visual Studio Code configuration for developing CosmoStream.

---

## Required Extensions

Install the following extensions:

- Python (`ms-python.python`)
- Ruff (`charliermarsh.ruff`)
- Docker (`ms-azuretools.vscode-docker`)
- GitHub Actions (`github.vscode-github-actions`)
- YAML (`redhat.vscode-yaml`)
- Markdown All in One (`yzhang.markdown-all-in-one`)
- GitLens (`eamodio.gitlens`)

These extensions provide support for Python development, Docker, YAML files, GitHub Actions workflows, Markdown editing, and Git history.

---

## Workspace Settings

The project includes a `.vscode/settings.json` file that configures the editor with the recommended settings.

Current configuration includes:

- Automatic formatting on save
- Ruff as the default Python formatter
- Removal of trailing whitespace
- Automatic insertion of a final newline
- Hidden Python cache directories

These settings help maintain a consistent coding style across the project.

---

## Debug Configuration

A debug configuration is provided in `.vscode/launch.json`.

It allows the backend FastAPI application to be started directly from VS Code for debugging purposes.

For normal development, the preferred method is:

```bash
docker compose up --build
```

The launch configuration is mainly intended for debugging Python code.

---

## Opening the Project

Open the repository root directory in VS Code.

```bash
code .
```

Do **not** open only the `backend` folder.

Opening the repository root ensures that:

- Workspace settings are loaded
- Recommended extensions are detected
- The complete project structure is available

---

## Using the Integrated Terminal

Open the integrated terminal using:

- **Terminal → New Terminal**
- or `Ctrl + \``

Run all project commands from the repository root.

Examples:

```bash
docker compose up --build
```

```bash
git status
```

```bash
ruff check backend
```

```bash
pre-commit run --all-files
```

---

## Project Structure

The VS Code workspace is configured for the complete CosmoStream repository.

```
CosmoStream/
├── backend/
├── frontend/
├── gateway/
├── docs/
├── docker/
└── .vscode/
```

---

## Future Improvements

As the project grows, additional VS Code configurations may be added, including:

- Tasks
- Dev Containers
- Remote debugging
- Test explorer integration
