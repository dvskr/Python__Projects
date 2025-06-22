# Pong Game - Python Turtle Arcade

A modern recreation of the classic Pong game built using Python's `turtle` graphics module. This project demonstrates object-oriented programming principles and real-time animation, making it a fun and educational arcade-style game.

---

## 🌟 Features

* Two-player paddle control (W/S for Player 1, Up/Down arrows for Player 2)
* Real-time ball movement with collision detection
* Scoreboard updates when a player scores
* Ball speed increases as the game progresses
* Simple and intuitive game logic using OOP

---

## 🚀 Technologies Used

* Python 3
* Turtle graphics module

---

## 🎯 Gameplay Instructions

* Launch the game by running `main.py`
* Player 1 (Left Paddle): Use `W` to move up and `S` to move down
* Player 2 (Right Paddle): Use `Up Arrow` and `Down Arrow` to control the paddle
* Keep the ball from passing your side; each miss gives your opponent a point
* First to the desired score (e.g., 5 or 10) wins (you can set your own win condition)

---

## 🔧 Project Structure

```
PongGame/
├── main.py         # Initializes the game loop, screen, and controls game flow
├── paddle.py       # Paddle class with movement logic
├── ball.py         # Ball class with bouncing and reset mechanics
├── scoreboard.py   # Scoreboard class for tracking and displaying scores
```

---

## 📝 Code Highlights

### `ball.py`

* The `Ball` class inherits from `Turtle`, encapsulates ball position, movement logic, and speed.
* It includes methods to bounce off walls (`bounce_y`), bounce off paddles (`bounce_x`), and reset position when a point is scored.

### `paddle.py`

* Defines a `Paddle` class with `go_up` and `go_down` methods to handle vertical movement.
* Uses turtle stretching to form paddles.

### `scoreboard.py`

* Tracks the score for each player and updates the screen accordingly.
* Uses turtle graphics to write scores at the top of the screen.

### `main.py`

* Handles screen setup and listens for user input.
* Contains the main game loop with ball movement, collision detection, and scoring logic.

---

## 🚀 How to Run

1. Make sure Python 3 is installed.
2. Save all files in the same directory.
3. Run the following command in terminal:

```bash
python main.py
```

---

## 🧱 Author

Created by **Sathish Daggula**

---

## 💡 Future Improvements

* Add game-over condition and restart option
* Introduce sounds for collision and scoring
* Add levels or AI opponent for single-player mode
* Enhance graphics with themes and paddle skins
