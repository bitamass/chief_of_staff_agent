# Chief of Staff Agent Demo

This independent exploratory Streamlit prototype applies repository-defined Chief of Staff skills to a linked synthetic executive operating context. The selected skill's `SKILL.md`, `INPUTS.md`, and `OUTPUTS.md` files determine the workflow contract, required-evidence checklist, and output structure.

`synthetic_context.py` is the single source of truth for a fully synthetic five-week executive operating context. It covers 21 days before the current date through 14 days after it, including day-by-day calendar entries, fictional participants, meeting notes, decisions, action items, initiatives, deliverables, and charters. The app uses the initiatives themselves as selectable scenarios and derives each initiative's relevant meeting, agenda, prior notes, background, questions, and next steps from its linked records.

The initiative selector appears above the timeline. Changing it immediately filters the people, prior meetings, prior decisions, prior actions, upcoming meetings, actions due and owners, upcoming decisions, and detailed supporting lists to the selected initiative.

The four synthetic initiatives are Clinical Operations Modernization, Agentification Pilot, Monthly Business Review, and Clinical Research Developments. All names, roles, meetings, decisions, actions, and supporting records are fictional and created only for this demonstration.

The app discovers numbered capability folders and their child skill folders directly from the GitHub repository checkout deployed by Streamlit. For execution, every skill must include `SKILL.md`, `INPUTS.md`, and `OUTPUTS.md`. This does not require a GitHub API token or a live network request. Repository changes appear after Streamlit redeploys the latest commit.

The repository-driven runner uses the selected initiative's synthetic meetings, decisions, actions, participants, charter, and deliverables as evidence. It builds the report sections from `OUTPUTS.md`, assesses input coverage from `INPUTS.md`, preserves the `SKILL.md` workflow and guardrail contract, and produces source-linked Markdown and Word outputs. The runner is deterministic and does not use a model API.

## Run on Windows

1. Extract the ZIP file.
2. Open the extracted folder.
3. Click the File Explorer address bar, type `cmd`, and press Enter.
4. Install dependencies:

   `python -m pip install -r requirements.txt`

5. Start the app:

   `python -m streamlit run app.py`

6. Choose an initiative and open **Skills View**.
7. Choose a capability and skill, select **Press to update to relevant skills**, and then select **Press to Create Relevant Executive Brief Materials**.

## Prototype boundary

Use sample data only. The app does not connect to Outlook, Teams, Epic, SharePoint, or any UW production system. Human review is required before using or distributing generated content.
