# CPIF Analytical Layers

## Layer 1 — Communication Context

Define the communication initiative before analysing metrics.

Required elements:

- communication objective;
- intended audience;
- platform and account characteristics;
- publication period and frequency;
- content themes and formats;
- organic or paid distribution;
- institutional and territorial context;
- relevant comparability constraints.

Output: a written context statement and explicit analytical questions.

## Layer 2 — Platform-recorded Metrics

Classify each metric by the observable communication process it represents.

Recommended classes:

- exposure metrics: reach, views, impressions;
- interaction metrics: likes, comments, shares, saves;
- audience-growth metrics: follows or subscriptions;
- derived metrics: interaction rates, reach-normalised rates, or other clearly defined ratios.

Output: a metric dictionary with definitions, units, denominators, and interpretive limits.

## Layer 3 — Metric Preparation and Standardisation

Prepare the dataset for reproducible analysis.

Tasks may include:

- data-type validation;
- missing-value assessment;
- duplicate detection;
- category harmonisation;
- metric range checks;
- derived-variable calculation;
- outlier documentation;
- reproducible audit trail.

Repository mapping: `03_audit_analytical_variables.py`.

Output: an audited analytical dataset and data-quality report.

## Layer 4 — Statistical Integration

Select statistical procedures according to the research question, data distribution, sample structure, and metric properties.

Repository mapping:

- `04_compare_projects.py` — project comparisons;
- `05_compare_post_formats.py` — global format comparisons;
- `06_stratified_format_analysis.py` — stratified analyses;
- `07_analyze_reach_normalized_rates.py` — normalised indicators;
- `08_spearman_correlations.py` — association structure;
- `09_outlier_sensitivity_analysis.py` — robustness assessment;
- `10_generate_figures.py` — visual integration.

Output: descriptive statistics, inferential tests, effect sizes, multiplicity adjustments, sensitivity analyses, and figures.

## Layer 5 — Communication-performance Interpretation

Interpret statistics according to metric class, context, effect magnitude, uncertainty, and observational limits.

Output: evidence statements that distinguish:

- statistical difference from practical relevance;
- exposure from interaction;
- interaction from communication outcomes;
- association from causation;
- platform-recorded behaviour from audience meaning.

## Layer 6 — Evidence-informed Decision Support

Translate findings into proportionate recommendations.

Decisions should specify:

- what should be maintained;
- what may be tested or adapted;
- which metrics require continued monitoring;
- which additional qualitative or outcome measures are needed;
- what cannot be concluded from the available evidence.

Output: an action-oriented decision table with evidence strength and limitations.
