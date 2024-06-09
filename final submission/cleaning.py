import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
import seaborn as sns
from ast import literal_eval


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

    is_pop = merged_df["playlist_genre"] == "pop"
    df = merged_df[is_pop]

    relevant_cols = [
        "danceability",
        "energy",
        "loudness",
        "speechiness",
        "acousticness",
        "instrumentalness",
        "liveness",
        "valence",
        "tempo",
        "duration_ms",
        "Streams",
    ]

    important_df = df[relevant_cols]

    return important_df


def Q1_data_loading() -> tuple[DataFrame, DataFrame]:
    main_df = pd.read_csv("data/spotify_songs.csv")
    stream_df = pd.read_csv("data/stream_data.csv", sep="#")

    return main_df, stream_df


def get_Q1_df() -> DataFrame:
    main_df, stream_df = Q1_data_loading()

    merged_df = Q1_data_cleaning(main_df, stream_df)
    return merged_df


def Q2_data_cleaning(df) -> tuple[DataFrame, list]:
    df = df.drop(df.columns[0], axis=1)

    important_cols = ["Age", "fav_music_genre"]
    important_data = df[important_cols]

    important_age_groups = ["12-20", "20-35", "35-60"]
    age_group_filter = important_data["Age"].isin(important_age_groups)
    important_data = important_data[age_group_filter]

    return important_data, important_age_groups


def Q2_data_loading() -> DataFrame:
    excel_file = pd.read_excel("data/user_questions.xlsx")
    excel_file.to_csv("data/user_questions.csv")

    return pd.read_csv("data/user_questions.csv")


def get_Q2_df() -> tuple[DataFrame, list]:
    df = Q2_data_loading()

    return Q2_data_cleaning(df)


def Q3_data_cleaning(df) -> tuple[DataFrame, DataFrame, DataFrame]:
    tempo_df = df["tempo"]
    key_df = df["key"]
    duration_df = df["duration_ms"]

    tempo_counts = (
        tempo_df.astype(int)
        .value_counts(sort=False)
        .rename_axis("unique_values")
        .reset_index(name="counts")
        .sort_values(by="unique_values")
    )

    key_counts = (
        key_df.value_counts(sort=False)
        .rename_axis("unique_values")
        .reset_index(name="counts")
        .sort_values(by="unique_values")
    )

    duration_counts = (
        duration_df.round(-3)
        .divide(1000)
        .astype(int)
        .value_counts(sort=False)
        .rename_axis("unique_values")
        .reset_index(name="counts")
        .sort_values(by="unique_values")
    )

    return tempo_counts, key_counts, duration_counts


def Q3_data_loading() -> DataFrame:
    return pd.read_csv("data/1000songdata.csv")


def get_Q3_dfs():
    df = Q3_data_loading()

    return Q3_data_cleaning(df)
