import datapane as dp
import pandas as pd


df = pd.read_csv("awards/2022/MVP.csv")
df = df.drop(['Year', 'Award'], axis=1)

table = dp.DataTable(df)

app = dp.Report(table)
app.upload(name="NBA-Awards-Explore")
