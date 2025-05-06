"""
Use cases
1. When we want a test procedure to fail
2. Skip test if condition is met

A test marker is used to tag a test in the pytest library

 decorator is a design pattern in Python that allows a user
 to add new functionality to an existing object without modifying its structure.
 
 o mark a test function, we add the decorator starting with "at pytest dot mark". 
 Then we continue by another "dot" and the marker name we want to use. 
 
 Markers
 1. ski
 2. skip if
 3. xfail
"""
import pytest
from datetime import datetime

def multiple_of_two(num):
    if num == 0:
        raise(ValueError)
    return num % 2 == 0

# Test that is expected to fail (marked with xfail)
@pytest.mark.xfail
def test_fails():
    # Write any assert test that will fail
    assert multiple_of_two(3) is False
    print("Test failed as expected!")  # This will print when the test is marked to fail

day_of_week = datetime.now().isoweekday()

def get_unique_values(lst):
    return list(set(lst))

condition_string = 'day_of_week == 6'

# Add the conditional skip marker and the string here
@pytest.mark.skipif(condition_string)
def test_function():
    # Complete the assertion tests here
    assert get_unique_values([1, 2, 3]) == [1, 2, 3]
    assert get_unique_values([1, 2, 3, 1]) == [1, 2, 3]
    print("Test passed and skipped due to condition!")  # This will be printed if the test is skipped

# Add a function to print results when test fails
@pytest.mark.parametrize("test_input, expected", [(3, False), (2, True), (5, False)])
def test_multiple_of_two(test_input, expected):
    try:
        assert multiple_of_two(test_input) == expected
        print(f"Test passed for input {test_input}!")  # Print success message
    except AssertionError:
        print(f"Test failed for input {test_input}. Expected {expected}.")  # Print failure message
        raise  # Reraise the error after printing
