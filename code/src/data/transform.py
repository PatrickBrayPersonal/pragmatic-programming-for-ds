"""
Register functions for filtering and transforming data
"""
from pandas import DataFrame


def drop_pattern(df: DataFrame, pattern: str) -> DataFrame:
    """Drops columns from the dataframe that match the regex pattern provided

    Args:
        df (DataFrame):
        pattern (str): regex drop pattern

    Returns:
        DataFrame:
    """
    return df.drop(columns=df.columns[df.columns.str.contains(pattern)])


def select_pattern(df: DataFrame, pattern: str) -> DataFrame:
    """Selects columns from the dataframe that match the regex pattern provided

    Args:
        df (DataFrame):
        pattern (str): regex select pattern

    Returns:
        DataFrame:
    """
    return df.filter(regex=pattern)


def column_ranks(
    df: DataFrame, on_col: str, by: str, top_n: int = 1000
) -> DataFrame:
    """Explodes a list column and provides ranks by the "by" group
    Args:
        df (DataFrame): _description_
        on_col (str): _description_
        by (str): _description_
        top_n (int, optional): _description_. Defaults to 1000.

    Returns:
        DataFrame: _description_
    """
    df = df.groupby([by, on_col]).agg("count").reset_index()
    count_col = f"{on_col}_count"
    df.rename(columns={df.columns[-1]: count_col}, inplace=True)
    rank_col = f"{on_col}_rank"
    df[rank_col] = df.groupby(by)[count_col].rank(ascending=False)
    df = df[df[rank_col] <= top_n]
    return df[[by, on_col, rank_col, count_col]]
