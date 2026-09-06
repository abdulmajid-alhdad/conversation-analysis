# ADR-0005 — Test Framework

**Status:** ADOPTED

## Context

M0 requires a working test entry point and a foundation for unit,
architecture, conformance, integration, and end-to-end tests.

## Decision

Use pytest as the project test framework.

Test categories:

- unit
- architecture
- conformance
- integration
- e2e
- support infrastructure

`tests/support` contains test infrastructure only.

`unittest.mock` is the baseline mocking facility.

Code coverage thresholds are deferred.

## Rationale

pytest is sufficient for the required M0 test structure without adding
an additional testing framework.

## Alternatives Considered

- unittest as the primary test runner — not selected.
- Additional mocking frameworks — not required.
- Coverage gate during M0 — deferred.

## Consequences

All project test categories share one test runner and can be expanded
incrementally as capabilities are implemented.

## Related Contracts

- 09-EVALUATION-STRATEGY v0.3
- M0-IMPLEMENTATION-READINESS v0.7

## Supersedes

None.

## Superseded By

None.