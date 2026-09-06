# ADR-0009 — Git and GitHub Version-Control Policy

**Status:** SUPERSEDED

## Context

M0 requires operational local and remote version control before milestone
closure.

## Decision

- Version control: Git.
- Primary branch: `main`.
- Remote host: GitHub.
- Initial repository visibility: PRIVATE.
- Remote name: `origin`.
- GitHub remote and initial push are required before M0 closure.
- `.gitignore` is mandatory.
- Secrets, tokens, passwords, raw personal conversations, local credentials,
  and project-environment contents MUST NOT enter the repository.
- `.github/` and GitHub Actions are deferred.
- The entire `.vscode/` directory is not ignored by default.

## Rationale

This provides a minimal safe version-control baseline while deferring CI
and collaboration-process decisions until required.

## Alternatives Considered

- Public repository from the start — not selected.
- GitHub Actions during M0 — deferred.
- Ignoring all VS Code configuration — rejected as a default.

## Consequences

M0 cannot close until the private GitHub repository, `origin`, and initial
push are verified.

## Related Contracts

- M0-IMPLEMENTATION-READINESS v0.7
- 10-IMPLEMENTATION-ROADMAP v0.4

## Supersedes

None.

## Superseded By

ADR-0010 - Repository Visibility Policy.