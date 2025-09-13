# 📰 Hacker News Top Article Scraper

A Python script that scrapes [Hacker News](https://news.ycombinator.com/) and identifies the **most upvoted article** on the front page using **BeautifulSoup**.

---

## 🚀 Features

* Fetches live HTML from Hacker News
* Extracts article **titles** and **links**
* Collects the **upvote count** for each article
* Handles cases where an article has **no votes yet**
* Prints the most popular article (title, upvotes, and link)

---

## 📂 Project Structure

```
.
├── main.py   # Scraper logic using BeautifulSoup & Requests
```

---

## ⚙️ Setup

### 1) Install Dependencies

```bash
pip install requests beautifulsoup4
```

### 2) Run Script

```bash
python main.py
```

---

## ▶️ Example Output

```
Most upvoted article: YC Interview Prep Guide
Number of upvotes: 245 points
Available at: https://example.com/yc-interview-prep
```

(Actual results vary since Hacker News updates constantly.)

---

## 🧪 Notes

* Uses **live Hacker News site**, so output will change each run.
* Optionally, you can point it at the **static practice page**:

  ```python
  # response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")
  ```
* Robust parsing ensures missing vote counts are handled gracefully.

---

## 🔮 Possible Extensions

* Export all articles with votes into a CSV or JSON
* Schedule as a cron job for daily top article alerts
* Add filtering by minimum votes
* Send notifications via email/Twilio (similar to the Flight Deal Finder project)

---


