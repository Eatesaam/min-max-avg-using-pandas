import pandas as pd
import datetime as dt

df = pd.read_excel("test.xlsx")

df['release'] = pd.to_datetime(df['release'])
df['analysis'] = pd.to_datetime(df['analysis'])

df["days"] = (df["release"] - df["analysis"]).dt.days

da = pd.DataFrame()
da['maximum'] = df.groupby(["artname"])['days'].max()
da['minimum'] = df.groupby(["artname"])['days'].min()
da['average'] = df.groupby(["artname"])['days'].mean()
# da['artname'] = df['artname'].unique()

print(da)
data_list = da.values.tolist()
# print(data_list)
index = da.index
index = list(index)
# print(ind)
# js = da.to_json(orient = 'index')
# print(js)
# dic = da.to_csv("file.csv")

for value, index in zip(data_list,index):
    art = index
    minimum = value[1]
    maximum = value[0]
    average = value[2]
    print(f"artname:{art},maximum:{maximum},minimum:{minimum},average:{average}")