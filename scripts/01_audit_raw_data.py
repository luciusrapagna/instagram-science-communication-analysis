from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"

FILES = {
    "Ocean Culture": RAW_DATA_DIR / "cultura_oceanica.csv",
    "PsicoCampus": RAW_DATA_DIR / "psicocampus.csv",
}


def audit_dataset(project_name: str, file_path: Path) -> pd.DataFrame:
    """Load and audit one raw Instagram dataset without modifying it."""

    data = pd.read_csv(file_path, encoding="utf-8-sig")

    print("\n" + "=" * 70)
    print(f"PROJECT: {project_name}")
    print(f"FILE: {file_path.name}")
    print("=" * 70)

    print(f"Rows: {len(data)}")
    print(f"Columns: {len(data.columns)}")

    print("\nColumn names:")
    for position, column in enumerate(data.columns, start=1):
        print(f"{position:02d}. {column}")

    duplicate_posts = data["Identificação do post"].duplicated(keep=False)
    print(f"\nRows with duplicated post ID: {duplicate_posts.sum()}")
    print(
        "Unique post IDs: "
        f"{data['Identificação do post'].nunique(dropna=True)}"
    )

    print("\nMissing values by column:")
    missing = data.isna().sum().sort_values(ascending=False)
    print(missing.to_string())

    if "Horário de publicação" in data.columns:
        parsed_datetimes = pd.to_datetime(
            data["Horário de publicação"],
            format="%m/%d/%Y %H:%M",
            errors="coerce",
        )

        print("\nPublication datetime audit:")
        print(f"Earliest valid datetime: {parsed_datetimes.min()}")
        print(f"Latest valid datetime: {parsed_datetimes.max()}")
        print(
            "Invalid or missing publication datetimes: "
            f"{parsed_datetimes.isna().sum()}"
        )

        print("\nPosts by publication month:")
        print(
            parsed_datetimes
            .dt.to_period("M")
            .value_counts()
            .sort_index()
            .to_string()
        )

    if "Tipo de post" in data.columns:
        print("\nPost types:")
        print(
            data["Tipo de post"]
            .fillna("[missing]")
            .value_counts(dropna=False)
            .to_string()
        )

    return data


def main() -> None:
    datasets = {}

    for project_name, file_path in FILES.items():
        datasets[project_name] = audit_dataset(
            project_name,
            file_path,
        )

    total_rows = sum(len(data) for data in datasets.values())

    print("\n" + "=" * 70)
    print("COMBINED RAW DATA")
    print("=" * 70)
    print(f"Total rows across both files: {total_rows}")


if __name__ == "__main__":
    main()
