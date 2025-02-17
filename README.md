# Intermediate Python Tasks

This repository contains solutions to three intermediate-level Python programming tasks. Each task demonstrates key Python concepts such as exception handling, user interaction, and file processing.

---

## **Tasks**

### **1. Interactive Calculator**
- **Description**:  
  A program that acts as an interactive calculator. It takes user input in the form of a formula (e.g., `5 + 3`), validates it, and performs calculations.
- **Features**:
  - Supports addition (`+`) and subtraction (`-`) operations.
  - Validates input using a custom exception (`FormulaError`).
  - Continues to prompt for new input until the user types "quit."

---

### **2. Number Guessing Game**
- **Description**:  
  A game where the user guesses a randomly generated secret number between 1 and 10.
- **Features**:
  - Validates user input using a custom exception (`InvalidInputError`).
  - Tracks the score (number of attempts) and provides feedback on wrong guesses.
  - Allows replaying the game or exiting after guessing correctly or failing.

---

### **3. Match Questions and Answers**
- **Description**:  
  Matches questions and answers from two files (`questions.txt` and `answers.txt`) based on numeric identifiers and writes them into a new file (`output.txt`).
- **Features**:
  - Optimized for efficiency using dictionaries for matching.
  - Handles missing or mismatched data gracefully.
  - Outputs the matched pairs in sorted order.

---
