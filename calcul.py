import tkinter as tk

root = tk.Tk()
root.title("Sachin Calculator")
root.geometry("400x520")  # Wider width to fit all buttons
root.config(bg="#f5f5f5")
root.resizable(False, False)

entry = tk.Entry(root, font=("Helvetica", 24), bd=2, relief="groove", justify="right", bg="white")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20, ipady=10)


def click(symbol):
    entry.insert(tk.END, symbol)

def clear():
    entry.delete(0, tk.END)

def backspace():
    entry.delete(len(entry.get()) - 1, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except ZeroDivisionError:
        entry.delete(0, tk.END)
        entry.insert(0, "Can't divide by 0")
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


btn_style = {"font": ("Helvetica", 16), "width": 6, "height": 2, "bd": 1, "relief": "raised"}
op_style = {"bg": "#ffb84d", "fg": "black"}
eq_style = {"bg": "#4CAF50", "fg": "white"}
clr_style = {"bg": "#f44336", "fg": "white"}


buttons = [
    ('C', 1, 0, clr_style, clear),
    ('(', 1, 1, {}, lambda: click('(')),
    (')', 1, 2, {}, lambda: click(')')),
    ('/', 1, 3, op_style, lambda: click('/')),

    ('7', 2, 0, {}, lambda: click('7')),
    ('8', 2, 1, {}, lambda: click('8')),
    ('9', 2, 2, {}, lambda: click('9')),
    ('*', 2, 3, op_style, lambda: click('*')),

    ('4', 3, 0, {}, lambda: click('4')),
    ('5', 3, 1, {}, lambda: click('5')),
    ('6', 3, 2, {}, lambda: click('6')),
    ('-', 3, 3, op_style, lambda: click('-')),

    ('1', 4, 0, {}, lambda: click('1')),
    ('2', 4, 1, {}, lambda: click('2')),
    ('3', 4, 2, {}, lambda: click('3')),
    ('+', 4, 3, op_style, lambda: click('+')),

    ('0', 5, 0, {}, lambda: click('0')),
    ('.', 5, 1, {}, lambda: click('.')),
    ('=', 5, 2, eq_style, calculate),
    ('←', 5, 3, clr_style, backspace)
]


for (text, row, col, style, command) in buttons:
    tk.Button(root, text=text, command=command, **btn_style, **style).grid(row=row, column=col, padx=5, pady=5)


root.mainloop()
