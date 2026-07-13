# Communication Performance Interpretation Framework (CPIF)

**Version:** 1.0.0-draft··
**Status:** Proposed framework under development

## Purpose

The Communication Performance Interpretation Framework (CPIF) is a platform-independent, statistically grounded approach for interpreting platform-recorded metrics from university science-communication initiatives. It addresses a recurring methodological problem: digital communication studies often report isolated counts without separating the processes represented by those counts, accounting for context, or communicating statistical uncertainty.

CPIF does not produce a universal score. It organizes evidence across communication context, metric meaning, data preparation, statistical integration, contextual interpretation, and evidence-informed decision support.

## Core concepts

- **Communication exposure** describes distribution and visibility, such as views, reach, impressions, and video plays.
- **Communication interaction** describes observable actions following exposure, such as likes, comments, shares, saves, follows, and clicks.
- **Communication effectiveness** describes educational, cognitive, attitudinal, behavioural, dialogical, or social outcomes, such as learning, scientific literacy, trust in science, behavioural change, participation, and societal impact.

CPIF directly evaluates exposure and interaction when valid platform data are available. Platform metrics are proxies of communication processes and are not direct measures of effectiveness.

## Principles

1. Communication performance is multidimensional.
2. Platform metrics represent distinct communication processes.
3. Statistical interpretation should extend beyond descriptive reporting.
4. Communication performance is context-dependent.
5. Platform metrics are proxies of communication processes rather than direct measures of educational or societal impact.

## Six-layer architecture

1. Communication Context
2. Platform-Recorded Metrics
3. Metric Preparation and Standardization
4. Statistical Integration
5. Communication-Performance Interpretation
6. Evidence-Informed Decision Support

The layers form an auditable analytical sequence rather than a scoring algorithm. Detailed specifications are provided in [CPIF_layers.md](docs/CPIF_layers.md), and objective safeguards are provided in [CPIF_interpretation_rules.md](docs/CPIF_interpretation_rules.md).

## Scope and limitations

CPIF is intended for studies using platform-recorded communication metrics in university science communication and related public-engagement initiatives. It can accommodate different platforms, study designs, sampling structures, and statistical methods. Metric names must not be assumed to be equivalent across platforms or across changes in platform definitions.

The framework has not been externally validated. It does not establish causal effects, infer audience experience from platform traces alone, prescribe cut-offs, or convert heterogeneous metrics into an arbitrary global score. Its suitability depends on transparent operational definitions, valid denominators, adequate study design, and context-sensitive interpretation.

## Initial empirical application

The first empirical demonstration uses 187 Instagram posts from two curricular university extension projects, Ocean Culture and PsicoCampus. It examines views, reach, likes, comments, shares, saves, follows, total interactions, interactions per 100 accounts reached, likes per 100 accounts reached, project-stratified and post-format comparisons, rank-biserial effect sizes, Holm correction, Spearman correlations, sensitivity analysis, and Open Science practices. This initial application is a proof of concept, not definitive validation, and Instagram is not the boundary of CPIF.

## Reproducing the figure

From the repository root, use the project virtual environment when available:

```powershell
.\.venv\Scripts\python.exe framework\scripts\generate_cpif_figure.py
```

The script uses Python 3 and matplotlib, requires no internet access, and writes SVG, PDF, and 300 dpi PNG files to `framework/figures/publication/`.

Validate the complete structure with:

```powershell
.\.venv\Scripts\python.exe framework\scripts\validate_cpif_structure.py
```

## Directory structure

```text
framework/
|-- README.md
|-- LICENSES.md
|-- docs/
|   |-- CPIF_conceptual_framework.md
|   |-- CPIF_principles.md
|   |-- CPIF_layers.md
|   |-- CPIF_interpretation_rules.md
|   |-- CPIF_reporting_checklist.md
|   |-- CPIF_figure_caption.md
|   `-- CPIF_version_history.md
|-- figures/
|   |-- source/
|   `-- publication/
|-- scripts/
|   |-- generate_cpif_figure.py
|   `-- validate_cpif_structure.py
`-- outputs/
```

## Provisional citation

Authors. (2026). *Communication Performance Interpretation Framework (CPIF), Version 1.0.0-draft*. Repository release pending. Author names, persistent identifier, and release metadata must be confirmed before publication.

## Licensing

Code is provisionally designated for the MIT License. Documentation and the CPIF figure are provisionally designated for CC BY 4.0. See [LICENSES.md](LICENSES.md). Final licensing must be confirmed by the authors.

## Development notice

CPIF is under development. External methodological review, multicentre application, cross-platform assessment, and prospective evaluation are required before stronger claims about validity or transferability can be made.
