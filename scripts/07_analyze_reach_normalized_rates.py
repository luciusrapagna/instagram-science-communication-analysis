from pathlib import Path

import pandas as pd
from scipy.stats import mannwhitneyu
from statsmodels.stats.multitest import multipletests


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data" / "public" / "instagram_posts_anonymized.csv"
OUTPUT_DIR = ROOT / "outputs" / "tables"

RATE_COLUMNS = [
    "interactions_per_100_reached",
    "likes_per_100_reached",
]

PROJECTS = ["Ocean Culture", "PsicoCampus"]


def rank_biserial(u_value: float, n1: int, n2: int) -> float:
    return (2 * u_value) / (n1 * n2) - 1


def add_rates(data: pd.DataFrame) -> pd.DataFrame:
    data = data.copy()

    valid_reach = data["reach"].gt(0)

    data.loc[
        valid_reach,
        "interactions_per_100_reached",
    ] = (
        data.loc[valid_reach, "total_interactions"]
        / data.loc[valid_reach, "reach"]
        * 100
    )

    data.loc[
        valid_reach,
        "likes_per_100_reached",
    ] = (
        data.loc[valid_reach, "likes"]
        / data.loc[valid_reach, "reach"]
        * 100
    )

    return data


def descriptive_results(data: pd.DataFrame) -> pd.DataFrame:
    rows = []

    for project, project_data in data.groupby("project"):
        for post_type, format_data in project_data.groupby("post_type"):
            for metric in RATE_COLUMNS:
                values = format_data[metric].dropna()

                rows.append(
                    {
                        "project": project,
                        "post_type": post_type,
                        "metric": metric,
                        "valid_n": len(values),
                        "q1": values.quantile(0.25),
                        "median": values.median(),
                        "q3": values.quantile(0.75),
                        "minimum": values.min(),
                        "maximum": values.max(),
                    }
                )

    return pd.DataFrame(rows)


def project_comparisons(data: pd.DataFrame) -> pd.DataFrame:
    rows = []

    for metric in RATE_COLUMNS:
        first = data.loc[
            data["project"].eq(PROJECTS[0]),
            metric,
        ].dropna()

        second = data.loc[
            data["project"].eq(PROJECTS[1]),
            metric,
        ].dropna()

        test = mannwhitneyu(
            first,
            second,
            alternative="two-sided",
            method="asymptotic",
        )

        rows.append(
            {
                "metric": metric,
                "group_1": PROJECTS[0],
                "group_1_n": len(first),
                "group_1_median": first.median(),
                "group_2": PROJECTS[1],
                "group_2_n": len(second),
                "group_2_median": second.median(),
                "mann_whitney_u": test.statistic,
                "p_value": test.pvalue,
                "rank_biserial": rank_biserial(
                    test.statistic,
                    len(first),
                    len(second),
                ),
            }
        )

    results = pd.DataFrame(rows)

    rejected, adjusted, _, _ = multipletests(
        results["p_value"],
        alpha=0.05,
        method="holm",
    )

    results["holm_p_value"] = adjusted
    results["holm_reject_0_05"] = rejected

    return results


def within_project_format_comparisons(
    data: pd.DataFrame,
) -> pd.DataFrame:
    rows = []

    comparisons = {
        "Ocean Culture": ("Image", "Carousel"),
        "PsicoCampus": ("Image", "Carousel"),
        "PsicoCampus_Reel": ("Image", "Reel"),
        "PsicoCampus_Carousel_Reel": ("Carousel", "Reel"),
    }

    for comparison_name, formats in comparisons.items():
        project = (
            "Ocean Culture"
            if comparison_name == "Ocean Culture"
            else "PsicoCampus"
        )

        project_data = data.loc[data["project"].eq(project)]

        for metric in RATE_COLUMNS:
            first = project_data.loc[
                project_data["post_type"].eq(formats[0]),
                metric,
            ].dropna()

            second = project_data.loc[
                project_data["post_type"].eq(formats[1]),
                metric,
            ].dropna()

            test = mannwhitneyu(
                first,
                second,
                alternative="two-sided",
                method="asymptotic",
            )

            rows.append(
                {
                    "comparison_family": comparison_name,
                    "project": project,
                    "metric": metric,
                    "format_1": formats[0],
                    "format_1_n": len(first),
                    "format_1_median": first.median(),
                    "format_2": formats[1],
                    "format_2_n": len(second),
                    "format_2_median": second.median(),
                    "mann_whitney_u": test.statistic,
                    "p_value": test.pvalue,
                    "rank_biserial": rank_biserial(
                        test.statistic,
                        len(first),
                        len(second),
                    ),
                }
            )

    results = pd.DataFrame(rows)

    rejected, adjusted, _, _ = multipletests(
        results["p_value"],
        alpha=0.05,
        method="holm",
    )

    results["holm_p_value"] = adjusted
    results["holm_reject_0_05"] = rejected

    return results


def main() -> None:
    data = pd.read_csv(INPUT)
    data = add_rates(data)

    descriptive = descriptive_results(data)
    projects = project_comparisons(data)
    formats = within_project_format_comparisons(data)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    descriptive.to_csv(
        OUTPUT_DIR / "normalized_rate_descriptives.csv",
        index=False,
        encoding="utf-8",
    )

    projects.to_csv(
        OUTPUT_DIR / "normalized_rate_project_tests.csv",
        index=False,
        encoding="utf-8",
    )

    formats.to_csv(
        OUTPUT_DIR / "normalized_rate_format_tests.csv",
        index=False,
        encoding="utf-8",
    )

    print("PROJECT COMPARISONS")
    print(
        projects.to_string(
            index=False,
            formatters={
                "p_value": "{:.3e}".format,
                "holm_p_value": "{:.3e}".format,
                "rank_biserial": "{:.3f}".format,
            },
        )
    )

    print("\nWITHIN-PROJECT FORMAT COMPARISONS")
    print(
        formats.to_string(
            index=False,
            formatters={
                "p_value": "{:.3e}".format,
                "holm_p_value": "{:.3e}".format,
                "rank_biserial": "{:.3f}".format,
            },
        )
    )

    print("\nImportant:")
    print(
        "Rates represent recorded interactions per 100 accounts reached. "
        "They are not percentages of unique users who interacted."
    )


if __name__ == "__main__":
    main()
