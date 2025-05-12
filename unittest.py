"""
Unittest is a built in framework for test automation. It is based on OOP. It is not for unit tests only
Test case- It is an instance of testing
Test suite- It is a collection of test suite
"""

# Example
import math
import unittest

"""
class TestSomething(unittest.TestCase):
    def test_example(self):
        self.assertEqual(1 + 1, 2)
"""

# Declaring the testcase
class Testsquared(unittest.Testcase):
    # Define the test 
    def test_negative(self):
        self.assertEqual(1 + 1, 2)

        
"""
assert methods
1. assertEqual(), assertNotEqual
2. assertIs(), assertIsNone()
3. assertTrue(), assertFalse()
4. assetIsinstance, assertIn()
4. assertRaises
"""        

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
        # Add the test for testing positives here
        self.assertEqual(func_factorial(5,) 120)


def func_factorial(number):
    if number < 0:
        raise ValueError('Factorial is not defined for negative values')
    factorial = 1
    while number > 1:
        factorial = factorial * number
        number = number - 1
    return factorial


class TestFactorial(unittest.TestCase):
    def test_negatives(self):
      	# Add the test for testing negatives here
        with self.assertRaises(ValueError):
            (func_factorial(-1))
            

# Implement a test to check that 17 is prime.
def is_prime(num):
    if num == 1: return False
    up_limit = int(math.sqrt(num)) + 1
    for i in range(2, up_limit):
        if num % i == 0:
            return False
    return True

class TestSuite(unittest.TestCase):
    def test_is_prime(self):
        # Check that 17 is prime
        self.assertTrue(is_prime(17))
        

# Implement a test to check that 6 is not prime.      
def is_prime(num):
    if num == 1: return False
    up_limit = int(math.sqrt(num)) + 1
    for i in range(2, up_limit):
        if num % i == 0:
            return False
    return True

class TestSuite(unittest.TestCase):
    def test_is_prime(self):
        # Check that 6 is not prime
        self.assertFalse(is_prime(6))              