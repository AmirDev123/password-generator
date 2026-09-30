#!/usr/bin/env python3
"""
Password generator — CLI and optional Tkinter GUI.
Run CLI:  python main.py
Run GUI:  python main.py --gui
"""
import argparse
import secrets
import string
import sys


def generate(length=16, use_upper=True, use_digits=True, use_symbols=True) -> str:
    alphabet = string.ascii_lowercase
    if use_upper:
        alphabet += string.ascii_uppercase
    if use_digits:
        alphabet += string.digits
    if use_symbols:
        alphabet += "!@#$%^&*()-_=+[]{}|;:,.<>?"

    # Guarantee at least one char from each requested set
    required = [secrets.choice(string.ascii_lowercase)]
    if use_upper:
        required.append(secrets.choice(string.ascii_uppercase))
    if use_digits:
        required.append(secrets.choice(string.digits))
    if use_symbols:
        required.append(secrets.choice("!@#$%^&*()-_=+[]{}|;:,.<>?"))

    remaining = [secrets.choice(alphabet) for _ in range(length - len(required))]
    password = required + remaining
    secrets.SystemRandom().shuffle(password)
    return "".join(password)


def run_cli(args):
    passwords = [
        generate(args.length, not args.no_upper, not args.no_digits, not args.no_symbols)
        for _ in range(args.count)
    ]
    for pw in passwords:
        print(pw)


def run_gui():
    import tkinter as tk
    from tkinter import messagebox

    root = tk.Tk()
    root.title("Password Generator")
    root.resizable(False, False)

    length_var = tk.IntVar(value=16)
    upper_var = tk.BooleanVar(value=True)
    digits_var = tk.BooleanVar(value=True)
    symbols_var = tk.BooleanVar(value=True)
    result_var = tk.StringVar()

    tk.Label(root, text="Length:").grid(row=0, column=0, sticky="w", padx=10, pady=5)
    tk.Spinbox(root, from_=8, to=128, textvariable=length_var, width=5).grid(row=0, column=1, sticky="w")

    tk.Checkbutton(root, text="Uppercase", variable=upper_var).grid(row=1, column=0, columnspan=2, sticky="w", padx=10)
    tk.Checkbutton(root, text="Digits", variable=digits_var).grid(row=2, column=0, columnspan=2, sticky="w", padx=10)
    tk.Checkbutton(root, text="Symbols", variable=symbols_var).grid(row=3, column=0, columnspan=2, sticky="w", padx=10)

    def on_generate():
        pw = generate(length_var.get(), upper_var.get(), digits_var.get(), symbols_var.get())
        result_var.set(pw)

    def on_copy():
        if result_var.get():
            root.clipboard_clear()
            root.clipboard_append(result_var.get())
            messagebox.showinfo("Copied", "Password copied to clipboard!")

    tk.Button(root, text="Generate", command=on_generate).grid(row=4, column=0, pady=10, padx=10)
    tk.Button(root, text="Copy", command=on_copy).grid(row=4, column=1, pady=10)
    tk.Entry(root, textvariable=result_var, width=36, font=("Courier", 11)).grid(row=5, column=0, columnspan=2, padx=10, pady=(0, 10))

    on_generate()
    root.mainloop()


def main():
    parser = argparse.ArgumentParser(description="Password Generator")
    parser.add_argument("--gui", action="store_true", help="Launch GUI")
    parser.add_argument("-l", "--length", type=int, default=16)
    parser.add_argument("-n", "--count", type=int, default=1, help="Number of passwords")
    parser.add_argument("--no-upper", action="store_true")
    parser.add_argument("--no-digits", action="store_true")
    parser.add_argument("--no-symbols", action="store_true")
    args = parser.parse_args()

    if args.gui:
        run_gui()
    else:
        run_cli(args)


if __name__ == "__main__":
    main()
