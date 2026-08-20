# Chief of Staff Agent — Guided Demonstration

This independent exploratory Streamlit prototype demonstrates one possible executive meeting-preparation use case. It prepares decision-ready briefs from curated sample agendas, prior notes, and background documents. It also demonstrates source traceability and a lightweight agent-governance record without connecting to UW production systems.

## Run on Windows

1. Extract the ZIP file.
2. Open the extracted folder.
3. Click the File Explorer address bar, type `cmd`, and press Enter.
4. Install dependencies:

   `python -m pip install -r requirements.txt`

5. Start the app:

   `python -m streamlit run app.py`

6. Choose one of the three demonstration scenarios, select **Load Selected Scenario**, and then select **Generate Decision-Ready Brief**.

## Prototype boundary

Use sample data only. The app does not connect to Outlook, Teams, Epic, SharePoint, or any UW production system. Human review is required before using or distributing generated content.
