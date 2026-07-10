from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_FILE = PROJECT_ROOT / "data" / "public" / "instagram_posts_anonymized.csv"
OUTPUT_DIR = PROJECT_ROOT / "outputs" / "tables"

METRICS = [
    "views",
    "reach",
    "likes",
    "shares",
    "comments",
    "saves",
    "follows",
    "total_interactions",
]


def build_quality_table(data: pd.DataFrame) -> pd.DataFrame:
    """Summarize completeness and basic validity for every metric."""

    rows = []

    for metric in METRICS:
        values = data[metric]

        rows.append(
            {
                "metric": metric,
                "valid_n": int(values.notna().sum()),
                "missing_n": int(values.isna().sum()),
                "zero_n": int(values.eq(0).sum()),
                "zero_percent_valid": (
                    values.eq(0).sum() / values.notna().sum() * 100
                ),
                "negative_n": int(values.lt(0).sum()),
            }
        )

    return pd.DataFrame(rows)


def build_descriptive_table(data: pd.DataFrame) -> pd.DataFrame:
    """Calculate descriptive statistics without imputing missing values."""

    rows = []

    for project, group in data.groupby("project", sort=True):
        for metric in METRICS:
            values = group[metric].dropna()

            rows.append(
                {
                    "project": project,
                    "metric": metric,
                    "valid_n": len(values),
                    "mean": values.mean(),
                    "standard_deviation": values.std(),
                    "minimum": values.min(),
                    "q1": values.quantile(0.25),
                    "median": values.median(),
                    "q3": values.quantile(0.75),
                    "maximum": values.max(),
                }
            )

    return pd.DataFrame(rows)


def main() -> None:
    data = pd.read_csv(INPUT_FILE)

    quality = build_quality_table(data)
    descriptive = build_descriptive_table(data)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    quality_file = OUTPUT_DIR / "data_quality_metrics.csv"
    descriptive_file = OUTPUT_DIR / "descriptive_statistics_by_project.csv"

    quality.to_csv(quality_file, index=False, encoding="utf-8")
    descriptive.to_csv(
        descriptive_file,
        index=False,
        encoding="utf-8",
    )

    print("DATA QUALITY BY METRIC")
    print(
        quality.to_string(
            index=False,
            formatters={
                "zero_percent_valid": "{:.1f}".format,
            },
        )
    )

    missing_rows = data[
        data[METRICS].isna().any(axis=1)
    ][
        [
            "project",
            "record_id",
            "publication_month",
            "post_type",
            *METRICS,
        ]
    ]

    print("\nROWS WITH MISSING ANALYTICAL VALUES")
    if missing_rows.empty:
        print("None")
    else:
        print(missing_rows.to_string(index=False))

    print("\nDESCRIPTIVE STATISTICS BY PROJECT")
    print(
        descriptive[
            [
                "project",
                "metric",
                "valid_n",
                "minimum",
                "q1",
                "median",
                "q3",
                "maximum",
            ]
        ].to_string(index=False)
    )

    print("\nSaved files:")
    print(quality_file)
    print(descriptive_file)


if __name__ == "__main__":
    main()
