# Chief of Staff Agent — Guided Demonstration

This independent exploratory Streamlit prototype demonstrates one Chief of Staff skill: Executive Meeting Preparation. It prepares decision-ready briefs from curated sample agendas, prior notes, and background documents. Other Chief of Staff capabilities described in the broader concept are not active in this demonstration.

The backend also contains a fully synthetic five-week executive operating context. It covers 21 days before the current date through 14 days after it, including day-by-day calendar entries, fictional participants, meeting notes, decisions, action items, initiatives, deliverables, and charters. Relative dates are recalculated whenever the app runs, and linked record identifiers show how past decisions affect today's work and future meetings.

## Run on Windows

1. Extract the ZIP file.
2. Open the extracted folder.
3. Click the File Explorer address bar, type `cmd`, and press Enter.
4. Install dependencies:

   `python -m pip install -r requirements.txt`

5. Start the app:

   `python -m streamlit run app.py`

6. Choose one of the three demonstration scenarios, select **Load Sample Meeting Materials**, and then select **Create Executive Meeting Brief**.

## Prototype boundary

Use sample data only. The app does not connect to Outlook, Teams, Epic, SharePoint, or any UW production system. Human review is required before using or distributing generated content.
