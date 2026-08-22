"""Synthetic executive context for the Chief of Staff demonstration.

Everything in this module is fictional. Dates use offsets from ``today`` so
the story always covers three weeks of history and two weeks of forward plans.
"""

from datetime import timedelta


PARTICIPANTS = {
    "p01": {"name": "Alex Morgan", "role": "Executive sponsor"},
    "p02": {"name": "Jordan Lee", "role": "Technology leader"},
    "p03": {"name": "Riley Chen", "role": "Finance partner"},
    "p04": {"name": "Morgan Patel", "role": "Clinical operations leader"},
    "p05": {"name": "Casey Williams", "role": "Enterprise architecture lead"},
    "p06": {"name": "Taylor Brooks", "role": "Program director"},
    "p07": {"name": "Avery Johnson", "role": "Security and privacy partner"},
    "p08": {"name": "Cameron Davis", "role": "Patient safety representative"},
    "p09": {"name": "Drew Thompson", "role": "Service owner"},
}

INITIATIVES = {
    "init01": {"name": "Clinical Operations Analytics Modernization", "owner": "p06", "status": "Proposed phase-one pilot", "objective": "Reduce manual reporting and improve decision latency.", "charter_id": "charter01"},
    "init02": {"name": "Executive Decision Intelligence Pilot", "owner": "p02", "status": "Concept validation", "objective": "Test source-linked preparation of executive meeting briefs.", "charter_id": "charter02"},
}

CHARTERS = {
    "charter01": {"title": "Analytics Modernization Phase-One Charter", "scope": "One operational domain, approved data, and a 90-day value review.", "out_of_scope": "Enterprise rollout, autonomous decisions, and unapproved clinical data.", "success_measures": ["Preparation time", "Accuracy", "Adoption", "Documented value"]},
    "charter02": {"title": "Executive Decision Intelligence Concept Charter", "scope": "Meeting preparation from curated demonstration documents with human review.", "out_of_scope": "Production integrations, autonomous actions, and institutional deployment.", "success_measures": ["Factual accuracy", "Source traceability", "Executive usefulness", "Time saved"]},
}

DELIVERABLES = {
    "del01": {"name": "Phase-one cost and dependency model", "initiative_id": "init01", "owner": "p03", "due_offset": 3, "status": "In progress"},
    "del02": {"name": "Integration and security readiness assessment", "initiative_id": "init01", "owner": "p05", "due_offset": 7, "status": "Not started"},
    "del03": {"name": "Executive meeting brief prototype", "initiative_id": "init02", "owner": "p02", "due_offset": -2, "status": "Draft complete"},
    "del04": {"name": "Concept-validation findings", "initiative_id": "init02", "owner": "p06", "due_offset": 12, "status": "Planned"},
}

MEETING_EVENTS = {
    -21: {"id": "m01", "title": "Monthly Portfolio Review", "participants": ["p01", "p02", "p03", "p06"], "initiative_ids": ["init01", "init02"], "summary": "Leadership requested clearer benefit measures before new commitments."},
    -18: {"id": "m02", "title": "Analytics Discovery Session", "participants": ["p02", "p04", "p05", "p06"], "initiative_ids": ["init01"], "summary": "The team confirmed that reporting delays and inconsistent definitions are the primary problems."},
    -15: {"id": "m03", "title": "Finance and Value Review", "participants": ["p03", "p04", "p06"], "initiative_ids": ["init01"], "summary": "Finance requested phased funding and a named owner for benefit realization."},
    -12: {"id": "m04", "title": "Executive Support Use-Case Workshop", "participants": ["p01", "p02", "p06"], "initiative_ids": ["init02"], "summary": "Participants selected executive meeting preparation as the first skill to demonstrate."},
    -9: {"id": "m05", "title": "Architecture and Risk Review", "participants": ["p02", "p05", "p07"], "initiative_ids": ["init01", "init02"], "summary": "The review identified identity, access, retention, traceability, and human review as required controls."},
    -6: {"id": "m06", "title": "Prototype Content Review", "participants": ["p02", "p06", "p07"], "initiative_ids": ["init02"], "summary": "The group asked that current functionality be clearly separated from future capabilities."},
    -3: {"id": "m07", "title": "Investment Pre-Read Review", "participants": ["p02", "p03", "p04", "p06"], "initiative_ids": ["init01"], "summary": "The estimate was incomplete without integration, support, and change-management costs."},
    0: {"id": "m08", "title": "Executive Technology Investment Review", "participants": ["p01", "p02", "p03", "p04", "p05"], "initiative_ids": ["init01"], "summary": "Today: determine whether evidence supports a limited phase-one investment and define funding conditions."},
    2: {"id": "m09", "title": "Executive Brief Prototype Demonstration", "participants": ["p01", "p02", "p06"], "initiative_ids": ["init02"], "summary": "Demonstrate the meeting-preparation skill and collect feedback on usefulness and missing context."},
    5: {"id": "m10", "title": "AI Agent Governance Discussion", "participants": ["p02", "p05", "p06", "p07"], "initiative_ids": ["init02"], "summary": "Explore governance questions and document controls required before any institutional connection."},
    8: {"id": "m11", "title": "Phase-One Charter Review", "participants": ["p01", "p03", "p04", "p06"], "initiative_ids": ["init01"], "summary": "Review the revised charter, cost model, owners, and release criteria."},
    10: {"id": "m14", "title": "UW Medicine Digital Operations Risk Review", "participants": ["p02", "p04", "p07", "p08", "p09"], "initiative_ids": ["init01"], "summary": "Assess whether operational, security, patient-safety, and continuity controls are sufficient for a limited pilot."},
    12: {"id": "m12", "title": "Concept Validation Readout", "participants": ["p01", "p02", "p06", "p07"], "initiative_ids": ["init02"], "summary": "Review feedback and decide whether a formal requirements package should be developed."},
    14: {"id": "m13", "title": "Biweekly Portfolio Decision Forum", "participants": ["p01", "p02", "p03", "p04", "p06"], "initiative_ids": ["init01", "init02"], "summary": "Reconcile decisions, dependencies, resources, and next-stage recommendations."},
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

# Display and briefing configuration belongs here—not in the user interface—so
# the synthetic backend remains the single source of truth.
DEMO_SCENARIO_CONFIG = {
    "Executive Technology Investment Review": {
        "meeting_id": "m08",
        "objective": "Decide whether to fund a two-phase clinical operations analytics modernization initiative and establish financial and delivery guardrails.",
        "questions": [
            "Which measurable operational outcome must the first phase deliver before additional funding is released?",
            "What costs and dependencies are not yet included in the current estimate?",
            "Which executive owns benefit realization after the technology is delivered?",
        ],
        "next_steps": [
            "Confirm the phase-one funding ceiling, executive sponsor, and accountable benefit owner.",
            "Validate integration, change-management, security, and ongoing support costs before contracting.",
            "Schedule a 90-day value review with agreed financial and operational measures.",
        ],
    },
    "AI Agent Governance Discussion": {
        "meeting_id": "m10",
        "objective": "Explore how agent governance could apply to an executive meeting-preparation use case and identify questions requiring further consideration.",
        "questions": [
            "What minimum information should every AI agent disclose before approval or deployment?",
            "Should registration and oversight be centralized or managed through a federated model?",
            "Which roles and evidence would be needed before institutional integration could be considered?",
        ],
        "next_steps": [
            "Identify the roles needed to evaluate a limited use case.",
            "Define measures for time saved, factual accuracy, source coverage, and executive usefulness.",
            "Document required privacy, security, records-management, and governance reviews.",
        ],
    },
    "UW Medicine Operational Risk Review": {
        "meeting_id": "m14",
        "objective": "Assess readiness for a limited clinical-support technology pilot and determine whether operational, security, patient-safety, and continuity risks are sufficiently controlled.",
        "questions": [
            "What event would trigger an immediate pause or rollback of the pilot?",
            "Who has final authority during a patient-safety, cybersecurity, or continuity incident?",
            "What evidence must be reviewed before expansion beyond the initial unit?",
        ],
        "next_steps": [
            "Name the service owner, clinical safety owner, and incident decision authority.",
            "Complete a tabletop exercise covering downtime, incorrect output, and access-control failure.",
            "Approve measurable go/no-go thresholds and a documented rollback plan before launch.",
        ],
    },
}


def build_synthetic_context(today):
    """Return the complete, dated five-week synthetic context."""
    calendar = [{"offset": offset, "date": today + timedelta(days=offset), "meeting": MEETING_EVENTS.get(offset)} for offset in range(-21, 15)]
    meetings = {event["id"]: {**event, "date": today + timedelta(days=offset), "offset": offset} for offset, event in MEETING_EVENTS.items()}
    decisions = [{**item, "date": today + timedelta(days=item["offset"])} for item in DECISIONS]
    actions = [{**item, "due_date": today + timedelta(days=item["due_offset"])} for item in ACTIONS]
    deliverables = {key: {**item, "due_date": today + timedelta(days=item["due_offset"])} for key, item in DELIVERABLES.items()}
    return {"today": today, "calendar": calendar, "meetings": meetings, "participants": PARTICIPANTS, "initiatives": INITIATIVES, "charters": CHARTERS, "deliverables": deliverables, "decisions": decisions, "actions": actions}


def build_demo_scenarios(context):
    """Derive all scenario-facing metadata from the linked backend records."""
    scenarios = {}
    for label, config in DEMO_SCENARIO_CONFIG.items():
        meeting = context["meetings"][config["meeting_id"]]
        attendee_roles = [context["participants"][pid]["role"] for pid in meeting["participants"]]
        scenarios[label] = {
            **config,
            "title": meeting["title"],
            "date": meeting["date"],
            "attendees": "; ".join(attendee_roles),
        }
    return scenarios


def build_scenario_records(context, scenario_label):
    """Render the three briefing sources from the same linked backend data."""
    scenario = build_demo_scenarios(context)[scenario_label]
    meeting = context["meetings"][scenario["meeting_id"]]
    initiative_ids = set(meeting["initiative_ids"])
    initiatives = [context["initiatives"][iid] for iid in meeting["initiative_ids"]]

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
    recent = sorted((d for d in context["decisions"] if d["date"] <= today), key=lambda x: x["date"], reverse=True)[:4]
    actions = sorted((a for a in context["actions"] if a["status"] != "Complete" and a["due_date"] >= today), key=lambda x: x["due_date"])
    meetings = sorted((m for m in context["meetings"].values() if m["date"] > today), key=lambda x: x["date"])[:5]
    return {"recent_decisions": recent, "open_actions": actions, "upcoming_meetings": meetings}
