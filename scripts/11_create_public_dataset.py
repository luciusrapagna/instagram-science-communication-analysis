from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data" / "processed" / "instagram_posts.csv"
OUTPUT_DIR = ROOT / "data" / "public"
OUTPUT = OUTPUT_DIR / "instagram_posts_anonymized.csv"

PUBLIC_COLUMNS = [
    "record_id",
    "project",
    "publication_month",
    "post_type",
    "duration_seconds",
    "views",
    "reach",
    "likes",
    "shares",
    "comments",
    "saves",
    "follows",
    "total_interactions",
]


def main() -> None:
    data = pd.read_csv(INPUT)

    data = data.sort_values(
        ["project", "publication_datetime", "post_id"]
    ).reset_index(drop=True)

    data.insert(
        0,
        "record_id",
        [f"POST_{number:03d}" for number in range(1, len(data) + 1)],
    )

    public_data = data[PUBLIC_COLUMNS].copy()

    if len(public_data) != 187:
        raise ValueError(
            f"Expected 187 public records, found {len(public_data)}"
        )

    if public_data["record_id"].duplicated().any():
        raise ValueError("Duplicated anonymous record IDs")

    forbidden_columns = {
        "post_id",
        "account_id",
        "account_username",
        "account_name",
        "description",
        "permalink",
        "publication_datetime",
        "publication_date",
    }

    exposed = forbidden_columns.intersection(public_data.columns)

    if exposed:
        raise ValueError(
            f"Identifying columns found in public data: {sorted(exposed)}"
        )

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    public_data.to_csv(
        OUTPUT,
        index=False,
        encoding="utf-8",
    )

    print(f"Public dataset: {OUTPUT}")
    print(f"Rows: {len(public_data)}")
    print(f"Columns: {len(public_data.columns)}")
    print("\nPublic columns:")
    print("\n".join(public_data.columns))

    print("\nMissing values:")
    print(public_data.isna().sum().to_string())


if __name__ == "__main__":
    main()
