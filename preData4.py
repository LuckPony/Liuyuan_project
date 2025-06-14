import pandas as pd

df1 = pd.read_excel('data/data_1_clear.xlsx', engine='openpyxl')
df2 = pd.read_excel('data/data_2_clear.xlsx', engine='openpyxl')
df3 = pd.read_excel('data/data_3_clear.xlsx', engine='openpyxl')
df4 = pd.read_excel('data/data_4_clear.xlsx', engine='openpyxl')
df5 = pd.read_excel('data/data_5_clear.xlsx', engine='openpyxl')
df6 = pd.read_excel('data/data_6_clear.xlsx', engine='openpyxl')

df = pd.merge(df1, df2, on='就诊流水号', how='left')
df = pd.merge(df, df3, on='就诊流水号', how='left')
df = pd.merge(df, df4, on='就诊流水号', how='left')
df = pd.merge(df, df5, on='就诊流水号', how='left')
df = pd.merge(df, df6, on='就诊流水号', how='left')


