#!/usr/bin/env python3
"""Generate the CPIF six-layer framework figure in PNG, SVG, and PDF."""
from __future__ import annotations

from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

LAYERS = [
    ("1", "Communication Context", "Objectives · audience · platform · institutional setting"),
    ("2", "Platform-recorded Metrics", "Exposure · interaction · audience growth · derived indicators"),
    ("3", "Metric Preparation and Standardisation", "Audit · harmonisation · missingness · derived variables"),
    ("4", "Statistical Integration", "Descriptives · tests · effect sizes · sensitivity analyses"),
    ("5", "Communication-performance Interpretation", "Magnitude · uncertainty · context · inferential limits"),
    ("6", "Evidence-informed Decision Support", "Maintain · adapt · test · monitor · collect additional evidence"),
]


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    out_dir = root / "figures" / "publication"
    out_dir.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=(11, 12))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 14)
    ax.axis("off")

    y_positions = [12.2, 10.2, 8.2, 6.2, 4.2, 2.2]
    for i, ((number, title, subtitle), y) in enumerate(zip(LAYERS, y_positions)):
        box = FancyBboxPatch(
            (1.0, y - 0.65), 8.0, 1.3,
            boxstyle="round,pad=0.03,rounding_size=0.12",
            linewidth=1.5,
            facecolor="white",
            edgecolor="black",
        )
        ax.add_patch(box)
        ax.text(1.35, y + 0.15, number, fontsize=18, fontweight="bold", va="center")
        ax.text(2.0, y + 0.18, title, fontsize=14, fontweight="bold", va="center")
        ax.text(2.0, y - 0.25, subtitle, fontsize=10.5, va="center")
        if i < len(y_positions) - 1:
            ax.add_patch(FancyArrowPatch((5, y - 0.67), (5, y_positions[i + 1] + 0.67), arrowstyle="-|>", mutation_scale=15, linewidth=1.3))

    # Iterative return arrow
    ax.add_patch(FancyArrowPatch((9.25, 2.2), (9.25, 12.2), connectionstyle="arc3,rad=-0.18", arrowstyle="-|>", mutation_scale=15, linewidth=1.2))
    ax.text(9.6, 7.2, "Iterative refinement", rotation=90, fontsize=10, va="center")

    ax.text(5, 13.45, "Communication Performance Interpretation Framework (CPIF)", ha="center", fontsize=17, fontweight="bold")
    ax.text(5, 13.05, "A structured workflow for quantitative digital science communication evaluation", ha="center", fontsize=11)
    ax.text(5, 0.65, "Metrics are interpreted according to the communication processes they represent and the limits of observational platform data.", ha="center", fontsize=9.5)

    fig.tight_layout()
    for suffix in ("png", "svg", "pdf"):
        fig.savefig(out_dir / f"cpif_framework_v2.{suffix}", dpi=300, bbox_inches="tight")
    print(f"CPIF figure generated in: {out_dir}")


if __name__ == "__main__":
    main()
