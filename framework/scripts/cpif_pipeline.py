#!/usr/bin/env python3
"""Run the repository analysis scripts as the CPIF Layers 3–4 pipeline."""
from __future__ import annotations

import argparse
from pathlib import Path
import subprocess
import sys

PIPELINE = [
    (3, "Metric Preparation and Standardisation", "03_audit_analytical_variables.py"),
    (4, "Statistical Integration", "04_compare_projects.py"),
    (4, "Statistical Integration", "05_compare_post_formats.py"),
    (4, "Statistical Integration", "06_stratified_format_analysis.py"),
    (4, "Statistical Integration", "07_analyze_reach_normalized_rates.py"),
    (4, "Statistical Integration", "08_spearman_correlations.py"),
    (4, "Statistical Integration", "09_outlier_sensitivity_analysis.py"),
    (4, "Visual Integration", "10_generate_figures.py"),
]


def locate_repository_root() -> Path:
    framework_dir = Path(__file__).resolve().parents[1]
    return framework_dir.parent


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="Show the execution plan without running scripts.")
    parser.add_argument("--continue-on-error", action="store_true", help="Continue after a failed script.")
    args = parser.parse_args()

    repo_root = locate_repository_root()
    scripts_dir = repo_root / "scripts"
    failures: list[str] = []

    print("CPIF v2.0 analytical pipeline")
    print(f"Repository root: {repo_root}")

    for layer, label, filename in PIPELINE:
        path = scripts_dir / filename
        print(f"\nLayer {layer} — {label}: {filename}")
        if not path.is_file():
            message = f"Missing script: {path}"
            print(f"ERROR: {message}")
            failures.append(message)
            if not args.continue_on_error:
                return 1
            continue
        if args.dry_run:
            print(f"Would run: {sys.executable} {path}")
            continue
        result = subprocess.run([sys.executable, str(path)], cwd=repo_root, check=False)
        if result.returncode != 0:
            message = f"{filename} exited with status {result.returncode}"
            print(f"ERROR: {message}")
            failures.append(message)
            if not args.continue_on_error:
                return result.returncode

    if failures:
        print("\nPipeline completed with failures:")
        for failure in failures:
            print(f" - {failure}")
        return 1

    print("\nCPIF analytical pipeline completed successfully.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
