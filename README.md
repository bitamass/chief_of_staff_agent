# Chief of Staff Agent — Guided Demonstration

This independent exploratory Streamlit prototype demonstrates one Chief of Staff skill: Executive Meeting Preparation. It prepares decision-ready briefs from agenda, prior-note, and background-memo views generated from one linked synthetic operating context. Other Chief of Staff capabilities described in the broader concept are not active in this demonstration.

`synthetic_context.py` is the single source of truth for a fully synthetic five-week executive operating context. It covers 21 days before the current date through 14 days after it, including day-by-day calendar entries, fictional participants, meeting notes, decisions, action items, initiatives, deliverables, and charters. The app uses the initiatives themselves as selectable scenarios and derives each initiative's relevant meeting, agenda, prior notes, background, questions, and next steps from its linked records.

The initiative selector appears above the timeline. Changing it immediately filters the people, prior meetings, prior decisions, prior actions, upcoming meetings, actions due and owners, upcoming decisions, and detailed supporting lists to the selected initiative.

The four synthetic initiatives are Clinical Operations Modernization, Agentification Pilot, Monthly Business Review, and Clinical Research Developments. All names, roles, meetings, decisions, actions, and supporting records are fictional and created only for this demonstration.

The app discovers numbered capability folders and their child skill folders directly from the repository. It currently connects selected meeting-intelligence, decision-log, and initiative-portfolio skills to the synthetic context; other discovered skills remain clearly labeled as framework-only until their instruction and input contracts are implemented.

## Run on Windows

1. Extract the ZIP file.
2. Open the extracted folder.
3. Click the File Explorer address bar, type `cmd`, and press Enter.
4. Install dependencies:

   `python -m pip install -r requirements.txt`

5. Start the app:

   `python -m streamlit run app.py`

6. Choose an initiative, select **Update Relevant Meeting Materials**, and then select **Create Executive Meeting Brief**.

## Prototype boundary

Use sample data only. The app does not connect to Outlook, Teams, Epic, SharePoint, or any UW production system. Human review is required before using or distributing generated content.
