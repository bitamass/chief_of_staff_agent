import re
from datetime import date
from io import BytesIO
from pathlib import Path

import streamlit as st
from docx import Document
from pypdf import PdfReader


st.set_page_config(
    page_title="Chief of Staff Agent",
    page_icon="🧭",
    layout="wide",
)

st.markdown(
    """
    <style>
    :root { --uw-purple:#4b2e83; --uw-gold:#b7a57a; --ink:#172033; --soft:#f5f3f8; }
    .block-container {padding-top: 2.2rem; max-width: 1280px;}
    h1, h2, h3 {color: var(--ink);}
    .hero {border-left:6px solid var(--uw-gold); padding:.25rem 0 .25rem 1rem; margin-bottom:1rem;}
    .hero h1 {margin:0; font-size:2.25rem;}
    .hero p {margin:.35rem 0 0; color:#5a6475;}
    .safe-banner {background:#f4f0fa; border:1px solid #d9cfea; border-radius:10px; padding:.8rem 1rem; margin:.7rem 0 1.2rem;}
    .brief-card {background:white; border:1px solid #e3e6eb; border-radius:12px; padding:1rem 1.1rem; min-height:145px; box-shadow:0 2px 8px rgba(20,30,50,.04);}
    .brief-card h4 {color:var(--uw-purple); margin:0 0 .5rem;}
    .source {color:#5b6677; font-size:.86rem;}
    div.stButton > button {background:var(--uw-purple); color:white; border:0; border-radius:8px; font-weight:650;}
    div.stButton > button:hover {background:#382261; color:white;}
    [data-testid="stMetric"] {background:#faf9fc; border:1px solid #e2dbea; padding:.8rem; border-radius:10px;}
    </style>
    """,
    unsafe_allow_html=True,
)

SCENARIOS = {
    "AI Agent Governance Discussion": {
        "folder": "ai_governance",
        "title": "AI Agent Governance Discussion",
        "objective": "Explore how agent governance could apply to an executive meeting-preparation use case and identify the questions that would require further consideration.",
        "attendees": "CIO; UW-IT partner; HR leader; AI governance lead",
        "questions": [
            "What minimum information should every UW AI agent disclose before it is approved or deployed?",
            "Should agent registration and oversight be centralized or managed through a federated UW/UW Medicine model?",
            "Who should own the pilot, and what evidence would be required before considering approved system integrations?",
        ],
        "next_steps": [
            "Identify the roles that would be needed to evaluate a limited use case.",
            "Define possible success measures, including preparation time saved, factual accuracy, source coverage, and executive usefulness.",
            "Document the privacy, security, records-management, and governance reviews that would be required before any institutional connection could be considered.",
        ],
    },
    "Executive Technology Investment Review": {
        "folder": "technology_investment",
        "title": "Executive Technology Investment Review",
        "objective": "Decide whether to fund a two-phase clinical operations analytics modernization initiative and establish financial and delivery guardrails.",
        "attendees": "CIO; CFO; clinical operations leader; enterprise architecture lead; finance partner",
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
    "UW Medicine Operational Risk Review": {
        "folder": "operational_risk",
        "title": "UW Medicine Digital Operations Risk Review",
        "objective": "Assess readiness for a limited clinical-support technology pilot and decide whether operational, security, and continuity risks are sufficiently controlled.",
        "attendees": "CIO; clinical operations leader; CISO delegate; patient safety representative; service owner",
        "questions": [
            "What event would trigger an immediate pause or rollback of the pilot?",
            "Who has final authority during a patient-safety, cybersecurity, or service-continuity incident?",
            "What evidence must be reviewed before the pilot expands beyond the initial unit?",
        ],
        "next_steps": [
            "Name the service owner, clinical safety owner, and incident decision authority.",
            "Complete a tabletop exercise covering downtime, incorrect output, and access-control failure.",
            "Approve measurable go/no-go thresholds and a documented rollback plan before launch.",
        ],
    },
}


def read_file(uploaded):
    name = uploaded.name.lower()
    raw = uploaded.read()
    if name.endswith((".txt", ".md")):
        return raw.decode("utf-8", errors="ignore")
    if name.endswith(".pdf"):
        return "\n".join((p.extract_text() or "") for p in PdfReader(BytesIO(raw)).pages)
    if name.endswith(".docx"):
        return "\n".join(p.text for p in Document(BytesIO(raw)).paragraphs)
    return ""


def source_label(filename):
    stem = re.sub(r"[_-]+", " ", filename.rsplit(".", 1)[0]).strip().title()
    return stem or filename


def find_sentences(records, keywords, limit=4, labels=None, excluded=None):
    found = []
    excluded = [x.lower() for x in (excluded or [])]
    for record in records:
        if labels and record["label"] not in labels:
            continue
        # Preserve paragraph boundaries so document titles and section labels do
        # not become fused with the first substantive sentence.
        sentences = re.split(r"\n+|(?<=[.!?])\s+|\s*[•]\s*", record["text"])
        for sentence in sentences:
            sentence = re.sub(r"^\s*\d+[.)]\s*", "", sentence).strip(" -\t")
            lowered = sentence.lower().rstrip(":")
            if lowered in {"agenda", "prior discussion notes", "background memo — executive meeting intelligence pilot"}:
                continue
            if "sample agenda" in lowered or lowered.startswith("background memo"):
                continue
            if any(term in lowered for term in excluded):
                continue
            for prefix in ("objective:", "decision requested:"):
                if lowered.startswith(prefix):
                    sentence = sentence.split(":", 1)[1].strip()
                    lowered = sentence.lower()
            if len(sentence) < 28:
                continue
            if any(term in sentence.lower() for term in excluded):
                continue
            if any(word.lower() in sentence.lower() for word in keywords):
                item = (sentence, record["label"])
                if item not in found:
                    found.append(item)
            if len(found) >= limit:
                return found
    return found


def make_demo_brief(title, objective, attendees, records, scenario_name=None):
    commitments = find_sentences(
        records,
        ["interest", "agreed", "requested", "supported", "required"],
        3,
        labels={"Prior Discussion Notes"},
        excluded=["no final decision"],
    )
    risks = find_sentences(
        records,
        ["concern", "risk", "permission", "access", "privacy", "security", "dependency", "downtime", "incident"],
        4,
        labels={"Prior Discussion Notes", "Background Memo"},
        excluded=["low-risk prototype", "no final decision", "suggested readiness measures"],
    )
    decisions = find_sentences(
        records,
        ["decision requested", "decide", "determine", "approve", "confirm", "identify"],
        3,
        labels={"Agenda"},
        excluded=["objective:", "no approval is requested"],
    )
    background = find_sentences(
        records,
        ["agent", "governance", "prototype", "executive", "initiative", "technology", "operational", "clinical", "investment", "demonstration"],
        4,
        labels={"Background Memo"},
    )

    # Keep the executive brief concise by preventing the same source sentence
    # from appearing in more than one section.
    used_text = {text for section in (commitments, risks, decisions) for text, _ in section}
    background = [item for item in background if item[0] not in used_text]

    if not commitments:
        commitments = [("No prior commitments were identified in the selected demonstration documents.", "Prior Discussion Notes")]
    if not risks:
        risks = [("The pilot requires explicit access controls, source traceability, human review, and an accountable owner.", "Background Memo")]
    if not decisions:
        decisions = [("No approval decision is requested; identify the questions that merit further exploration.", "Agenda")]

    scenario = SCENARIOS.get(scenario_name or "AI Agent Governance Discussion", SCENARIOS["AI Agent Governance Discussion"])
    questions = scenario["questions"]
    next_steps = scenario["next_steps"]
    return {
        "title": title,
        "objective": objective,
        "attendees": attendees,
        "background": background,
        "commitments": commitments,
        "risks": risks,
        "decisions": decisions,
        "questions": questions,
        "next_steps": next_steps,
    }


def cited_markdown(items):
    return "\n".join(f"- {text} **[{source}]**" for text, source in items)


def brief_markdown(brief, records):
    questions = "\n".join(f"- {x}" for x in brief["questions"])
    next_steps = "\n".join(f"- {x}" for x in brief["next_steps"])
    sources = "\n".join(f"- {r['label']} ({r['name']})" for r in records)
    return f"""# Executive Meeting Brief

**Meeting:** {brief['title']}  
**Objective:** {brief['objective']}  
**Attendees / roles:** {brief['attendees']}

## Relevant Background
{cited_markdown(brief['background'])}

## Prior Decisions and Commitments
{cited_markdown(brief['commitments'])}

## Open Issues and Risks
{cited_markdown(brief['risks'])}

## Decisions or Alignment Needed
{cited_markdown(brief['decisions'])}

## Recommended Questions
{questions}

## Recommended Next Steps
{next_steps}

## Sources Reviewed
{sources}

## Governance Notice
Generated from selected demonstration documents. Human review is required. This prototype is not connected to UW production systems.
"""


def brief_docx(brief, records):
    doc = Document()
    doc.add_heading("Executive Meeting Brief", 0)
    doc.add_paragraph(f"Meeting: {brief['title']}")
    doc.add_paragraph(f"Objective: {brief['objective']}")
    doc.add_paragraph(f"Attendees / roles: {brief['attendees']}")
    sections = [
        ("Relevant Background", brief["background"], True),
        ("Prior Decisions and Commitments", brief["commitments"], True),
        ("Open Issues and Risks", brief["risks"], True),
        ("Decisions or Alignment Needed", brief["decisions"], True),
        ("Recommended Questions", brief["questions"], False),
        ("Recommended Next Steps", brief["next_steps"], False),
    ]
    for heading, items, cited in sections:
        doc.add_heading(heading, level=1)
        for item in items:
            text = f"{item[0]} [{item[1]}]" if cited else item
            doc.add_paragraph(text, style="List Bullet")
    doc.add_heading("Sources Reviewed", level=1)
    for record in records:
        doc.add_paragraph(f"{record['label']} ({record['name']})", style="List Bullet")
    doc.add_heading("Governance Notice", level=1)
    doc.add_paragraph("Generated from selected demonstration documents. Human review is required. This prototype is not connected to UW production systems.")
    output = BytesIO()
    doc.save(output)
    return output.getvalue()


st.markdown(
    '<div class="hero"><h1>Chief of Staff Agent</h1>'
    '<p>Independent exploratory prototype demonstrating one possible executive meeting-preparation use case.</p></div>',
    unsafe_allow_html=True,
)
st.markdown(
    '<div class="safe-banner"><b>Guided demonstration:</b> Uses sample data only. '
    'No UW production systems, Epic, Outlook, Teams, or SharePoint are connected.</div>',
    unsafe_allow_html=True,
)

with st.sidebar:
    st.header("Agent Governance & Safeguards")
    st.success("Guided demonstration")
    for label in [
        "Human review required",
        "Source traceability enabled",
        "Session-only document use",
        "No production or Epic data",
    ]:
        st.checkbox(label, value=True, disabled=True)
    st.divider()
    st.subheader("Future state—not connected")
    st.caption("Outlook calendar · Teams summaries · SharePoint · Approved external intelligence")

st.subheader("Choose a demonstration scenario")
scenario_name = st.selectbox(
    "Scenario",
    list(SCENARIOS),
    label_visibility="collapsed",
    key="scenario_name",
)
scenario = SCENARIOS[scenario_name]
scenario_action, scenario_description = st.columns([1, 2.4])
with scenario_action:
    if st.button("Load Selected Scenario", use_container_width=True):
        st.session_state.meeting_title = scenario["title"]
        st.session_state.meeting_objective = scenario["objective"]
        st.session_state.attendees = scenario["attendees"]
        st.session_state.active_scenario = scenario_name
        st.session_state.pop("brief", None)
        st.rerun()
with scenario_description:
    st.caption("Loads three curated demonstration documents and updates the meeting context.")

if "meeting_title" not in st.session_state:
    st.session_state.meeting_title = SCENARIOS["AI Agent Governance Discussion"]["title"]
if "meeting_objective" not in st.session_state:
    st.session_state.meeting_objective = SCENARIOS["AI Agent Governance Discussion"]["objective"]
if "attendees" not in st.session_state:
    st.session_state.attendees = SCENARIOS["AI Agent Governance Discussion"]["attendees"]

left, right = st.columns([1.15, 1])
with left:
    meeting_title = st.text_input("Meeting title", key="meeting_title")
    meeting_objective = st.text_area(
        "Meeting objective",
        key="meeting_objective",
        height=95,
    )
with right:
    meeting_date = st.date_input("Meeting date", value=date.today())
    attendees = st.text_area("Attendees / roles", key="attendees", height=95)

records = []
if st.session_state.get("active_scenario"):
    active_name = st.session_state.active_scenario
    sample_dir = Path(__file__).parent / "sample_data" / SCENARIOS[active_name]["folder"]
    for path in [
        sample_dir / "agenda.txt",
        sample_dir / "prior_discussion_notes.txt",
        sample_dir / "background_memo.txt",
    ]:
        if path.exists():
            records.append({"name": path.name, "label": source_label(path.name), "text": path.read_text(encoding="utf-8")})

if records:
    st.info("Sources ready: " + ", ".join(r["name"] for r in records))

if st.button("Generate Decision-Ready Brief", use_container_width=True):
    if not records:
        st.warning("Select Load Selected Scenario before generating the brief.")
    else:
        st.session_state.brief = make_demo_brief(
            meeting_title,
            meeting_objective,
            attendees,
            records,
            st.session_state.get("active_scenario"),
        )
        st.session_state.records = records
        st.session_state.generated_date = str(meeting_date)

if "brief" in st.session_state:
    brief = st.session_state.brief
    saved_records = st.session_state.records
    st.divider()
    st.header("Executive Brief")
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Sources reviewed", len(saved_records))
    m2.metric("Decisions surfaced", len(brief["decisions"]))
    m3.metric("Risks identified", len(brief["risks"]))
    m4.metric("Review status", "Human review")

    st.subheader(brief["title"])
    st.caption(f"Meeting date: {st.session_state.generated_date}  ·  Prepared from selected demonstration documents")
    st.write(brief["objective"])

    a, b = st.columns(2)
    with a:
        st.markdown("#### Decisions or Alignment Needed")
        for text, source in brief["decisions"]:
            st.markdown(f"- {text}  \n  <span class='source'>Source: {source}</span>", unsafe_allow_html=True)
    with b:
        st.markdown("#### Open Issues and Risks")
        for text, source in brief["risks"]:
            st.markdown(f"- {text}  \n  <span class='source'>Source: {source}</span>", unsafe_allow_html=True)

    st.markdown("#### Prior Decisions and Commitments")
    for text, source in brief["commitments"]:
        st.markdown(f"- {text} **[{source}]**")

    with st.expander("Relevant background and evidence", expanded=True):
        for text, source in brief["background"]:
            st.markdown(f"- {text} **[{source}]**")

    qcol, ncol = st.columns(2)
    with qcol:
        st.markdown("#### Recommended Questions")
        for item in brief["questions"]:
            st.markdown(f"- {item}")
    with ncol:
        st.markdown("#### Recommended Next Steps")
        for item in brief["next_steps"]:
            st.markdown(f"- {item}")

    with st.expander("Agent governance record"):
        st.write("**Purpose:** Prepare an executive meeting brief from user-selected documents.")
        st.write("**Data accessed:** " + ", ".join(r["name"] for r in saved_records))
        st.write("**External systems accessed:** None")
        st.write("**Retention:** Session only")
        st.write("**Required control:** Human review before use or distribution")
        st.write("**Known limitation:** Demonstration synthesis; no automated validation against UW systems")

    md = brief_markdown(brief, saved_records)
    docx = brief_docx(brief, saved_records)
    d1, d2 = st.columns(2)
    d1.download_button("Download Word Brief", docx, "executive_meeting_brief.docx", "application/vnd.openxmlformats-officedocument.wordprocessingml.document", use_container_width=True)
    d2.download_button("Download Markdown Brief", md, "executive_meeting_brief.md", "text/markdown", use_container_width=True)

st.divider()
st.caption("Prototype boundary: sample data only; no autonomous actions; no production connections. Any institutional pilot would require approved authentication, role-based access, logging, privacy, security, records-management, and governance review.")
