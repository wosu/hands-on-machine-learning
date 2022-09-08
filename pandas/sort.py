import pandas as pd
from pandas import DataFrame

data_path = "./datas/linkflow_data_sample.csv"
sample_data:DataFrame = pd.read_csv(data_path,header=None,names=['user_id','action','fre'])

# sort_values:对值排序，by=[]指定排序的列，ascending指定降序还是升序
print(sample_data.sort_values(by=['action','fre'],ascending=False))

# sort_index:对index排序，当axis=0即按照行名进行排序,axis=1时按照列名排序
print(sample_data.sort_index(axis=0,ascending=False))