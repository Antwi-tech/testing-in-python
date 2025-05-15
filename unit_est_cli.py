import unittest

def func_factorial(number):
    if number < 0:
        raise ValueError('Factorial is not defined for negative values')
    factorial = 1
    while number > 1:
        factorial = factorial * number
        number = number - 1
    return factorial

class TestFactorial(unittest.TestCase):
    def test_positives(self):
        self.assertEqual(func_factorial(5), 120)

    def test_zero(self):
        self.assertEqual(func_factorial(0), 1)

    def test_negatives(self):
        with self.assertRaises(ValueError):
            func_factorial(-1)
