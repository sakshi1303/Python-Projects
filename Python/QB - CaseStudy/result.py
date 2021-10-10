import pandas as pd
import json
from pandas.io.json import json_normalize
df_timesheets = pd.read_csv('timesheets.csv', sep = '|')
df_equipment = pd.read_csv('equipment_lu.csv', sep = '|')
df_machine = pd.read_json('machine_transaction.json', orient = 'records')
#print(df_timesheets.head())
#print(df_equipment.head())
#print(df_machine.head())
with open('machine_transaction.json') as f:
    jdata = json.load(f)
#print(type(jdata))
df_res = json_normalize(jdata, None, None)
print(df_res.head())
df_final = df_res.merge(df_equipment, on = 'eq_id')
print(df_final.head())