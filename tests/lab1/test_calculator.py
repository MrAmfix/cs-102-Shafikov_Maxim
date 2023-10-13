import unittest
from src.lab1.calculator import calculator
class CalculatorTestCase(unittest.TestCase):
    def test_calculator(self):
        self.assertAlmostEqual(calculator("4+5"), 9)
        self.assertAlmostEqual(calculator("-5.0  - 2.2"), -7.2)
        self.assertEqual(calculator("5.2/ 0"), "Incorrect expression")
        self.assertEqual(calculator("++5.2 - 44.1"), "Incorrect expression")
        self.assertEqual(calculator("154  / 0.00000"), "Incorrect expression")
        self.assertAlmostEqual(calculator("50.25 / 5.0 +2"), 12.05)

if __name__ == "__main__":
    unittest.main()
