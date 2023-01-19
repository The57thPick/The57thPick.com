import os

import datapane as dp
import pandas as pd

blocks = []
for year in sorted(os.listdir("awards"), reverse=True):
    path = os.path.join("awards", year)
    if not os.path.isdir(path):
        continue

    for award in sorted(os.listdir(path)):
        if not award.endswith(".csv"):
            continue

        df = pd.read_csv(os.path.join("awards", year, award))
        df = df.drop(["Year", "Award"], axis=1)

        name = award.split(".")[0]
        blocks.append(dp.DataTable(df, label=f"{name} - {year}"))

app = dp.App(dp.Select(blocks=blocks, type=dp.SelectType.DROPDOWN))
app.upload(name="NBA-Awards-Explore")
