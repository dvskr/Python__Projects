import requests
import os
import csv
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
POLYGON_API_KEY = os.getenv("POLYGON_API_KEY")

LIMIT = 1000
url = f"https://api.polygon.io/v3/reference/tickers?limit={LIMIT}&apiKey={POLYGON_API_KEY}"

response = requests.get(url)
data = response.json()

tickers = []

# Collect first batch
for ticker in data.get("results", []):
    tickers.append(ticker)

# Handle pagination
while "next_url" in data:
    print("requesting next page", data["next_url"])
    response = requests.get(data["next_url"] + f"&apiKey={POLYGON_API_KEY}")
    data = response.json()
    for ticker in data.get("results", []):
        tickers.append(ticker)

# Use first ticker as schema reference
example_ticker = tickers[0] if tickers else {}
fieldnames = list(example_ticker.keys())

# Write tickers to CSV
output_csv = "tickers.csv"
with open(output_csv, mode="w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for t in tickers:
        # ensure missing keys don’t break
        row = {key: t.get(key, "") for key in fieldnames}
        writer.writerow(row)

print(f"Wrote {len(tickers)} rows to {output_csv}")
