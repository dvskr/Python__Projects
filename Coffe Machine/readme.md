# 🍵 Coffee Machine Project

A mini console-based coffee vending machine written in Python. It simulates ordering different types of coffee, deducting resources, and managing payments through a virtual coin system.

---

## 🚀 Project Overview

This project demonstrates object-oriented programming (OOP), user interaction, resource management, and simulation of a simple business logic system.

---

## 🤖 Features

* Choose from a menu of drinks: `espresso`, `latte`, or `cappuccino`
* Simulated payment with coin input (quarters, dimes, nickels, pennies)
* Automated resource checking and deduction (water, milk, coffee)
* Profit tracking and reporting system
* Admin commands: `report` (show resources & profits), `off` (shut down machine)

---

## 🔧 How It Works

### 1. Menu System (`menu.py`)

Defines available drinks using the `MenuItem` class and stores them in the `Menu` class:

* Each drink has a name, required ingredients, and cost.
* Provides utility methods to list available drinks and fetch drink details.

### 2. Coffee Machine Logic (`coffee_maker.py`)

Manages ingredients and checks resource availability:

* `report()` prints current resource status.
* `is_resource_sufficient()` ensures enough ingredients for the selected drink.
* `make_coffee()` deducts used resources and confirms order.

### 3. Payment Handling (`money_machine.py`)

Handles virtual coin input and payment processing:

* Accepts coin counts, calculates total input.
* Checks if payment covers cost, returns change if needed.
* Tracks and reports total profit.

### 4. User Interface (`main.py`)

Main loop that ties everything together:

* Asks for user input.
* Processes commands or serves drinks accordingly.
* Combines resource and money management before serving coffee.

---

## 📅 Usage

Run `main.py` to start the machine:

```bash
python main.py
```

Follow the console prompts to order a drink or manage the machine.

---

## 🎓 Concepts Practiced

* Object-Oriented Programming (OOP)
* Class composition and modular design
* Simulating real-world systems in code
* Input validation and user-driven logic

---

## 🚀 Future Enhancements

* GUI interface with Tkinter or PyQt
* Save/load machine state
* Enhanced admin features (refill, reset, maintenance mode)

---

## ✍️ Author

Created by **Sathish Daggula** as a personal Python learning project.
