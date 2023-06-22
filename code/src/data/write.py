"""
Register data writers
"""
from re import match

import pandas as pd

from src.utils import error


def df_to_file(df: pd.DataFrame, path: str, **kwargs):
    funcs = {
        ".*.parquet": df.to_parquet,
        ".*.p": df.to_pickle,
        ".*.csv": df.to_csv,
        ".*.xlsx": df.to_excel,
    }
    for pattern, func in funcs.items():
        if match(pattern, path) is not None:
            func(path, **kwargs)
            return True
    error(
        f"{path} does not match a known file pattern {', '.join(list(funcs.keys()))}"
    )
