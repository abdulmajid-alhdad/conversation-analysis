# ADR-0001 — Python Runtime and Environment Policy

**Status:** ADOPTED

## Context

The project requires CPython 3.13. The current workstation provides
CPython 3.13.15 managed by uv. Direct pip mutation of that base
installation is blocked because it is externally managed.

The project also requires dependency isolation without placing a
project-local `.venv` inside the repository.

## Decision

- Runtime contract: CPython >=3.13,<3.14.
- Current base runtime: uv-managed CPython 3.13.15.
- Base runtime discovery: `uv python find 3.13`.
- The base runtime MUST NOT receive project dependency mutations.
- `--break-system-packages` MUST NOT be used.
- A repository-external, project-specific virtual environment is required.
- Current workstation binding:
  `D:\python-envs\conversation-analysis`.
- Project-local `.venv`, `venv`, and `env` are not used.
- `--system-site-packages` MUST NOT be used.
- The project environment MUST NOT inherit shared site-packages.
- `uv venv` is the environment provisioner.
- uv MAY provide environment bootstrap/seed behavior.
- pip remains the primary project dependency installer.
- `pyproject.toml` remains the authoritative dependency manifest.
- The base interpreter and project interpreter are distinct.
- Project commands use the project interpreter explicitly.
- Environment activation is optional.
- uv cache and pip cache are not assumed interchangeable.
- Environment setup follows Verify-and-Reuse First.

## Rationale

This model isolates the project from other Python projects while reusing
the already available compliant CPython runtime and avoiding unnecessary
runtime installation.

## Alternatives Considered

- Mutating the shared uv-managed Python installation — rejected.
- Using `--break-system-packages` — rejected.
- Creating `.venv` inside the repository — rejected for the current workflow.
- Installing another CPython 3.13 runtime — unnecessary.

## Consequences

Project dependencies are isolated from other projects. Developer commands
must target the project interpreter explicitly. The external environment
path is workstation-specific and must not become a portable project contract.

## Related Contracts

- M0-IMPLEMENTATION-READINESS v0.7
- 05-ARCHITECTURE v0.3
- 10-IMPLEMENTATION-ROADMAP v0.4

## Supersedes

None.

## Superseded By

None.