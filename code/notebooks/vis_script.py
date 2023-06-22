import pandas as pd

from src.data.read import file_to_df
from src.data.transform import column_ranks
from src.data.write import df_to_file


def top_n_by(
    songs: pd.DataFrame,
    by: str,
    on_col: str,
    top_n: int = 3,
    delim: str = ", ",
) -> pd.Series:
    """_summary_

    Args:
        songs (pd.DataFrame): _description_
        by (str): _description_
        on_col (str): _description_
        top_n (int, optional): _description_. Defaults to 3.
        delim (str, optional): _description_. Defaults to ", ".

    Returns:
        pd.Series: _description_
    """
    playlists = column_ranks(songs, by=by, on_col=on_col, top_n=top_n)
    strings = playlists.groupby(by)[on_col].agg(lambda x: delim.join(x))
    return strings


songs = file_to_df("data/raw/example_data.parquet")
genres = top_n_by(
    songs.explode("genres"), by="playlist", on_col="genres", top_n=3
)
artists = top_n_by(songs, by="playlist", on_col="artist", top_n=3)

df = pd.DataFrame()
df["genres"] = genres
df["artists"] = artists


print(df)
df_to_file(df, "data/processed/genres.parquet")
print("done")
