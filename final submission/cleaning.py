import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from ast import literal_eval


def get_Q1_df() -> pd.DataFrame:
    main_df, stream_df = Q1_data_loading()

    merged_df = Q1_data_cleaning(main_df, stream_df)
    return merged_df


def Q1_data_loading() -> tuple[pd.DataFrame, pd.DataFrame]:
    main_df = pd.read_csv("data/spotify_songs.csv")
    stream_df = pd.read_csv("data/stream_data.csv", sep="#")

    return main_df, stream_df


def Q1_data_cleaning(main_df, stream_df):
    main_df_clean = main_df.drop_duplicates(subset="track_id")
    main_df_clean = main_df_clean.dropna()

    stream_df_clean = stream_df.drop(columns=["Date", "Position"])

    stream_df_clean = stream_df_clean.dropna()

    stream_df_clean["Genre"] = stream_df_clean["Genre"].apply(literal_eval)

    # Group by 'Track Name' and 'Artist', sum the 'Streams', and aggregate genres
    stream_grouped = (
        stream_df.groupby(["Track Name", "Artist"])
        .agg(
            {
                "Streams": "sum",
                "Genre": lambda x: list(
                    set([genre for sublist in x for genre in sublist])
                ),
            }
        )
        .reset_index()
    )

    sorted_stream_group = stream_grouped.sort_values(
        "Streams", ascending=False
    )

    merged_df = main_df_clean.merge(
        sorted_stream_group,
        left_on=["track_name", "track_artist"],
        right_on=["Track Name", "Artist"],
    )

    return merged_df
