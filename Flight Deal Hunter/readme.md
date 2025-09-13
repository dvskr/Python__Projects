# ✈️ Flight Deal Finder

A production‑minded Python project that integrates **Amadeus**, **Sheety**, **Twilio**, and **SMTP** to monitor destinations, search flight offers, pick the **cheapest option**, and **notify subscribers** via SMS/WhatsApp/Email.

---

## 🚀 Highlights

* Fetch & maintain **IATA codes** for destinations (via Sheety)
* Query **direct & indirect** flight offers (Amadeus Self‑Service APIs)
* Identify the **cheapest** itinerary with basic stopover awareness
* Broadcast alerts over **Twilio (SMS/WhatsApp)** and **SMTP email**
* Clean `.env`‑driven configuration and modular codebase

---

## 🧱 Architecture

```
Google Sheet (destinations & users)  ──┐
                                     │  (Sheety API)
Data Manager  <───────────────────────┘
      │
      │     (OAuth2 client credentials)
      ▼
Flight Search ─────────► Amadeus: IATA Lookup + Flight Offers
      │
      ▼
Flight Data  ──► pick cheapest offer (direct first, then fallback to non‑stop=false)
      │
      ▼
Notification Manager ─► Twilio (SMS/WhatsApp) + SMTP Email
      │
      ▼
   End Users
```

---

## 📂 Project Structure

```
.
├── data_manager.py          # Sheety: destinations & users (GET/PUT)
├── flight_data.py           # FlightData model + find_cheapest_flight()
├── flight_search.py         # Amadeus: token, IATA lookup, flight offers
├── notification_manager.py  # Twilio & SMTP notifications
├── main.py                  # Orchestration (ETL + alerts)
├── requirements.txt         # Dependencies
└── .env                     # Credentials (keep out of VCS!)
```

---

## ⚙️ Setup

### 1) Clone & Install

```bash
git clone https://github.com/yourusername/flight-deal-finder.git
cd flight-deal-finder
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 2) Configure Environment

Create a `.env` file in the project root:

```env
SHEETY_USERNAME="your_sheety_username"
SHEETY_PASSWORD="your_sheety_password"
SHEETY_PRICES_ENDPOINT="your_prices_sheet_endpoint"
SHEETY_USERS_ENDPOINT="your_users_sheet_endpoint"
AMADEUS_API_KEY="your_amadeus_api_key"
AMADEUS_SECRET="your_amadeus_secret"
TWILIO_SID="your_twilio_sid"
TWILIO_AUTH_TOKEN="your_twilio_auth_token"
TWILIO_VIRTUAL_NUMBER="+1xxxxxxxxxx"
TWILIO_VERIFIED_NUMBER="+1yyyyyyyyyy"
TWILIO_WHATSAPP_NUMBER="+1zzzzzzzzzz"  # Twilio Sandbox or approved sender
EMAIL_PROVIDER_SMTP_ADDRESS="smtp.gmail.com"  # or your provider
MY_EMAIL="your_email@example.com"
MY_EMAIL_PASSWORD="your_app_password"
```

> **Tip:** Use an **App Password** for Gmail/Outlook/Yahoo. For WhatsApp, enroll your number in the Twilio Sandbox or use an approved sender.

### 3) Prepare Sheets (Sheety)

* **Prices sheet** (e.g., `prices` tab) with columns like: `city`, `iataCode`, `lowestPrice`.
* **Users sheet** (e.g., `users` tab) with an email column referenced in code as `whatIsYourEmail?` (adjust if your column name differs).
* Create **Sheety** endpoints for both tabs and paste them into `.env`.

---

## ▶️ Run

```bash
python main.py
```

What happens:

1. Load destinations from Sheety; backfill missing **IATA codes** using Amadeus.
2. For each destination, search **direct** flights from the origin (default `LON`).
3. If no direct results, retry with **nonStop=false** (allow stopovers).
4. Compute the **cheapest** option; if below your sheet’s `lowestPrice`, send notifications.

> Origin is set in `main.py` via `ORIGIN_CITY_IATA`. Change as needed (e.g., `JFK`, `DFW`).

---

## 🔍 Key Modules

* **`data_manager.py`** — Wraps Sheety (GET/PUT) and exposes `get_destination_data()`, `update_destination_codes()`, `get_customer_emails()`.
* **`flight_search.py`** — Handles Amadeus token (`_get_new_token()`), IATA lookup (`get_destination_code()`), and flight offers (`check_flights()`).
* **`flight_data.py`** — `FlightData` model + `find_cheapest_flight()` to extract the best‑priced itinerary and stop count.
* **`notification_manager.py`** — Twilio SMS/WhatsApp and SMTP email broadcast.
* **`main.py`** — End‑to‑end orchestration, simple throttling to avoid API rate limits.

---

## 📦 Requirements

See `requirements.txt`:

* `python-dotenv==1.0.1`
* `Requests==2.32.3`
* `twilio==9.1.1`

Python ≥ 3.10 recommended.

---

## 🧪 Environment & Testing Notes

* Use separate **test** credentials for Amadeus (test environment endpoints are already set) and Twilio Sandbox for WhatsApp.
* Sheety endpoints can point at **staging** copies of your sheets to avoid spamming real users.
* Add `time.sleep()` between API calls (already present) to reduce rate‑limit risks.

---

## 🔒 Security

* Never commit `.env` or secrets; add `.env` to `.gitignore`.
* Prefer provider **App Passwords** over raw account passwords for SMTP.
* Rotate API keys/credentials regularly and restrict Twilio senders/receivers.

---

## 🛡️ Error Handling & Troubleshooting

* **Amadeus 401/403**: Verify `AMADEUS_API_KEY/SECRET`, token flow, and environment (test vs live).
* **Empty flight data**: The code returns `"N/A"` safely; consider logging the offending query.
* **Sheety 4xx/5xx**: Check endpoint URL, auth, and sheet/tab names. Ensure your columns match the code.
* **Email not delivered**: Confirm SMTP host/port, app password, and that `starttls()` is supported by your provider.
* **WhatsApp not delivered**: Ensure the recipient joined the Twilio Sandbox and messaging is enabled in your region.

---

## 🧭 Roadmap

* Token reuse & caching (avoid fetching a new Amadeus token each run)
* Multi‑origin & multi‑currency support
* Persistence layer for **price history** and deduped notifications
* Streamlit/Flask dashboard with simple rules engine (e.g., per‑user max price, date windows)
* Basic retries/exponential backoff for transient API errors

---

## 📄 License

MIT (or your preferred license). Add a `LICENSE` file if you plan to open‑source.

---

## 🙌 Acknowledgments

* Amadeus Self‑Service APIs
* Sheety for effortless Google Sheet endpoints
* Twilio Programmable Messaging

> If you share this on LinkedIn/GitHub, consider adding badges (Python version, dependencies) and a short demo GIF of the console run + a sample WhatsApp alert.
