from pathlib import Path

import pandas as pd
from scipy.stats import mannwhitneyu
from statsmodels.stats.multitest import multipletests


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data" / "public" / "instagram_posts_anonymized.csv"
OUTPUT = ROOT / "outputs" / "tables" / "outlier_sensitivity.csv"

GROUP_1 = "Ocean Culture"
GROUP_2 = "PsicoCampus"

# The IQR-based sensitivity analysis is restricted to metrics with
# sufficient variation above zero. It is unsuitable for highly
# zero-inflated outcomes whose first and third quartiles are both zero.
METRICS = [
    "views",
    "reach",
    "likes",
    "total_interactions",
]


def upper_extreme_threshold(values: pd.Series) -> float:
    valid = values.dropna()
    q1 = valid.quantile(0.25)
    q3 = valid.quantile(0.75)
    iqr = q3 - q1
    return q3 + 3 * iqr


def rank_biserial(u_value: float, n1: int, n2: int) -> float:
    return (2 * u_value) / (n1 * n2) - 1


def compare(
    group_1: pd.Series,
    group_2: pd.Series,
) -> dict:
    first = group_1.dropna()
    second = group_2.dropna()

    test = mannwhitneyu(
        first,
        second,
        alternative="two-sided",
        method="asymptotic",
    )

    return {
        "group_1_n": len(first),
        "group_1_median": first.median(),
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


def main() -> None:
    data = pd.read_csv(INPUT)
    rows = []

    for metric in METRICS:
        group_1_full = data.loc[
            data["project"].eq(GROUP_1),
            metric,
        ]

        group_2_full = data.loc[
            data["project"].eq(GROUP_2),
            metric,
        ]

        threshold_1 = upper_extreme_threshold(group_1_full)
        threshold_2 = upper_extreme_threshold(group_2_full)

        group_1_trimmed = group_1_full.loc[
            group_1_full.le(threshold_1)
            | group_1_full.isna()
        ]

        group_2_trimmed = group_2_full.loc[
            group_2_full.le(threshold_2)
            | group_2_full.isna()
        ]

        full = compare(group_1_full, group_2_full)
        trimmed = compare(group_1_trimmed, group_2_trimmed)

        rows.append(
            {
                "metric": metric,
                "group_1_threshold": threshold_1,
                "group_1_removed": (
                    group_1_full.gt(threshold_1).sum()
                ),
                "group_2_threshold": threshold_2,
                "group_2_removed": (
                    group_2_full.gt(threshold_2).sum()
                ),
                "full_group_1_n": full["group_1_n"],
                "full_group_2_n": full["group_2_n"],
                "full_rank_biserial": full["rank_biserial"],
                "full_p_value": full["p_value"],
                "trimmed_group_1_n": trimmed["group_1_n"],
                "trimmed_group_2_n": trimmed["group_2_n"],
                "trimmed_group_1_median": trimmed[
                    "group_1_median"
                ],
                "trimmed_group_2_median": trimmed[
                    "group_2_median"
                ],
                "trimmed_rank_biserial": trimmed[
                    "rank_biserial"
                ],
                "trimmed_p_value": trimmed["p_value"],
            }
        )

    results = pd.DataFrame(rows)

    full_rejected, full_adjusted, _, _ = multipletests(
        results["full_p_value"],
        alpha=0.05,
        method="holm",
    )

    trimmed_rejected, trimmed_adjusted, _, _ = multipletests(
        results["trimmed_p_value"],
        alpha=0.05,
        method="holm",
    )

    results["full_holm_p_value"] = full_adjusted
    results["full_holm_reject_0_05"] = full_rejected
    results["trimmed_holm_p_value"] = trimmed_adjusted
    results["trimmed_holm_reject_0_05"] = trimmed_rejected

    results["decision_consistent"] = (
        results["full_holm_reject_0_05"]
        == results["trimmed_holm_reject_0_05"]
    )

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    results.to_csv(OUTPUT, index=False, encoding="utf-8")

    display = [
        "metric",
        "group_1_removed",
        "group_2_removed",
        "full_rank_biserial",
        "full_holm_p_value",
        "trimmed_rank_biserial",
        "trimmed_holm_p_value",
        "decision_consistent",
    ]

    print("OUTLIER SENSITIVITY ANALYSIS")
    print(
        results[display].to_string(
            index=False,
            formatters={
                "full_rank_biserial": "{:.3f}".format,
                "full_holm_p_value": "{:.3e}".format,
                "trimmed_rank_biserial": "{:.3f}".format,
                "trimmed_holm_p_value": "{:.3e}".format,
            },
        )
    )

    print("\nImportant:")
    print(
        "Extreme observations are retained in the primary analysis. "
        "Temporary exclusion is used only to assess robustness."
    )

    print(f"\nSaved: {OUTPUT}")


if __name__ == "__main__":
    main()

