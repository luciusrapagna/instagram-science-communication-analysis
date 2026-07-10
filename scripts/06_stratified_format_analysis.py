from itertools import combinations
from pathlib import Path

import pandas as pd
from scipy.stats import kruskal, mannwhitneyu
from statsmodels.stats.multitest import multipletests


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data" / "public" / "instagram_posts_anonymized.csv"
OUTPUT = ROOT / "outputs" / "tables" / "stratified_format_tests.csv"

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

PROJECT_FORMATS = {
    "Ocean Culture": ["Image", "Carousel"],
    "PsicoCampus": ["Image", "Carousel", "Reel"],
}


def rank_biserial(u_value: float, n1: int, n2: int) -> float:
    return (2 * u_value) / (n1 * n2) - 1


def compare_two_formats(
    data: pd.DataFrame,
    project: str,
    formats: list[str],
) -> list[dict]:
    rows = []

    for metric in METRICS:
        first = data.loc[
            data["post_type"].eq(formats[0]),
            metric,
        ].dropna()

        second = data.loc[
            data["post_type"].eq(formats[1]),
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
                "project": project,
                "analysis": "two_format_comparison",
                "metric": metric,
                "format_1": formats[0],
                "format_1_n": len(first),
                "format_1_median": first.median(),
                "format_2": formats[1],
                "format_2_n": len(second),
                "format_2_median": second.median(),
                "statistic": test.statistic,
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

    return results.to_dict("records")


def compare_three_formats(
    data: pd.DataFrame,
    project: str,
    formats: list[str],
) -> list[dict]:
    omnibus_rows = []

    for metric in METRICS:
        groups = [
            data.loc[data["post_type"].eq(fmt), metric].dropna()
            for fmt in formats
        ]

        test = kruskal(*groups)

        omnibus_rows.append(
            {
                "project": project,
                "analysis": "kruskal_wallis",
                "metric": metric,
                "format_1": None,
                "format_1_n": None,
                "format_1_median": None,
                "format_2": None,
                "format_2_n": None,
                "format_2_median": None,
                "statistic": test.statistic,
                "p_value": test.pvalue,
                "rank_biserial": None,
            }
        )

    omnibus = pd.DataFrame(omnibus_rows)
    rejected, adjusted, _, _ = multipletests(
        omnibus["p_value"],
        alpha=0.05,
        method="holm",
    )
    omnibus["holm_p_value"] = adjusted
    omnibus["holm_reject_0_05"] = rejected

    all_rows = omnibus.to_dict("records")

    significant_metrics = omnibus.loc[
        omnibus["holm_reject_0_05"],
        "metric",
    ]

    for metric in significant_metrics:
        pairwise_rows = []

        for first_format, second_format in combinations(formats, 2):
            first = data.loc[
                data["post_type"].eq(first_format),
                metric,
            ].dropna()

            second = data.loc[
                data["post_type"].eq(second_format),
                metric,
            ].dropna()

            test = mannwhitneyu(
                first,
                second,
                alternative="two-sided",
                method="asymptotic",
            )

            pairwise_rows.append(
                {
                    "project": project,
                    "analysis": "post_hoc",
                    "metric": metric,
                    "format_1": first_format,
                    "format_1_n": len(first),
                    "format_1_median": first.median(),
                    "format_2": second_format,
                    "format_2_n": len(second),
                    "format_2_median": second.median(),
                    "statistic": test.statistic,
                    "p_value": test.pvalue,
                    "rank_biserial": rank_biserial(
                        test.statistic,
                        len(first),
                        len(second),
                    ),
                }
            )

        pairwise = pd.DataFrame(pairwise_rows)
        rejected, adjusted, _, _ = multipletests(
            pairwise["p_value"],
            alpha=0.05,
            method="holm",
        )
        pairwise["holm_p_value"] = adjusted
        pairwise["holm_reject_0_05"] = rejected
        all_rows.extend(pairwise.to_dict("records"))

    return all_rows


def main() -> None:
    data = pd.read_csv(INPUT)
    rows = []

    for project, formats in PROJECT_FORMATS.items():
        project_data = data.loc[data["project"].eq(project)].copy()

        if len(formats) == 2:
            rows.extend(
                compare_two_formats(project_data, project, formats)
            )
        else:
            rows.extend(
                compare_three_formats(project_data, project, formats)
            )

    results = pd.DataFrame(rows)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    results.to_csv(OUTPUT, index=False, encoding="utf-8")

    print(
        results.to_string(
            index=False,
            formatters={
                "p_value": "{:.3e}".format,
                "holm_p_value": "{:.3e}".format,
                "rank_biserial": lambda value: (
                    "" if pd.isna(value) else f"{value:.3f}"
                ),
            },
        )
    )

    print("\nInterpretive boundary:")
    print(
        "These analyses describe within-project associations. "
        "They do not establish causal format effects."
    )
    print(f"\nSaved: {OUTPUT}")


if __name__ == "__main__":
    main()
