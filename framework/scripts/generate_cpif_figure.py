#!/usr/bin/env python3
"""Generate the CPIF conceptual figure in publication-ready formats."""

from pathlib import Path
import sys
import shutil

try:
    import matplotlib

    matplotlib.use("Agg")

    import matplotlib.pyplot as plt
    from matplotlib.patches import FancyBboxPatch
except ImportError as exc:
    raise SystemExit(
        "Required dependency unavailable. Activate the project virtual "
        "environment and install matplotlib."
    ) from exc


FRAMEWORK_DIR = Path(__file__).resolve().parents[1]
SOURCE_DIR = FRAMEWORK_DIR / "figures" / "source"
PUBLICATION_DIR = FRAMEWORK_DIR / "figures" / "publication"
# Grayscale-safe palette suitable for print.
TEXT_COLOR = "#1A1A1A"
EDGE_COLOR = "#3A3A3A"
ARROW_COLOR = "#505050"
MAIN_FILL = "#E6E6E6"
SECONDARY_FILL = "#F4F4F4"
NOTE_FILL = "#FFFFFF"


def add_box(
    ax,
    x: float,
    y: float,
    width: float,
    height: float,
    title: str,
    details: str = "",
    *,
    facecolor: str = MAIN_FILL,
    linewidth: float = 1.2,
    title_size: float = 10.5,
    detail_size: float = 8.3,
) -> None:
    """Add a labeled rounded box using axes-relative coordinates."""
    box = FancyBboxPatch(
        (x, y),
        width,
        height,
        boxstyle="round,pad=0.008,rounding_size=0.008",
        facecolor=facecolor,
        edgecolor=EDGE_COLOR,
        linewidth=linewidth,
    )
    ax.add_patch(box)

    title_y = y + height * (0.64 if details else 0.50)
    ax.text(
        x + width / 2,
        title_y,
        title,
        ha="center",
        va="center",
        fontsize=title_size,
        fontweight="bold",
        color=TEXT_COLOR,
    )

    if details:
        ax.text(
            x + width / 2,
            y + height * 0.30,
            details,
            ha="center",
            va="center",
            fontsize=detail_size,
            color=TEXT_COLOR,
            linespacing=1.25,
        )


def add_down_arrow(
    ax,
    x: float,
    start_y: float,
    end_y: float,
) -> None:
    """Add a vertical arrow connecting two layers."""
    ax.annotate(
        "",
        xy=(x, end_y),
        xytext=(x, start_y),
        arrowprops={
            "arrowstyle": "-|>",
            "color": ARROW_COLOR,
            "linewidth": 1.25,
            "mutation_scale": 12,
        },
    )
def build_figure():
    """Build and return the CPIF conceptual figure."""
    fig, ax = plt.subplots(figsize=(11, 14))
    fig.patch.set_facecolor("white")

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    ax.text(
        0.5,
        0.975,
        "Communication Performance Interpretation Framework (CPIF)",
        ha="center",
        va="center",
        fontsize=16,
        fontweight="bold",
        color=TEXT_COLOR,
    )

    ax.text(
        0.5,
        0.951,
        "Context-sensitive interpretation of platform-recorded communication metrics",
        ha="center",
        va="center",
        fontsize=9.5,
        color=ARROW_COLOR,
    )

    main_x = 0.06
    main_width = 0.61
    center_x = main_x + main_width / 2

    # Layer 1
    add_box(
        ax,
        main_x,
        0.865,
        main_width,
        0.065,
        "1. Communication Context",
        "initiative | objectives | audience | institution | platform | period",
        title_size=11.5,
        detail_size=8.2,
    )

    # Layer 2 frame
    layer_2_y = 0.700
    layer_2_height = 0.135
    layer_2_frame = FancyBboxPatch(
        (main_x, layer_2_y),
        main_width,
        layer_2_height,
        boxstyle="round,pad=0.008,rounding_size=0.008",
        facecolor=MAIN_FILL,
        edgecolor=EDGE_COLOR,
        linewidth=1.2,
    )
    ax.add_patch(layer_2_frame)

    ax.text(
        center_x,
        layer_2_y + layer_2_height - 0.025,
        "2. Platform-Recorded Metrics",
        ha="center",
        va="center",
        fontsize=11.5,
        fontweight="bold",
        color=TEXT_COLOR,
    )

    sub_width = 0.17
    sub_y = layer_2_y + 0.020

    add_box(
        ax,
        0.085,
        sub_y,
        sub_width,
        0.060,
        "Exposure",
        "reach, views,\nimpressions, plays",
        facecolor=SECONDARY_FILL,
        title_size=9.3,
        detail_size=7.3,
    )
    add_box(
        ax,
        0.280,
        sub_y,
        sub_width,
        0.060,
        "Interaction",
        "likes, comments, shares,\nsaves, follows, clicks",
        facecolor=SECONDARY_FILL,
        title_size=9.3,
        detail_size=7.1,
    )
    add_box(
        ax,
        0.475,
        sub_y,
        sub_width,
        0.060,
        "Other indicators",
        "platform-specific\nmeasures",
        facecolor=SECONDARY_FILL,
        title_size=9.0,
        detail_size=7.3,
    )

    # Layer 3 frame
    layer_3_y = 0.535
    layer_3_height = 0.135
    layer_3_frame = FancyBboxPatch(
        (main_x, layer_3_y),
        main_width,
        layer_3_height,
        boxstyle="round,pad=0.008,rounding_size=0.008",
        facecolor=MAIN_FILL,
        edgecolor=EDGE_COLOR,
        linewidth=1.2,
    )
    ax.add_patch(layer_3_frame)

    ax.text(
        center_x,
        layer_3_y + layer_3_height - 0.025,
        "3. Metric Preparation and Standardization",
        ha="center",
        va="center",
        fontsize=11.2,
        fontweight="bold",
        color=TEXT_COLOR,
    )

    preparation_y = layer_3_y + 0.020

    add_box(
        ax,
        0.085,
        preparation_y,
        sub_width,
        0.060,
        "Raw metrics",
        "audited and\npreserved",
        facecolor=SECONDARY_FILL,
        title_size=9.2,
        detail_size=7.3,
    )
    add_box(
        ax,
        0.280,
        preparation_y,
        sub_width,
        0.060,
        "Normalized metrics",
        "valid denominators\nand definitions",
        facecolor=SECONDARY_FILL,
        title_size=9.0,
        detail_size=7.3,
    )
    add_box(
        ax,
        0.475,
        preparation_y,
        sub_width,
        0.060,
        "Analytical outcomes",
        "comparable within\ndocumented limits",
        facecolor=SECONDARY_FILL,
        title_size=8.8,
        detail_size=7.2,
    )

    # Layer 4
    add_box(
        ax,
        main_x,
        0.350,
        main_width,
        0.150,
        "4. Statistical Integration",
        (
            "descriptive statistics | group comparisons | effect sizes\n"
            "multiplicity | associations | sensitivity and robustness\n"
            "methods selected according to design, distribution, and dependence"
        ),
        title_size=11.5,
        detail_size=8.1,
    )

    # Layer 5
    add_box(
        ax,
        main_x,
        0.205,
        main_width,
        0.110,
        "5. Communication-Performance Interpretation",
        (
            "exposure + interaction + normalized indicators\n"
            "magnitude + uncertainty + associations + robustness\n"
            "institutional + editorial + platform context"
        ),
        title_size=11.0,
        detail_size=8.0,
    )

    # Layer 6
    add_box(
        ax,
        main_x,
        0.065,
        main_width,
        0.105,
        "6. Evidence-Informed Decision Support",
        (
            "editorial planning | format testing | monitoring\n"
            "hypothesis generation | future study design"
        ),
        title_size=11.0,
        detail_size=8.1,
    )

    # Arrows connecting the six layers.
    add_down_arrow(ax, center_x, 0.865, 0.840)
    add_down_arrow(ax, center_x, 0.700, 0.675)
    add_down_arrow(ax, center_x, 0.535, 0.505)
    add_down_arrow(ax, center_x, 0.350, 0.320)
    add_down_arrow(ax, center_x, 0.205, 0.175)

    # Boundary box: outcomes not measured directly by CPIF.
    add_box(
        ax,
        0.720,
        0.485,
        0.245,
        0.275,
        "What CPIF does not\ndirectly measure",
        (
            "learning\n"
            "trust\n"
            "scientific literacy\n"
            "behavioural change\n"
            "societal impact"
        ),
        facecolor=NOTE_FILL,
        linewidth=1.4,
        title_size=10.5,
        detail_size=9.0,
    )

    ax.text(
        0.842,
        0.455,
        "Effectiveness requires\noutcome-specific measures.",
        ha="center",
        va="center",
        fontsize=8.2,
        color=ARROW_COLOR,
        fontstyle="italic",
    )

    ax.text(
        0.5,
        0.025,
        "Platform-independent | Context-sensitive | No universal score",
        ha="center",
        va="center",
        fontsize=8.8,
        color=ARROW_COLOR,
    )

    return fig
def save_outputs(fig) -> None:
    """Save the figure and an exact snapshot of its generating source."""
    output_stem = PUBLICATION_DIR / "cpif_conceptual_framework"

    for file_format in ("svg", "pdf", "png"):
        output_path = output_stem.with_suffix(f".{file_format}")

        fig.savefig(
            output_path,
            format=file_format,
            dpi=300,
            bbox_inches="tight",
            pad_inches=0.15,
            facecolor="white",
        )

        if file_format == "svg":
            svg_text = output_path.read_text(encoding="utf-8")
            normalized_svg = (
                "\n".join(line.rstrip() for line in svg_text.splitlines())
                + "\n"
            )
            output_path.write_text(normalized_svg, encoding="utf-8")

        print(f"Created: {output_path}")

    source_snapshot = SOURCE_DIR / "generate_cpif_figure.py"
    shutil.copy2(Path(__file__), source_snapshot)
    print(f"Created source snapshot: {source_snapshot}")

def ensure_directories() -> None:
    """Create the figure directories when they do not already exist."""
    SOURCE_DIR.mkdir(parents=True, exist_ok=True)
    PUBLICATION_DIR.mkdir(parents=True, exist_ok=True)


def main() -> None:
    """Generate and save the CPIF conceptual figure."""
    ensure_directories()

    print("Generating the CPIF conceptual figure...")

    fig = build_figure()

    try:
        save_outputs(fig)
    finally:
        plt.close(fig)

    print("CPIF figure generation completed successfully.")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"CPIF figure generation failed: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc