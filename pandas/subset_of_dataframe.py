import pandas as pd
from pandas import DataFrame

data_path = "./datas/linkflow_data_sample.csv"
sample_data:DataFrame = pd.read_csv(data_path,header=None,names=['user_id','action','fre'])
# 获取指定的单列，如user_id,返回Series
print(sample_data["user_id"])
# 获取多列,传入列名list,返回一个DataFrame
print(sample_data[['user_id','action']])

# 条件过滤，用条件筛选出满足条件的所有行
# 如筛选频次>5的所有行,返回一个DataFrame(user_id,action,fre)
print(sample_data[sample_data['fre']>5])
# 返回action='WECHAT_WXA__PAGE_SHOW'的所有行
print(sample_data[sample_data['action']=='WECHAT_WXA__PAGE_SHOW'])
print(sample_data[sample_data['action'].isin(['UDE_362ZKHLROK7','WECHAT_WXA__PAGE_SHOW'])])

# 筛选频次在[5,8]这个区间
# 多条件When combining multiple conditional statements, each condition must be surrounded by parentheses ().
# Moreover, you can not use or/and but need to use the or operator | and the and operator &.
print("==",sample_data['fre'].isin([5,8]))
print("==",sample_data[sample_data['fre'].isin([5,8])],sample_data[(sample_data['fre']>=5) & (sample_data['fre']<=8)]['fre'].isin([6]))
# notna()方法，筛选不为Null的行, notna()和notnull()等价, isna(),isnull()
print("notna()",sample_data[sample_data['user_id'].notna()])
#  select specific rows and columns from a DataFrame
# 第一个表示想要筛选的行，第二个表示想要筛选的列
print(" select specific rows and columns from a DataFrame: ",sample_data.loc[sample_data['fre']==5,['user_id','fre']])
print(" select specific rows and columns from a DataFrame: ",sample_data.loc[0:2,['user_id']])
print(" select specific rows and columns from a DataFrame: ",sample_data.iloc[0:2,0])
print("slice: ",sample_data[0:2], '\n--',sample_data[::2])
print("\n==",sample_data[sample_data['action']=='WECHAT_WXA__PAGE_SHOW'].loc[:,'fre'].mean())
action_mean = sample_data[sample_data['action']=='WECHAT_WXA__PAGE_SHOW'].loc[:,'fre'].mean()
print('action_mean',action_mean,type(action_mean))
# 广播操作
# sample_data['fre'] = sample_data['fre']/action_mean
# print("mean:",sample_data)
# 增加一列
sample_data.loc[:,'action_fre_mean'] = sample_data['fre']/action_mean
sample_data.dropna(axis=0,how='all')
print("add column:",sample_data)
# 自定义函数


