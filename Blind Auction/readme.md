# 🏆 Silent Auction Console App

A fun and interactive console-based Python application that simulates a **silent auction**. This program allows multiple participants to bid anonymously, and finally reveals the highest bidder!

---

## 🎯 Objective

To create a basic auction system where users can enter their name and bid amount. The app collects all bids and determines the winner with the highest bid.

---

## 📁 Project Structure

```
auction_bid_game/
├── main.py       # Main application logic for collecting bids and determining winner
├── art.py        # ASCII logo art displayed at the beginning
```

---

## 🚀 How It Works

1. When the program starts, it displays a decorative ASCII art logo (`art.py`).
2. It prompts each participant to enter their name and their bid amount.
3. After each entry, it asks whether there are more bidders.

   * If yes, the screen clears (simulated by printing new lines).
   * If no, the auction ends.
4. The highest bidder is then determined and displayed.

---

## 🧠 Core Logic (main.py)

* `find_highest_bidder(bidding_record)`:

  * Loops through the `bids` dictionary.
  * Tracks the highest bid and the corresponding bidder.
  * Displays the winner.
* User input is gathered in a `while` loop until no more bids are to be placed.

---

## 🖼 ASCII Art (art.py)

A fancy logo is printed to make the auction feel official and engaging:

```
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | '-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
```

---

## 🧪 Example Run

```
What is your name?: Alice
What is your bid?: $100
Are there any other bidders? Type 'yes or 'no'.
yes




What is your name?: Bob
What is your bid?: $150
Are there any other bidders? Type 'yes or 'no'.
no
The winner is Bob with a bid of $150
```

---

## 📌 Notes

* Simple but effective for learning Python fundamentals like loops, conditionals, functions, and dictionaries.
* This program is a foundation to build more advanced auction or marketplace systems.

---

## 👨‍💻 Created By

Sathish Daggula
