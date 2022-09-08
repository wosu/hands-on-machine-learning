'''
参考：https://pandas.pydata.org/docs/getting_started/intro_tutorials/05_add_columns.html

Create a new column by assigning the output to the DataFrame with a new column name in between the [].

Operations are element-wise, no need to loop over rows.

Use rename with a dictionary or function to rename row labels or column names.

'''

import pandas as pd
from pandas import DataFrame

data_path = "./datas/linkflow_data_sample.csv"
sample_data:DataFrame = pd.read_csv(data_path,header=None,names=['user_id','action','fre'])
# 删除指定的列
sample_data.drop(1000000,axis=0,inplace=True)
print(sample_data)
# 从已有的列中，创建新的列
sample_data['fre_square'] = sample_data['fre']*sample_data['fre']
print(sample_data)
#  element-wise, so the * is applied for the values in each row.
sample_data['fre_square'] = (sample_data['fre']*sample_data['fre'])
print('===',sample_data)

# rename the data columns to the corresponding station identifiers used by openAQ
sample_data_rename = sample_data.rename(columns={
    "user_id":"sample_id"
},inplace=False)
sample_data_rename = sample_data.rename(columns=str.upper)
print(sample_data_rename)