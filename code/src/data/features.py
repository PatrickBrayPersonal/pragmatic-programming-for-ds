"""
Register feature engineering functions
"""
from pandas import DataFrame


def pattern_std(df: DataFrame, pattern: str) -> DataFrame:
    """
    Calculate the standard deviation of columns matching a pattern
    returns standard deviation for each row in the dataframe
    """
    return df.filter(regex=pattern).std(axis=1)
