# Communication Performance Interpretation Framework (CPIF) v2.0

CPIF is a methodological interpretation framework for the quantitative evaluation of digital science communication initiatives. It is not a predictive model, psychometric instrument, composite score, or causal inference method.

The framework connects communication objectives, platform-recorded metrics, data preparation, statistical evidence, contextual interpretation, and evidence-informed decision support in six iterative analytical layers.

## Six analytical layers

1. Communication Context
2. Platform-recorded Metrics
3. Metric Preparation and Standardisation
4. Statistical Integration
5. Communication-performance Interpretation
6. Evidence-informed Decision Support

## Integration with this repository

The current statistical workflow is mapped as follows:

- Layer 3: `scripts/03_audit_analytical_variables.py`
- Layer 4: `scripts/04_compare_projects.py` through `scripts/09_outlier_sensitivity_analysis.py`
- Visual reporting: `scripts/10_generate_figures.py`
- CPIF orchestration: `framework/scripts/cpif_pipeline.py`
- CPIF validation: `framework/scripts/validate_cpif_structure.py`
- CPIF figure: `framework/scripts/generate_cpif_figure.py`
- Interpretation report: `framework/scripts/cpif_report.py`

## Quick start

```bash
python framework/scripts/validate_cpif_structure.py
python framework/scripts/generate_cpif_figure.py
python framework/scripts/cpif_pipeline.py --dry-run
```

To execute the repository scripts sequentially:

```bash
python framework/scripts/cpif_pipeline.py
```

## Version

CPIF v2.0.0 — reconstructed and aligned with the current manuscript and reproducible analysis pipeline.
