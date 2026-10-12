"""Unit tests for the scientific calculator module."""

import unittest
import math
from calculator import (
    add, subtract, multiply, divide, power, modulo, floor_divide,
    square_root, cube_root, nth_root, factorial, sin_deg, cos_deg,
    evaluate_expression
)


class TestScientificCalculator(unittest.TestCase):
    def test_basic_arithmetic(self):
        self.assertEqual(add(10, 5), 15)
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(multiply(4, 5), 20)
        self.assertEqual(divide(10, 2), 5)

    def test_powers_and_roots(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(square_root(144), 12)
        self.assertAlmostEqual(cube_root(27), 3)
        self.assertAlmostEqual(nth_root(32, 5), 2)
        with self.assertRaises(ValueError):
            square_root(-4)

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)
        with self.assertRaises(ValueError):
            factorial(-1)

    def test_trigonometry(self):
        self.assertAlmostEqual(sin_deg(90), 1.0)
        self.assertAlmostEqual(cos_deg(0), 1.0)

    def test_expression_evaluation(self):
        self.assertAlmostEqual(evaluate_expression("sqrt(144) + 2^3"), 20)
        self.assertAlmostEqual(evaluate_expression("fact(4) / 2"), 12)
        self.assertAlmostEqual(evaluate_expression("sin(90)", is_degree=True), 1.0)
        with self.assertRaises(ZeroDivisionError):
            evaluate_expression("10 / 0")


if __name__ == "__main__":
    unittest.main()
