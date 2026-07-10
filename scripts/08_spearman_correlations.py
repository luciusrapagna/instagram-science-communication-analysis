from itertools import combinations
from pathlib import Path

import pandas as pd
from scipy.stats import spearmanr
from statsmodels.stats.multitest import multipletests


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data" / "public" / "instagram_posts_anonymized.csv"
OUTPUT = ROOT / "outputs" / "tables" / "spearman_correlations.csv"

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

ANALYSIS_GROUPS = [
    "All posts",
    "Ocean Culture",
    "PsicoCampus",
]


def calculate_correlations(
    data: pd.DataFrame,
    group_name: str,
) -> pd.DataFrame:
    rows = []

    for metric_1, metric_2 in combinations(METRICS, 2):
        pairs = data[[metric_1, metric_2]].dropna()

        test = spearmanr(
            pairs[metric_1],
            pairs[metric_2],
        )

        overlaps_total = (
            "total_interactions" in {metric_1, metric_2}
            and bool(
                {
                    metric_1,
                    metric_2,
                }
                & {
                    "likes",
                    "shares",
                    "comments",
                    "saves",
                }
            )
        )

        rows.append(
            {
                "analysis_group": group_name,
                "metric_1": metric_1,
                "metric_2": metric_2,
                "complete_pairs_n": len(pairs),
                "spearman_rho": test.statistic,
                "p_value": test.pvalue,
                "mathematical_overlap": overlaps_total,
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
    frames = []

    for group_name in ANALYSIS_GROUPS:
        if group_name == "All posts":
            subset = data
        else:
            subset = data.loc[data["project"].eq(group_name)]

        frames.append(
            calculate_correlations(subset, group_name)
        )

    results = pd.concat(frames, ignore_index=True)

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    results.to_csv(OUTPUT, index=False, encoding="utf-8")

    priority_pairs = {
        frozenset(("views", "reach")),
        frozenset(("views", "total_interactions")),
        frozenset(("reach", "total_interactions")),
        frozenset(("reach", "likes")),
        frozenset(("views", "likes")),
    }

    priority = results.loc[
        results.apply(
            lambda row: frozenset(
                (row["metric_1"], row["metric_2"])
            )
            in priority_pairs,
            axis=1,
        )
    ]

    print("PRIORITY CORRELATIONS")
    print(
        priority.to_string(
            index=False,
            formatters={
                "spearman_rho": "{:.3f}".format,
                "p_value": "{:.3e}".format,
                "holm_p_value": "{:.3e}".format,
            },
        )
    )

    print("\nINTERPRETIVE WARNINGS")
    print(
        "Correlation does not establish causation. "
        "Total interactions mathematically include likes, shares, "
        "comments, and saves."
    )

    print(f"\nSaved: {OUTPUT}")


if __name__ == "__main__":
    main()
