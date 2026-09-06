import pytest

from tests.support.fixture_loader import (
    read_expected_json,
    read_utf8_source,
    resolve_case_path,
)


def test_reads_utf8_source() -> None:
    case_path = resolve_case_path("evaluation", "m0-loader-smoke")

    source = read_utf8_source(case_path)

    assert "مرحبا" in source
    assert "UTF-8" in source


def test_reads_expected_json() -> None:
    case_path = resolve_case_path("evaluation", "m0-loader-smoke")

    expected = read_expected_json(case_path)

    assert expected == {
        "case": "m0-loader-smoke",
        "status": "loaded",
    }


def test_missing_case_fails_explicitly() -> None:
    with pytest.raises(FileNotFoundError):
        resolve_case_path("evaluation", "missing-case")


def test_missing_source_fails_explicitly() -> None:
    case_path = resolve_case_path("evaluation", "m0-loader-smoke")

    with pytest.raises(FileNotFoundError):
        read_utf8_source(case_path, "missing-source.txt")


def test_missing_expected_json_fails_explicitly() -> None:
    case_path = resolve_case_path("evaluation", "m0-loader-smoke")

    with pytest.raises(FileNotFoundError):
        read_expected_json(case_path, "missing-expected.json")
