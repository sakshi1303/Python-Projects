import os
import pandas as pd
df = pd.read_csv('releaselog.txt', delimiter='/|:' , engine = 'python', header = None)
df_final, df_new, df_err = pd.DataFrame(), pd.DataFrame(), pd.DataFrame()
for i in range(len(df)):
    if (os.path.exists(df[3].values[i])):
        df_new = df_new.append(pd.DataFrame([[df[1].values[i], df[2].values[i], df[3].values[i], df[4].values[i],df[5].values[i]]]))
        #df_new = df_new.append(pd.DataFrame('/' +  '/'.join([df[0:3].values[i]]) + ':' + ':'.join([df[3:5].values[i]])))
    else:
        df_err = df_err.append(pd.DataFrame([[df[1].values[i], df[2].values[i], df[3].values[i]]]))
df_err.to_csv('error.txt', sep = '/' ,header = None, index = False)
mylist = df_new.values.tolist()
myli = []
for i in mylist:
    mystr = '/' +  '/'.join(i[0:3]) + ':' + ':'.join(i[3:5])
    myli.append(mystr)
df_new = pd.DataFrame(myli)
df_new.to_csv('release_file.txt', header = None, index = False, quoting = None)
df_file = pd.DataFrame()
li = pd.read_csv('config_file.csv' , header = None).values.tolist()
df_file = pd.read_csv('release_file.txt', delimiter='/' , header = None)
for i in li:
    df_final = df_final.append(df_file[(df_file[1] == i[0]) & (df_file[2] == i[1])])
df_final.to_csv('release_final.txt', sep = '/', header = None, index = False)
