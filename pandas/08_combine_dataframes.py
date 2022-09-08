'''
concat:这个就是简单的堆沿着横纵轴合并.其一般用于堆叠，可以用于纵向和横向的堆叠，只需要对应地选择axis参数即可
       但无法指定关联的key.
       # axis:{0/'index', 1/'columns'}, default 0 指定关联方向，是往后追加还是横向
        # keys 参数 ：为了明确哪些数据来源于哪个变量
merge:这种方式比较像SQL语句，有多种参数可选，是比较推荐的
combine_first:主要用来合并缺失值的。
join:其用于将两表按照索引列进行合并，能使用的参数也相对比较少.
     https://zhuanlan.zhihu.com/p/108674041
'''

# 对多个表进行关联
import pandas as pd
from pandas import DataFrame
import random

data_path = "./datas/linkflow_data_sample.csv"
sample_data:DataFrame = pd.read_csv(data_path,header=None,names=['user_id','action','fre'])

# 975139
user_id_df = sample_data['user_id']
user_id_df = user_id_df.drop_duplicates(inplace=False)
user_count = user_id_df.count()
labels = [random.getrandbits(1) for i  in range(user_count+1)]

user_id_df = pd.DataFrame(user_id_df,columns=['user_id'])
user_id_df['label'] = labels
user_id_df = user_id_df.head(10000)
print(user_id_df)

# merge:类似sql使用
# left:表示左表 right:表示右表
# how:连接方式，{‘left’, ‘right’, ‘outer’, ‘inner’, ‘cross’}, default ‘inner’
# on: 可以是一个指定的label，或list(表示多个条件),关联的条件，Column or index level names to join on
# left on和right on参数，当两个表的关联的某一列名称不同，但含义相同
join_df = pd.merge(left=sample_data,right=user_id_df,how='left',left_on=['user_id'],right_on=['user_id'])

# on参数指定多个列作为连接列时，这些列都要在调用join()方法的DataFrame中，此时，
# 传入join()方法的DataFrame必须为多重行索引(MultiIndex)，且与on指定的列数相等，否则会报错。
# 当列重叠时会报错，如果是按照行拼接，需要指定重叠列的后缀
df1 = pd.DataFrame({'A': [3, 4, 8, 9], 'B': [1.2, 2.4, 4.5, 7.3], 'C': ["aa", "bb", "cc", "dd"]})
df2 = pd.DataFrame({'D': [1, 2]})
df3 = pd.DataFrame({'A': [1, 2,3,4],'F':[5,8,12,4]})
print("join 按行拼接:",df1.join(df2))
print("join 列重叠，按行拼接:",df1.join(df3,lsuffix="_l",rsuffix="_r"))
print("join设置行索引，相当于对按列关联：",df1.set_index("A").join(df3.set_index("A"),on="A"))

# 默认是按照行索引拼接，如果是想按照列索引拼接，则需要设置索引。
# 相当于，把user_id设置成了行索引
join_df2 = sample_data.set_index("user_id").join(user_id_df.set_index("user_id"),on="user_id")

print("join_df1 shape:",join_df.shape," join_df2 shape:",join_df2.shape," sample_data shape:",sample_data.shape)

print(join_df2)
print(join_df)

