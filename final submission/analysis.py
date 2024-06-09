import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import cleaning
import numpy as np


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
    plt.savefig("output/Q1_correlation_graph")
    plt.close()


def Q2_analysis():
    df, age_groups = cleaning.get_Q2_df()

    fig, [ax1, ax2, ax3] = plt.subplots(ncols=3, figsize=(15, 7))

    axes = [ax1, ax2, ax3]

    for age, axis in zip(age_groups, axes):
        is_age = df["Age"] == age
        age_df = df[is_age]
        total_counts = age_df.count()

        genre_counts = age_df["fav_music_genre"].value_counts()

        axis.bar(genre_counts.index, genre_counts.values)

        axis.set_xlabel("Favorite Music Genre")
        axis.set_ylabel("Count")
        axis.set_title(
            f"{age}",
            fontdict={"fontsize": 20},
        )

        print(total_counts)

        axis.tick_params(axis="x", rotation=90)

    plt.show(axis)
    plt.savefig("output/Q2_bar_graphs")
    plt.close()


def Q3_analysis():
    tempo_counts, key_counts, duration_counts = cleaning.get_Q3_dfs()

    ax = tempo_counts.plot(
        kind="bar",
        x="unique_values",
        y="counts",
        color="skyblue",
        legend=False,
    )

    ax.set_xlabel("Tempo")
    ax.set_ylabel("Count")
    ax.set_title("Tempo Counts")
    ax.set_xticks(
        np.arange(
            0,
            203,
            step=5,
        )
    )
    ax.set_xlim(
        0,
        tempo_counts["unique_values"].max()
        - tempo_counts["unique_values"].min()
        - 11,
    )

    plt.show(ax)
    plt.savefig("output/Q3_tempo_counts")
    plt.close()

    ax = key_counts.plot(
        kind="bar",
        x="unique_values",
        y="counts",
        color="skyblue",
        legend=False,
    )

    ax.set_xlabel("Key")
    ax.set_ylabel("Count")
    ax.set_title("Key Counts")
    ax.set_xticks(
        np.arange(
            -1,
            12,
        )
    )
    ax.set_xlim(-1, key_counts["unique_values"].max() + 1)

    plt.show(ax)
    plt.savefig("output/Q3_key_counts")
    plt.close()

    ax = duration_counts.plot(
        kind="bar",
        x="unique_values",
        y="counts",
        color="skyblue",
        legend=False,
    )

    ax.set_xlabel("Duration (seconds)")
    ax.set_ylabel("Count")
    ax.set_title("Duration Counts")
    ax.set_xticks(
        np.arange(
            0,
            600,
            step=10,
        )
    )

    ax.set_xlim(
        0,
        220,
    )

    plt.show(ax)
    plt.savefig("output/Q3_duration_counts")
    plt.close()
    
def main():
    Q1_analysis()

if __name__ =
