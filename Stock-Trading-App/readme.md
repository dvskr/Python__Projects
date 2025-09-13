# 📈 Polygon.io Tickers Exporter

A concise, production‑minded Python utility that pulls **reference tickers** from the Polygon.io v3 API, follows **cursor‑based pagination** (`next_url`), and writes the unified payload to a clean **CSV**. The script is environment‑driven, resilient to sparse fields, and ready to slot into a data pipeline.

---

## 🚀 What This Does

* Calls `GET /v3/reference/tickers` with a configurable `limit` (default 1000).
* Iterates `next_url` until exhaustion, consolidating **all pages**.
* Infers the CSV schema from the first item returned, and safely handles missing keys for subsequent records.
* Emits `tickers.csv` with a stable header and one row per ticker document.

---

## 🧩 How It Works (from `script.py`)

* Loads `POLYGON_API_KEY` from `.env` using `python‑dotenv`.
* Issues the first request: `https://api.polygon.io/v3/reference/tickers?limit=1000&apiKey=...`.
* Appends results, then follows `data["next_url"]` (when present), re‑issuing requests until there are no more pages.
* Uses the **first** ticker dict as the header template; writes all rows via `csv.DictWriter`, backfilling missing keys with empty strings.

> Design choice: inferring the schema from the first element ensures a deterministic header while avoiding an O(n) union across all keys. If you need a full key union, see the *Extensions* section.

---

## 📂 Project Layout

```
.
├── script.py          # Main: fetch, paginate, write CSV
├── requirements.txt   # requests, openai (optional), dotenv
└── .env               # POLYGON_API_KEY
```

---

## ⚙️ Setup

### 1) Install Dependencies

```bash
pip install -r requirements.txt
```

### 2) Configure Environment

Create `.env` with your key:

```env
POLYGON_API_KEY="your_polygon_api_key_here"
```

### 3) Run

```bash
python script.py
```

Output example:

```
requesting next page https://api.polygon.io/v3/reference/tickers?cursor=...
requesting next page https://api.polygon.io/v3/reference/tickers?cursor=...
Wrote 9,893 rows to tickers.csv
```

---

## 🧪 Notes & Assumptions

* **Pagination:** Polygon uses cursor‑based pagination; the script follows `next_url` until absent.
* **Schema Stability:** The first record defines `fieldnames`. New/rare fields appearing later will be dropped unless you adopt the “union of keys” strategy below.
* **Encoding:** CSV is written with `encoding="utf-8"` and safe missing‑key handling.
* **Rate Limits:** If you hit 429s, introduce `time.sleep()` between pages or request higher rate limits.

---

## 🛡️ Error Handling & Hardening Ideas

* Add HTTP status checks (`response.raise_for_status()`), retry/backoff (e.g., `tenacity`), and defensive guards for `data.get("results", [])`.
* Validate that `tickers` is non‑empty before deriving `fieldnames`; fall back to a minimal header when empty.
* Log metadata (page count, total rows, runtime) for observability.

---

## 🔧 Extensions (drop‑in enhancements)

* **Union Schema:** Build a union of keys across all pages, then write header → ensures no field loss.
* **CLI Flags:** `--market`, `--type`, `--active`, `--limit`, `--dest` for flexible usage.
* **Pandas Export:** Convert to DataFrame → `to_parquet()`/`to_csv(index=False)` for analytics.
* **Incremental Loads:** Track last cursor or `updated` watermark; persist to a DB (SQLite/Postgres/Snowflake).
* **Validation:** Add lightweight Pydantic model to validate each ticker payload.

---

## ✅ Requirements

See `requirements.txt`:

* `requests`
* `dotenv` (aka `python-dotenv`)
* `openai` (not used by the script; keep if you plan to enrich with LLM‑based tagging)

Python 3.10+ recommended.

---

## 📄 License

MIT (or your preferred). Add a `LICENSE` file if open‑sourcing.

---

## 🙌 Attribution

Polygon.io Reference Data API — thanks for a clean cursor‑based model that scales well for exports.
