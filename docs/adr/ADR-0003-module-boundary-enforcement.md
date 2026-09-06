# ADR-0003 — Module Boundary Enforcement

**Status:** ADOPTED

## Context

The adopted architecture requires Ports and Adapters, explicit dependency
direction, and an acyclic Core dependency graph.

## Decision

Module boundaries are enforced through:

- Python package boundaries.
- Explicit import rules.
- Automated architecture tests.

Rules:

- `core` MUST NOT depend on `application`, `delivery`, or `infrastructure`.
- `application` MAY depend on `core`.
- `delivery` MAY depend on application/core contracts when justified.
- `infrastructure` MAY depend on application ports/core contracts.
- Core code dependencies MUST remain acyclic.

Architecture tests MUST be non-vacuous:
an allowed dependency case must pass and a forbidden dependency case
must be detected.

## Rationale

Package naming alone does not enforce architecture. Executable conformance
tests provide objective enforcement.

## Alternatives Considered

- Documentation-only boundaries — rejected.
- Specialized import-linter tooling in M0 — deferred.

## Consequences

Dependency violations become test failures. More specialized enforcement
may be added later without changing the architectural contracts.

## Related Contracts

- 05-ARCHITECTURE v0.3
- M0-IMPLEMENTATION-READINESS v0.7

## Supersedes

None.

## Superseded By

None.