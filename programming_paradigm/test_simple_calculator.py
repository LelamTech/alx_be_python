# test_simple_calculator.py
import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        # positive numbers
        self.assertEqual(self.calc.add(2, 3), 5)
        # negative and positive
        self.assertEqual(self.calc.add(-1, 1), 0)
        # zeros
        self.assertEqual(self.calc.add(0, 0), 0)
        # floats
        self.assertAlmostEqual(self.calc.add(2.5, 1.2), 3.7, places=7)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(10, 4), 6)
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        self.assertEqual(self.calc.subtract(0, 5), -5)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 5), 15)
        self.assertEqual(self.calc.multiply(-2, 4), -8)
        self.assertEqual(self.calc.multiply(0, 100), 0)

    def test_divide_normal(self):
        # normal division
        self.assertEqual(self.calc.divide(10, 2), 5)
        # float result
        self.assertAlmostEqual(self.calc.divide(7, 2), 3.5, places=7)

    def test_divide_by_zero(self):
        # according to provided SimpleCalculator, divide returns None for b==0
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(0, 0))

    def test_various_types(self):
        # ints and floats combined
        self.assertAlmostEqual(self.calc.add(1, 2.5), 3.5)
        self.assertAlmostEqual(self.calc.subtract(5.0, 2), 3.0)
        self.assertAlmostEqual(self.calc.multiply(2.5, 2), 5.0)

if __name__ == "__main__":
    unittest.main()
