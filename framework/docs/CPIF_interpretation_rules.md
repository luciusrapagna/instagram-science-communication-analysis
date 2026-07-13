# CPIF interpretation rules
The Communication Performance Interpretation Framework (CPIF) establishes the following minimum safeguards for the interpretation of platform-recorded communication metrics.

These rules define minimum safeguards for a CPIF-aligned analysis. A deviation may be methodologically defensible, but it must be explicit and justified.

1. **Do not interpret a single metric as global communication performance.** Report the dimension represented and examine complementary evidence.
2. **Separate communication exposure from communication interaction.** Do not label visibility counts as engagement or combine exposure and interaction without retaining their distinct meanings.
3. **Use normalized indicators only with valid denominators.** State the numerator, denominator, multiplier, missing-value treatment, and conceptual meaning. Do not calculate a rate when the denominator is zero, structurally missing, or not comparable. When the numerator counts repeatable events and the denominator counts accounts, report the indicator as events per denominator unit rather than as a percentage or proportion of users; values may exceed 100 per 100 accounts.
4. **State whether metrics count events, content items, accounts, estimated unique users, or another unit.** Repeated events and unique users must not be treated as equivalent.
5. **Do not interpret correlation as causality.** Associations between exposure and interaction do not establish that exposure caused the action or that either caused effectiveness.
6. **Consider cumulative exposure time.** Record publication dates, extraction date, observation window, and unequal time-at-risk where available; qualify comparisons when exposure durations differ.
7. **Consider clustering and dependence.** Posts may be nested within projects, campaigns, series, accounts, or time periods, and repeated observations may violate independence assumptions.
8. **Consider imbalance between formats and projects.** Report group sizes and avoid attributing compositional differences to format effects without appropriate stratification, adjustment, or qualification.
9. **Report effect magnitude and uncertainty, not only p-values.** Use effect sizes and confidence intervals when supported; where intervals are not estimable, state the limitation and provide distributional context.
10. **Control multiplicity when the inferential family warrants it.** Define the family, correction method, and distinction between confirmatory and exploratory analyses.
11. **Distinguish communication performance from communication effectiveness.** Platform-recorded exposure and interaction are not direct measures of learning, trust, literacy, behavioural change, participation, or societal impact.
12. **Limit generalization to the available design.** Identify the sampled accounts, projects, period, platform, content, and audience context; do not use causal language for observational comparisons.
13. **Record platform-specific definitions and classification decisions.** Preserve the definition source or dashboard wording, extraction date, interface or API route, attribution window, known definition changes, and justified primary and secondary analytical roles. Similar labels across platforms are not assumed equivalent.
14. **Preserve data, code, and documentation.** Maintain versioned scripts, data dictionaries, analysis decisions, figure-generation code, and validation reports, subject to privacy, ethics, platform terms, and licensing.
15. **Treat robustness as evidence about stability, not proof of truth.** State what each sensitivity analysis changes and which conclusions remain or do not remain supported.
16. **Avoid arbitrary cut-offs and universal benchmarks.** Thresholds require an explicit empirical or decision-theoretic basis in the relevant context.
17. **Keep composite totals transparent.** If total interactions are used, list components and avoid implicit weighting claims.
18. **Document deviations and ambiguity.** When a platform definition, denominator, or time window cannot be verified, retain the uncertainty in the interpretation rather than inventing precision.
