# 🎮 Quiz App - Console-Based Trivia Game

## 📍 Overview

This is a **Python console quiz application** that delivers multiple True/False questions in succession, checks user input, tracks score, and displays the final result. It simulates a lightweight terminal-based trivia experience and demonstrates modular design and object-oriented programming in Python.

---

## ✨ Features

* 🔎 **True/False Questions** based on computer science trivia
* ✅ **Instant Feedback** on each answer
* 📊 **Score Tracking** throughout the quiz
* 📚 **Question Bank** imported from an external data source
* ⚖️ **Difficulty Variety** (easy to hard)

---

## 🛠️ Tech Stack

* **Python 3.x**
* CLI / Console Input-Output
* OOP Concepts (Classes, Methods)

---

## 📁 Project Structure

```
project/
├── main.py             # Application entry point
├── data.py             # Static dataset of trivia questions
├── question_model.py   # Class to model a question object
└── quiz_brain.py       # Quiz logic (progress, scoring, input handling)
```

---

## 🚀 How It Works

1. Loads all questions from `data.py`.
2. Creates a list of `Question` objects (from `question_model.py`).
3. Uses `QuizBrain` class (from `quiz_brain.py`) to control quiz flow.
4. Displays each question in the terminal with a prompt.
5. Checks user input against correct answer, updates score, and prints feedback.
6. Shows final score after all questions are answered.

---

## 📱 Sample Output

```
Q.1: The HTML5 standard was published in 2014. (True/False): True
You got it right!
The correct answer was: True.
Your current score is: 1/1

Q.2: The first computer bug was formed by faulty wires. (True/False): True
That's wrong.
The correct answer was: False.
Your current score is: 1/2

Q.3: FLAC stands for 'Free Lossless Audio Condenser'. (True/False): False
You got it right!
The correct answer was: False.
Your current score is: 2/3

...

You've completed the quiz
Your final score was: 7/10
```

---

## 📬 Learning Outcomes

This project showcases the ability to:

* Implement modular and readable Python code using object-oriented principles
* Work with basic data structures and external modules
* Handle user interaction via console input
* Write clean logic to manage state, progress, and scoring

It demonstrates foundational back-end Python skills with good separation of concerns and is easily extendable into a web or GUI-based quiz system.
