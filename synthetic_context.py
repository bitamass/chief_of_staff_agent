"""Synthetic executive context for the Chief of Staff demonstration.

Everything in this module is fictional, including individual names, titles, and roles.

Dates use offsets from ``today`` so the model always covers three weeks of history and two weeks of forward plans.
"""

from datetime import timedelta


DATASET_VERSION = "four-initiatives-v5"


PARTICIPANTS = {
    "p01": {"name": "Alex Morgan", "role": "Chief Technology Officer"},
    "p02": {"name": "Jordan Lee", "role": "Senior Technology Manager"},
    "p03": {"name": "Riley Chen", "role": "Finance Manager"},
    "p04": {"name": "Morgan Patel", "role": "Clinical Operations Manager"},
    "p05": {"name": "Casey Williams", "role": "Enterprise Architect"},
    "p06": {"name": "Taylor Brooks", "role": "Program Director"},
    "p07": {"name": "Avery Johnson", "role": "Enterprise Security and Privacy Manager"},
    "p08": {"name": "Cameron Davis", "role": "Clinical Research Director, M.D."},
    "p09": {"name": "Drew Thompson", "role": "Oncologist and Principal Investigator, M.D."},
    "p10": {"name": "Parker Wilson", "role": "Cardiologist and Clinical Researcher, M.D."},
    "p11": {"name": "Quinn Martinez", "role": "Neurologist and Clinical Researcher, M.D."},
    "p12": {"name": "Reese Anderson", "role": "Infectious Disease Physician and Clinical Researcher, M.D."},
}

INITIATIVES = {
    "init01": {"name": "Clinical Operations Modernization", "owner": "p06", "status": "Proposed phase-one pilot", "objective": "Reduce manual reporting and improve decision latency.", "charter_id": "charter01", "participant_ids": ["p01", "p02", "p03", "p04", "p05", "p06", "p07"]},
    "init02": {"name": "Agentification Pilot", "owner": "p02", "status": "Concept validation", "objective": "Test source-linked preparation of executive meeting briefs.", "charter_id": "charter02", "participant_ids": ["p01", "p02", "p03", "p05", "p07"]},
    "init03": {"name": "Monthly Business Review", "owner": "p03", "status": "Active monthly operating rhythm", "objective": "Review the medical center's business performance, operating updates, financial outlook, risks, and executive follow-up actions.", "charter_id": "charter03", "participant_ids": ["p01", "p02", "p03", "p04", "p06"]},
    "init04": {"name": "Clinical Research Developments", "owner": "p08", "status": "Requirements discovery", "objective": "Review technology requirements, dependencies, safeguards, and priorities for clinical research conducted in the medical center.", "charter_id": "charter04", "participant_ids": ["p01", "p08", "p09", "p10", "p11", "p12"]},
}

CHARTERS = {
    "charter01": {"title": "Clinical Operations Modernization Phase 1 Charter", "scope": "One operational domain, approved data, and a 90-day value review.", "out_of_scope": "Enterprise rollout, autonomous decisions, and unapproved clinical data.", "success_measures": ["Preparation time", "Accuracy", "Adoption", "Documented value"]},
    "charter02": {"title": "Executive Decision Intelligence Concept Charter", "scope": "Meeting preparation from curated demonstration documents with human review.", "out_of_scope": "Production integrations, autonomous actions, and institutional deployment.", "success_measures": ["Factual accuracy", "Source traceability", "Executive usefulness", "Time saved"]},
    "charter03": {"title": "Monthly Business Review Charter", "scope": "Monthly medical center business performance, operating updates, financial outlook, material risks, decisions, and accountable follow-up.", "out_of_scope": "Clinical case review, individual personnel matters, and decisions without an accountable executive owner.", "success_measures": ["Timely reporting", "Forecast accuracy", "Decision closure", "Action completion"]},
    "charter04": {"title": "Clinical Research Technology Requirements Charter", "scope": "Technology requirements for approved clinical research, including data, workflow, integration, security, researcher experience, and operational support.", "out_of_scope": "Clinical protocol approval, autonomous clinical decisions, and access to unapproved patient or research data.", "success_measures": ["Requirements coverage", "Researcher validation", "Security readiness", "Delivery feasibility"]},
}

DELIVERABLES = {
    "del01": {"name": "Phase-one cost and dependency model", "initiative_id": "init01", "owner": "p03", "due_offset": 3, "status": "In progress"},
    "del02": {"name": "Integration and security readiness assessment", "initiative_id": "init01", "owner": "p05", "due_offset": 7, "status": "Not started"},
    "del03": {"name": "Executive meeting brief", "initiative_id": "init02", "owner": "p02", "due_offset": -2, "status": "Draft complete"},
    "del04": {"name": "Concept validation findings", "initiative_id": "init02", "owner": "p02", "due_offset": 12, "status": "Planned"},
    "del05": {"name": "Monthly medical center business performance package", "initiative_id": "init03", "owner": "p03", "due_offset": 3, "status": "In progress"},
    "del06": {"name": "Business review decision and action log", "initiative_id": "init03", "owner": "p06", "due_offset": 9, "status": "Planned"},
    "del07": {"name": "Clinical research technology requirements inventory", "initiative_id": "init04", "owner": "p08", "due_offset": 1, "status": "In progress"},
    "del08": {"name": "Clinical research architecture and feasibility recommendation", "initiative_id": "init04", "owner": "p01", "due_offset": 7, "status": "Planned"},
}

MEETING_EVENTS = {
    -21: {"id": "m01", "title": "Monthly Business Review", "participants": ["p01", "p02", "p03", "p06"], "initiative_ids": ["init01", "init02"], "summary": "Leadership requested clearer benefit measures before new commitments."},
    -20: {"id": "m14", "title": "Clinical Operations Baseline Review", "participants": ["p02", "p04", "p06"], "initiative_ids": ["init01"], "summary": "The team documented current reporting effort, turnaround time, and data-quality issues to establish a measurable baseline."},
    -19: {"id": "m15", "title": "Agentification Use-Case Intake", "participants": ["p01", "p02", "p06"], "initiative_ids": ["init02"], "summary": "The group reviewed possible executive-support use cases and agreed to evaluate them against usefulness, feasibility, and governance needs."},
    -18: {"id": "m02", "title": "Analytics Discovery Session", "participants": ["p02", "p04", "p05", "p06"], "initiative_ids": ["init01"], "summary": "The team confirmed that reporting delays and inconsistent definitions are the primary problems."},
    -17: {"id": "m22", "title": "Medical Center Monthly Performance Preparation", "participants": ["p02", "p03", "p04", "p06"], "initiative_ids": ["init03"], "summary": "Leaders reviewed preliminary financial, access, workforce, and operating updates and identified material variances requiring executive attention."},
    -16: {"id": "m23", "title": "Clinical Research Technology Intake", "participants": ["p01", "p08", "p09", "p10", "p11", "p12"], "initiative_ids": ["init04"], "summary": "The clinicians described active research workflows, technology pain points, data dependencies, and upcoming study requirements."},
    -15: {"id": "m03", "title": "Finance and ROI Review", "participants": ["p03", "p04", "p06"], "initiative_ids": ["init01"], "summary": "Finance requested phased funding and a named owner for benefit realization."},
    -12: {"id": "m04", "title": "Executive Decision Support Workshop", "participants": ["p01", "p02", "p06"], "initiative_ids": ["init02"], "summary": "Participants selected executive meeting preparation as the first skill to demonstrate."},
    -11: {"id": "m16", "title": "Clinical Operations Data Readiness Review", "participants": ["p02", "p04", "p05", "p07"], "initiative_ids": ["init01"], "summary": "The review identified source ownership, data definitions, access dependencies, and validation work required for a limited phase-one pilot."},
    -10: {"id": "m24", "title": "Monthly Business Variance Review", "participants": ["p01", "p03", "p04", "p06"], "initiative_ids": ["init03"], "summary": "The group reviewed material budget, volume, staffing, and service-performance variances and requested owner-level recovery plans."},
    -9: {"id": "m05", "title": "Enterprise Architecture and Risk Review", "participants": ["p02", "p05", "p07"], "initiative_ids": ["init01", "init02"], "summary": "The review identified identity, access, retention, traceability, and human review as required controls."},
    -8: {"id": "m25", "title": "Clinical Research Workflow and Data Review", "participants": ["p01", "p08", "p09", "p10", "p11", "p12"], "initiative_ids": ["init04"], "summary": "The team mapped research data flows, integration needs, consent boundaries, researcher access, and support requirements."},
    -7: {"id": "m17", "title": "Agentification Brief Design Review", "participants": ["p01", "p02", "p06"], "initiative_ids": ["init02"], "summary": "The team agreed that the brief should connect prior decisions, open actions, current risks, and upcoming meetings with visible source traceability."},
    -6: {"id": "m06", "title": "Agentification Prototype Content Review", "participants": ["p02", "p06", "p07"], "initiative_ids": ["init02"], "summary": "The group asked that current functionality be clearly separated from future capabilities."},
    -3: {"id": "m07", "title": "Technology Investment Review", "participants": ["p02", "p03", "p04", "p06"], "initiative_ids": ["init01"], "summary": "The estimate was incomplete without integration, support, and change-management costs."},
    0: {"id": "m08", "title": "Executive Technology Investment Review", "participants": ["p01", "p02", "p03", "p04", "p05"], "initiative_ids": ["init01"], "summary": "Today: determine whether evidence supports a limited phase-one investment and define funding conditions."},
    2: {"id": "m09", "title": "Executive Brief Prototype Demonstration", "participants": ["p01", "p02", "p06"], "initiative_ids": ["init02"], "summary": "Demonstrate the meeting-preparation skill and collect feedback on usefulness and missing context."},
    1: {"id": "m26", "title": "Clinical Research Requirements Prioritization", "participants": ["p01", "p08", "p09", "p10", "p11", "p12"], "initiative_ids": ["init04"], "summary": "Prioritize technology requirements by research value, urgency, feasibility, data sensitivity, and cross-study reuse."},
    3: {"id": "m27", "title": "Medical Center Monthly Business Review", "participants": ["p01", "p02", "p03", "p04", "p06"], "initiative_ids": ["init03"], "summary": "Review the monthly business package, confirm explanations for material variances, make operating decisions, and assign accountable follow-up."},
    4: {"id": "m18", "title": "Clinical Operations Funding Conditions Review", "participants": ["p01", "p03", "p04", "p06"], "initiative_ids": ["init01"], "summary": "Review the proposed funding ceiling, benefit owner, phase-one measures, and conditions that must be satisfied before funds are released."},
    5: {"id": "m10", "title": "Security and Data Handling Working Session", "participants": ["p02", "p05", "p07"], "initiative_ids": ["init01", "init02"], "summary": "Document controls required before any institutional connection."},
    6: {"id": "m19", "title": "Agentification Feedback Synthesis", "participants": ["p02", "p06", "p07"], "initiative_ids": ["init02"], "summary": "Synthesize demonstration feedback, corrections, missing context, and proposed evaluation measures for the next concept review."},
    7: {"id": "m28", "title": "Clinical Research Architecture Recommendation", "participants": ["p01", "p08", "p09", "p10", "p11", "p12"], "initiative_ids": ["init04"], "summary": "Review the proposed architecture, security conditions, delivery dependencies, and phased implementation recommendation."},
    8: {"id": "m11", "title": "Phase-One Charter Review", "participants": ["p01", "p03", "p04", "p06"], "initiative_ids": ["init01"], "summary": "Review the revised charter, cost model, owners, and release criteria."},
    9: {"id": "m29", "title": "Monthly Business Action Closure Review", "participants": ["p02", "p03", "p04", "p06"], "initiative_ids": ["init03"], "summary": "Review completion of actions assigned during the monthly business review and escalate unresolved operating or financial issues."},
    11: {"id": "m20", "title": "Clinical Operations Pilot Readiness Check", "participants": ["p02", "p04", "p05", "p06", "p07"], "initiative_ids": ["init01"], "summary": "Confirm whether cost, data, architecture, security, ownership, and change-management conditions are ready for an executive recommendation."},
    12: {"id": "m12", "title": "Agentification Concept Validation Readout", "participants": ["p01", "p02", "p06", "p07"], "initiative_ids": ["init02"], "summary": "Review feedback and decide whether a formal requirements package should be developed."},
    13: {"id": "m21", "title": "Agentification Requirements Planning", "participants": ["p02", "p05", "p06", "p07"], "initiative_ids": ["init02"], "summary": "If concept validation is favorable, define the business, data, permission, instruction, architecture, governance, and operating requirements for a limited pilot."},
    14: {"id": "m13", "title": "Biweekly Portfolio Review Governance", "participants": ["p01", "p02", "p03", "p04", "p06"], "initiative_ids": ["init01", "init02"], "summary": "Reconcile decisions, dependencies, resources, and next-stage recommendations."},
}

DECISIONS = [
    {"id": "dec01", "meeting_id": "m01", "initiative_id": "init01", "offset": -21, "decision": "Do not request full program funding until phase-one outcomes and ownership are defined."},
    {"id": "dec02", "meeting_id": "m03", "initiative_id": "init01", "offset": -15, "decision": "Use a two-phase funding model with a value checkpoint before phase two."},
    {"id": "dec03", "meeting_id": "m04", "initiative_id": "init02", "offset": -12, "decision": "Demonstrate executive meeting preparation as the first Chief of Staff skill."},
    {"id": "dec04", "meeting_id": "m05", "initiative_id": "init02", "offset": -9, "decision": "Use synthetic data only and require human review for the demonstration."},
    {"id": "dec05", "meeting_id": "m06", "initiative_id": "init02", "offset": -6, "decision": "Present other Chief of Staff skills as future possibilities, not active capabilities."},
    {"id": "dec06", "meeting_id": "m22", "initiative_id": "init03", "offset": -17, "decision": "Use one consolidated monthly package for financial, access, workforce, and operating updates."},
    {"id": "dec07", "meeting_id": "m24", "initiative_id": "init03", "offset": -10, "decision": "Require accountable recovery plans for every material unfavorable variance."},
    {"id": "dec08", "meeting_id": "m23", "initiative_id": "init04", "offset": -16, "decision": "Create a shared requirements inventory before selecting technology solutions for individual studies."},
    {"id": "dec09", "meeting_id": "m25", "initiative_id": "init04", "offset": -8, "decision": "Treat consent, data access, interoperability, and researcher workflow as required architecture inputs."},
]

ACTIONS = [
    {"id": "act01", "source_meeting_id": "m03", "initiative_id": "init01", "owner": "p03", "due_offset": 3, "status": "In progress", "action": "Complete the phase-one cost and dependency model.", "review_meeting_id": "m11"},
    {"id": "act02", "source_meeting_id": "m05", "initiative_id": "init01", "owner": "p05", "due_offset": 7, "status": "Not started", "action": "Document integration, identity, security, and support dependencies.", "review_meeting_id": "m11"},
    {"id": "act03", "source_meeting_id": "m06", "initiative_id": "init02", "owner": "p02", "due_offset": -2, "status": "Complete", "action": "Revise the prototype so its skill and boundaries are immediately clear.", "review_meeting_id": "m09"},
    {"id": "act04", "source_meeting_id": "m06", "initiative_id": "init02", "owner": "p02", "due_offset": 12, "status": "Planned", "action": "Capture validation feedback and recommend whether to develop requirements.", "review_meeting_id": "m12"},
    {"id": "act05", "source_meeting_id": "m22", "initiative_id": "init03", "owner": "p03", "due_offset": 3, "status": "In progress", "action": "Complete the consolidated monthly business performance package and variance commentary.", "review_meeting_id": "m27"},
    {"id": "act06", "source_meeting_id": "m24", "initiative_id": "init03", "owner": "p06", "due_offset": 9, "status": "Planned", "action": "Maintain the decision and action log and escalate overdue recovery commitments.", "review_meeting_id": "m29"},
    {"id": "act07", "source_meeting_id": "m23", "initiative_id": "init04", "owner": "p08", "due_offset": 1, "status": "In progress", "action": "Consolidate and prioritize technology requirements across the five clinical research areas.", "review_meeting_id": "m26"},
    {"id": "act08", "source_meeting_id": "m25", "initiative_id": "init04", "owner": "p01", "due_offset": 7, "status": "Planned", "action": "Prepare an architecture and feasibility recommendation addressing data, security, integration, and support.", "review_meeting_id": "m28"},
]

UPCOMING_DECISIONS = [
    {"id": "ud01", "meeting_id": "m09", "initiative_id": "init02", "decision": "Determine whether the executive brief is useful and complete enough to justify continued concept validation."},
    {"id": "ud02", "meeting_id": "m18", "initiative_id": "init01", "decision": "Confirm the funding ceiling, benefit owner, and conditions required before phase-one funds are released."},
    {"id": "ud03", "meeting_id": "m11", "initiative_id": "init01", "decision": "Approve or revise the phase-one charter, accountable owners, measures, and release criteria."},
    {"id": "ud04", "meeting_id": "m20", "initiative_id": "init01", "decision": "Determine whether the initiative is ready for an executive pilot recommendation."},
    {"id": "ud05", "meeting_id": "m12", "initiative_id": "init02", "decision": "Decide whether to develop a formal requirements package for the Agentification Pilot."},
    {"id": "ud06", "meeting_id": "m13", "initiative_id": "init01", "decision": "Reconcile dependencies and determine the next stage for the initiative portfolio."},
    {"id": "ud07", "meeting_id": "m27", "initiative_id": "init03", "decision": "Confirm the medical center's response to material business variances and assign accountable recovery owners."},
    {"id": "ud08", "meeting_id": "m29", "initiative_id": "init03", "decision": "Close completed business-review actions and escalate commitments requiring executive intervention."},
    {"id": "ud09", "meeting_id": "m26", "initiative_id": "init04", "decision": "Approve the prioritized clinical research technology requirements for architecture assessment."},
    {"id": "ud10", "meeting_id": "m28", "initiative_id": "init04", "decision": "Select the recommended architecture direction and conditions for phased clinical research technology delivery."},
]

def build_synthetic_context(today):
    """Return the complete, dated five-week synthetic context."""
    calendar = [{"offset": offset, "date": today + timedelta(days=offset), "meeting": MEETING_EVENTS.get(offset)} for offset in range(-21, 15)]
    meetings = {event["id"]: {**event, "date": today + timedelta(days=offset), "offset": offset} for offset, event in MEETING_EVENTS.items()}
    decisions = [{**item, "date": today + timedelta(days=item["offset"])} for item in DECISIONS]
    actions = [{**item, "due_date": today + timedelta(days=item["due_offset"])} for item in ACTIONS]
    deliverables = {key: {**item, "due_date": today + timedelta(days=item["due_offset"])} for key, item in DELIVERABLES.items()}
    upcoming_decisions = [{**item, "date": meetings[item["meeting_id"]]["date"]} for item in UPCOMING_DECISIONS]
    return {"today": today, "calendar": calendar, "meetings": meetings, "participants": PARTICIPANTS, "initiatives": INITIATIVES, "charters": CHARTERS, "deliverables": deliverables, "decisions": decisions, "actions": actions, "upcoming_decisions": upcoming_decisions}


def build_initiative_scenarios(context):
    """Turn every initiative into a selectable, time-aware briefing scenario."""
    scenarios = {}
    today = context["today"]
    for initiative_id, initiative in context["initiatives"].items():
        related_meetings = sorted(
            (meeting for meeting in context["meetings"].values() if initiative_id in meeting["initiative_ids"]),
            key=lambda meeting: meeting["date"],
        )
        upcoming = next((meeting for meeting in related_meetings if meeting["date"] > today), None)
        current = next((meeting for meeting in related_meetings if meeting["date"] == today), None)
        meeting = upcoming or current or related_meetings[-1]
        attendee_ids = [pid for pid in meeting["participants"] if pid in initiative["participant_ids"]]
        attendee_roles = [context["participants"][pid]["role"] for pid in attendee_ids]
        charter = context["charters"][initiative["charter_id"]]
        owner = context["participants"][initiative["owner"]]
        open_actions = [action for action in context["actions"] if action["initiative_id"] == initiative_id and action["status"] != "Complete"]
        deliverables = [item for item in context["deliverables"].values() if item["initiative_id"] == initiative_id]
        next_deliverable = min(deliverables, key=lambda item: item["due_date"])
        questions = [
            f"Which of the charter success measures—{', '.join(charter['success_measures'])}—must be demonstrated next?",
            f"What must be resolved before {meeting['title']} on {meeting['date']:%b %d}?",
            f"Does the {owner['role']} have the information and authority needed to advance this initiative?",
        ]
        next_steps = [action["action"] for action in open_actions[:3]]
        if len(next_steps) < 3:
            next_steps.append(f"Confirm readiness and ownership for {next_deliverable['name']} due {next_deliverable['due_date']:%b %d}.")
        if len(next_steps) < 3:
            next_steps.append(f"Review progress at {meeting['title']} on {meeting['date']:%b %d}.")
        scenarios[initiative["name"]] = {
            "initiative_id": initiative_id,
            "meeting_id": meeting["id"],
            "title": meeting["title"],
            "date": meeting["date"],
            "objective": initiative["objective"],
            "attendees": "; ".join(attendee_roles),
            "questions": questions,
            "next_steps": next_steps[:3],
        }
    return scenarios


def build_scenario_records(context, initiative_name):
    """Render the three briefing sources from the same linked backend data."""
    scenario = build_initiative_scenarios(context)[initiative_name]
    meeting = context["meetings"][scenario["meeting_id"]]
    initiative_id = scenario["initiative_id"]
    initiative_ids = {initiative_id}
    initiatives = [context["initiatives"][initiative_id]]

    prior_meetings = sorted(
        (
            item for item in context["meetings"].values()
            if item["date"] < meeting["date"] and initiative_ids.intersection(item["initiative_ids"])
        ),
        key=lambda item: item["date"],
    )[-4:]
    prior_decisions = [
        item for item in context["decisions"]
        if item["date"] < meeting["date"] and item["initiative_id"] in initiative_ids
    ]
    related_actions = [item for item in context["actions"] if item["initiative_id"] in initiative_ids]
    related_deliverables = [item for item in context["deliverables"].values() if item["initiative_id"] in initiative_ids]
    charters = [context["charters"][item["charter_id"]] for item in initiatives]

    agenda_text = "\n".join([
        f"{meeting['title']} — Synthetic Agenda",
        f"Date: {meeting['date']:%Y-%m-%d}",
        f"Objective: {scenario['objective']}",
        "Participants: " + scenario["attendees"],
        "Agenda:",
        *[f"{index}. {question}" for index, question in enumerate(scenario["questions"], start=1)],
        "Decision requested: Confirm the appropriate decision, conditions, accountable owners, and next review point.",
    ])
    notes_text = "\n".join([
        "Prior Discussion Notes",
        *[f"{item['date']:%Y-%m-%d} — {item['title']}: {item['summary']}" for item in prior_meetings],
        "Prior decisions:",
        *[f"- {item['decision']}" for item in prior_decisions],
        "Commitments and actions:",
        *[f"- {item['action']} Owner: {context['participants'][item['owner']]['role']}. Status: {item['status']}. Due: {item['due_date']:%Y-%m-%d}." for item in related_actions],
    ])
    background_text = "\n".join([
        "Background Memo — Synthetic Executive Operating Context",
        "Initiatives:",
        *[f"- {item['name']}: {item['objective']} Status: {item['status']}." for item in initiatives],
        "Charter boundaries:",
        *[f"- {item['title']}. Scope: {item['scope']} Out of scope: {item['out_of_scope']}" for item in charters],
        "Deliverables:",
        *[f"- {item['name']}. Status: {item['status']}. Due: {item['due_date']:%Y-%m-%d}." for item in related_deliverables],
    ])
    return [
        {"name": "synthetic_agenda.txt", "label": "Agenda", "text": agenda_text},
        {"name": "synthetic_prior_discussion_notes.txt", "label": "Prior Discussion Notes", "text": notes_text},
        {"name": "synthetic_background_memo.txt", "label": "Background Memo", "text": background_text},
    ]


def today_continuity(context):
    """Return the operating history and forward dependencies relevant today."""
    today = context["today"]
    prior_meetings = sorted((m for m in context["meetings"].values() if m["date"] < today), key=lambda x: x["date"], reverse=True)
    prior_decisions = sorted((d for d in context["decisions"] if d["date"] <= today), key=lambda x: x["date"], reverse=True)
    prior_actions = sorted((a for a in context["actions"] if a["status"] == "Complete" or a["due_date"] < today), key=lambda x: x["due_date"], reverse=True)
    upcoming_meetings = sorted((m for m in context["meetings"].values() if m["date"] > today), key=lambda x: x["date"])
    actions_due = sorted((a for a in context["actions"] if a["status"] != "Complete" and a["due_date"] >= today), key=lambda x: x["due_date"])
    upcoming_decisions = sorted((d for d in context["upcoming_decisions"] if d["date"] > today), key=lambda x: x["date"])
    return {
        "prior_meetings": prior_meetings,
        "prior_decisions": prior_decisions,
        "prior_actions": prior_actions,
        "upcoming_meetings": upcoming_meetings,
        "actions_due": actions_due,
        "upcoming_decisions": upcoming_decisions,
    }


def initiative_continuity(context, initiative_id):
    """Return past and forward records for one selected initiative."""
    today = context["today"]
    related_meetings = [
        meeting for meeting in context["meetings"].values()
        if initiative_id in meeting["initiative_ids"]
    ]
    prior_meetings = sorted((m for m in related_meetings if m["date"] < today), key=lambda x: x["date"], reverse=True)
    upcoming_meetings = sorted((m for m in related_meetings if m["date"] > today), key=lambda x: x["date"])
    current_meetings = sorted((m for m in related_meetings if m["date"] == today), key=lambda x: x["date"])
    prior_decisions = sorted(
        (d for d in context["decisions"] if d["initiative_id"] == initiative_id and d["date"] <= today),
        key=lambda x: x["date"],
        reverse=True,
    )
    upcoming_decisions = sorted(
        (d for d in context["upcoming_decisions"] if d["initiative_id"] == initiative_id and d["date"] > today),
        key=lambda x: x["date"],
    )
    all_actions = sorted(
        (a for a in context["actions"] if a["initiative_id"] == initiative_id),
        key=lambda x: x["due_date"],
    )
    prior_actions = [a for a in all_actions if a["status"] == "Complete" or a["due_date"] < today]
    actions_due = [a for a in all_actions if a["status"] != "Complete" and a["due_date"] >= today]
    participant_ids = context["initiatives"][initiative_id]["participant_ids"]
    return {
        "prior_meetings": prior_meetings,
        "current_meetings": current_meetings,
        "upcoming_meetings": upcoming_meetings,
        "prior_decisions": prior_decisions,
        "upcoming_decisions": upcoming_decisions,
        "prior_actions": prior_actions,
        "actions_due": actions_due,
        "all_actions": all_actions,
        "participants": [context["participants"][pid] for pid in participant_ids],
    }
