# ♦♥ Blackjack Game (Python Terminal Edition) ♣♠

Welcome to a thrilling command-line Blackjack experience!
This game was crafted as a personal spin-off project under the guidance of **Angela Yu's Python Bootcamp** — complete with interactive gameplay, smart dealer logic, and stylish ASCII visuals.

---

## 🎉 Features

* ✨ Eye-catching ASCII art banner
* 🃏 Realistic card dealing with J, Q, K, A logic
* ⭐ Dynamic Ace handling (11 or 1 depending on hand)
* 🌟 Player vs. Dealer turns with live score updates
* ♻️ Continuous gameplay with replay option
* 📈 Outcome comparison: Win, Lose, or Draw

---

## 📚 Technologies Used

* Python Standard Library: `random`
* Custom ASCII Art module: `art.py`

---

## 🕹️ How to Play

1. Run `main.py` in your terminal.
2. Type `yes` when asked if you'd like to start the game.
3. Watch cards being dealt to you and the dealer.
4. Choose whether to `hit` (draw a card) or `stand`.
5. Dealer will draw until reaching at least 17.
6. Game ends with a printed outcome and replay prompt.

---

## 📁 Project Structure

### `art.py`

Displays a large stylized ASCII logo upon launching the game.

### `main.py`

Contains all gameplay logic:

* `deal()` – Random card selection with proper scoring
* Game loops for player and dealer turns
* Condition checks for bust, win, draw
* User inputs to manage replay

---

## 🌀 Blackjack Rules Simulated

* **Aces** count as **11** but convert to **1** if over 21
* **Face cards (J, Q, K)** count as **10**
* Dealer must hit until their score is **17+**
* Players choose to continue drawing or stand
* Busted if total > 21
* Ties if both have equal scores

---

## 🎬 Sample Gameplay

```
Do you want to start the game choose: yes or no
> yes

card drawn 5
dealer Current count is 5
card drawn K
player Current count is 10
Do you want to pick one more card?: Yes or No
> yes
card drawn 2
player Current count is 12
Do you want to pick one more card?: Yes or No
> no
...
```

---

## 👨‍🏫 Author

Created by **Sathish Daggula**.

---

## 📝 License

Distributed under the MIT License. Free to use and modify!
