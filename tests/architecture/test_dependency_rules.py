from tests.support.architecture_rules import dependency_violations


def test_allowed_dependency_graph_passes() -> None:
    edges = (
        ("application", "core"),
        ("delivery", "application"),
        ("delivery", "core"),
        ("infrastructure", "application"),
        ("infrastructure", "core"),
    )

    assert dependency_violations(edges) == ()


def test_forbidden_core_dependency_is_detected() -> None:
    edges = (
        ("core", "application"),
        ("core", "infrastructure"),
    )

    assert dependency_violations(edges) == (
        ("core", "application"),
        ("core", "infrastructure"),
    )


def test_forbidden_application_dependency_is_detected() -> None:
    edges = (
        ("application", "delivery"),
        ("application", "infrastructure"),
    )

    assert dependency_violations(edges) == (
        ("application", "delivery"),
        ("application", "infrastructure"),
    )


def test_unknown_layer_fails_explicitly() -> None:
    try:
        dependency_violations((("core", "unknown"),))
    except ValueError as error:
        assert str(error) == "Unknown target layer: unknown"
    else:
        raise AssertionError("Unknown architecture layer was not rejected")
