# ADR-0004 — Dependency and Build Management

**Status:** ADOPTED

## Context

The project requires explicit packaging metadata, reproducible dependency
declarations, and editable development installation without premature
dependency-locking policy.

## Decision

- Authoritative manifest: `pyproject.toml`.
- Primary dependency installer: pip.
- Build backend: `setuptools.build_meta`.
- Minimum setuptools requirement: `setuptools>=77.0.3`.
- Project distribution name: `arabic-conversation-analysis`.
- Import package name: `conversation_analysis`.
- Bootstrap package version: `0.0.0`.
- Python requirement: `>=3.13,<3.14`.
- Development installation: editable installation.
- Runtime dependencies are initially empty.
- pytest, Ruff, and mypy are development tooling.
- Dependency locking is deferred.
- Verify-and-Reuse First applies during environment setup.

Offline recovery from an existing local uv cache MAY be used as an
environment bootstrap mechanism when no network download occurs; this
does not replace `pyproject.toml` as the dependency manifest.

## Rationale

This is the minimum standards-based packaging model needed for M0 while
avoiding premature release and locking mechanisms.

## Alternatives Considered

- requirements.txt as the authoritative manifest — rejected.
- uv-specific project metadata as the authoritative manifest — not adopted.
- Dependency locking in M0 — deferred.

## Consequences

Packaging remains standards-based and provider-independent. Build and
development installation can evolve without changing project-domain contracts.

## Related Contracts

- M0-IMPLEMENTATION-READINESS v0.7

## Supersedes

None.

## Superseded By

None.