# bcgx-genai-forage-chatbot
AI-powered Financial Chatbot (Flask App) Interactive GenAI chatbot that answers financial data questions from CSV files. Built for the BCGx GenAI Job Simulation on Forage by Chonnikarn Yuthchana.

==========================

Overview
--------
This project is a rule-based, AI-powered financial chatbot designed for interactive querying of company financial data from 2022–2024. Built with Python (Flask + Pandas), it offers a modern, web-based chat interface for efficient exploration and analysis of company financial metrics. The chatbot emphasizes user-friendly communication and supports session-based conversation history.

Principles and Features
-----------------------
- **Rule-Based Logic:**  
  The chatbot uses predefined logic and keyword matching to understand and answer queries about company performance.
- **Structured Data Retrieval:**  
  Financial data is sourced from a structured CSV file (`Task1_Summary-Finding.csv`). Pandas is used to filter and extract relevant information in real time.
- **Clear Financial Communication:**  
  Responses are crafted to simplify complex financial data and present it in an accessible, easy-to-read format.
- **Session Memory:**  
  Chat history is maintained during each session, allowing users to follow the flow of questions and answers.
- **Modern User Experience:**  
  The interface features a clean, finance-themed color palette, chat bubbles, and is responsive for desktop and mobile use.

Supported Queries
-----------------
You can ask questions about:
- Company revenue, net income, total assets, total liabilities, cash flow, and profit margin for a specific year.
- Growth rates for revenue and net income between two years (e.g., "What was Microsoft’s revenue growth from 2023 to 2024?")
- Whether a company's revenue or net income declined in a given year.

**Example queries:**
- What is Apple’s revenue in 2024?
- What was Microsoft’s net income growth from 2023 to 2024?
- Did Tesla’s revenue decline in 2023?
- What is Tesla’s profit margin in 2022?

How to Update Data
------------------
- Edit or replace `Task1_Summary-Finding.csv` with new or updated financial data.  
  (Keep the column names and structure the same for compatibility.)
- The chatbot will use the new data the next time the application is restarted.

Limitations and Considerations
-----------------------------
- **Rule-Based Only:**  
  The chatbot recognizes queries based on keyword logic; it may not understand spelling errors, synonyms, or conversational follow-ups.
- **No Real-Time or External Data:**  
  All responses are based on the current CSV file; the chatbot does not fetch or update from live sources.
- **Static Knowledge:**  
  Only companies, years, and metrics present in the CSV can be queried.
- **Extensibility:**  
  To expand beyond the current prototype, you could integrate more advanced NLP, connect to external financial APIs, or support broader conversational context.

How to Run
----------
1. Make sure you have Python 3.8+ installed.
2. Install required dependencies:
    pip install flask pandas
3. Place `app.py`, `Task1_Summary-Finding.csv`, and the `templates` folder (with `index.html`) in the same directory.
4. Start the chatbot:
    python app.py
5. Open your browser and navigate to:
    http://127.0.0.1:5000/

Opportunities for Enhancement
-----------------------------
- Add support for more natural language and fuzzy matching.
- Integrate real-time financial data sources or APIs.
- Expand to support additional financial metrics and analytics.
- Enhance conversation flow with multi-turn dialogue and suggestions.

Credits
-------
- Developed for the BCGx AI/Finance Virtual Internship, 2025.
- Interface inspired by modern conversational AI platforms.

