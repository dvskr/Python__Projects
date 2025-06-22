# Hangman Game in Python

A classic Hangman word-guessing game built using core Python functionalities. This project uses modular design principles with clean separation of concerns for gameplay logic, word list data, and visual art.

---

## 🌐 Project Overview

This terminal-based Hangman game randomly selects a challenging word from a large predefined list and allows the player to guess it letter by letter. The game visually depicts a hanging man that progresses with each incorrect guess, adding tension and fun!

---

## 🚀 Features

* Random word selection from a large and diverse word bank
* Step-by-step ASCII visual feedback as the player loses lives
* Game state updates in real-time with input validation
* Modular code using multiple Python files
* Win/Lose end-game messages with final word reveal

---

## 📂 File Structure

```bash
hangman_project/
│
├── main.py             # Game logic and main loop
├── hangman_words.py    # Large list of unique English words
└── hangman_arts.py     # ASCII art for stages and logo
```

---

## 📁 Modules Explained

### 1. `hangman_words.py`

Contains a large list of English words used in the game. A word is randomly picked at the start of each session.

### 2. `hangman_arts.py`

Includes ASCII art representations for each stage of the hangman as lives decrease. Also features a custom Hangman logo.

### 3. `main.py`

The central script that:

* Initializes game state (`lives = 6`, placeholders)
* Displays the logo and selects a random word
* Accepts and processes user guesses
* Validates repeat inputs
* Updates the visual placeholder and prints the current state
* Ends the game when the user wins or runs out of lives

---

## 🤗 How to Play

1. Run `main.py`
2. A word is randomly selected and shown as underscores
3. Type in a letter each turn
4. Correct guesses reveal the letters
5. Incorrect guesses reduce your lives and update the hangman drawing
6. The game ends when you guess all letters or run out of lives

---

## 🔧 How to Run

1. Clone or download this repository
2. Ensure you have Python 3 installed
3. In your terminal, run:

```bash
python main.py
```

---

## 🌟 Highlights

* Great starter project for learning Python conditionals, loops, lists, and user input
* Introduces modularity and clean file separation
* Engages users with fun ASCII visuals

---

## 📊 Future Enhancements

* Add difficulty levels (easy, medium, hard)
* Include score tracking and high-score system
* Enable multiplayer or timed modes
* Add GUI using Tkinter or web version using Flask

---

## 📄 Credits

Created with passion by **Sathish Daggula**.
