from datetime import date
from pathlib import Path

import streamlit as st

from skill_catalog import discover_skill_catalog
from skill_runner import REQUIRED_DOCUMENTS, result_docx, result_markdown, run_repository_skill
from synthetic_context import (
    DATASET_VERSION,
    build_initiative_scenarios,
    build_scenario_records,
    build_synthetic_context,
    initiative_continuity,
)


st.set_page_config(page_title="Chief of Staff Agent Demo", page_icon="🧭", layout="wide")
st.markdown(
    """
    <style>
    :root { --earth:#6f5b45; --clay:#9b7653; --sand:#d8c7ad; --cream:#f7f2e8; --sage:#7a846b; --ink:#34312d; }
    .block-container {padding-top:2.2rem; max-width:1280px;}
    h1,h2,h3 {color:var(--ink);}
    .hero {border-left:6px solid var(--clay); padding:.25rem 0 .25rem 1rem; margin-bottom:1rem;}
    .hero h1 {margin:0; font-size:2.25rem;}
    .hero p {margin:.35rem 0 0; color:#5a6475;}
    .safe-banner {background:var(--cream); border:1px solid var(--sand); border-radius:10px; padding:.8rem 1rem; margin:.7rem 0 1.2rem;}
    .source {color:#5b6677; font-size:.86rem;}
    .result-card {background:var(--cream); border:1px solid var(--sand); border-radius:10px; padding:.7rem .8rem; min-height:92px;}
    .result-card-label {color:#5d5a54; font-size:.78rem; margin-bottom:.42rem;}
    .result-card-value {color:var(--ink); font-size:1.55rem; line-height:1.12; overflow-wrap:anywhere;}
    .result-card-value.long {font-size:1.05rem; line-height:1.25;}
    div.stButton > button {background:var(--earth); color:white; border:1px solid var(--earth); border-radius:8px; font-weight:650;}
    div.stButton > button:hover {background:var(--clay); border-color:var(--clay); color:white;}
    [data-testid="stMetric"] {background:var(--cream); border:1px solid var(--sand); padding:.8rem; border-radius:10px;}
    [data-testid="stVerticalBlockBorderWrapper"] {border-color:var(--sand) !important; background:#fffdf9;}
    div[data-testid="stAlert"] {background:var(--cream); color:var(--ink); border-color:var(--sand);}
    </style>
    """,
    unsafe_allow_html=True,
)


def clear_skill_result():
    st.session_state.pop("skill_result", None)


def render_result_card(column, label, value, compact=False):
    value_class = "result-card-value long" if compact else "result-card-value"
    with column:
        st.markdown(
            f'<div class="result-card"><div class="result-card-label">{label}</div>'
            f'<div class="{value_class}">{value}</div></div>',
            unsafe_allow_html=True,
        )


def set_meeting_context(scenario):
    st.session_state.meeting_title = scenario["title"]
    st.session_state.meeting_objective = scenario["objective"]
    st.session_state.attendees = scenario["attendees"]
    st.session_state.meeting_date = scenario["date"]
    st.session_state.meeting_context_signature = (
        scenario["initiative_id"],
        scenario["meeting_id"],
        scenario["date"],
    )
    clear_skill_result()


def render_source_item(item):
    st.markdown(
        f"- {item['text']}  \n  <span class='source'>Source: {item['source']}</span>",
        unsafe_allow_html=True,
    )


def render_skill_result(result):
    with st.container(border=True):
        st.header(result["skill_name"])
        m1, m2, m3, m4 = st.columns(4)
        render_result_card(m1, "Repository files", len(result["documents_used"]))
        render_result_card(m2, "Output sections", len(result["sections"]))
        render_result_card(m3, "Initiative", result["scenario_name"], compact=True)
        render_result_card(m4, "Review status", "Human review", compact=True)
        st.caption(
            f"{result['engine']} · Loaded from `{result['repository_path']}` · "
            "Generated from synthetic demonstration records"
        )

    for index in range(0, len(result["sections"]), 2):
        columns = st.columns(2)
        for column, section in zip(columns, result["sections"][index : index + 2]):
            with column:
                with st.container(border=True):
                    st.markdown(f"#### {section['heading']}")
                    for item in section["items"]:
                        render_source_item(item)

    with st.expander("Input coverage from INPUTS.md"):
        st.caption("Shows which documented input requirements are represented in the synthetic demo context.")
        st.dataframe(result["input_checks"], width="stretch", hide_index=True)

    with st.expander("Agent governance record"):
        st.write("**Purpose:** Execute the selected repository skill against the selected synthetic initiative.")
        st.write("**Skill files used:** SKILL.md, INPUTS.md, OUTPUTS.md")
        st.write("**External systems accessed:** None")
        st.write("**Retention:** Streamlit session only")
        st.write("**Required control:** Human review before use or distribution")
        st.write("**Known limitation:** Deterministic demonstration synthesis; no model API or UW-system validation")

    markdown = result_markdown(result)
    word = result_docx(result)
    safe_name = result["skill_name"].lower().replace(" ", "_").replace("/", "_")
    d1, d2 = st.columns(2)
    d1.download_button("Download Word Output", word, f"{safe_name}.docx", "application/vnd.openxmlformats-officedocument.wordprocessingml.document", width="stretch")
    d2.download_button("Download Markdown Output", markdown, f"{safe_name}.md", "text/markdown", width="stretch")


def render_skills_view(context, scenarios, scenario_name, catalog):
    capabilities = {capability: list(skills) for capability, skills in catalog.items()}

    with st.container(border=True):
        st.subheader("Choose a Chief of Staff capability and skill")
        scenario_name = st.selectbox(
            "Apply this skill to initiative",
            list(scenarios),
            key="scenario_name",
            help="The selected skill uses this initiative's synthetic meetings, decisions, actions, and deliverables.",
        )
        scenario = scenarios[scenario_name]
        capability_labels = list(capabilities)
        default_capability = next((i for i, label in enumerate(capability_labels) if label.startswith("02 ")), 0)
        capability_name = st.selectbox("Capability", capability_labels, index=default_capability, key="capability_name")
        skill_options = capabilities[capability_name]
        preferred = "Prepare Pre-Meeting Briefing Materials"
        default_skill = skill_options.index(preferred) if preferred in skill_options else 0
        skill_name = st.selectbox("Skill", skill_options, index=default_skill, key=f"skill_name_{capability_name}")
        selected_skill = catalog[capability_name][skill_name]
        documents = selected_skill["documents"]
        missing = [name for name in REQUIRED_DOCUMENTS if not documents.get(name, "").strip()]
        signature = (capability_name, skill_name, scenario_name)
        if st.session_state.get("skill_signature") != signature:
            clear_skill_result()
            st.session_state.skill_signature = signature

        if selected_skill["source"] != "repository":
            st.error("The capability folders were not included in this deployment, so repository execution is unavailable.")
        elif missing:
            st.error("This skill cannot run until the following files are present: " + ", ".join(missing))
        else:
            st.success(
                f"Ready to execute: {capability_name} → {skill_name}. "
                f"Loaded SKILL.md, INPUTS.md, and OUTPUTS.md from `{selected_skill['repository_path']}`."
            )

    with st.container(border=True):
        st.subheader("Most relevant upcoming meeting")

        # Streamlit retains widget values between reruns. Synchronize the
        # meeting fields whenever the selected initiative changes.
        meeting_signature = (
            scenario["initiative_id"],
            scenario["meeting_id"],
            scenario["date"],
        )
        if st.session_state.get("meeting_context_signature") != meeting_signature:
            set_meeting_context(scenario)

        action, description = st.columns([1, 2.4])
        with action:
            if st.button("Refresh Relevant Meeting Context", width="stretch"):
                set_meeting_context(scenario)
                st.rerun()
        with description:
            st.caption("Refreshes the meeting context and synthetic evidence supplied to the selected repository skill.")

        left, right = st.columns([1.15, 1])
        with left:
            st.text_input("Meeting title", key="meeting_title")
            st.text_area("Meeting objective", key="meeting_objective", height=95)
        with right:
            st.date_input("Meeting date", key="meeting_date")
            st.text_area("Attendees / roles", key="attendees", height=95)

        records = build_scenario_records(context, scenario_name)
        st.info("Synthetic sources ready: " + ", ".join(record["name"] for record in records))

    with st.container(border=True):
        st.subheader(f"Run {skill_name}")
        st.caption(
            "The app uses SKILL.md as the workflow and guardrails, INPUTS.md as the evidence checklist, "
            "and OUTPUTS.md as the output structure."
        )
        disabled = bool(missing) or selected_skill["source"] != "repository"
        if st.button("Press to Create Relevant Executive Brief Materials", width="stretch", disabled=disabled):
            try:
                st.session_state.skill_result = run_repository_skill(selected_skill, context, scenario_name)
            except ValueError as error:
                st.error(str(error))

    if "skill_result" in st.session_state:
        render_skill_result(st.session_state.skill_result)

    with st.expander("View the selected repository skill definition"):
        if documents:
            st.caption("Read from the GitHub repository checkout deployed with this Streamlit app; no GitHub token is used.")
            labels = {"SKILL.md": "Workflow and guardrails", "INPUTS.md": "Required inputs", "OUTPUTS.md": "Expected outputs"}
            for filename in REQUIRED_DOCUMENTS:
                if filename in documents:
                    st.markdown(f"##### {labels[filename]}")
                    st.markdown(documents[filename])
        else:
            st.warning("No repository definition files were found for this skill.")


st.markdown(
    '<div class="hero"><h1>Chief of Staff Agent Demo</h1>'
    '<p>An exploratory demonstration of an executive assistant agent based on relevant skills - by Bita Massoudi</p></div>',
    unsafe_allow_html=True,
)
st.markdown(
    '<div class="safe-banner">This demonstration has no connection to any University of Washington (UW) production systems. '
    'All data used in this demo is synthetic and was created solely for demonstration purposes. Any resemblance to actual '
    'individuals, organizations, projects, or activities is entirely coincidental. The synthetic dataset and agent skills '
    'used in this demonstration are created by Bita Massoudi and are available on GitHub for evaluation and review.</div>',
    unsafe_allow_html=True,
)
st.caption(f"Synthetic dataset version: {DATASET_VERSION}")

context = build_synthetic_context(date.today())
scenarios = build_initiative_scenarios(context)
catalog = discover_skill_catalog(Path(__file__).parent)

st.session_state.setdefault("view_mode", "Initiative View")
st.session_state.setdefault("scenario_name", next(iter(scenarios)))
navigation_left, navigation_right = st.columns(2)
with navigation_left:
    if st.button("Initiative View", width="stretch", type="primary" if st.session_state.view_mode == "Initiative View" else "secondary"):
        st.session_state.view_mode = "Initiative View"
        st.rerun()
with navigation_right:
    if st.button("Skills View", width="stretch", type="primary" if st.session_state.view_mode == "Skills View" else "secondary"):
        st.session_state.view_mode = "Skills View"
        st.rerun()
st.caption(f"Current workspace: {st.session_state.view_mode}")

scenario_name = st.session_state.scenario_name
scenario = scenarios[scenario_name]

if st.session_state.view_mode == "Skills View":
    render_skills_view(context, scenarios, scenario_name, catalog)
    st.divider()
    st.caption("Prototype boundary: repository-driven skills, synthetic data only, no autonomous actions, and no production connections. Human review is required.")
    st.stop()

st.subheader("Choose an initiative")
scenario_name = st.selectbox("Initiative", list(scenarios), label_visibility="collapsed", key="scenario_name")
scenario = scenarios[scenario_name]
continuity = initiative_continuity(context, scenario["initiative_id"])

st.markdown("#### People connected to this initiative")
people_columns = st.columns(min(len(continuity["participants"]), 4))
for index, person in enumerate(continuity["participants"]):
    with people_columns[index % len(people_columns)]:
        st.markdown(f"**{person['name']}**  \n{person['role']}")

st.subheader("Executive timeline")
st.caption(f"Filtered to {scenario_name}: three weeks of operating history and two weeks of forward plans.")
st.markdown("#### Prior context")
past1, past2, past3 = st.columns(3)
past1.metric("Prior meetings", len(continuity["prior_meetings"]))
past2.metric("Prior decisions", len(continuity["prior_decisions"]))
past3.metric("Prior actions", len(continuity["prior_actions"]))
st.markdown("#### Forward view")
future1, future2, future3 = st.columns(3)
future1.metric("Upcoming meetings", len(continuity["upcoming_meetings"]))
future2.metric("Actions due and owners", len(continuity["actions_due"]))
future3.metric("Upcoming decisions", len(continuity["upcoming_decisions"]))

st.markdown("#### Meetings, decisions, and actions for the selected initiative")
meeting_col, decision_col, action_col = st.columns(3)
with meeting_col:
    st.markdown("##### Meetings")
    with st.container(border=True):
        st.markdown("**Prior**")
        for item in reversed(continuity["prior_meetings"]):
            st.markdown(f"- **{item['date']:%b %d}:** {item['title']}")
    with st.container(border=True):
        st.markdown("**Current and upcoming**")
        for item in continuity["current_meetings"]:
            st.markdown(f"- **Today · {item['date']:%b %d}:** {item['title']}")
        for item in continuity["upcoming_meetings"]:
            st.markdown(f"- **{item['date']:%b %d}:** {item['title']}")
with decision_col:
    st.markdown("##### Decisions")
    with st.container(border=True):
        st.markdown("**Prior**")
        for item in reversed(continuity["prior_decisions"]):
            source = context["meetings"][item["meeting_id"]]["title"]
            st.markdown(f"- **{item['date']:%b %d}:** {item['decision']}  \n  <span class='source'>{source}</span>", unsafe_allow_html=True)
    with st.container(border=True):
        st.markdown("**Upcoming**")
        for item in continuity["upcoming_decisions"]:
            source = context["meetings"][item["meeting_id"]]["title"]
            st.markdown(f"- **{item['date']:%b %d}:** {item['decision']}  \n  <span class='source'>{source}</span>", unsafe_allow_html=True)
with action_col:
    st.markdown("##### Actions")
    with st.container(border=True):
        st.markdown("**Prior**")
        for item in continuity["prior_actions"]:
            owner = context["participants"][item["owner"]]
            st.markdown(f"- **{item['status']} · Due {item['due_date']:%b %d}:** {item['action']}  \n  <span class='source'>Owner: {owner['name']} — {owner['role']}</span>", unsafe_allow_html=True)
    with st.container(border=True):
        st.markdown("**Upcoming**")
        for item in continuity["actions_due"]:
            owner = context["participants"][item["owner"]]
            st.markdown(f"- **{item['status']} · Due {item['due_date']:%b %d}:** {item['action']}  \n  <span class='source'>Owner: {owner['name']} — {owner['role']}</span>", unsafe_allow_html=True)

with st.expander("Explore the complete five-week synthetic calendar and supporting records"):
    rows = []
    for day in context["calendar"]:
        event = day["meeting"]
        rows.append({
            "Date": day["date"].strftime("%a, %b %d"),
            "Relative day": "Today" if day["offset"] == 0 else f"{day['offset']:+d}",
            "Meeting": event["title"] if event else "—",
            "Context": event["summary"] if event else "No scheduled executive meeting; continuity retained.",
        })
    st.dataframe(rows, width="stretch", hide_index=True)

with st.sidebar:
    st.header("Demonstration Safeguards")
    st.success("Chiefs of Staff Demo")
    for label in ("Human review required", "Source traceability enabled", "Session-only document use", "No production or Epic data"):
        st.checkbox(label, value=True, disabled=True)
    st.divider()
    st.subheader("Future state—not connected")
    st.caption("Outlook calendar · Teams summaries · SharePoint · Approved external intelligence")

st.divider()
st.caption("Switch to Skills View to run a repository-backed Chief of Staff skill against this synthetic initiative context.")
