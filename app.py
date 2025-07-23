import pandas as pd
from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = '1234567890abcdef'  # Change this to a secure key in production

DATA_FILE = "Task1_Summary-Finding.csv"

METRIC_MAP = {
    "revenue": "Total Revenue(Million$)",
    "net income": "Net Income",
    "assets": "Total Assets",
    "liabilities": "Total Liabilities",
    "cash flow": "Cash Flow",
    "revenue growth": "Revenue Growth(%)",
    "net income growth": "Net Income Growth (%)",
    "profit margin": "Profit Margin (%)"
}

def load_data():
    df = pd.read_csv(DATA_FILE)
    return df

def get_bool_col(keyword):
    if "revenue decline" in keyword:
        return "Revenue Decline?"
    if "net income decline" in keyword:
        return "Net Income Decline?"
    return None

def detect_metric(user_query):
    if ("revenue" in user_query) and ("growth" in user_query or "percentage" in user_query or "increase" in user_query):
        return "revenue growth"
    if ("net income" in user_query) and ("growth" in user_query or "percentage" in user_query or "increase" in user_query):
        return "net income growth"
    for k in METRIC_MAP:
        if k in user_query:
            return k
    return None

def chatbot_response(user_query):
    user_query = user_query.lower()
    df = load_data()

    companies = df["Company"].str.lower().unique()
    company = next((c for c in companies if c in user_query), None)
    if company:
        company_row = df[df["Company"].str.lower() == company]
    else:
        return "Please specify a company (e.g., Apple, Microsoft, Tesla)."

    import re
    year_matches = re.findall(r"(20\d{2})", user_query)
    year1 = year_matches[0] if len(year_matches) > 0 else None
    year2 = year_matches[1] if len(year_matches) > 1 else None

    metric_key = detect_metric(user_query)
    bool_key = get_bool_col(user_query)

    if bool_key and year1:
        row = company_row[company_row["Year"] == float(year1)]
        if row.empty:
            return f"No data found for {company.title()} in {year1}."
        val = row.iloc[0][bool_key]
        return f"{company.title()}'s {bool_key.replace('?', '')} in {year1}: {'Yes' if val else 'No'}"

    if metric_key and "growth" in metric_key and year1 and year2:
        row1 = company_row[company_row["Year"] == float(year1)]
        row2 = company_row[company_row["Year"] == float(year2)]
        if row1.empty or row2.empty:
            return f"Not enough data to calculate {metric_key.replace('_',' ')} from {year1} to {year2}."
        val1 = row1.iloc[0][METRIC_MAP["revenue"]]
        val2 = row2.iloc[0][METRIC_MAP["revenue"]]
        try:
            pct_growth = ((val2 - val1) / val1) * 100
            return (f"{company.title()}'s revenue grew by {pct_growth:.2f}% from {year1} to {year2} "
                    f"(from {val1:,.0f}$ to {val2:,.0f}$).")
        except Exception as e:
            return "Could not compute the growth value."

    if metric_key and year1:
        metric_col = METRIC_MAP[metric_key]
        row = company_row[company_row["Year"] == float(year1)]
        if row.empty:
            return f"No data found for {company.title()} in {year1}."
        val = row.iloc[0][metric_col]
        try:
            formatted_val = f"{val:,.0f}$" if isinstance(val, (int, float, float)) else f"{val}$"
        except:
            formatted_val = f"{val}$"
        return f"{company.title()}'s {metric_col} in {year1} was {formatted_val}."

    if company and not year1:
        return f"Please specify the year for {company.title()} (e.g., 2023, 2024)."

    return ("Sorry, I can only answer questions about specific companies, years, "
            "and standard metrics such as revenue, growth, and profit margin.")

from flask import Flask, render_template, request, session, redirect, url_for

# ... (rest of your app)

@app.route("/clear", methods=["POST"])
def clear():
    session.pop("history", None)
    return redirect(url_for("index"))

@app.route("/", methods=["GET", "POST"])
def index():
    if "history" not in session:
        session["history"] = []
    history = session["history"]

    if request.method == "POST":
        user_input = request.form["user_input"]
        bot_reply = chatbot_response(user_input)
        history.append({"role": "user", "text": user_input})
        history.append({"role": "bot", "text": bot_reply})
        session["history"] = history

    return render_template("index.html", history=history)

if __name__ == "__main__":
    app.run(debug=True)
