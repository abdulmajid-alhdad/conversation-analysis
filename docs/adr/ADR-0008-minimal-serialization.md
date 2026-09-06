# ADR-0008 — Minimal Serialization

**Status:** ADOPTED

## Context

M0 needs a minimal serialization baseline for fixtures and early structured
artifacts without selecting production persistence technology prematurely.

## Decision

- JSON is the baseline external structured representation.
- Text encoding is UTF-8.
- Internal project representations use typed Python objects where appropriate.
- Serialization boundaries must remain explicit.

Not adopted in M0:

- Pickle as an official format.
- YAML requirement.
- JSON Schema.
- Pydantic.
- NDJSON/JSONL.
- Production persistence format.

## Rationale

JSON and UTF-8 are sufficient for fixtures and initial interoperable
structured data while keeping later schema technology decisions open.

## Alternatives Considered

- Pickle — rejected as an official interchange format.
- YAML — unnecessary in M0.
- Pydantic/JSON Schema — deferred until a validation boundary requires them.

## Consequences

Early fixtures remain simple and portable. Stronger schemas can be
introduced later without changing the M0 baseline.

## Related Contracts

- M0-IMPLEMENTATION-READINESS v0.7

## Supersedes

None.

## Superseded By

None.