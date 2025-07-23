
# BCGx GenAI Financial Chatbot

> **AI-powered, rule-based chatbot for interactive financial data analysis.**  
> Built with Python, Flask, and Pandas as part of the BCGx GenAI Job Simulation on Forage  
> by **Chonnikarn Yuthchana**.

---

## 🚀 Overview

A web-based financial chatbot that enables users to quickly query, compare, and analyze company financial metrics from structured data. Featuring a modern conversational interface, animated chat bubbles, and a rule-based engine for interpreting financial queries.

- **Purpose:** Instant access to company financial metrics and trends, presented conversationally.
- **Tech:** Python, Flask, Pandas, HTML/CSS (responsive, chat-style UI).
- **Data:** Reads from an easily updatable CSV file (`Task1_Summary-Finding.csv`).

---

## 💡 What Can the Chatbot Answer?

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

## 🛠️ Features

- Clean, chat-style web UI (with animated typing effect)
- Session-based chat history (cleared with one click)
- Responsive, finance-inspired color theme
- CSV-driven: simply replace/update your financial data file
- Easy to customize and extend

---


## ⚙️ How It Works

- Loads financial data from a CSV file.
- Uses rule-based logic to interpret queries (company, year, metric).
- Retrieves and displays relevant data using Pandas.
- Maintains chat history (per session) in a clean, chat-bubble format.
- Fully responsive design and finance-themed color palette.

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


## 📁 How to Run the Project

1. **Clone this repo**  
    ```bash
    git clone https://github.com/yourusername/bcgx-genai-forage-chatbot.git
    cd bcgx-genai-forage-chatbot
    ```

2. **Install Python dependencies**  
    ```bash
    pip install flask pandas
    ```

3. **Check project structure**  
    ```
    bcgx-genai-forage-chatbot/
      app.py
      Task1_Summary-Finding.csv
      requirements.txt
      templates/
        index.html
      static/
        styles.css
    ```

4. **Start the app**  
    ```bash
    python app.py
    ```
    (or `flask run` if you prefer)

5. **Open your browser**  
    - Go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## 📝 How to Update the Financial Data

- Edit or replace `Task1_Summary-Finding.csv` (keep the same columns: Company, Year, Revenue, etc).
- Restart the chatbot.
- The new data will be loaded automatically.

---

## ⚠️ Limitations

- **Rule-based logic:** Only recognizes supported keywords/phrases.
- **No typo/fuzzy matching:** Misspelled company names or unexpected phrasing won't be understood.
- **Static data:** Limited to the CSV provided; does not fetch real-time data.
- **No deep context:** Each query is answered independently.

---

## 📸 Screenshots

*Add your screenshots here for extra portfolio appeal!*

---

## ✨ Credits

- Developed for the [BCGx GenAI Job Simulation](https://www.theforage.com/virtual-internships/prototype/oF3i9qjq9GbMAv2Hh/BCGx-GenAI-Job-Simulation) (Forage Virtual Experience), 2025.
- Designed & implemented by **Chonnikarn Yuthchana**.
- Interface inspired by leading conversational AI products.

---

## 📢 Disclaimer

*This chatbot is a simulation for the BCGx GenAI Job Simulation.  
It does **not** provide real financial advice.*
