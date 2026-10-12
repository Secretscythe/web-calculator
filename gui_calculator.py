"""Modern Scientific Desktop GUI Calculator built with Python and Tkinter."""

import tkinter as tk
from tkinter import ttk, messagebox
import math
from calculator import (
    add, subtract, multiply, divide, power, modulo, floor_divide,
    square_root, cube_root, nth_root, factorial, ln, log10, log2,
    evaluate_expression
)


class ModernScientificCalculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Scientific Calculator")
        self.geometry("480x620")
        self.minsize(420, 560)
        self.configure(bg="#181825")

        # Calculator State
        self.current_expression = ""
        self.is_degree = True
        self.memory = 0.0

        self._setup_styles()
        self._create_widgets()
        self._bind_keys()

    def _setup_styles(self):
        self.colors = {
            "bg": "#181825",
            "display_bg": "#11111b",
            "text_primary": "#cdd6f4",
            "text_secondary": "#a6adc8",
            "btn_num_bg": "#313244",
            "btn_num_active": "#45475a",
            "btn_sci_bg": "#1e1e2e",
            "btn_sci_fg": "#89b4fa",
            "btn_sci_active": "#313244",
            "btn_op_bg": "#89b4fa",
            "btn_op_fg": "#11111b",
            "btn_op_active": "#b4befe",
            "btn_fn_bg": "#45475a",
            "btn_fn_fg": "#f5e0dc",
            "btn_equal_bg": "#a6e3a1",
            "btn_equal_fg": "#11111b",
            "btn_clear_bg": "#f38ba8",
            "btn_clear_fg": "#11111b",
        }

    def _create_widgets(self):
        # Top Header Bar (Angle Mode & Title)
        header_frame = tk.Frame(self, bg=self.colors["bg"], padx=14, pady=6)
        header_frame.pack(fill="x")

        title_lbl = tk.Label(
            header_frame,
            text="Scientific Calculator",
            font=("Helvetica", 11, "bold"),
            fg=self.colors["text_secondary"],
            bg=self.colors["bg"]
        )
        title_lbl.pack(side="left")

        self.angle_btn = tk.Button(
            header_frame,
            text="DEG",
            font=("Helvetica", 10, "bold"),
            bg=self.colors["btn_num_bg"],
            fg=self.colors["btn_sci_fg"],
            bd=0,
            padx=10,
            pady=2,
            relief="flat",
            cursor="pointinghand",
            command=self.toggle_angle_mode
        )
        self.angle_btn.pack(side="right")

        # Display screen
        display_frame = tk.Frame(self, bg=self.colors["display_bg"], padx=16, pady=12)
        display_frame.pack(fill="x", padx=12, pady=(4, 8))

        self.history_label = tk.Label(
            display_frame,
            text="",
            anchor="e",
            font=("Helvetica", 11),
            fg=self.colors["text_secondary"],
            bg=self.colors["display_bg"],
        )
        self.history_label.pack(fill="x")

        self.display_var = tk.StringVar(value="0")
        self.display_label = tk.Label(
            display_frame,
            textvariable=self.display_var,
            anchor="e",
            font=("Helvetica", 26, "bold"),
            fg=self.colors["text_primary"],
            bg=self.colors["display_bg"],
            pady=4,
        )
        self.display_label.pack(fill="x")

        # Keypad Grid Frame
        keypad_frame = tk.Frame(self, bg=self.colors["bg"])
        keypad_frame.pack(fill="both", expand=True, padx=10, pady=(4, 10))

        # 6 columns layout
        for j in range(6):
            keypad_frame.columnconfigure(j, weight=1)
        for i in range(6):
            keypad_frame.rowconfigure(i, weight=1)

        # Scientific Buttons definition: (text, row, col, type, action)
        buttons = [
            # Row 0: Scientific functions
            ("sin", 0, 0, "sci", lambda: self.apply_fn("sin")),
            ("cos", 0, 1, "sci", lambda: self.apply_fn("cos")),
            ("tan", 0, 2, "sci", lambda: self.apply_fn("tan")),
            ("ln", 0, 3, "sci", lambda: self.apply_fn("ln")),
            ("log", 0, 4, "sci", lambda: self.apply_fn("log")),
            ("π", 0, 5, "sci", lambda: self.insert_token("pi")),

            # Row 1: Powers, Roots & Constants
            ("√x", 1, 0, "sci", lambda: self.apply_fn("sqrt")),
            ("x²", 1, 1, "sci", lambda: self.apply_fn("sq")),
            ("x^y", 1, 2, "sci", lambda: self.insert_token("^")),
            ("e^x", 1, 3, "sci", lambda: self.apply_fn("exp")),
            ("n!", 1, 4, "sci", lambda: self.apply_fn("fact")),
            ("e", 1, 5, "sci", lambda: self.insert_token("e")),

            # Row 2: Standard Row 1
            ("C", 2, 0, "clear", self.clear),
            ("⌫", 2, 1, "fn", self.backspace),
            ("(", 2, 2, "fn", lambda: self.insert_token("(")),
            (")", 2, 3, "fn", lambda: self.insert_token(")")),
            ("%", 2, 4, "fn", lambda: self.insert_token("%")),
            ("/", 2, 5, "op", lambda: self.insert_token("/")),

            # Row 3: Numbers & Multiply
            ("7", 3, 0, "num", lambda: self.insert_token("7")),
            ("8", 3, 1, "num", lambda: self.insert_token("8")),
            ("9", 3, 2, "num", lambda: self.insert_token("9")),
            ("1/x", 3, 3, "sci", lambda: self.apply_fn("inv")),
            ("|x|", 3, 4, "sci", lambda: self.apply_fn("abs")),
            ("*", 3, 5, "op", lambda: self.insert_token("*")),

            # Row 4: Numbers & Subtract
            ("4", 4, 0, "num", lambda: self.insert_token("4")),
            ("5", 4, 1, "num", lambda: self.insert_token("5")),
            ("6", 4, 2, "num", lambda: self.insert_token("6")),
            ("//", 4, 3, "sci", lambda: self.insert_token("//")),
            ("∛x", 4, 4, "sci", lambda: self.apply_fn("cbrt")),
            ("-", 4, 5, "op", lambda: self.insert_token("-")),

            # Row 5: Bottom row & Equals
            ("1", 5, 0, "num", lambda: self.insert_token("1")),
            ("2", 5, 1, "num", lambda: self.insert_token("2")),
            ("3", 5, 2, "num", lambda: self.insert_token("3")),
            ("0", 5, 3, "num", lambda: self.insert_token("0")),
            (".", 5, 4, "num", lambda: self.insert_token(".")),
            ("+", 5, 5, "op", lambda: self.insert_token("+")),
        ]

        for text, r, c, btype, cmd in buttons:
            btn = self._make_button(keypad_frame, text, btype, cmd)
            btn.grid(row=r, column=c, padx=3, pady=3, sticky="nsew")

        # Equals button row (Row 6)
        eq_btn = self._make_button(keypad_frame, "=", "equal", self.calculate_result)
        eq_btn.grid(row=6, column=0, columnspan=6, padx=3, pady=(3, 4), sticky="nsew")
        keypad_frame.rowconfigure(6, weight=1)

    def _make_button(self, parent, text, btype, command):
        if btype == "num":
            bg = self.colors["btn_num_bg"]
            fg = self.colors["text_primary"]
            active_bg = self.colors["btn_num_active"]
        elif btype == "sci":
            bg = self.colors["btn_sci_bg"]
            fg = self.colors["btn_sci_fg"]
            active_bg = self.colors["btn_sci_active"]
        elif btype == "op":
            bg = self.colors["btn_op_bg"]
            fg = self.colors["btn_op_fg"]
            active_bg = self.colors["btn_op_active"]
        elif btype == "equal":
            bg = self.colors["btn_equal_bg"]
            fg = self.colors["btn_equal_fg"]
            active_bg = "#86efac"
        elif btype == "clear":
            bg = self.colors["btn_clear_bg"]
            fg = self.colors["btn_clear_fg"]
            active_bg = "#fca5a5"
        else:
            bg = self.colors["btn_fn_bg"]
            fg = self.colors["btn_fn_fg"]
            active_bg = self.colors["btn_num_active"]

        btn = tk.Button(
            parent,
            text=text,
            font=("Helvetica", 13, "bold"),
            bg=bg,
            fg=fg,
            activebackground=active_bg,
            activeforeground=fg,
            bd=0,
            relief="flat",
            cursor="pointinghand",
            command=command,
        )
        return btn

    def toggle_angle_mode(self):
        self.is_degree = not self.is_degree
        self.angle_btn.config(text="DEG" if self.is_degree else "RAD")

    def _bind_keys(self):
        self.bind("<Key>", self._on_key_press)

    def _on_key_press(self, event):
        char = event.char
        keysym = event.keysym

        if char in "0123456789.+-*/%^()":
            self.insert_token(char)
        elif char == "=" or keysym in ("Return", "KP_Enter"):
            self.calculate_result()
        elif keysym in ("BackSpace",):
            self.backspace()
        elif keysym in ("Escape",):
            self.clear()

    def insert_token(self, token: str):
        if self.current_expression == "0" and token not in (".", "+", "-", "*", "/", "^"):
            self.current_expression = token
        else:
            self.current_expression += token
        self._update_display()

    def backspace(self):
        if self.current_expression:
            self.current_expression = self.current_expression[:-1]
            self._update_display()

    def clear(self):
        self.current_expression = ""
        self.history_label.config(text="")
        self.display_var.set("0")

    def apply_fn(self, fn: str):
        if not self.current_expression:
            return
        try:
            val = evaluate_expression(self.current_expression, self.is_degree)
            if fn == "sqrt":
                res = square_root(val)
                label = f"√({val})"
            elif fn == "cbrt":
                res = cube_root(val)
                label = f"∛({val})"
            elif fn == "sq":
                res = val ** 2
                label = f"({val})²"
            elif fn == "sin":
                rad = math.radians(val) if self.is_degree else val
                res = math.sin(rad)
                label = f"sin({val})"
            elif fn == "cos":
                rad = math.radians(val) if self.is_degree else val
                res = math.cos(rad)
                label = f"cos({val})"
            elif fn == "tan":
                rad = math.radians(val) if self.is_degree else val
                res = math.tan(rad)
                label = f"tan({val})"
            elif fn == "ln":
                res = ln(val)
                label = f"ln({val})"
            elif fn == "log":
                res = log10(val)
                label = f"log({val})"
            elif fn == "exp":
                res = math.exp(val)
                label = f"e^({val})"
            elif fn == "fact":
                res = factorial(val)
                label = f"{val}!"
            elif fn == "abs":
                res = abs(val)
                label = f"|{val}|"
            elif fn == "inv":
                if val == 0:
                    raise ZeroDivisionError()
                res = 1 / val
                label = f"1/({val})"
            else:
                return

            if isinstance(res, float) and res.is_integer():
                res = int(res)
            elif isinstance(res, float):
                res = round(res, 10)

            self.history_label.config(text=f"{label} =")
            self.display_var.set(str(res))
            self.current_expression = str(res)

        except Exception as e:
            self.display_var.set("Error")
            self.current_expression = ""

    def calculate_result(self):
        if not self.current_expression:
            return

        expr = self.current_expression.strip()
        try:
            res = evaluate_expression(expr, self.is_degree)
            if isinstance(res, float) and res.is_integer():
                res = int(res)
            elif isinstance(res, float):
                res = round(res, 10)

            self.history_label.config(text=f"{expr} =")
            self.display_var.set(str(res))
            self.current_expression = str(res)

        except ZeroDivisionError:
            self.display_var.set("Error: Div by 0")
            self.current_expression = ""
        except Exception as e:
            self.display_var.set("Error")
            self.current_expression = ""

    def _update_display(self):
        text = self.current_expression.strip()
        self.display_var.set(text if text else "0")


def main():
    app = ModernScientificCalculator()
    app.mainloop()


if __name__ == "__main__":
    main()
