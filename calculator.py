"""Scientific Calculator supporting arithmetic, power, roots, trigonometry, and logarithms."""

import math
from typing import Dict, Callable, Any


# --- Basic & Scientific Math Functions ---

def add(a: float, b: float) -> float:
    return a + b

def subtract(a: float, b: float) -> float:
    return a - b

def multiply(a: float, b: float) -> float:
    return a * b

def divide(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

def power(a: float, b: float) -> float:
    return math.pow(a, b)

def modulo(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Cannot calculate modulo by zero.")
    return a % b

def floor_divide(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Cannot floor divide by zero.")
    return a // b

def square_root(x: float) -> float:
    if x < 0:
        raise ValueError("Cannot take square root of negative number.")
    return math.sqrt(x)

def cube_root(x: float) -> float:
    return math.copysign(abs(x) ** (1 / 3), x)

def nth_root(x: float, n: float) -> float:
    if n == 0:
        raise ZeroDivisionError("Root degree cannot be zero.")
    if x < 0 and n % 2 == 0:
        raise ValueError("Cannot compute even root of negative number.")
    if x < 0:
        return -((-x) ** (1 / n))
    return x ** (1 / n)

def factorial(x: float) -> int:
    if x < 0 or not float(x).is_integer():
        raise ValueError("Factorial is only defined for non-negative integers.")
    return math.factorial(int(x))

def sin_deg(x: float) -> float:
    return math.sin(math.radians(x))

def cos_deg(x: float) -> float:
    return math.cos(math.radians(x))

def tan_deg(x: float) -> float:
    rad = math.radians(x)
    if math.isclose(math.cos(rad), 0.0, abs_tol=1e-9):
        raise ValueError("Tangent is undefined.")
    return math.tan(rad)

def ln(x: float) -> float:
    if x <= 0:
        raise ValueError("Natural log is only defined for positive numbers.")
    return math.log(x)

def log10(x: float) -> float:
    if x <= 0:
        raise ValueError("Log base 10 is only defined for positive numbers.")
    return math.log10(x)

def log2(x: float) -> float:
    if x <= 0:
        raise ValueError("Log base 2 is only defined for positive numbers.")
    return math.log2(x)


# Safe evaluation dictionary for expressions
SAFE_MATH_ENV: Dict[str, Any] = {
    # Constants
    "pi": math.pi,
    "e": math.e,
    "tau": math.tau,
    
    # Functions
    "sqrt": square_root,
    "cbrt": cube_root,
    "root": nth_root,
    "fact": factorial,
    "abs": abs,
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "asin": math.asin,
    "acos": math.acos,
    "atan": math.atan,
    "sind": sin_deg,
    "cosd": cos_deg,
    "tand": tan_deg,
    "ln": ln,
    "log": log10,
    "log2": log2,
    "exp": math.exp,
    "floor": math.floor,
    "ceil": math.ceil,
}


def evaluate_expression(expr: str, is_degree: bool = False) -> float:
    """Evaluate a mathematical expression string safely with operator precedence and scientific functions."""
    # Pre-process common symbols
    sanitized = (
        expr.replace("×", "*")
        .replace("÷", "/")
        .replace("−", "-")
        .replace("^", "**")
        .replace("π", "pi")
    )

    # Adjust trig functions if in degree mode
    if is_degree:
        sanitized = (
            sanitized.replace("sin(", "sind(")
            .replace("cos(", "cosd(")
            .replace("tan(", "tand(")
        )

    # Validate characters
    allowed_chars = set("0123456789.+-*/%^()_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ")
    if not set(sanitized).issubset(allowed_chars):
        raise ValueError("Expression contains invalid characters.")

    try:
        # Evaluate within safe math environment (no builtins)
        result = eval(sanitized, {"__builtins__": None}, SAFE_MATH_ENV)
        return float(result)
    except ZeroDivisionError:
        raise ZeroDivisionError("Cannot divide by zero.")
    except Exception as e:
        raise ValueError(f"Invalid expression: {e}")


def main() -> None:
    print("=" * 55)
    print("        Scientific Python Calculator")
    print("=" * 55)
    print("Features & Functions supported:")
    print("  • Basic: +, -, *, /, //, %, ** (or ^)")
    print("  • Powers & Roots: sqrt(x), cbrt(x), root(x, n)")
    print("  • Exponential & Logs: exp(x), ln(x), log(x), log2(x)")
    print("  • Trigonometry: sin(x), cos(x), tan(x), sind(deg)...")
    print("  • Constants: pi, e, tau | Functions: fact(n), abs(x)")
    print("-" * 55)
    print("Examples: 'sqrt(144) + 2^3', 'sin(pi / 2)', 'fact(5) * log(100)'")
    print("Type 'q' to quit.")
    print("=" * 55)

    while True:
        try:
            expr = input("\nSci-Calc > ").strip()
            if not expr:
                continue
            if expr.lower() in ("q", "quit", "exit"):
                print("Goodbye!")
                break

            result = evaluate_expression(expr)
            if result.is_integer():
                print(f"Result: {int(result)}")
            else:
                # Format to remove floating point artifacts
                print(f"Result: {round(result, 10):.10g}")

        except (ValueError, ZeroDivisionError) as err:
            print(f"Error: {err}")
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            break


if __name__ == "__main__":
    main()
