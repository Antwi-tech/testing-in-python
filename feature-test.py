"""
A feature is a software functionality that satisfies a particular user requiement. It is wider than a unit
Feature testing verifies the behavoir of a specific feature eg: Data distribution and report preparation        
"""
import pandas as pd
import pytest

df = pd.read_csv('laptops.csv')

# filter the dataset
def filter_data_by_manuf(df, manufacture_name):
    filtered_df = df[df["Manufacturer"] == manufacture_name]
    return filtered_df    

# Feature test
def test_uique():
    manuf_name = 'Apple'
    filtered = filter_data_by_manuf(df, manuf_name)
    assert filtered['Manufacturer'].nunique() == 1
    assert filtered['Manufacturer'].unique()[0] == manuf_name
    
"""
Example 2
"""    
# Don't forget to run
# pytest agg_with_sum.py 
# in the CLI to actually run the test!


# Fixture to prepare the data
@pytest.fixture
def get_df():
    return pd.read_csv('laptops.csv')

# Aggregation feature
def agg_with_sum(data, group_by_column, aggregate_column):
    return data.groupby(group_by_column)[aggregate_column].sum()

# Test function
def test_agg_feature(get_df):
    # Aggregate preparation
    aggregated = agg_with_sum(get_df, 'Manufacturer', 'Price')
    # Test the type of the aggregated
    assert isinstance(aggregated, pd.Series)
   # Test the number of rows of the aggregated
    assert aggregated.shape[0] > 0

    # Test the data type of the aggregated
    assert aggregated.dtype in (int, float)
