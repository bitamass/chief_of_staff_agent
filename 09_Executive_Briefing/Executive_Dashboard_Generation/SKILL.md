# Skill: Executive Dashboard Generation

## Purpose

This skill designs and generates an executive dashboard that converts approved strategic, operational, financial, initiative, risk, decision, and action data into a concise decision-support view.

It helps executives understand:

- Whether strategic objectives and major initiatives are on track.
- What materially changed.
- Which outcomes, milestones, risks, issues, and commitments require attention.
- What decisions or interventions are needed.
- Whether the underlying data is current, consistent, and reliable.
- Where additional detail can be reviewed.

The skill emphasizes decision relevance, exception visibility, and traceability. It does not replace systems of record, financial reporting, compliance reporting, clinical oversight, formal governance, or human validation.

## Core design principles

### Decision-first design

Every dashboard element must support a specific executive question or decision.

Examples:

- Are major priorities on track?
- What changed since the last review?
- Where is intervention required?
- Which decisions are approaching?
- Which risks exceed tolerance?
- Are expected benefits being realized?

Do not include a metric solely because data is available.

### Exception-oriented presentation

Executives should be able to identify:

- Material variance.
- Worsening trends.
- Missed commitments.
- Risks above tolerance.
- Critical issues.
- Pending decisions.
- Stale or unreliable data.

Routine detail should remain available through drill-down rather than dominating the main dashboard.

### Clear hierarchy

A typical hierarchy is:

1. Executive summary.
2. KPI and strategic-priority status.
3. Initiative or portfolio performance.
4. Risk, issue, decision, and action exceptions.
5. Forward look.
6. Supporting detail and sources.

### Traceability

Every material measure or conclusion should connect to:

- A definition.
- A calculation.
- A source.
- An owner.
- A reporting period.
- A last-updated date.
- Supporting records.

## Core activities

### 1. Define the dashboard decision model

Confirm:

- Executive audience.
- Decisions and oversight responsibilities.
- Required scope.
- Reporting cadence.
- Critical thresholds.
- Necessary detail.
- Distribution and access requirements.

Translate each executive question into a required metric, status, exception, or analysis.

### 2. Select decision-relevant metrics

A metric should be included when it:

- Measures an important outcome.
- Indicates progress toward an objective.
- Provides early warning.
- Supports a recurring decision.
- Reveals a material exception.
- Measures an obligation or commitment.

Avoid:

- Vanity metrics.
- Duplicative metrics.
- Metrics without owners.
- Metrics without defined targets.
- Activity measures presented as outcomes.
- Measures that cannot be explained or verified.

### 3. Validate metric definitions

For every metric:

- Confirm the business definition.
- Confirm the formula.
- Confirm the source and owner.
- Confirm the reporting period.
- Confirm target and thresholds.
- Confirm the favorable direction.
- Confirm exclusions.
- Confirm refresh timing.

Do not combine values with inconsistent definitions, populations, or periods.

### 4. Evaluate data quality

Assess:

- Accuracy.
- Completeness.
- Timeliness.
- Consistency.
- Reconciliation.
- Lineage.
- Access authorization.
- Manual adjustment.
- Confidence.

If data is stale, missing, or unreliable, display the limitation instead of implying precision.

### 5. Calculate status

Use approved status logic.

When approved logic is unavailable:

- Do not invent institutional thresholds silently.
- Clearly label demonstration logic.
- Show the underlying value, target, and variance.
- Flag the status for owner confirmation.

Overall status should not be a simple mathematical average of unrelated measures. A material exception may determine executive status when its consequence warrants it.

### 6. Analyze trends and variance

For each important measure:

- Compare current value with target.
- Compare with previous period.
- Compare with baseline.
- Evaluate forecast.
- Identify direction and rate of change.
- Explain material variance.
- Identify required corrective action.

Do not use a trend arrow without defining the comparison period.

### 7. Connect performance with management context

Relate metrics to:

- Initiatives.
- Deliverables.
- Decisions.
- Actions and commitments.
- Risks and issues.
- Resources.
- Stakeholders.
- Governance milestones.

This allows executives to understand not only what changed, but why and what action may be needed.

### 8. Design visual hierarchy

Use the simplest visual appropriate to the information:

- KPI card for a single measure.
- Line chart for trend.
- Bar chart for comparison.
- Table for exact values and ownership.
- Milestone view for schedule.
- Risk matrix for probability and impact.
- Exception list for leadership attention.

Avoid:

- Decorative visuals.
- Excessive colors.
- Three-dimensional charts.
- Gauges without meaningful thresholds.
- Too many charts on one page.
- Color as the only status signal.
- Small text or overcrowded labels.

### 9. Apply status and color consistently

Use:

- Neutral colors for ordinary information.
- Limited accent colors for status.
- Text labels or icons in addition to color.
- Consistent status definitions throughout.
- Accessible contrast.

Do not rely solely on red, yellow, and green because of accessibility and interpretation limitations.

### 10. Provide drill-down and explanation

Executives should be able to review:

- Metric definitions.
- Supporting trends.
- Underlying initiatives.
- Related decisions and actions.
- Risks and issues.
- Data sources.
- Owner commentary.
- Data limitations.

The summary must remain understandable without requiring drill-down.

### 11. Prepare the forward view

Show:

- Upcoming decisions.
- Milestones.
- Actions.
- Governance reviews.
- Risks approaching thresholds.
- Expected metric changes.
- Required executive participation.

### 12. Validate with the audience

Before official use:

- Confirm the dashboard answers executive questions.
- Remove unused metrics.
- Confirm terminology.
- Confirm status logic.
- Validate source data.
- Test accessibility and readability.
- Confirm the required refresh process.
- Confirm ownership for maintenance.

## Decision rules

- Include only decision-relevant measures.
- Assign an owner to every displayed metric.
- Show target, period, source, and freshness.
- Distinguish outcome measures from activity measures.
- Distinguish current values from forecasts.
- Distinguish actual performance from owner commentary.
- Do not average unrelated statuses automatically.
- Do not hide material exceptions in aggregate views.
- Do not use color without labels.
- Do not imply precision when data quality is weak.
- Do not compare inconsistent populations, definitions, or periods.
- Show material changes from the previous reporting period.
- Preserve access controls and audience restrictions.

## Quality standards

A strong executive dashboard must be:

- Decision-relevant.
- Concise.
- Exception-oriented.
- Current.
- Comparable.
- Traceable.
- Accessible.
- Consistent.
- Confidence-aware.
- Actionable.

An executive should be able to understand the current state, material change, required decision, and next milestone within a few minutes.

## Safeguards and limitations

- Do not fabricate metrics, targets, formulas, status, forecasts, or source data.
- Do not create official financial, clinical, regulatory, audit, or compliance reporting without authorized review.
- Do not expose restricted information to unauthorized audiences.
- Do not change source records.
- Do not hide missing or unfavorable data.
- Do not present provisional thresholds as approved institutional standards.
- Do not publish or distribute automatically.
- Flag stale, conflicting, incomplete, or manually adjusted data.
- Require human validation before consequential use.

## Human role

The executive sponsor, business owner, metric owner, data steward, analyst, communication or design partner, and specialized reviewer must:

- Confirm executive questions.
- Approve metric selection.
- Validate definitions and calculations.
- Confirm targets and thresholds.
- Review data quality.
- Approve status and commentary.
- Validate access and confidentiality.
- Approve the dashboard before distribution.
- Maintain and review it as needs change.
