import json
from pathlib import Path
from typing import Any

FIXTURES_ROOT = Path(__file__).resolve().parents[2] / "fixtures"


def resolve_case_path(*parts: str) -> Path:
    path = FIXTURES_ROOT.joinpath(*parts)

    if not path.exists():
        raise FileNotFoundError(f"Fixture case does not exist: {path}")

    if not path.is_dir():
        raise NotADirectoryError(f"Fixture case is not a directory: {path}")

    return path


def read_utf8_source(case_path: Path, filename: str = "source.txt") -> str:
    source_path = case_path / filename

    if not source_path.is_file():
        raise FileNotFoundError(f"Fixture source does not exist: {source_path}")

    return source_path.read_text(encoding="utf-8")


def read_expected_json(
    case_path: Path,
    filename: str = "expected.json",
) -> Any:
    expected_path = case_path / filename

    if not expected_path.is_file():
        raise FileNotFoundError(
            f"Expected fixture JSON does not exist: {expected_path}"
        )

    with expected_path.open("r", encoding="utf-8") as handle:
        return json.load(handle)
