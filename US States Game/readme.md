# 🌊 US States Game

### 🌟 Overview

Welcome to the **US States Game** — an interactive, geography-based guessing game designed to help you master all 50 states of the USA in a fun and visual way! Built with Python’s `turtle` graphics and `pandas`, this game challenges you to correctly name all states as they appear on a map.

---

### 🚀 Features

* 🌍 Beautiful graphical US map using Turtle
* ✏️ Type your guesses interactively
* ✨ Real-time placement of correct state names
* ❌ Exit anytime and get a personalized study sheet (`states_to_learn.csv`)
* 🎓 Educational and beginner-friendly Python project

---

### 🔍 How It Works

1. **Map Setup**

   * The Turtle screen loads a blank US map (`blank_states_img.gif`).

2. **Data Integration**

   * Loads state names and coordinates from `50_states.csv`.
   * Creates a list of all valid state names.

3. **Interactive Game Loop**

   * You’ll be prompted to enter state names.
   * If the guess is correct: the state name appears on the map at its real location.
   * Type `Exit` anytime to end the game and save unguessed states to `states_to_learn.csv`.

4. **Visualization**

   * Turtle writes the guessed state names in their correct positions.
   * Coordinates from the CSV ensure accurate placement.

---

### 📂 Project Files

* `main.py` — Game logic
* `50_states.csv` — Dataset containing state names and coordinates
* `blank_states_img.gif` — Background image of the US map
* `states_to_learn.csv` — Automatically created list of unguessed states

---

### 📅 How to Run

1. Make sure the following files are in the same folder:

   * `main.py`
   * `50_states.csv`
   * `blank_states_img.gif`
2. Run the game with:

   ```bash
   python main.py
   ```
3. Start typing state names in the pop-up box
4. Want to end early? Type `Exit` and check `states_to_learn.csv` to improve your knowledge!

---

### 🚀 Future Enhancements

* ⏱ Add a timer for speed rounds
* 🧬 Add hints or autocomplete for near-correct answers
* 🔹 Quiz mode for capitals, abbreviations, or nicknames
* 🌟 Progress bar or scoring system

---

### 🎨 Created By

**Sathish Daggula**

---

### 📄 Learning Outcomes

* Practice US geography in an engaging format
* Learn the basics of GUI with `turtle`
* Master data handling using `pandas`
* Understand file input/output in Python

Let's turn learning into play! 🎉
