'''
1. pivot：无法聚合，只能简单重塑，如果存在重复数据将会报错；常用于处理非数字数据。
2. pivot_table：可以聚合，正好弥补 pivot 的缺陷。
列转行：多列转为一行

REMEMBER
Sorting by one or more columns is supported by sort_values

The pivot function is purely restructuring of the data, pivot_table supports aggregations

The reverse of pivot (long to wide format) is melt (wide to long format)
'''

import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt

data_path = "./datas/linkflow_data_sample.csv"
sample_data:DataFrame = pd.read_csv(data_path,header=None,names=['user_id','action','fre'])

# sort_values,by=[col1,col2...]指定列名
print(sample_data.sort_values(by=['fre'],ascending=False))
# 宽表和长表转换 long table,wide table
# 长表转换成宽表，使用pivot函数,返回一个DataFrame
# 以user_id为行名，action作为列名，对频次重塑成一行
sample_data_wide1 = sample_data.pivot(index='user_id',columns='action',values=['fre'])
print('\n',sample_data_wide1.index)

sample_data_wide2 = sample_data.pivot_table(index='user_id',columns='action',values='fre')
print('\n',sample_data_wide2)

df = pd.DataFrame({'foo': ['one', 'one', 'one', 'two', 'two',
                           'two'],
                   'bar': ['A', 'B', 'C', 'A', 'B', 'C'],
                   'baz': [1, 2, 3, 4, 5, 6],
                   'zoo': ['x', 'y', 'z', 'q', 'w', 't']})
print(df)
df_wide_foo = df.pivot(index='foo',columns='bar')

print('\nwide:',df_wide_foo,'\n baz:',df_wide_foo['baz'])

df_wide_foo_table = df.pivot_table(index='foo',columns='bar',values='baz',aggfunc='sum')
print("\ndf_wide_foo_table: ",df_wide_foo_table)
# 宽表转换成长表，使用melt函数进行打散
# id_vars:就是我们自行指定哪些列作为identifier variables
# value_vars:指定哪些列被unprivo
# var_name：给varivale那一列的别名。如果没指定或者为None，那么则默认为frame.columns.name 或者varivale
# value_name：给value那一列的别名。默认为value
sample_data.melt()


