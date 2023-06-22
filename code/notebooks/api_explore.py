import os

import pandas as pd
import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyClientCredentials

from src.data.write import df_to_file

# set your Spotify app credentials
load_dotenv()
# authorization
client_credentials_manager = SpotifyClientCredentials(
    client_id=os.getenv("CLIENT"), client_secret=os.getenv("SECRET")
)
spotify = spotipy.Spotify(
    client_credentials_manager=client_credentials_manager
)

# query Spotify API
user = "pbnbray"
playlists = spotify.user_playlists(user)

# print the playlist names
data = []
for playlist in playlists["items"][0:10]:
    print(f"Playlist: {playlist['name']}")

    # query Spotify API for tracks in the current playlist
    tracks = spotify.playlist_items(playlist["id"])
    playlist_name = playlist["name"]

    # for each track...
    for item in tracks["items"]:
        track = item["track"]
        artist = spotify.artist(track["artists"][0]["id"])
        data.append(
            [
                playlist_name,
                track["name"],
                track["id"],
                track["artists"][0]["name"],
                artist["genres"],
            ]
        )

df = pd.DataFrame(
    data, columns=["playlist", "track", "track_id", "artist", "genres"]
)

print("done")

df_to_file(df, "data/raw/example_data.parquet")
