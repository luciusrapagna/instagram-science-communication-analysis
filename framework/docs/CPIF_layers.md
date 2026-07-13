# CPIF layers

The Communication Performance Interpretation Framework is organized into six connected layers. The layers define an auditable analytical sequence rather than a universal scoring system. Decisions and uncertainties identified in later layers may require researchers to revisit earlier layers.

## Layer 1 — Communication Context

### Purpose

To document the conditions under which the communication initiative was designed, implemented, and observed, providing the contextual basis required for interpretation.

### Inputs

- Type and scope of the communication initiative
- Communication objectives
- Intended and observed audiences, when available
- Institution and participating projects
- Digital platform
- Observation period and extraction date
- Editorial calendar and publication practices
- Paid, boosted, or organic distribution
- Relevant institutional, temporal, and platform conditions

### Processes

Researchers define the unit of analysis, describe the communication setting, record the observation window, identify contextual differences between groups, and document factors that may influence exposure or interaction.

### Outputs

- Structured communication-context record
- Definition of the analytical scope
- Identification of relevant contextual strata
- List of potential contextual limitations and sources of non-comparability

### Methodological decisions

Researchers must decide which contextual variables are necessary for the research questions, whether comparisons require stratification or adjustment, and how cumulative exposure time and promotional conditions will be represented.

### Interpretation risks

Incomplete context may lead to inappropriate comparisons, attribution of contextual differences to content characteristics, or generalization beyond the observed projects, audiences, periods, and platform conditions.

### Minimum reporting requirements

Report the initiative, objectives, audience, institution, platform, observation period, extraction date, unit of analysis, editorial conditions, promotion status, cumulative exposure considerations, and relevant contextual differences between analytical groups.

### Application to the current study

The initial application includes 187 Instagram publications from Ocean Culture and PsicoCampus, two curricular university extension projects. The study records project membership, post format, publication period, and available platform context. Comparisons are interpreted within the observed projects and period, without assuming that their audience or editorial conditions are equivalent.
## Layer 2 — Platform-Recorded Metrics

### Purpose

To identify, define, and classify the metrics recorded by the digital platform according to the communication processes they represent.

### Inputs

- Raw platform-exported variables
- Platform documentation and dashboard definitions
- Metric extraction date
- Counting units and accumulation rules
- Information about unique users, accounts, events, or repeated actions
- Known changes in metric definitions or platform interfaces

### Processes

Each metric is assigned an operational definition and a justified primary analytical role. Secondary roles may be recorded when a metric plausibly represents more than one process:

- Exposure
- Interaction
- Audience growth
- Content consumption
- Navigation or click behaviour
- Other platform-specific indicators

The primary analytical role of each metric should be explicit. When a metric may represent more than one process, any secondary role, ambiguity, attribution window, and classification decision must be documented.

### Outputs

- Metric dictionary with operational definitions
- Classification of metrics by communication process
- Identification of raw and derived variables
- Record of counting units and platform-specific limitations
- List of metrics that are unavailable, ambiguous, or non-comparable

### Methodological decisions

Researchers must decide which metrics are relevant to the communication objectives, how each metric will be classified, whether it counts events or unique accounts, and whether similarly named metrics are comparable across content formats, periods, accounts, or platforms.

### Interpretation risks

Metric labels may conceal different counting rules. Repeated events may be mistaken for unique users, estimated reach may be treated as an exact count, and metrics from different platforms or definition periods may be interpreted as equivalent without sufficient evidence.

### Minimum reporting requirements

Report the platform-specific name, operational definition, communication-process classification, counting unit, extraction date, data source, known definition changes, and whether each variable is raw or derived.

### Application to the current study

In the initial Instagram application, views and reach are classified as exposure metrics. Likes, comments, shares, and saves are retained as distinct interaction metrics. Follows are retained as recorded actions and assigned a primary classification according to the study definition, while their potential audience-growth role and attribution window remain explicit. Total interactions is documented as a derived variable rather than an independent platform construct. Any ambiguity in counting units or metric definitions must remain explicit in the interpretation.

## Layer 3 — Metric Preparation and Standardization

### Purpose

To transform platform-recorded metrics into transparent, valid, and comparable analytical outcomes while preserving the meaning and provenance of the original data.

### Inputs

- Raw platform-recorded metrics
- Metric dictionary produced in Layer 2
- Content identifiers and publication dates
- Project, account, campaign, or institutional identifiers
- Content-format classifications
- Observation and extraction dates
- Missing-value indicators
- Candidate numerators and denominators for normalized indicators

### Processes

Metric preparation may include:

- Auditing and cleaning the data
- Identifying duplicates, impossible values, and inconsistent records
- Assessing missingness and distinguishing missing values from true zeros
- Confirming operational definitions
- Classifying content formats
- Evaluating comparability across groups and periods
- Preserving raw variables before deriving new indicators
- Calculating normalized indicators only with valid denominators
- Documenting cumulative exposure time
- Defining comparable analytical outcomes

### Outputs

- Audited analytical dataset
- Reproducible data-preparation record
- Missing-data summary
- Documented content-format classification
- Raw and normalized analytical variables
- List of exclusions, transformations, and comparability limitations

### Methodological decisions

Researchers must decide how missing values and zeros will be distinguished, which observations are comparable, whether transformations are necessary, which denominators represent valid opportunities for interaction, and how unequal cumulative exposure time will be handled or reported.

### Interpretation risks

Invalid denominators may produce misleading rates. Missing values may be incorrectly converted to zeros, cumulative metrics may be compared across unequal observation periods, and normalized indicators may create an appearance of comparability that is not supported by the underlying data.

### Minimum reporting requirements

Report all cleaning rules, exclusions, missing-data decisions, variable transformations, content-format definitions, numerator and denominator definitions, normalization multipliers, handling of zero denominators, cumulative exposure considerations, and procedures used to preserve the raw data.

### Application to the current study

The initial application preserves the platform-recorded metrics and derives total interactions, interactions per 100 accounts reached, and likes per 100 accounts reached. Reach-normalized indicators are calculated only when the reach denominator is valid. They quantify recorded action events per 100 accounts reached, are not interpreted as percentages or proportions of users, and may exceed 100 when multiple events per account are possible. Project and post-format classifications are retained for stratified analyses, and data preparation is documented without modifying the original source data.

## Layer 4 — Statistical Integration

### Purpose

To integrate descriptive and inferential evidence using statistical methods appropriate to the study design, data distribution, sampling structure, dependence between observations, and research questions.

### Inputs

- Audited raw and normalized analytical outcomes
- Research questions, estimands or descriptive targets, and analysis plan
- Group and stratification variables
- Sample sizes and distributional characteristics
- Information about clustering or repeated observations
- Prespecified inferential families
- Candidate sensitivity and robustness specifications

### Processes

Statistical integration may include:

- Descriptive statistics and distributional summaries
- Stratified comparisons
- Parametric or non-parametric tests
- Effect sizes and confidence intervals
- Multiplicity correction
- Correlation or other association analyses
- Sensitivity analyses
- Robustness assessment

CPIF does not prescribe a fixed set of tests. Methods must be selected according to the study design, distribution of the data, sample structure, number of groups, dependence between observations, and research questions.

### Outputs

- Descriptive and comparative statistical results
- Effect-size and uncertainty estimates, when supported
- Multiplicity-adjusted inferences, when required
- Association estimates
- Sensitivity and robustness findings
- Explicit record of assumptions, analytical families, and limitations

### Methodological decisions

Researchers must define each estimand or descriptive target, select methods that match the scale and distribution of each outcome, determine whether observations can be treated as independent, define inferential families for multiplicity control, choose effect-size and uncertainty measures, and specify sensitivity analyses that address plausible analytical vulnerabilities.

### Interpretation risks

Inappropriate tests, ignored dependence, selective reporting, small or imbalanced groups, multiple uncorrected comparisons, and reliance on p-values alone may produce misleading conclusions. Associations must not be interpreted as causal effects.

### Minimum reporting requirements

Report the analytical rationale, estimands or descriptive targets, statistical methods, assumptions, group sizes, effect-size definitions, uncertainty intervals for inferential claims or a justification for their omission, multiplicity procedures, association measures, sensitivity analyses, software and versions, and any deviations from the analysis plan.

### Application to the current study

The initial Instagram application combines descriptive statistics with project and post-format comparisons, project-stratified analyses, rank-biserial effect sizes, Holm correction, Spearman correlations, and sensitivity analysis. These methods support a context-sensitive empirical demonstration but do not establish causality or definitive validation of CPIF.
## Layer 5 — Communication-Performance Interpretation

### Purpose

To integrate the analytical evidence into a multidimensional, context-sensitive interpretation of communication performance without producing a universal score.

### Inputs

- Communication context from Layer 1
- Metric definitions and classifications from Layer 2
- Raw and normalized outcomes from Layer 3
- Descriptive and inferential results from Layer 4
- Effect sizes and uncertainty estimates
- Association analyses
- Sensitivity and robustness findings
- Institutional, editorial, temporal, and platform limitations

### Processes

Interpretation integrates:

- Communication exposure
- Communication interaction
- Normalized indicators
- Effect magnitude
- Statistical uncertainty
- Associations between metrics
- Sensitivity and robustness
- Institutional context
- Editorial context
- Platform context

Convergent, divergent, and uncertain findings are described as a communication-performance profile. No single metric or arbitrary composite is treated as global performance.

### Outputs

- Contextualized communication-performance interpretation
- Identification of dimensions with different observed patterns
- Statement of the strength, uncertainty, and robustness of the evidence
- Explicit separation between performance and effectiveness
- Bounded conclusions and unresolved questions

### Methodological decisions

Researchers must decide how evidence from different dimensions will be integrated, how conflicting or uncertain findings will be represented, which contextual factors materially limit interpretation, and which conclusions are supported by the available design.

### Interpretation risks

Selective emphasis on favourable metrics, reliance on statistical significance alone, concealment of divergent dimensions, overgeneralization, causal language, and interpretation of platform traces as direct evidence of effectiveness may produce unsupported conclusions.

### Minimum reporting requirements

Report exposure and interaction separately, describe normalized indicators and their denominators, present effect magnitude and uncertainty, summarize relevant associations and robustness findings, identify contextual constraints, distinguish performance from effectiveness, and state the limits of generalization.

### Application to the current study

The initial Instagram application integrates views and reach with raw and reach-normalized interaction indicators, project and post-format comparisons, effect sizes, multiplicity-adjusted evidence, correlations, and sensitivity analyses. The result is interpreted as a contextual communication-performance profile for the observed projects and period, not as a universal ranking, causal effect, or measure of communication effectiveness.
## Layer 6 — Evidence-Informed Decision Support

### Purpose

To translate the contextualized interpretation into transparent, proportionate decisions, hypotheses, and future research priorities without exceeding the evidential limits of the study.

### Inputs

- Communication-performance interpretation from Layer 5
- Communication objectives and institutional priorities
- Dimensions with distinct or uncertain performance patterns
- Evidence magnitude, uncertainty, and robustness
- Editorial and operational constraints
- Limitations and unresolved questions
- Stakeholder information needs

### Processes

Evidence-informed decision support may include:

- Reviewing editorial planning
- Selecting formats for further testing
- Monitoring communication projects over time
- Identifying dimensions with distinct performance patterns
- Formulating new hypotheses
- Improving future data collection
- Designing longitudinal, experimental, qualitative, or mixed-method studies
- Identifying outcomes that require direct effectiveness measurement

Decisions should be documented as context-bound responses to the available evidence, not as universal prescriptions.

### Outputs

- Evidence-informed editorial options
- Monitoring priorities and indicators
- Testable hypotheses
- Recommendations for improved data collection
- Design proposals for future studies
- Explicit record of evidence limitations and decision uncertainty

### Methodological decisions

Researchers and stakeholders must decide which findings are sufficiently robust and relevant to inform action, which decisions require additional evidence, how competing communication objectives will be balanced, and how subsequent evaluation will be designed.

### Interpretation risks

Weak or uncertain findings may be converted into rigid prescriptions, observational associations may be treated as causal guidance, short-term platform performance may displace broader communication objectives, and optimization for platform metrics may be mistaken for educational or societal effectiveness.

### Minimum reporting requirements

Report the decision or hypothesis supported, the evidence on which it is based, relevant uncertainty and limitations, the institutional and editorial context, the person or group responsible for implementation, and the proposed method and timing for subsequent evaluation.

### Application to the current study

The initial Instagram application may inform editorial reflection, selection of formats for further testing, monitoring priorities, and new research questions for Ocean Culture and PsicoCampus. Any resulting action remains specific to the observed context and should be evaluated prospectively. Direct claims about learning, trust, scientific literacy, behavioural change, or societal impact require additional outcome-specific research.
