import json
import os

import datapane as dp
import altair as alt
import pandas as pd


def award_box(year: str, award: str):
    with open("db/ranks.json") as f:
        ranks = json.load(f)
        data = ranks[award]
        return pd.DataFrame(data, columns=["stat", "rank", "player", "year"])


if __name__ == "__main__":
    limit = 20

    blocks = []
    for year in sorted(os.listdir("awards"), reverse=True):
        path = os.path.join("awards", year)
        if not os.path.isdir(path):
            continue

        for award in ["All-NBA", "All-Defensive", "All-Rookie"]:
            test_df = award_box(year, award)

            c = (
                alt.Chart(test_df)
                .mark_boxplot(extent=0.5)
                .encode(
                    x="stat:O",
                    y="rank:Q",
                    color=alt.Color("stat", legend=None),
                    tooltip=["player", "rank", "year"],
                )
            )

            blocks.append(dp.Plot(c, label=f"{award} - {year}"))

    app = dp.App(dp.Select(blocks=blocks, type=dp.SelectType.DROPDOWN))
    app.upload(name="NBA-Awards-Leaders")
