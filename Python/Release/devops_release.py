import pandas as pd
li = pd.read_csv('config_file.csv' , header = None).values.tolist()
df = pd.read_csv('releaselog.txt', delimiter='/' , header = None)
df_final = pd.DataFrame()
for i in li:
    df_final = df_final.append(df[(df[1] == i[0]) & (df[2] == i[1])])
df_final.to_csv('release.txt', sep = '/', header = None, index = False)