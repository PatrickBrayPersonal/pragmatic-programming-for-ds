import streamlit as st

from src.data.read import file_to_df

# Read the table data from a csv file
genres = file_to_df("data/processed/genres.parquet")
# Display the table as an interactive dataframe
st.dataframe(genres)
