# Caesar Cipher Encryption Tool

This is a simple and interactive command-line tool for encoding and decoding messages using the **Caesar Cipher** encryption technique. The project was developed by **Sathish Daggula** as part of a guided bootcamp experience, and showcases core Python concepts such as functions, loops, conditionals, user input, and modularization.

---

## 🛡️ What is a Caesar Cipher?

The Caesar Cipher is one of the oldest known encryption techniques. It works by shifting the letters of the alphabet by a fixed number of positions. For example, with a shift of 3, 'a' becomes 'd', 'b' becomes 'e', and so on. Decoding reverses the process.

---

## 📄 Features

* Encode messages with a user-defined shift value.
* Decode encrypted messages by reversing the shift.
* Handles non-alphabet characters without altering them.
* Allows repeated usage through a loop until the user decides to exit.

---

## 💡 How It Works

1. Displays a custom ASCII logo using the external `art` module.
2. Prompts the user to select either `encode` or `decode`.
3. Accepts a message and a shift value as input.
4. Applies the Caesar Cipher algorithm.
5. Displays the transformed message.
6. Asks the user if they want to continue or exit.

---

## 🔧 Installation & Usage

### Requirements

* Python 3.x
* `art` module for logo display

Install the required module using:


### Running the Program

```bash
python main.py
```

Then, follow the on-screen instructions to encode or decode your message.

---

## 📁 File Structure

```text
.
├── main.py       # Main logic for Caesar cipher
└── art.py        # Contains ASCII logo used for UI (must be present in the same directory)
```

---

## 🧑‍💻 Technologies Used

* Python 3
* Custom module (`art.py`)

---

## 🚀 Future Improvements

* Add support for uppercase letters while preserving their case.
* Implement a GUI using Tkinter or a web interface with Flask.
* Include input validation for edge cases.
* Option to encrypt/decrypt files.

---

## 📚 Learning Outcome

This project reinforces fundamental Python programming skills such as working with:

* Lists and strings
* Functions with parameters
* Looping constructs and conditionals
* Input/output operations
* Modular coding practices

---

## 📄 Author

**Sathish Daggula**

Developed as a personal implementation of the Caesar Cipher tool.
