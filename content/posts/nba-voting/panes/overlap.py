import json
import os

import rbo
import datapane as dp
import altair as alt
import pandas as pd

from tinydb import TinyDB, Query

DB = TinyDB("db/db.json")
Q = Query()


def truncate(df, col, limit):
    if limit >= len(df):
        limit = len(df) - 1
    return df.sort_values(col)[0:limit]


def award_rbo(year: str, award: str):
    """Calculate the Rank-Biased Overlap (RBO) for the given award.

    See https://github.com/changyaochen/rbo.
    """
    data = DB.search((Q.Award == award) & (Q.Year == str(year)))
    non_placements = ["Voter", "Affiliation", "Year", "Award"]

    with open("db/results.json") as f:
        results = json.load(f)
        standard = results.get(f"{year}-{award}")
        if not standard:
            return None

        distance = []
        for i, row in enumerate(data):
            sample = []
            for key in [k for k in row.keys() if k not in non_placements]:
                v = row[key]
                if v.lower() == "abstained" or not v:
                    continue
                sample.append(v)

            if not sample:
                continue

            d = rbo.RankingSimilarity(standard, sample).rbo()
            if d == 0:
                # NOTE: This is to ensure that the value is visible on the
                # chart.
                #
                # TODO: A better way?
                d = 0.01
            distance.append([row["Voter"], d, "; ".join(sample)])

    return pd.DataFrame(distance, columns=["Voter", "RBO", "Ballot"])


if __name__ == "__main__":
    limit = 20

    blocks = []
    for year in sorted(os.listdir("awards"), reverse=True):
        path = os.path.join("awards", year)
        if not os.path.isdir(path):
            continue

        for award in ["MVP", "COY", "DPOY", "MIP", "6th", "ROY"]:
            rbo_results = award_rbo(year, award)
            rbo_results = truncate(rbo_results, "RBO", limit)

            c = (
                alt.Chart(rbo_results)
                .mark_bar()
                .encode(
                    x="RBO",
                    y=alt.Y(
                        "Voter",
                        sort=alt.EncodingSortField(field="RBO", order="ascending"),
                        title="",
                    ),
                    tooltip=["Ballot", "RBO"],
                    color=alt.Color(
                        "RBO",
                        scale=alt.Scale(
                            scheme="greenblue", domain=[1, 0], reverse=True
                        ),
                    ),
                )
            )
            blocks.append(dp.Plot(c, label=f"{award} - {year}"))

    app = dp.App(dp.Select(blocks=blocks, type=dp.SelectType.DROPDOWN))
    app.upload(name="NBA-Awards-RBO")
