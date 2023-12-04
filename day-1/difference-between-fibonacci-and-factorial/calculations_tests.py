import unittest
from calculations import *


class MathCalculationsTestCases(unittest.TestCase):
    __factorial = FactorialCalculation()
    __fibonacci = FibonacciCalculation()
    __calculations = CoreCalculation()

    def test_factorial(self):
        self.assertEqual(self.__factorial.get_factorial_item(3), 6)
        self.assertEqual(self.__factorial.get_factorial_item(7), 5040)
        self.assertEqual(self.__factorial.get_factorial_item(5), 120)
        self.assertEqual(self.__factorial.get_factorial_item(0), 1)

    def test_fibonacci(self):
        self.assertEqual(self.__fibonacci.get_fibonacci_item(8), 21)
        self.assertEqual(self.__fibonacci.get_fibonacci_item(12), 144)
        self.assertEqual(self.__fibonacci.get_fibonacci_item(2), 1)
        self.assertEqual(self.__fibonacci.get_fibonacci_item(5), 5)

    def test_core_calculations(self):
        self.assertEqual(self.__calculations.get_core_elements_difference(5), 115)
        self.assertEqual(self.__calculations.get_core_elements_difference(8), 40299)
        self.assertEqual(self.__calculations.get_core_elements_difference(0), 0)


if __name__ == '__main__':
    unittest.main()
