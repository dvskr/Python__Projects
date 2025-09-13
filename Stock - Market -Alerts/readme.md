# 📈 Stock News SMS Alert

Monitor a stock’s daily price movement with **Alpha Vantage**. If the move exceeds a configurable threshold, fetch the latest headlines from **NewsAPI** and deliver them to your phone via **Twilio SMS**.

> Works great for quick market nudges (earnings, major news days). Built around a simple Python script using `requests` and `twilio`.

---

## ✨ What it does

* Pulls **daily close prices** for a ticker (e.g., `TSLA`)
* Calculates **percentage change** between **yesterday** and **the day before**
* If change > **threshold** (default 5% recommended), fetches **top 3 headlines** for the company
* Sends each headline + brief as an **SMS** via **Twilio**

---

## 🧱 Repo structure (suggested)

```
.
├── stock_news_alert.py          # Your main script (from this repo)
├── README.md                    # This file
├── .env.example                 # Copy to .env and fill in secrets (optional)
├── requirements.txt             # requests, twilio
└── .gitignore                   # excludes .env, __pycache__, etc.
```

**`requirements.txt`** (suggested):

```
requests
twilio
python-dotenv  # optional if you want .env support
```

**`.gitignore`** (suggested):

```
# Python
__pycache__/
*.pyc

# Env & secrets
.env
.env.*
```

---

## 🛠️ Prerequisites

* **Python** 3.8+
* **Alpha Vantage** API key → [https://www.alphavantage.co/support/#api-key](https://www.alphavantage.co/support/#api-key)
* **NewsAPI** key → [https://newsapi.org/register](https://newsapi.org/register)
* **Twilio** account & a phone number → [https://www.twilio.com/](https://www.twilio.com/)

  * Verify your personal phone number in Twilio (required for trial accounts)

> **Heads‑up:** Alpha Vantage free tier has a request limit (typically 5 calls/minute, 500/day). NewsAPI also has usage limits. Twilio SMS costs apply (trial accounts prepend messages with a trial notice).

---

## 🔐 Configuration

You can configure the script via **environment variables** (recommended) or by **editing constants** inside the script.

### Option A: Environment variables (recommended)

Create a `.env` file (if you use `python-dotenv`) or export variables in your shell.

**`.env.example`**

```
# Twilio
VIRTUAL_TWILIO_NUMBER="+1234567890"
VERIFIED_NUMBER="+1987654321"
TWILIO_SID="ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
TWILIO_AUTH_TOKEN="xxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# APIs
STOCK_API_KEY="your_alpha_vantage_key"
NEWS_API_KEY="your_newsapi_key"

# Logic
STOCK_NAME="TSLA"
COMPANY_NAME="Tesla Inc"
PRICE_MOVE_THRESHOLD=5     # percent; integer or float
NEWS_COUNT=3               # top N articles to send
```

**Bash / macOS / Linux:**

```bash
export VIRTUAL_TWILIO_NUMBER="+1234567890"
export VERIFIED_NUMBER="+1987654321"
export TWILIO_SID="AC..."
export TWILIO_AUTH_TOKEN="..."
export STOCK_API_KEY="..."
export NEWS_API_KEY="..."
export STOCK_NAME="TSLA"
export COMPANY_NAME="Tesla Inc"
export PRICE_MOVE_THRESHOLD=5
export NEWS_COUNT=3
```

**PowerShell (Windows):**

```powershell
$env:VIRTUAL_TWILIO_NUMBER = "+1234567890"
$env:VERIFIED_NUMBER = "+1987654321"
$env:TWILIO_SID = "AC..."
$env:TWILIO_AUTH_TOKEN = "..."
$env:STOCK_API_KEY = "..."
$env:NEWS_API_KEY = "..."
$env:STOCK_NAME = "TSLA"
$env:COMPANY_NAME = "Tesla Inc"
$env:PRICE_MOVE_THRESHOLD = "5"
$env:NEWS_COUNT = "3"
```

### Option B: Edit the script constants

Inside `stock_news_alert.py`, set:

```python
VIRTUAL_TWILIO_NUMBER = "your virtual twilio number"
VERIFIED_NUMBER = "your phone number verified with Twilio"

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_API_KEY = "YOUR OWN API KEY FROM ALPHAVANTAGE"
NEWS_API_KEY = "YOUR OWN API KEY FROM NEWSAPI"
TWILIO_SID = "YOUR TWILIO ACCOUNT SID"
TWILIO_AUTH_TOKEN = "YOUR TWILIO AUTH TOKEN"
```

---

## 📦 Install & Run

### 1) Clone

```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
```

### 2) (Optional) Use a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
```

### 3) Install deps

```bash
pip install -r requirements.txt
# or
pip install requests twilio python-dotenv
```

### 4) Run

```bash
python stock_news_alert.py
```

> If the daily % move exceeds your threshold, you’ll receive up to `NEWS_COUNT` SMS messages.

---

## 🔍 How it works (logic)

1. **Alpha Vantage** → `TIME_SERIES_DAILY` endpoint → parse the JSON → collect the last two closing prices
2. Compute **difference** and **percentage change**
3. If `abs(percentage_change) >= PRICE_MOVE_THRESHOLD` → **NewsAPI** search (`qInTitle=COMPANY_NAME`)
4. Take the **first N** articles (default N=3) and format messages
5. **Twilio** sends each article as a separate SMS: `"TICKER: 🔺/🔻X%\nHeadline: ...\nBrief: ..."`

**Example SMS**

```
TSLA: 🔺6%
Headline: Tesla beats earnings expectations
Brief: Revenue and margins surprise; shares jump in after-hours.
```

---

## ⚙️ Optional enhancements

* **.env support**: Add \`python
