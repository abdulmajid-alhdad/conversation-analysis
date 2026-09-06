import importlib

from conversation_analysis.__main__ import main


def test_package_is_importable() -> None:
    package = importlib.import_module("conversation_analysis")

    assert package.__name__ == "conversation_analysis"


def test_runtime_entrypoint_returns_success() -> None:
    assert main() == 0
