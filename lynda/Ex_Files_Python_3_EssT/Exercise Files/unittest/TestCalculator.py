import unittest
from . import Calculator

class MyTestCase(unittest.TestCase):
    def test_something(self):
        calculator = Calculator.Calculator(4)
        self.assertTrue(16, calculator.square())

if __name__ == '__main__':
    unittest.main()
