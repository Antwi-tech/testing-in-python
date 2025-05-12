"""
This test ensures that an interaction behaves normally.Tests the interaction between different modules
Examples:
1. Power cables- Integrates some hardware intergrated with some software
2. Internet connection- Device with internet
3. File reading driver-  file system and the software that wants to read it.
4. Database Connection- client you connect with the database.
5. API- client and the service

Interation problems
1. Lost connection
2. loss of data
3. interaction delays
4. low bandwidth 
5. Version cnflicts etc
"""

import pandas as pd
import pytest

# Fixture to read the dataframe
@pytest.fixture
def get_df():
    return pd.read_csv('laptops.csv')

# Integration test function
def test_get_df(get_df):
    # Check the type
    assert type(get_df) == pd.DataFrame
    # Check the number of rows
    assert get_df.shape[0] > 0