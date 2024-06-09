import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import cleaning


def Q1_analysis():
    df = cleaning.get_Q1_df()

    is_pop = df["playlist_genre"] == "pop"
    df = df[is_pop]

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

    corr_matrix = important_df.corr()

    popularity_corr = corr_matrix["Streams"].drop("Streams")

    print(popularity_corr)

    plt.figure(figsize=(10, 6))
    palette = [
        "#D98672" if value < 0 else "#859FE5"
        for value in popularity_corr.values
    ]
    sns.barplot(
        x=popularity_corr.index, y=popularity_corr.values, palette=palette
    )

    plt.xticks(rotation=90)
    plt.xlabel("Factors")
    plt.ylabel("Correlation with # of Streams")
    plt.title("Correlation of Factors with # of Streams")
    plt.show()
    plt.savefig("")
