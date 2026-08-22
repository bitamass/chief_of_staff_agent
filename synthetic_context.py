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
    -20: {"id": "m14", "title": "Clinical Operations Baseline Review", "participants": ["p02", "p04", "p06"], "initiative_ids": ["init01"], "summary": "The team documented current reporting effort, turnaround time, and data-quality issues to establish a measurable baseline."},
    -19: {"id": "m15", "title": "Agentification Use-Case Intake", "participants": ["p01", "p02", "p06"], "initiative_ids": ["init02"], "summary": "The group reviewed possible executive-support use cases and agreed to evaluate them against usefulness, feasibility, and governance needs."},
    -18: {"id": "m02", "title": "Analytics Discovery Session", "participants": ["p02", "p04", "p05", "p06"], "initiative_ids": ["init01"], "summary": "The team confirmed that reporting delays and inconsistent definitions are the primary problems."},
    -15: {"id": "m03", "title": "Finance and ROI Review", "participants": ["p03", "p04", "p06"], "initiative_ids": ["init01"], "summary": "Finance requested phased funding and a named owner for benefit realization."},
    -12: {"id": "m04", "title": "Executive Decision Support Workshop", "participants": ["p01", "p02", "p06"], "initiative_ids": ["init02"], "summary": "Participants selected executive meeting preparation as the first skill to demonstrate."},
    -11: {"id": "m16", "title": "Clinical Operations Data Readiness Review", "participants": ["p02", "p04", "p05", "p07"], "initiative_ids": ["init01"], "summary": "The review identified source ownership, data definitions, access dependencies, and validation work required for a limited phase-one pilot."},
    -9: {"id": "m05", "title": "Enterprise Architecture and Risk Review", "participants": ["p02", "p05", "p07"], "initiative_ids": ["init01", "init02"], "summary": "The review identified identity, access, retention, traceability, and human review as required controls."},
    -7: {"id": "m17", "title": "Agentification Brief Design Review", "participants": ["p01", "p02", "p06"], "initiative_ids": ["init02"], "summary": "The team agreed that the brief should connect prior decisions, open actions, current risks, and upcoming meetings with visible source traceability."},
    -6: {"id": "m06", "title": "Agentification Prototype Content Review", "participants": ["p02", "p06", "p07"], "initiative_ids": ["init02"], "summary": "The group asked that current functionality be clearly separated from future capabilities."},
    -3: {"id": "m07", "title": "Technology Investment Review", "participants": ["p02", "p03", "p04", "p06"], "initiative_ids": ["init01"], "summary": "The estimate was incomplete without integration, support, and change-management costs."},
    0: {"id": "m08", "title": "Executive Technology Investment Review", "participants": ["p01", "p02", "p03", "p04", "p05"], "initiative_ids": ["init01"], "summary": "Today: determine whether evidence supports a limited phase-one investment and define funding conditions."},
    2: {"id": "m09", "title": "Executive Brief Prototype Demonstration", "participants": ["p01", "p02", "p06"], "initiative_ids": ["init02"], "summary": "Demonstrate the meeting-preparation skill and collect feedback on usefulness and missing context."},
    4: {"id": "m18", "title": "Clinical Operations Funding Conditions Review", "participants": ["p01", "p03", "p04", "p06"], "initiative_ids": ["init01"], "summary": "Review the proposed funding ceiling, benefit owner, phase-one measures, and conditions that must be satisfied before funds are released."},
    5: {"id": "m10", "title": "Security and Data Handling Working Session", "participants": ["p02", "p05", "p07"], "initiative_ids": ["init01", "init02"], "summary": "Document controls required before any institutional connection."},
    6: {"id": "m19", "title": "Agentification Feedback Synthesis", "participants": ["p02", "p06", "p07"], "initiative_ids": ["init02"], "summary": "Synthesize demonstration feedback, corrections, missing context, and proposed evaluation measures for the next concept review."},
    8: {"id": "m11", "title": "Phase-One Charter Review", "participants": ["p01", "p03", "p04", "p06"], "initiative_ids": ["init01"], "summary": "Review the revised charter, cost model, owners, and release criteria."},
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
]

ACTIONS = [
    {"id": "act01", "source_meeting_id": "m03", "initiative_id": "init01", "owner": "p03", "due_offset": 3, "status": "In progress", "action": "Complete the phase-one cost and dependency model.", "review_meeting_id": "m11"},
    {"id": "act02", "source_meeting_id": "m05", "initiative_id": "init01", "owner": "p05", "due_offset": 7, "status": "Not started", "action": "Document integration, identity, security, and support dependencies.", "review_meeting_id": "m11"},
    {"id": "act03", "source_meeting_id": "m06", "initiative_id": "init02", "owner": "p02", "due_offset": -2, "status": "Complete", "action": "Revise the prototype so its skill and boundaries are immediately clear.", "review_meeting_id": "m09"},
    {"id": "act04", "source_meeting_id": "m06", "initiative_id": "init02", "owner": "p06", "due_offset": 12, "status": "Planned", "action": "Capture validation feedback and recommend whether to develop requirements.", "review_meeting_id": "m12"},
]

UPCOMING_DECISIONS = [
    {"id": "ud01", "meeting_id": "m09", "initiative_id": "init02", "decision": "Determine whether the executive brief is useful and complete enough to justify continued concept validation."},
    {"id": "ud02", "meeting_id": "m18", "initiative_id": "init01", "decision": "Confirm the funding ceiling, benefit owner, and conditions required before phase-one funds are released."},
    {"id": "ud03", "meeting_id": "m11", "initiative_id": "init01", "decision": "Approve or revise the phase-one charter, accountable owners, measures, and release criteria."},
    {"id": "ud04", "meeting_id": "m20", "initiative_id": "init01", "decision": "Determine whether the initiative is ready for an executive pilot recommendation."},
    {"id": "ud05", "meeting_id": "m12", "initiative_id": "init02", "decision": "Decide whether to develop a formal requirements package for the Agentification Pilot."},
    {"id": "ud06", "meeting_id": "m13", "initiative_id": "init01", "decision": "Reconcile dependencies and determine the next stage for the initiative portfolio."},
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
        current = next((meeting for meeting in related_meetings if meeting["date"] == today), None)
        upcoming = next((meeting for meeting in related_meetings if meeting["date"] > today), None)
        meeting = current or upcoming or related_meetings[-1]
        attendee_roles = [context["participants"][pid]["role"] for pid in meeting["participants"]]
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
    participant_ids = sorted({pid for meeting in related_meetings for pid in meeting["participants"]})
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
