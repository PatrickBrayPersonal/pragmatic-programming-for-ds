"""
Register data readers
"""
from re import match

import pandas as pd

from src.utils import error


def file_to_df(path: str, **kwargs):
    funcs = {
        ".*.parquet": pd.read_parquet,
        ".*.p": pd.read_pickle,
        ".*.csv": pd.read_csv,
        ".*.xlsx": pd.read_excel,
    }
    for pattern, func in funcs.items():
        if match(pattern, path) is not None:
            return func(path, **kwargs)
    error(
        f"{path} does not match a known file pattern {', '.join(list(funcs.keys()))}"
    )
