from collections.abc import Iterable

LAYERS = frozenset(
    {
        "core",
        "application",
        "delivery",
        "infrastructure",
    }
)

_ALLOWED_INTERNAL_DEPENDENCIES = {
    "core": frozenset(),
    "application": frozenset({"core"}),
    "delivery": frozenset({"core", "application"}),
    "infrastructure": frozenset({"core", "application"}),
}


def dependency_violations(
    edges: Iterable[tuple[str, str]],
) -> tuple[tuple[str, str], ...]:
    violations: list[tuple[str, str]] = []

    for source, target in edges:
        if source not in LAYERS:
            raise ValueError(f"Unknown source layer: {source}")

        if target not in LAYERS:
            raise ValueError(f"Unknown target layer: {target}")

        if source == target:
            continue

        if target not in _ALLOWED_INTERNAL_DEPENDENCIES[source]:
            violations.append((source, target))

    return tuple(sorted(violations))
