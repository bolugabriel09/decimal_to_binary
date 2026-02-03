# decimal_to_binary
import tkinter as tk
from tkinter import messagebox


# ---------- Conversion Logic ----------
def decimal_to_binary():
    try:
        decimal = int(decimal_entry.get())
        if decimal < 0:
            raise ValueError
        binary = bin(decimal)[2:]
        result_label.config(text=f"Binary: {binary}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid positive decimal number")


def binary_to_decimal():
    binary = binary_entry.get()
    try:
        decimal = int(binary, 2)
        result_label.config(text=f"Decimal: {decimal}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid binary number")


# ---------- Main Window ----------
root = tk.Tk()
root.title("Decimal ↔ Binary Converter")
root.geometry("450x400")
root.config(bg="#1e1e2f")


# ---------- Heading ----------
title = tk.Label(
    root,
    text="Number System Converter",
    font=("Arial", 18, "bold"),
    fg="white",
    bg="#1e1e2f"
)
title.pack(pady=20)


# ---------- Decimal to Binary ----------
decimal_label = tk.Label(
    root,
    text="Decimal to Binary",
    font=("Arial", 12, "bold"),
    fg="white",
    bg="#1e1e2f"
)
decimal_label.pack()

decimal_entry = tk.Entry(root, font=("Arial", 12), width=25)
decimal_entry.pack(pady=5)

decimal_button = tk.Button(
    root,
    text="Convert to Binary",
    font=("Arial", 11),
    bg="#4CAF50",
    fg="white",
    width=20,
    command=decimal_to_binary
)
decimal_button.pack(pady=10)


# ---------- Binary to Decimal ----------
binary_label = tk.Label(
    root,
    text="Binary to Decimal",
    font=("Arial", 12, "bold"),
    fg="white",
    bg="#1e1e2f"
)
binary_label.pack()

binary_entry = tk.Entry(root, font=("Arial", 12), width=25)
binary_entry.pack(pady=5)

binary_button = tk.Button(
    root,
    text="Convert to Decimal",
    font=("Arial", 11),
    bg="#2196F3",
    fg="white",
    width=20,
    command=binary_to_decimal
)
binary_button.pack(pady=10)


# ---------- Result ----------
result_label = tk.Label(
    root,
    text="Result will appear here",
    font=("Arial", 14, "bold"),
    fg="#FFD700",
    bg="#1e1e2f"
)
result_label.pack(pady=20)


# ---------- Run App ----------
root.mainloop()
chidera leave me alone
