"""Synthetic executive context for the Chief of Staff demonstration.

Everything in this module is fictional, including individual names, titles, and roles.

Dates use offsets from ``today`` so the model always covers three weeks of history and two weeks of forward plans.
"""

from datetime import timedelta


PARTICIPANTS = {
    "p01": {"name": "Alex Morgan", "role": "Chief Technology Officer"},
    "p02": {"name": "Jordan Lee", "role": "Senior Technology Manager"},
    "p03": {"name": "Riley Chen", "role": "Finance Manager"},
    "p04": {"name": "Morgan Patel", "role": "Clinical Operations Manager"},
    "p05": {"name": "Casey Williams", "role": "Enterprise architect"},
    "p06": {"name": "Taylor Brooks", "role": "Program director"},
    "p07": {"name": "Avery Johnson", "role": "Enterprise Security and privacy Manager"},
}

INITIATIVES = {
    "init01": {"name": "Clinical Operations Modernization", "owner": "p06", "status": "Proposed phase-one pilot", "objective": "Reduce manual reporting and improve decision latency.", "charter_id": "charter01"},
    "init02": {"name": "Agentification Pilot", "owner": "p02", "status": "Concept validation", "objective": "Test source-linked preparation of executive meeting briefs.", "charter_id": "charter02"},
}

CHARTERS = {
    "charter01": {"title": "Clinical Operations Modernization Phase 1 Charter", "scope": "One operational domain, approved data, and a 90-day value review.", "out_of_scope": "Enterprise rollout, autonomous decisions, and unapproved clinical data.", "success_measures": ["Preparation time", "Accuracy", "Adoption", "Documented value"]},
    "charter02": {"title": "Executive Decision Intelligence Concept Charter", "scope": "Meeting preparation from curated demonstration documents with human review.", "out_of_scope": "Production integrations, autonomous actions, and institutional deployment.", "success_measures": ["Factual accuracy", "Source traceability", "Executive usefulness", "Time saved"]},
}

DELIVERABLES = {
    "del01": {"name": "Phase-one cost and dependency model", "initiative_id": "init01", "owner": "p03", "due_offset": 3, "status": "In progress"},
    "del02": {"name": "Integration and security readiness assessment", "initiative_id": "init01", "owner": "p05", "due_offset": 7, "status": "Not started"},
    "del03": {"name": "Executive meeting brief", "initiative_id": "init02", "owner": "p02", "due_offset": -2, "status": "Draft complete"},
    "del04": {"name": "Concept validation findings", "initiative_id": "init02", "owner": "p06", "due_offset": 12, "status": "Planned"},
}

MEETING_EVENTS = {
    -21: {"id": "m01", "title": "Monthly Business Review", "participants": ["p01", "p02", "p03", "p06"], "initiative_ids": ["init01", "init02"], "summary": "Leadership requested clearer benefit measures before new commitments."},
    -18: {"id": "m02", "title": "Analytics Discovery Session", "participants": ["p02", "p04", "p05", "p06"], "initiative_ids": ["init01"], "summary": "The team confirmed that reporting delays and inconsistent definitions are the primary problems."},
    -15: {"id": "m03", "title": "Finance and ROI Review", "participants": ["p03", "p04", "p06"], "initiative_ids": ["init01"], "summary": "Finance requested phased funding and a named owner for benefit realization."},
    -12: {"id": "m04", "title": "Executive Decision Support Workshop", "participants": ["p01", "p02", "p06"], "initiative_ids": ["init02"], "summary": "Participants selected executive meeting preparation as the first skill to demonstrate."},
    -9: {"id": "m05", "title": "Enterprise Architecture and Risk Review", "participants": ["p02", "p05", "p07"], "initiative_ids": ["init01", "init02"], "summary": "The review identified identity, access, retention, traceability, and human review as required controls."},
    -6: {"id": "m06", "title": "Agentification Prototype Content Review", "participants": ["p02", "p06", "p07"], "initiative_ids": ["init02"], "summary": "The group asked that current functionality be clearly separated from future capabilities."},
    -3: {"id": "m07", "title": "Technology Investment Review", "participants": ["p02", "p03", "p04", "p06"], "initiative_ids": ["init01"], "summary": "The estimate was incomplete without integration, support, and change-management costs."},
    0: {"id": "m08", "title": "Executive Technology Investment Review", "participants": ["p01", "p02", "p03", "p04", "p05"], "initiative_ids": ["init01"], "summary": "Today: determine whether evidence supports a limited phase-one investment and define funding conditions."},
    2: {"id": "m09", "title": "Executive Brief Prototype Demonstration", "participants": ["p01", "p02", "p06"], "initiative_ids": ["init02"], "summary": "Demonstrate the meeting-preparation skill and collect feedback on usefulness and missing context."},
    5: {"id": "m10", "title": "Security and Data Handling Working Session", "participants": ["p02", "p05", "p07"], "initiative_ids": ["init01", "init02"], "summary": "Document controls required before any institutional connection."},
    8: {"id": "m11", "title": "Phase-One Charter Review", "participants": ["p01", "p03", "p04", "p06"], "initiative_ids": ["init01"], "summary": "Review the revised charter, cost model, owners, and release criteria."},
    12: {"id": "m12", "title": "Agentification Concept Validation Readout", "participants": ["p01", "p02", "p06", "p07"], "initiative_ids": ["init02"], "summary": "Review feedback and decide whether a formal requirements package should be developed."},
    14: {"id": "m13", "title": "Biweekly Portfolio Review Governance", "participants": ["p01", "p02", "p03", "p04", "p06"], "initiative_ids": ["init01", "init02"], "summary": "Reconcile decisions, dependencies, resources, and next-stage recommendations."},
}

DECISIONS = [
    {"id": "dec01", "meeting_id": "m01", "initiative_id": "init01", "offset": -21, "decision": "Do not request full program funding until phase-one outcomes and ownership are defined."},
    {"id": "dec02", "meeting_id": "m03", "initiative_id": "init01", "offset": -15, "decision": "Use a two-phase funding model with a value checkpoint before phase two."},
    {"id": "dec03", "meeting_id": "m04", "initiative_id": "init02", "offset": -12, "decision": "Demonstrate executive meeting preparation as the first Chief of Staff skill."},
    {"id": "dec04", "meeting_id": "m05", "initiative_id": "init02", "offset": -9, "decision": "Use synthetic data only and require human review for the demonstration."},
    {"id": "dec05", "meeting_id": "m06", "initiative_id": "init02", "offset": -6, "decision": "Present other Chief of Staff skills as future possibilities, not active capabilities."},
]

ACTIONS = [
    {"id": "act01", "source_meeting_id": "m03", "initiative_id": "init01", "owner": "p03", "due_offset": 3, "status": "In progress", "action": "Complete the phase-one cost and dependency model.", "review_meeting_id": "m11"},
    {"id": "act02", "source_meeting_id": "m05", "initiative_id": "init01", "owner": "p05", "due_offset": 7, "status": "Not started", "action": "Document integration, identity, security, and support dependencies.", "review_meeting_id": "m11"},
    {"id": "act03", "source_meeting_id": "m06", "initiative_id": "init02", "owner": "p02", "due_offset": -2, "status": "Complete", "action": "Revise the prototype so its skill and boundaries are immediately clear.", "review_meeting_id": "m09"},
    {"id": "act04", "source_meeting_id": "m06", "initiative_id": "init02", "owner": "p06", "due_offset": 12, "status": "Planned", "action": "Capture validation feedback and recommend whether to develop requirements.", "review_meeting_id": "m12"},
]


def build_synthetic_context(today):
    """Return the complete, dated five-week synthetic context."""
    calendar = [{"offset": offset, "date": today + timedelta(days=offset), "meeting": MEETING_EVENTS.get(offset)} for offset in range(-21, 15)]
    meetings = {event["id"]: {**event, "date": today + timedelta(days=offset), "offset": offset} for offset, event in MEETING_EVENTS.items()}
    decisions = [{**item, "date": today + timedelta(days=item["offset"])} for item in DECISIONS]
    actions = [{**item, "due_date": today + timedelta(days=item["due_offset"])} for item in ACTIONS]
    deliverables = {key: {**item, "due_date": today + timedelta(days=item["due_offset"])} for key, item in DELIVERABLES.items()}
    return {"today": today, "calendar": calendar, "meetings": meetings, "participants": PARTICIPANTS, "initiatives": INITIATIVES, "charters": CHARTERS, "deliverables": deliverables, "decisions": decisions, "actions": actions}


def today_continuity(context):
    """Return the operating history and forward dependencies relevant today."""
    today = context["today"]
    recent = sorted((d for d in context["decisions"] if d["date"] <= today), key=lambda x: x["date"], reverse=True)[:4]
    actions = sorted((a for a in context["actions"] if a["status"] != "Complete" and a["due_date"] >= today), key=lambda x: x["due_date"])
    meetings = sorted((m for m in context["meetings"].values() if m["date"] > today), key=lambda x: x["date"])[:5]
    return {"recent_decisions": recent, "open_actions": actions, "upcoming_meetings": meetings}
