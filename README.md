# Instagram Science Communication in Curricularized University Extension

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21302521.svg)](https://doi.org/10.5281/zenodo.21302521)

This repository contains the anonymized data, reproducible analysis scripts,
tables, and figures supporting a study of Instagram-based science communication
in two curricularized university extension projects in Brazil.

## Research objective

The study evaluates the performance of digital science communication developed
within two university extension projects. It compares reach and engagement
indicators across projects and post formats and examines associations among
performance indicators.

The Instagram indicators assess the communication dimension of the extension
initiatives. They do not, by themselves, constitute a comprehensive evaluation
of dialogical interaction, student learning, social transformation, or causal
extension impact.

## Study design

- Observational, retrospective, quantitative study
- Unit of analysis: one Instagram post
- Study period: April to July 2026
- Total sample: 187 posts
- Ocean Culture: 93 posts
- PsicoCampus: 94 posts
- Post formats: image, carousel, and Reel

## Repository structure

```text
data/public/     Anonymized post-level dataset
docs/            Analysis plan and data dictionary
outputs/tables/  Reproducible statistical tables
outputs/figures/ Publication-ready figures
scripts/         Data preparation, analysis, and figure scripts
```

Raw platform exports and the identifiable processed dataset are excluded from
version control. They contain account names, usernames, post identifiers,
permanent links, descriptions, and exact publication timestamps.

## Public dataset

The file `data/public/instagram_posts_anonymized.csv` contains 187 anonymous
records. Direct platform identifiers and text fields were removed. Exact
timestamps were reduced to publication month.

Two reach values and two follow values are missing in the same two Ocean
Culture posts. Missing values were retained and were not replaced with zero.

## Main analytical approach

- Median and interquartile range as primary descriptive summaries
- Mann-Whitney U tests for comparisons between projects
- Kruskal-Wallis tests and Holm-adjusted post-hoc comparisons for post formats
- Project-stratified format analyses because format distribution was unbalanced
- Rank-biserial correlations as effect sizes
- Spearman correlations with Holm adjustment
- Reach-normalized interaction measures
- Sensitivity analyses excluding project-specific upper-extreme observations

All tests are two-sided. Multiplicity is controlled with the Holm method.

## Reproducing the analysis

Python 3.11 or newer is recommended.

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Run the public-data analyses in order:

```powershell
python scripts\03_audit_analytical_variables.py
python scripts\04_compare_projects.py
python scripts\05_compare_post_formats.py
python scripts\06_stratified_format_analysis.py
python scripts\07_analyze_reach_normalized_rates.py
python scripts\08_spearman_correlations.py
python scripts\09_outlier_sensitivity_analysis.py
python scripts\10_generate_figures.py
```

Scripts `01_audit_raw_data.py`, `02_prepare_data.py`, and
`11_create_public_dataset.py` document the private-to-public preparation
workflow but require the restricted raw platform exports.

## Interpretation boundary

The results support conclusions about observed communication performance.
They should not be interpreted as proof that Instagram caused engagement or as
a complete evaluation of university extension effectiveness under Brazilian
education regulations.

## Authors

- Luciano Rapagnã (corresponding author)
- Jaqueline Pereira de Azeredo Rapagnã
- Flaviane Melo de Anchieta
- Marcus Vinícius Gomes de Oliveira
- Gustavo Borges de Oliveira

Correspondence: lucianorapagna@id.uff.br

## Affiliations

1. Curso de Pedagogia, Universidade de Vassouras, Saquarema, RJ, Brazil
2. Observatório Oceanográfico, Universidade Federal Fluminense, Niterói, RJ, Brazil
3. Secretaria Municipal de Educação, Ciência, Tecnologia, Esporte e Lazer, Arraial do Cabo, RJ, Brazil
4. Programa de Pós-graduação em Dinâmica dos Oceanos e da Terra, Universidade Federal Fluminense, Niterói, RJ, Brazil
5. UNILAGOS – Faculdade União Araruama de Ensino, Curso de Medicina, Araruama, RJ, Brazil

## Licenses

Analysis code is released under the MIT License. The anonymized dataset and
documentation are released under the Creative Commons Attribution 4.0
International License (CC BY 4.0). See `LICENSE` and `DATA_LICENSE.md`.

## Citation

Citation metadata are provided in `CITATION.cff`. Version 1.0.0 is permanently
archived at https://doi.org/10.5281/zenodo.21302521.
