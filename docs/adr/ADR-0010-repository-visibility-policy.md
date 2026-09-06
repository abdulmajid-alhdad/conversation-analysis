# ADR-0010 — Repository Visibility Policy

**Status:** ADOPTED

## Context

ADR-0009 required the GitHub repository to be PRIVATE.
The Project Owner has explicitly accepted PUBLIC repository visibility.

## Decision

- Repository visibility MAY be PUBLIC or PRIVATE.
- Visibility is selected explicitly by the Project Owner.
- Current visibility is PUBLIC.
- GitHub remote `origin` and initial push remain required.
- Security and data-protection rules apply regardless of visibility.

Secrets, tokens, passwords, raw personal conversations, local credentials,
local secret configuration, and Project Environment contents MUST NOT enter Git.

## Consequences

M0 may close with PUBLIC or PRIVATE visibility when explicitly selected
by the Project Owner and repository-protection rules remain satisfied.

## Related Contracts

- M0-IMPLEMENTATION-READINESS v0.8
- 10-IMPLEMENTATION-ROADMAP v0.4

## Supersedes

ADR-0009 — Git and GitHub Version-Control Policy.

## Superseded By

None.
