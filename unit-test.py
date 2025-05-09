"""
Unit is the smallest working part of a system or application that can be tested
A test case creates a blueprint of future tests

How To Create A Unit Test
1. Decide unit to test
2. Define the test cases (what ae the possible otcomes, how should the unit behave etc)
3. Write code for each test case
4. Run the test and analyse it 
"""
import pytest

# Define the unit 
def sum_of_arr(array:list) -> int:
    return sum(array)

"""
Test cases for the above:
1. When input is a list of numbers
2. If an empty list is passed to it
3. If one number is passed 

"""
# Test case 1
def test_regular():
    assert sum_of_arr([1,2,3]) == 6
    assert sum_of_arr([100,150]) ==250

# Test Case 2
def test_empty():
    assert sum_of_arr([]) == 0

# Test Case 3 
def test_a_num():
    assert sum_of_arr([10]) == 10    
    assert sum_of_arr([0]) == 0
    
# Test Case 4: The array is not an integer
def test_datatype():
    with pytest.raises(TypeError):
        sum_of_arr([1,2,'three',4])

def test_data():
   assert sum_of_arr(["2", "1"])  == 3
   
   

"""
Different Unit Test Case
"""   
   
# main function
def factorial(n):
    if n == 0: return 1
    elif (type(n) == int):
        return n * factorial(n-1)
    else: return -1

# Test case: zero input
def test_zero():
	assert factorial(0) == 1

# Test case: expected input
def test_regular():
	assert factorial(5) ==120
        

# Test case: input of a wrong type
def test_str():
    assert factorial('5') == -1
    print('Test passed')

