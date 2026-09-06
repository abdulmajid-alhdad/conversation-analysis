# ADR-0007 — Code Quality Tooling

**Status:** ADOPTED

## Context

M0 requires a local quality gate before business implementation begins.

## Decision

Use:

- Ruff as formatter.
- Ruff as linter.
- mypy with strict checking for production source code.
- pytest as the test runner.

The local quality gate is:

- `ruff format --check src tests`
- `ruff check src tests`
- `mypy src/conversation_analysis`
- `pytest`

Global type-checking suppressions are not adopted.

## Rationale

A small, explicit toolchain provides formatting, linting, type checking,
and testing without overlapping tools.

## Alternatives Considered

- Separate formatter and linter packages — unnecessary.
- Global mypy suppressions — rejected.
- pre-commit in M0 — deferred.

## Consequences

Code must satisfy the same local checks before M0 closure and later
implementation milestones.

## Related Contracts

- M0-IMPLEMENTATION-READINESS v0.7

## Supersedes

None.

## Superseded By

None.