'''
分组统计，按照split-apply-combine原则
split:按照列分组
apply:使用函数对每组进行计算
combine：返回一个结构化的结果（如DataFrame)

REMEMBER：
Aggregation statistics can be calculated on entire columns or rows

groupby provides the power of the split-apply-combine pattern

value_counts is a convenient shortcut to count the number of entries in each category of a variable
'''

import pandas as pd
from pandas import DataFrame

data_path = "./datas/linkflow_data_sample.csv"
sample_data:DataFrame = pd.read_csv(data_path,header=None,names=['user_id','action','fre'])
sample_data['fre_mean'] = sample_data['fre']/sample_data['fre'].mean()
print(sample_data)
# Aggregating statistics(聚合统计）
print('mean: ',sample_data['fre'].mean())
# describe:显示指定列的均值，标准差，最小值，最大值，分位数（1/4，1/2，3/4）等等
print('describe ',sample_data['fre'].describe())

# agg()
agg_out = sample_data.agg({
    'fre':['mean','max','min','skew'],
    'fre_mean':['mean','max','min','median']
})
print('agg:',type(agg_out),agg_out)

# 分组聚合，groupby agg
print('groupby--',sample_data.groupby('action')['fre'].mean())
# 以action分组后，计算所有整数列的均值，
g1 = sample_data.groupby('action').mean()
print('sample_data.groupby(\'action\').mean()',g1)
# 取action列和fre列，在按action分组，求均值
print('\n --',sample_data[['action','fre']].groupby('action').mean())

# 多值分组
print('多值分组: ',sample_data.groupby(['action','user_id']).mean(),' \nindex:',
      sample_data.groupby(['action','user_id']).mean().index)

# value_counts():统计每个事件的覆盖人群数量,下面两个方法等价
print(sample_data['action'].value_counts())
print('\n',sample_data.sort_values().groupby(['action'])['action'].count())

# 分组统计每个事件，频次分布，返回一个Series
print('\n',sample_data.groupby(['action'])['fre'].value_counts())
# 分组统计每个事件，对应的每个事件的总的频次数量,与value_counts完全不同
print('\n',sample_data.groupby(['action'])['fre'].count())

