# bcgx-genai-forage-chatbot
AI-powered Financial Chatbot (Flask App) Interactive GenAI chatbot that answers financial data questions from CSV files. Built for the BCGx GenAI Job Simulation on Forage by Chonnikarn Yuthchana.

A rule-based, AI-powered financial chatbot for querying company financial data from 2022–2024. Built with Python, Flask, and Pandas, this project features an interactive, modern web chat interface inspired by leading conversational AI designs.

---

## 🚀 Overview

- **Purpose:** Quickly access, compare, and analyze company financial metrics.
- **Technologies:** Python, Flask, Pandas, HTML/CSS (responsive, chat-style UI).
- **Data:** Reads from an updatable CSV file (`Task1_Summary-Finding.csv`).

---

## ⚙️ How It Works

- Loads financial data from a CSV file.
- Uses rule-based logic to interpret queries (company, year, metric).
- Retrieves and displays relevant data using Pandas.
- Maintains chat history (per session) in a clean, chat-bubble format.
- Fully responsive design and finance-themed color palette.

---

## 💡 Supported Queries

The chatbot answers questions about:

- **Financial Metrics:**
  - Revenue
  - Net Income
  - Total Assets
  - Total Liabilities
  - Cash Flow
  - Profit Margin (%)
- **Growth Comparisons:**
  - Revenue growth between two years
  - Net income growth between two years
- **Performance Checks:**
  - Revenue or net income decline in a specific year

**Example queries:**
- `What is Apple’s revenue in 2024?`
- `What was Microsoft’s net income growth from 2023 to 2024?`
- `Did Tesla’s revenue decline in 2023?`
- `What is Tesla’s profit margin in 2022?`

---

## 📝 How to Update Data

- Edit or replace `Task1_Summary-Finding.csv` with new data (keep column names the same).
- Restart the chatbot. It will use the updated data automatically.

---

## ⚠️ Limitations

- **Rule-based:** Only understands queries matching its logic and keywords.
- **No fuzzy matching:** Typos, unusual phrasing, or unsupported metrics won’t be recognized.
- **Static data:** Does not fetch live/external data; limited to the CSV provided.
- **No context memory:** Does not support conversational follow-ups outside of the current question.

---

## 🛠️ How to Run

1. **Install dependencies:**
    ```bash
    pip install flask pandas
    ```
2. **Project structure:**
    ```
    your_project/
      app.py
      Task1_Summary-Finding.csv
      templates/
        index.html
    ```
3. **Start the app:**
    ```bash
    python app.py
    ```
4. **Open your browser:**
    - Go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## ✨ Credits

- Developed for the BCGx AI/Finance Virtual Internship, 2025.
- Interface design inspired by modern conversational AI apps.

---

