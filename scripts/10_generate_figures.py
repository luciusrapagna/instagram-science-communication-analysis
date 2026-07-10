from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data" / "public" / "instagram_posts_anonymized.csv"
OUTPUT_DIR = ROOT / "outputs" / "figures"

PROJECT_ORDER = ["Ocean Culture", "PsicoCampus"]
FORMAT_ORDER = ["Image", "Carousel", "Reel"]

PROJECT_PALETTE = {
    "Ocean Culture": "#007C91",
    "PsicoCampus": "#D1495B",
}

FORMAT_PALETTE = {
    "Image": "#8DA0CB",
    "Carousel": "#66C2A5",
    "Reel": "#FC8D62",
}


def save_figure(figure: plt.Figure, stem: str) -> None:
    png = OUTPUT_DIR / f"{stem}.png"
    pdf = OUTPUT_DIR / f"{stem}.pdf"

    figure.savefig(
        png,
        dpi=300,
        bbox_inches="tight",
        facecolor="white",
    )
    figure.savefig(
        pdf,
        bbox_inches="tight",
        facecolor="white",
    )

    print(f"Saved: {png}")
    print(f"Saved: {pdf}")


def figure_project_distributions(data: pd.DataFrame) -> None:
    metrics = {
        "views": "Views",
        "reach": "Reach",
        "likes": "Likes",
        "total_interactions": "Total interactions",
    }

    figure, axes = plt.subplots(
        2,
        2,
        figsize=(10, 8),
        constrained_layout=True,
    )

    for axis, (metric, label) in zip(axes.flat, metrics.items()):
        sns.boxplot(
            data=data,
            x="project",
            y=metric,
            order=PROJECT_ORDER,
            hue="project",
            palette=PROJECT_PALETTE,
            legend=False,
            showfliers=False,
            width=0.55,
            ax=axis,
        )

        sns.stripplot(
            data=data,
            x="project",
            y=metric,
            order=PROJECT_ORDER,
            color="#252525",
            alpha=0.42,
            jitter=0.22,
            size=3,
            ax=axis,
        )

        axis.set_yscale("log")
        axis.set_title(label, fontweight="bold")
        axis.set_xlabel("")
        axis.set_ylabel(f"{label} (log scale)")
        axis.grid(axis="y", alpha=0.25)

    figure.suptitle(
        "Distribution of Instagram performance indicators by project",
        fontsize=14,
        fontweight="bold",
    )

    save_figure(
        figure,
        "figure_1_project_distributions",
    )
    plt.close(figure)


def figure_formats_by_project(data: pd.DataFrame) -> None:
    plot_data = data.copy()
    plot_data = plot_data.loc[
        ~(
            plot_data["project"].eq("Ocean Culture")
            & plot_data["post_type"].eq("Reel")
        )
    ]

    figure, axes = plt.subplots(
        2,
        2,
        figsize=(11, 8),
        constrained_layout=True,
    )

    panels = [
        ("Ocean Culture", "views", "Views"),
        ("Ocean Culture", "total_interactions", "Total interactions"),
        ("PsicoCampus", "views", "Views"),
        ("PsicoCampus", "total_interactions", "Total interactions"),
    ]

    for axis, (project, metric, label) in zip(
        axes.flat,
        panels,
    ):
        subset = plot_data.loc[
            plot_data["project"].eq(project)
        ]

        available_formats = [
            value
            for value in FORMAT_ORDER
            if value in subset["post_type"].unique()
        ]

        sns.boxplot(
            data=subset,
            x="post_type",
            y=metric,
            order=available_formats,
            hue="post_type",
            palette=FORMAT_PALETTE,
            legend=False,
            showfliers=False,
            width=0.6,
            ax=axis,
        )

        sns.stripplot(
            data=subset,
            x="post_type",
            y=metric,
            order=available_formats,
            color="#252525",
            alpha=0.45,
            jitter=0.2,
            size=3,
            ax=axis,
        )

        axis.set_yscale("log")
        axis.set_title(f"{project}: {label}", fontweight="bold")
        axis.set_xlabel("Post format")
        axis.set_ylabel(f"{label} (log scale)")
        axis.grid(axis="y", alpha=0.25)

    figure.suptitle(
        "Performance indicators by post format within each project",
        fontsize=14,
        fontweight="bold",
    )

    save_figure(
        figure,
        "figure_2_formats_within_projects",
    )
    plt.close(figure)


def figure_reach_interactions(data: pd.DataFrame) -> None:
    plot_data = data.dropna(
        subset=["reach", "total_interactions"]
    ).copy()

    figure, axis = plt.subplots(figsize=(8, 6))

    sns.scatterplot(
        data=plot_data,
        x="reach",
        y="total_interactions",
        hue="project",
        hue_order=PROJECT_ORDER,
        palette=PROJECT_PALETTE,
        style="post_type",
        style_order=FORMAT_ORDER,
        s=65,
        alpha=0.75,
        edgecolor="white",
        linewidth=0.5,
        ax=axis,
    )

    axis.set_xscale("log")
    axis.set_yscale("log")
    axis.set_xlabel("Reach (log scale)")
    axis.set_ylabel("Total interactions (log scale)")
    axis.set_title(
        "Relationship between reach and total interactions",
        fontweight="bold",
    )
    axis.grid(alpha=0.25)
    axis.legend(
        title="Project / post format",
        frameon=True,
        bbox_to_anchor=(1.02, 1),
        loc="upper left",
    )

    figure.tight_layout()

    save_figure(
        figure,
        "figure_3_reach_and_interactions",
    )
    plt.close(figure)


def main() -> None:
    sns.set_theme(
        style="whitegrid",
        context="paper",
        font_scale=1.15,
    )

    data = pd.read_csv(INPUT)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    figure_project_distributions(data)
    figure_formats_by_project(data)
    figure_reach_interactions(data)

    print("\nAll figures generated successfully.")


if __name__ == "__main__":
    main()
