Sachin Calculator
A simple and stylish calculator built with Python and Tkinter.
Supports basic arithmetic operations with a user-friendly graphical interface.

Features
1)Basic operations: Addition, Subtraction, Multiplication, Division

2)Support for parentheses () and decimal numbers .

3)Clear (C) button to reset the input

4)Backspace (←) button to delete last character

5)Handles errors like division by zero gracefully

6)Clean and modern button styling

7)Window size is fixed (non-resizable)


How to Run
Make sure you have Python installed.

Save the code in a file, e.g., calculator.py.

Run it using:
python calculator.py  <-in the terminal

bash
Copy
Edit
python calculator.py
Code Overview
Tkinter is used for GUI window and buttons.

An Entry widget is used as the display screen.

Buttons are dynamically created using a loop for cleaner code.

Main functionalities:

click(symbol): Insert number or operator into the input field.

clear(): Clears the whole input.

backspace(): Deletes the last character.

calculate(): Evaluates the expression using eval(), with error handling.