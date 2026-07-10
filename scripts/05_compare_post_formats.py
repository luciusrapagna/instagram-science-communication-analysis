from itertools import combinations
from pathlib import Path

import pandas as pd
from scipy.stats import kruskal, mannwhitneyu
from statsmodels.stats.multitest import multipletests


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data" / "public" / "instagram_posts_anonymized.csv"
OUTPUT_DIR = ROOT / "outputs" / "tables"

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

FORMATS = ["Image", "Carousel", "Reel"]


def omnibus_tests(data: pd.DataFrame) -> pd.DataFrame:
    rows = []

    for metric in METRICS:
        groups = [
            data.loc[data["post_type"].eq(post_format), metric].dropna()
            for post_format in FORMATS
        ]

        test = kruskal(*groups)

        rows.append(
            {
                "metric": metric,
                "kruskal_h": test.statistic,
                "p_value": test.pvalue,
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


def pairwise_tests(
    data: pd.DataFrame,
    significant_metrics: list[str],
) -> pd.DataFrame:
    rows = []

    for metric in significant_metrics:
        metric_rows = []

        for format_1, format_2 in combinations(FORMATS, 2):
            group_1 = data.loc[
                data["post_type"].eq(format_1),
                metric,
            ].dropna()

            group_2 = data.loc[
                data["post_type"].eq(format_2),
                metric,
            ].dropna()

            test = mannwhitneyu(
                group_1,
                group_2,
                alternative="two-sided",
                method="asymptotic",
            )

            effect = (
                2 * test.statistic / (len(group_1) * len(group_2))
            ) - 1

            metric_rows.append(
                {
                    "metric": metric,
                    "format_1": format_1,
                    "format_1_n": len(group_1),
                    "format_1_median": group_1.median(),
                    "format_2": format_2,
                    "format_2_n": len(group_2),
                    "format_2_median": group_2.median(),
                    "mann_whitney_u": test.statistic,
                    "p_value": test.pvalue,
                    "rank_biserial": effect,
                }
            )

        metric_results = pd.DataFrame(metric_rows)

        rejected, adjusted, _, _ = multipletests(
            metric_results["p_value"],
            alpha=0.05,
            method="holm",
        )

        metric_results["holm_p_value_within_metric"] = adjusted
        metric_results["holm_reject_0_05"] = rejected
        rows.append(metric_results)

    if not rows:
        return pd.DataFrame()

    return pd.concat(rows, ignore_index=True)


def main() -> None:
    data = pd.read_csv(INPUT)

    counts = pd.crosstab(data["project"], data["post_type"])
    print("FORMAT COUNTS BY PROJECT")
    print(counts.to_string())

    omnibus = omnibus_tests(data)

    significant_metrics = omnibus.loc[
        omnibus["holm_reject_0_05"],
        "metric",
    ].tolist()

    pairwise = pairwise_tests(data, significant_metrics)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    omnibus_file = OUTPUT_DIR / "format_omnibus_tests.csv"
    pairwise_file = OUTPUT_DIR / "format_pairwise_tests.csv"

    omnibus.to_csv(omnibus_file, index=False, encoding="utf-8")
    pairwise.to_csv(pairwise_file, index=False, encoding="utf-8")

    print("\nKRUSKAL-WALLIS TESTS")
    print(
        omnibus.to_string(
            index=False,
            formatters={
                "p_value": "{:.3e}".format,
                "holm_p_value": "{:.3e}".format,
            },
        )
    )

    print("\nPAIRWISE TESTS")
    if pairwise.empty:
        print("No post-hoc comparisons were triggered.")
    else:
        print(
            pairwise.to_string(
                index=False,
                formatters={
                    "p_value": "{:.3e}".format,
                    "holm_p_value_within_metric": "{:.3e}".format,
                    "rank_biserial": "{:.3f}".format,
                },
            )
        )

    print("\nCaution:")
    print(
        "Project and post format are unbalanced; "
        "Ocean Culture contains only one Reel."
    )


if __name__ == "__main__":
    main()
