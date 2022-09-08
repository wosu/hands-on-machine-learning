import pandas as pd

# 读取表格数据
from pandas import DataFrame

data_path = "./datas/linkflow_data_sample.csv"
sample_data:DataFrame = pd.read_csv(data_path,header=None,names=['user_id','action','fre'])
print('sample data: ',sample_data)
print('columns:',sample_data.columns)
# 更改列名
sample_data.columns = ['user_id','action','frequency']
# 返回Index类型
print('columns af: ' ,type(sample_data.columns),sample_data.columns,sample_data.columns[0])
print('shape:',sample_data.shape)
print('head 10',sample_data.head(10), ' tail 10:',sample_data.tail(10))
# 查看df各列类型,返回的是一个Series
print('dtypes:',type(sample_data.dtypes),sample_data.dtypes,'\n')
print('column action data type:',sample_data.dtypes['action'],'\n')

#  data as a spreadsheet index参数：是否谢列名
# sample_data.to_excel('./datas/linkflow_data_sample.xlsx',sheet_name='test',index=True)

# summary info of dataframe
print('summary info: ',sample_data.info())

# 创建DataFrame
# 分组统计
# 分组聚合
# 统计某个维度的的平均数