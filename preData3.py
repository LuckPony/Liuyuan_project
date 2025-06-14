import pandas as pd
import numpy as np

df = pd.read_excel('data/data_3.xlsx', engine='openpyxl')
df.columns = df.columns.str.strip()  # 清理列名空格

df['原始顺序'] = range(len(df))

cols_to_check = [col for col in df.columns if col not in ['就诊流水号', '原始顺序']]
df[cols_to_check] = df[cols_to_check].replace([0, 2], np.nan)


def merge_group(group):
    group_filled = group.ffill().bfill()
    return group_filled.iloc[0]

df_merged = df.groupby('就诊流水号', group_keys=False).apply(merge_group)

df_merged = df_merged.sort_values('原始顺序')
df_merged.drop(columns='原始顺序', inplace=True)

df_merged.to_excel('data/data_3_去重.xlsx', index=False)
