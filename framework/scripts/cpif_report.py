#!/usr/bin/env python3
"""Create a structured Markdown template for CPIF interpretation and decision support."""
from __future__ import annotations

from datetime import date
from pathlib import Path
import argparse

TEMPLATE = """# CPIF Interpretation Report

Generated: {date}

## 1. Communication Context

- Communication objective:
- Intended audience:
- Platform and accounts:
- Observation period:
- Publication frequency:
- Organic/paid distribution:
- Themes and formats:
- Comparability constraints:

## 2. Platform-recorded Metrics

### Exposure metrics

- Views:
- Reach:

### Interaction metrics

- Likes:
- Comments:
- Shares:
- Saves:
- Total interactions:

### Audience-growth metrics

- Follows:

### Derived metrics

- Rate definition(s):

## 3. Metric Preparation and Standardisation

- Analytical sample:
- Missing data:
- Duplicates:
- Category harmonisation:
- Outliers:
- Audit outcome:

## 4. Statistical Integration

### Descriptive findings


### Group comparisons


### Format comparisons


### Correlations


### Sensitivity analyses


## 5. Communication-performance Interpretation

For each principal finding, report the observed metric class, direction, magnitude, uncertainty, contextual meaning, and inferential limit.

| Finding | Metric class | Statistical evidence | Effect magnitude | Contextual interpretation | What cannot be concluded |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

## 6. Evidence-informed Decision Support

| Evidence | Decision | Rationale | Priority | Additional evidence required |
|---|---|---|---|---|
|  |  |  |  |  |

## Reporting Statement

CPIF was used as a methodological interpretation framework rather than as a predictive model or composite scoring system. Platform-recorded metrics were classified according to the communication processes they represent, and findings were interpreted within the inferential limits of observational social media data.
"""


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default=None, help="Output Markdown path.")
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    output = Path(args.output) if args.output else root / "outputs" / "cpif_interpretation_report.md"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(TEMPLATE.format(date=date.today().isoformat()), encoding="utf-8")
    print(f"CPIF report template created: {output}")


if __name__ == "__main__":
    main()
