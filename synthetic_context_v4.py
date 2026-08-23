"""Versioned synthetic context extension used to prevent stale deployment imports.

This module extends the existing synthetic_context module with the two newest
initiatives. Updates are idempotent, so it works with either the older two-
initiative backend or the current four-initiative backend.
"""

import synthetic_context as base


base.PARTICIPANTS.update({
    "p08": {"name": "Cameron Davis", "role": "Clinical Research Director, M.D."},
    "p09": {"name": "Drew Thompson", "role": "Oncologist and Principal Investigator, M.D."},
    "p10": {"name": "Parker Wilson", "role": "Cardiologist and Clinical Researcher, M.D."},
    "p11": {"name": "Quinn Martinez", "role": "Neurologist and Clinical Researcher, M.D."},
    "p12": {"name": "Reese Anderson", "role": "Infectious Disease Physician and Clinical Researcher, M.D."},
})

base.INITIATIVES.update({
    "init03": {"name": "Monthly Business Review", "owner": "p03", "status": "Active monthly operating rhythm", "objective": "Review the medical center's business performance, operating updates, financial outlook, risks, and executive follow-up actions.", "charter_id": "charter03", "participant_ids": ["p01", "p02", "p03", "p04", "p06"]},
    "init04": {"name": "Clinical Research Developments", "owner": "p08", "status": "Requirements discovery", "objective": "Review technology requirements, dependencies, safeguards, and priorities for clinical research conducted in the medical center.", "charter_id": "charter04", "participant_ids": ["p01", "p08", "p09", "p10", "p11", "p12"]},
})

base.CHARTERS.update({
    "charter03": {"title": "Monthly Business Review Charter", "scope": "Monthly medical center business performance, operating updates, financial outlook, material risks, decisions, and accountable follow-up.", "out_of_scope": "Clinical case review, individual personnel matters, and decisions without an accountable executive owner.", "success_measures": ["Timely reporting", "Forecast accuracy", "Decision closure", "Action completion"]},
    "charter04": {"title": "Clinical Research Technology Requirements Charter", "scope": "Technology requirements for approved clinical research, including data, workflow, integration, security, researcher experience, and operational support.", "out_of_scope": "Clinical protocol approval, autonomous clinical decisions, and access to unapproved patient or research data.", "success_measures": ["Requirements coverage", "Researcher validation", "Security readiness", "Delivery feasibility"]},
})

base.DELIVERABLES.update({
    "del05": {"name": "Monthly medical center business performance package", "initiative_id": "init03", "owner": "p03", "due_offset": 3, "status": "In progress"},
    "del06": {"name": "Business review decision and action log", "initiative_id": "init03", "owner": "p06", "due_offset": 9, "status": "Planned"},
    "del07": {"name": "Clinical research technology requirements inventory", "initiative_id": "init04", "owner": "p08", "due_offset": 1, "status": "In progress"},
    "del08": {"name": "Clinical research architecture and feasibility recommendation", "initiative_id": "init04", "owner": "p01", "due_offset": 7, "status": "Planned"},
})

base.MEETING_EVENTS.update({
    -17: {"id": "m22", "title": "Medical Center Monthly Performance Preparation", "participants": ["p02", "p03", "p04", "p06"], "initiative_ids": ["init03"], "summary": "Leaders reviewed preliminary financial, access, workforce, and operating updates and identified material variances requiring executive attention."},
    -16: {"id": "m23", "title": "Clinical Research Technology Intake", "participants": ["p01", "p08", "p09", "p10", "p11", "p12"], "initiative_ids": ["init04"], "summary": "The clinicians described active research workflows, technology pain points, data dependencies, and upcoming study requirements."},
    -10: {"id": "m24", "title": "Monthly Business Variance Review", "participants": ["p01", "p03", "p04", "p06"], "initiative_ids": ["init03"], "summary": "The group reviewed material budget, volume, staffing, and service-performance variances and requested owner-level recovery plans."},
    -8: {"id": "m25", "title": "Clinical Research Workflow and Data Review", "participants": ["p01", "p08", "p09", "p10", "p11", "p12"], "initiative_ids": ["init04"], "summary": "The team mapped research data flows, integration needs, consent boundaries, researcher access, and support requirements."},
    1: {"id": "m26", "title": "Clinical Research Requirements Prioritization", "participants": ["p01", "p08", "p09", "p10", "p11", "p12"], "initiative_ids": ["init04"], "summary": "Prioritize technology requirements by research value, urgency, feasibility, data sensitivity, and cross-study reuse."},
    3: {"id": "m27", "title": "Medical Center Monthly Business Review", "participants": ["p01", "p02", "p03", "p04", "p06"], "initiative_ids": ["init03"], "summary": "Review the monthly business package, confirm explanations for material variances, make operating decisions, and assign accountable follow-up."},
    7: {"id": "m28", "title": "Clinical Research Architecture Recommendation", "participants": ["p01", "p08", "p09", "p10", "p11", "p12"], "initiative_ids": ["init04"], "summary": "Review the proposed architecture, security conditions, delivery dependencies, and phased implementation recommendation."},
    9: {"id": "m29", "title": "Monthly Business Action Closure Review", "participants": ["p02", "p03", "p04", "p06"], "initiative_ids": ["init03"], "summary": "Review completion of actions assigned during the monthly business review and escalate unresolved operating or financial issues."},
})


def _extend_unique(target, records):
    existing_ids = {item["id"] for item in target}
    target.extend(item for item in records if item["id"] not in existing_ids)


_extend_unique(base.DECISIONS, [
    {"id": "dec06", "meeting_id": "m22", "initiative_id": "init03", "offset": -17, "decision": "Use one consolidated monthly package for financial, access, workforce, and operating updates."},
    {"id": "dec07", "meeting_id": "m24", "initiative_id": "init03", "offset": -10, "decision": "Require accountable recovery plans for every material unfavorable variance."},
    {"id": "dec08", "meeting_id": "m23", "initiative_id": "init04", "offset": -16, "decision": "Create a shared requirements inventory before selecting technology solutions for individual studies."},
    {"id": "dec09", "meeting_id": "m25", "initiative_id": "init04", "offset": -8, "decision": "Treat consent, data access, interoperability, and researcher workflow as required architecture inputs."},
])

_extend_unique(base.ACTIONS, [
    {"id": "act05", "source_meeting_id": "m22", "initiative_id": "init03", "owner": "p03", "due_offset": 3, "status": "In progress", "action": "Complete the consolidated monthly business performance package and variance commentary.", "review_meeting_id": "m27"},
    {"id": "act06", "source_meeting_id": "m24", "initiative_id": "init03", "owner": "p06", "due_offset": 9, "status": "Planned", "action": "Maintain the decision and action log and escalate overdue recovery commitments.", "review_meeting_id": "m29"},
    {"id": "act07", "source_meeting_id": "m23", "initiative_id": "init04", "owner": "p08", "due_offset": 1, "status": "In progress", "action": "Consolidate and prioritize technology requirements across the five clinical research areas.", "review_meeting_id": "m26"},
    {"id": "act08", "source_meeting_id": "m25", "initiative_id": "init04", "owner": "p01", "due_offset": 7, "status": "Planned", "action": "Prepare an architecture and feasibility recommendation addressing data, security, integration, and support.", "review_meeting_id": "m28"},
])

_extend_unique(base.UPCOMING_DECISIONS, [
    {"id": "ud07", "meeting_id": "m27", "initiative_id": "init03", "decision": "Confirm the medical center's response to material business variances and assign accountable recovery owners."},
    {"id": "ud08", "meeting_id": "m29", "initiative_id": "init03", "decision": "Close completed business-review actions and escalate commitments requiring executive intervention."},
    {"id": "ud09", "meeting_id": "m26", "initiative_id": "init04", "decision": "Approve the prioritized clinical research technology requirements for architecture assessment."},
    {"id": "ud10", "meeting_id": "m28", "initiative_id": "init04", "decision": "Select the recommended architecture direction and conditions for phased clinical research technology delivery."},
])


DATASET_VERSION = "four-initiatives-v4"
build_synthetic_context = base.build_synthetic_context
build_initiative_scenarios = base.build_initiative_scenarios
build_scenario_records = base.build_scenario_records
initiative_continuity = base.initiative_continuity
