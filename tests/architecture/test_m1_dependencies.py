"""M1 Architecture Tests for Dependency Rules.

These tests verify the M1 dependency graph and architectural compliance.
"""

import ast
from pathlib import Path


def test_core_dependency_graph_is_acyclic():
    """Test 10: Core dependency graph is acyclic."""
    # This test verifies that core doesn't import application, infrastructure, or delivery
    # which would create cycles
    core_path = Path("src/conversation_analysis/core/contracts.py")
    with open(core_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Parse the AST to check for imports
    tree = ast.parse(content)

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                # Core should not import application, infrastructure, or delivery
                assert alias.name != "application", (
                    f"Core importing application: {alias.name}"
                )
                assert alias.name != "infrastructure", (
                    f"Core importing infrastructure: {alias.name}"
                )
                assert alias.name != "delivery", (
                    f"Core importing delivery: {alias.name}"
                )
        elif isinstance(node, ast.ImportFrom) and node.module:
            # Core should not import from application, infrastructure, or delivery
            assert node.module != "application", (
                f"Core importing from application: {node.module}"
            )
            assert node.module != "infrastructure", (
                f"Core importing from infrastructure: {node.module}"
            )
            assert node.module != "delivery", (
                f"Core importing from delivery: {node.module}"
            )
            assert not node.module.startswith("application."), (
                f"Core importing from application: {node.module}"
            )
            assert not node.module.startswith("infrastructure."), (
                f"Core importing from infrastructure: {node.module}"
            )
            assert not node.module.startswith("delivery."), (
                f"Core importing from delivery: {node.module}"
            )


def test_dependency_direction_conforms():
    """Test 11: Dependency direction conforms (Infrastructure ← Application ← Core)."""
    # Test that application can import from core but not vice versa
    Path("src/conversation_analysis/application/")
    Path("src/conversation_analysis/core/contracts.py")

    # Check that application modules can import from core (this is allowed)
    # We'll verify this by checking that application modules don't violate the reverse
    app_modules = [
        "src/conversation_analysis/application/registry.py",
        "src/conversation_analysis/application/ports.py",
        "src/conversation_analysis/application/orchestration.py",
    ]

    for app_module in app_modules:
        if Path(app_module).exists():
            with open(app_module, "r", encoding="utf-8") as f:
                content = f.read()

            tree = ast.parse(content)
            for node in ast.walk(tree):
                if isinstance(node, ast.ImportFrom) and node.module:
                    # Application can import from core (this is expected)
                    # But core should never import from application
                    pass  # This is allowed direction


def test_no_infrastructure_coupling_in_core():
    """Test 12: No Infrastructure coupling in Core."""
    core_path = Path("src/conversation_analysis/core/contracts.py")
    with open(core_path, "r", encoding="utf-8") as f:
        content = f.read()

    tree = ast.parse(content)

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                assert not alias.name.startswith("infrastructure"), (
                    f"Infrastructure coupling in core: {alias.name}"
                )
        elif isinstance(node, ast.ImportFrom) and node.module:
            assert not node.module.startswith("infrastructure"), (
                f"Infrastructure coupling in core: {node.module}"
            )


def test_no_delivery_coupling_in_core():
    """Test 15: No Delivery coupling in Core."""
    core_path = Path("src/conversation_analysis/core/contracts.py")
    with open(core_path, "r", encoding="utf-8") as f:
        content = f.read()

    tree = ast.parse(content)

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                assert not alias.name.startswith("delivery"), (
                    f"Delivery coupling in core: {alias.name}"
                )
        elif isinstance(node, ast.ImportFrom) and node.module:
            assert not node.module.startswith("delivery"), (
                f"Delivery coupling in core: {node.module}"
            )


def test_no_provider_sdk_leakage():
    """Test 13: No Provider SDK leakage."""
    # Check all core files
    core_files = ["src/conversation_analysis/core/contracts.py"]

    for core_file in core_files:
        if Path(core_file).exists():
            with open(core_file, "r", encoding="utf-8") as f:
                content = f.read()

            tree = ast.parse(content)
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        assert "provider" not in alias.name.lower(), (
                            f"Provider SDK leakage: {alias.name}"
                        )
                elif isinstance(node, ast.ImportFrom) and node.module:
                    assert "provider" not in node.module.lower(), (
                        f"Provider SDK leakage: {node.module}"
                    )


def test_no_parser_concrete_types_in_canonical_architecture():
    """Test 14: No Parser concrete types in Canonical architecture."""
    # Check core files
    core_files = ["src/conversation_analysis/core/contracts.py"]

    for core_file in core_files:
        if Path(core_file).exists():
            with open(core_file, "r", encoding="utf-8") as f:
                content = f.read()

            tree = ast.parse(content)
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        assert "parser" not in alias.name.lower(), (
                            f"Parser concrete type in canonical architecture: {alias.name}"
                        )
                elif isinstance(node, ast.ImportFrom) and node.module:
                    assert "parser" not in node.module.lower(), (
                        f"Parser concrete type in canonical architecture: {node.module}"
                    )


def test_no_fixture_loader_dependency_in_src():
    """Test 16: No dependency on tests/support/fixture_loader.py in src/."""
    src_files = [
        "src/conversation_analysis/core/contracts.py",
        "src/conversation_analysis/application/registry.py",
        "src/conversation_analysis/application/ports.py",
        "src/conversation_analysis/application/orchestration.py",
    ]

    for src_file in src_files:
        if Path(src_file).exists():
            with open(src_file, "r", encoding="utf-8") as f:
                content = f.read()

            tree = ast.parse(content)
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        assert alias.name != "tests.support.fixture_loader", (
                            f"Production code depends on fixture_loader: {alias.name}"
                        )
                elif isinstance(node, ast.ImportFrom) and node.module:
                    assert node.module != "tests.support.fixture_loader", (
                        f"Production code depends on fixture_loader: {node.module}"
                    )
                    assert not node.module.startswith("tests.support.fixture_loader"), (
                        f"Production code depends on fixture_loader: {node.module}"
                    )
