
"""
This is a prepared environment that can be used for test execution

"""

import pytest
import pandas as pd

@pytest.fixture
def prepare_data():
    return [i for i in range(10)]

def test_elements(prepare_data):
    assert 9 in prepare_data
    assert 10 not in prepare_data


"""
# Fixtures Chain Request- It allows a fixture to request another fixture
# It can be used to test processes like data initialisation, data processing, data loading 
# which are use cases in a data pipeline

"""

# Define the fixture for returning the length
@pytest.fixture
def list_length():
    return 10

# Define the fixture for a list preparation
@pytest.fixture
def prepare_list(list_length):
    return [i for i in range(list_length)]

def test_9(prepare_list):
    assert 9 in prepare_list
    assert 10 not in prepare_list

"""
Autose argument is passed to the fixture decorator, it is a boolean. It reduces the number of redundant fixture codes

# autouse fixture example
 This Fails the test 
"""

@pytest.fixture
def init_list():
    return []

# Declare the fixture with autouse
@pytest.fixture(autouse= True)
def add_numbers_to_list(init_list):
    init_list.extend([i for i in range(10)])

# Complete the tests
def test_elements(init_list):
    assert 1 in add_numbers_to_list
    assert 9 in add_numbers_to_list





"""
Fixture teardown - It is the processes of cleaning up resources allocated during env setup
It avoids
1. Memory leaks
2. Performance Issues
3. Invalid tests results
4. Pipeline failures and errors 

replace return with yield keyword and provide all the code after
"""

import pytest

@pytest.fixture
def prepare_data():
    data = [i for i in range(10)]
    # Return the data with the special keyword
    yield data
    # Clear the data list
    data.clear()
    # Delete the data variable
    del data

def test_elements(prepare_data):
    assert 9 in prepare_data
    assert 10 not in prepare_data

@pytest.fixture
def data():
    df = pd.read_csv('/usr/local/share/games.csv')
    # Return df with the special keyword
    yield df
    # Remove all rows in df
    df.drop(df.index, inplace=True)
    # Delete the df variable
    del df

def test_type(data):
    assert type(data) == pd.DataFrame

def test_shape(data):
    assert data.shape[0] == 1512