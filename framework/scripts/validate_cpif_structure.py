#!/usr/bin/env python3
"""Validate the required CPIF v2.0 repository structure."""
from __future__ import annotations

from pathlib import Path
import sys

REQUIRED = [
    "README.md",
    "docs/CPIF_conceptual_framework.md",
    "docs/CPIF_layers.md",
    "docs/CPIF_principles.md",
    "docs/CPIF_interpretation_rules.md",
    "docs/CPIF_reporting_checklist.md",
    "docs/CPIF_figure_caption.md",
    "docs/CHANGELOG.md",
    "scripts/generate_cpif_figure.py",
    "scripts/validate_cpif_structure.py",
    "scripts/cpif_pipeline.py",
    "scripts/cpif_report.py",
    "templates/communication_context.yml",
    "templates/metric_dictionary.csv",
    "templates/decision_support.csv",
    "examples/cpif_mapping.md",
]


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    missing = [path for path in REQUIRED if not (root / path).is_file()]
    if missing:
        print("CPIF structure validation failed. Missing files:")
        for path in missing:
            print(f" - {path}")
        return 1
    print(f"CPIF structure valid: {len(REQUIRED)} required files found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
