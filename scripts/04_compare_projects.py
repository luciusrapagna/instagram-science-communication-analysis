from pathlib import Path

import pandas as pd
from scipy.stats import mannwhitneyu
from statsmodels.stats.multitest import multipletests


PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_FILE = PROJECT_ROOT / "data" / "public" / "instagram_posts_anonymized.csv"
OUTPUT_FILE = (
    PROJECT_ROOT
    / "outputs"
    / "tables"
    / "project_comparisons.csv"
)

GROUP_1 = "Ocean Culture"
GROUP_2 = "PsicoCampus"

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


def summarize(values: pd.Series) -> dict:
    """Return robust descriptive statistics for one group."""

    valid = values.dropna()

    return {
        "n": len(valid),
        "median": valid.median(),
        "q1": valid.quantile(0.25),
        "q3": valid.quantile(0.75),
    }


def rank_biserial_from_u(
    u_statistic: float,
    n_group_1: int,
    n_group_2: int,
) -> float:
    """
    Calculate rank-biserial correlation from Mann-Whitney U.

    Positive values indicate that Group 1 tends to have larger values.
    Negative values indicate that Group 2 tends to have larger values.
    """

    return (2 * u_statistic) / (n_group_1 * n_group_2) - 1


def main() -> None:
    data = pd.read_csv(INPUT_FILE)
    results = []

    for metric in METRICS:
        group_1 = data.loc[
            data["project"].eq(GROUP_1),
            metric,
        ].dropna()

        group_2 = data.loc[
            data["project"].eq(GROUP_2),
            metric,
        ].dropna()

        summary_1 = summarize(group_1)
        summary_2 = summarize(group_2)

        test = mannwhitneyu(
            group_1,
            group_2,
            alternative="two-sided",
            method="asymptotic",
        )

        effect = rank_biserial_from_u(
            test.statistic,
            len(group_1),
            len(group_2),
        )

        results.append(
            {
                "metric": metric,
                "group_1": GROUP_1,
                "group_1_n": summary_1["n"],
                "group_1_median": summary_1["median"],
                "group_1_q1": summary_1["q1"],
                "group_1_q3": summary_1["q3"],
                "group_2": GROUP_2,
                "group_2_n": summary_2["n"],
                "group_2_median": summary_2["median"],
                "group_2_q1": summary_2["q1"],
                "group_2_q3": summary_2["q3"],
                "mann_whitney_u": test.statistic,
                "p_value": test.pvalue,
                "rank_biserial": effect,
            }
        )

    results = pd.DataFrame(results)

    rejected, adjusted_p, _, _ = multipletests(
        results["p_value"],
        alpha=0.05,
        method="holm",
    )

    results["holm_p_value"] = adjusted_p
    results["holm_reject_0_05"] = rejected

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    results.to_csv(
        OUTPUT_FILE,
        index=False,
        encoding="utf-8",
    )

    display_columns = [
        "metric",
        "group_1_n",
        "group_1_median",
        "group_2_n",
        "group_2_median",
        "mann_whitney_u",
        "p_value",
        "holm_p_value",
        "rank_biserial",
        "holm_reject_0_05",
    ]

    print("PROJECT COMPARISONS")
    print(
        results[display_columns].to_string(
            index=False,
            formatters={
                "p_value": "{:.6f}".format,
                "holm_p_value": "{:.6f}".format,
                "rank_biserial": "{:.3f}".format,
            },
        )
    )

    print("\nEffect-size direction:")
    print(f"Positive rank-biserial: higher tendency in {GROUP_1}")
    print(f"Negative rank-biserial: higher tendency in {GROUP_2}")

    print(f"\nSaved: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
