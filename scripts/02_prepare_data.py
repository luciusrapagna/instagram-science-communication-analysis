from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = PROJECT_ROOT / "data" / "raw"
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"
OUTPUT_FILE = PROCESSED_DIR / "instagram_posts.csv"

SOURCE_FILES = {
    "Ocean Culture": RAW_DIR / "cultura_oceanica.csv",
    "PsicoCampus": RAW_DIR / "psicocampus.csv",
}

COLUMN_MAP = {
    "Identificação do post": "post_id",
    "Identificação da conta": "account_id",
    "Nome de usuário da conta": "account_username",
    "Nome da conta": "account_name",
    "Descrição": "description",
    "Duração (s)": "duration_seconds",
    "Horário de publicação": "publication_datetime",
    "Link permanente": "permalink",
    "Tipo de post": "post_type",
    "Comentário de dados": "data_comment",
    "Data": "aggregation_label",
    "Visualizações": "views",
    "Alcance": "reach",
    "Curtidas": "likes",
    "Compartilhamentos": "shares",
    "Seguimentos": "follows",
    "Comentários": "comments",
    "Salvamentos": "saves",
}

POST_TYPE_MAP = {
    "Imagem do Instagram": "Image",
    "Carrossel do Instagram": "Carousel",
    "Reel do Instagram": "Reel",
}

NUMERIC_COLUMNS = [
    "duration_seconds",
    "views",
    "reach",
    "likes",
    "shares",
    "follows",
    "comments",
    "saves",
]


def load_and_standardize(project: str, file_path: Path) -> pd.DataFrame:
    """Read one raw file and standardize its variables."""

    data = pd.read_csv(file_path, encoding="utf-8-sig")
    data = data.rename(columns=COLUMN_MAP)
    data.insert(0, "project", project)

    data["publication_datetime"] = pd.to_datetime(
        data["publication_datetime"],
        format="%m/%d/%Y %H:%M",
        errors="raise",
    )

    data["post_type"] = data["post_type"].map(POST_TYPE_MAP)

    if data["post_type"].isna().any():
        raise ValueError(f"Unknown post type found in {file_path.name}")

    for column in NUMERIC_COLUMNS:
        data[column] = pd.to_numeric(data[column], errors="coerce")

    # Total content interactions used in this project:
    # likes + shares + comments + saves.
    # Follows are retained as a separate outcome.
    data["total_interactions"] = data[
        ["likes", "shares", "comments", "saves"]
    ].sum(axis=1, min_count=1)

    data["publication_date"] = data["publication_datetime"].dt.date
    data["publication_month"] = (
        data["publication_datetime"].dt.to_period("M").astype(str)
    )
    data["publication_weekday"] = data[
        "publication_datetime"
    ].dt.day_name()

    return data


def validate(processed: pd.DataFrame) -> None:
    """Stop execution if a core data-integrity rule is violated."""

    if len(processed) != 187:
        raise ValueError(f"Expected 187 rows, found {len(processed)}")

    if processed["post_id"].duplicated().any():
        raise ValueError("Duplicated post IDs found after combination")

    if processed["publication_datetime"].isna().any():
        raise ValueError("Missing publication datetime found")

    if not processed["project"].value_counts().to_dict() == {
        "PsicoCampus": 94,
        "Ocean Culture": 93,
    }:
        raise ValueError("Unexpected project sample sizes")


def main() -> None:
    frames = [
        load_and_standardize(project, file_path)
        for project, file_path in SOURCE_FILES.items()
    ]

    processed = pd.concat(frames, ignore_index=True)
    processed = processed.sort_values(
        ["publication_datetime", "project", "post_id"]
    ).reset_index(drop=True)

    validate(processed)

    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    processed.to_csv(
        OUTPUT_FILE,
        index=False,
        encoding="utf-8",
        date_format="%Y-%m-%d %H:%M:%S",
    )

    print(f"Processed file: {OUTPUT_FILE}")
    print(f"Rows: {len(processed)}")
    print(f"Columns: {len(processed.columns)}")

    print("\nRows by project:")
    print(processed["project"].value_counts().to_string())

    print("\nRows by project and post type:")
    print(
        pd.crosstab(
            processed["project"],
            processed["post_type"],
        ).to_string()
    )

    print("\nMissing analytical values:")
    print(processed[NUMERIC_COLUMNS].isna().sum().to_string())


if __name__ == "__main__":
    main()
