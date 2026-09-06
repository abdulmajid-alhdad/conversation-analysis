# ADR-0002 — Repository Structure

**Status:** ADOPTED

## Context

The project requires explicit ownership boundaries without prematurely
creating technology-specific modules.

## Decision

Use a `src`-based repository:

- `src/conversation_analysis/core`
- `src/conversation_analysis/application`
- `src/conversation_analysis/delivery`
- `src/conversation_analysis/infrastructure`
- `tests/unit`
- `tests/architecture`
- `tests/conformance`
- `tests/integration`
- `tests/e2e`
- `tests/support`
- `fixtures/sources`
- `fixtures/canonical`
- `fixtures/analysis`
- `fixtures/evaluation`
- `docs/adr`

Generic packages such as `shared`, `common`, `utils`, or `helpers`
MUST NOT be introduced without clear ownership.

## Rationale

The structure establishes architectural ownership without introducing
premature application capabilities or infrastructure technologies.

## Alternatives Considered

- Flat package layout — rejected.
- Technology-oriented folders from the beginning — rejected.
- Generic shared utility packages — rejected as a default.

## Consequences

Future modules must be placed according to ownership and dependency rules.
The structure may expand when capabilities require it.

## Related Contracts

- M0-IMPLEMENTATION-READINESS v0.7
- 05-ARCHITECTURE v0.3

## Supersedes

None.

## Superseded By

None.