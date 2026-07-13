#!/usr/bin/env python3
"""Validate the structure and minimum content of the CPIF framework."""

from datetime import datetime, timezone
from pathlib import Path
import re
import sys


FRAMEWORK_DIR = Path(__file__).resolve().parents[1]
OUTPUT_DIR = FRAMEWORK_DIR / "outputs"
REPORT_PATH = OUTPUT_DIR / "cpif_validation_report.txt"

REQUIRED_FILES = [
    "README.md",
    "LICENSES.md",
    "docs/CPIF_conceptual_framework.md",
    "docs/CPIF_principles.md",
    "docs/CPIF_layers.md",
    "docs/CPIF_interpretation_rules.md",
    "docs/CPIF_reporting_checklist.md",
    "docs/CPIF_figure_caption.md",
    "docs/CPIF_version_history.md",
    "scripts/generate_cpif_figure.py",
    "scripts/validate_cpif_structure.py",
    "figures/source/generate_cpif_figure.py",
    "figures/publication/cpif_conceptual_framework.svg",
    "figures/publication/cpif_conceptual_framework.pdf",
    "figures/publication/cpif_conceptual_framework.png",
]

CORE_DOCUMENTS = [
    "README.md",
    "docs/CPIF_conceptual_framework.md",
    "docs/CPIF_principles.md",
    "docs/CPIF_layers.md",
    "docs/CPIF_interpretation_rules.md",
]


def read_text(relative_path: str) -> str:
    """Read a UTF-8 framework file, returning an empty string if unavailable."""
    path = FRAMEWORK_DIR / relative_path

    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return ""


def add_check(
    checks: list[tuple[bool, str]],
    condition: bool,
    message: str,
) -> None:
    """Append one validation result."""
    checks.append((bool(condition), message))


def validate_required_files(checks: list[tuple[bool, str]]) -> None:
    """Check whether all mandatory files exist."""
    for relative_path in REQUIRED_FILES:
        path = FRAMEWORK_DIR / relative_path
        add_check(
            checks,
            path.is_file(),
            f"Required file exists: {relative_path}",
        )


def validate_non_empty_files(checks: list[tuple[bool, str]]) -> None:
    """Check that no framework file is empty."""
    empty_files = [
        path.relative_to(FRAMEWORK_DIR).as_posix()
        for path in FRAMEWORK_DIR.rglob("*")
        if path.is_file()
        and path != REPORT_PATH
        and path.stat().st_size == 0
    ]

    add_check(
        checks,
        not empty_files,
        (
            "No empty files detected"
            if not empty_files
            else f"Empty files detected: {', '.join(empty_files)}"
        ),
    )


def validate_principles(checks: list[tuple[bool, str]]) -> None:
    """Check for the five numbered CPIF principles."""
    content = read_text("docs/CPIF_principles.md")

    headings = re.findall(
        r"^## Principle\s+([1-5])\b",
        content,
        flags=re.MULTILINE,
    )

    add_check(
        checks,
        sorted(set(headings)) == ["1", "2", "3", "4", "5"],
        f"Five CPIF principles present: found {len(set(headings))}",
    )


def validate_layers(checks: list[tuple[bool, str]]) -> None:
    """Check for the six numbered CPIF layers."""
    content = read_text("docs/CPIF_layers.md")

    headings = re.findall(
        r"^## Layer\s+([1-6])\b",
        content,
        flags=re.MULTILINE,
    )

    add_check(
        checks,
        sorted(set(headings)) == ["1", "2", "3", "4", "5", "6"],
        f"Six CPIF layers present: found {len(set(headings))}",
    )


def validate_concepts(checks: list[tuple[bool, str]]) -> None:
    """Check for the three required communication concepts."""
    combined_text = "\n".join(
        path.read_text(encoding="utf-8", errors="replace")
        for path in FRAMEWORK_DIR.rglob("*.md")
    ).lower()

    concepts = [
        "communication exposure",
        "communication interaction",
        "communication effectiveness",
    ]

    for concept in concepts:
        add_check(
            checks,
            concept in combined_text,
            f"Required concept present: {concept}",
        )


def validate_cpif_name(checks: list[tuple[bool, str]]) -> None:
    """Check consistent use of the CPIF name in core documentation."""
    full_name = "Communication Performance Interpretation Framework"

    for relative_path in CORE_DOCUMENTS:
        content = read_text(relative_path)

        add_check(
            checks,
            "CPIF" in content and full_name in content,
            f"CPIF name is consistent in: {relative_path}",
        )


def validate_licenses(checks: list[tuple[bool, str]]) -> None:
    """Check for the provisional code and content licenses."""
    content = read_text("LICENSES.md")

    add_check(
        checks,
        "MIT License" in content,
        "Provisional MIT License designation is present",
    )
    add_check(
        checks,
        "CC BY 4.0" in content,
        "Provisional CC BY 4.0 designation is present",
    )


def write_report(checks: list[tuple[bool, str]]) -> bool:
    """Write the validation report and return the overall result."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    passed = sum(condition for condition, _ in checks)
    failed = len(checks) - passed
    overall_success = failed == 0

    lines = [
        "CPIF STRUCTURE VALIDATION REPORT",
        "=" * 40,
        f"Generated: {datetime.now(timezone.utc).isoformat()}",
        f"Framework directory: {FRAMEWORK_DIR}",
        f"Overall status: {'PASS' if overall_success else 'FAIL'}",
        f"Checks passed: {passed}",
        f"Checks failed: {failed}",
        "",
        "DETAILED RESULTS",
        "-" * 40,
    ]

    for condition, message in checks:
        label = "PASS" if condition else "FAIL"
        lines.append(f"[{label}] {message}")

    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"Validation report created: {REPORT_PATH}")
    print(f"Overall status: {'PASS' if overall_success else 'FAIL'}")
    print(f"Checks passed: {passed}")
    print(f"Checks failed: {failed}")

    return overall_success


def main() -> int:
    """Run all CPIF validation checks."""
    checks: list[tuple[bool, str]] = []

    validate_required_files(checks)
    validate_non_empty_files(checks)
    validate_principles(checks)
    validate_layers(checks)
    validate_concepts(checks)
    validate_cpif_name(checks)
    validate_licenses(checks)

    return 0 if write_report(checks) else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"CPIF validation failed unexpectedly: {exc}", file=sys.stderr)
        raise SystemExit(2) from exc