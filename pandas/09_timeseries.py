'''
处理时间序列数据（time series data）

REMEMBER：
1.Valid date strings can be converted to datetime objects using to_datetime function or as part of read functions.

2.Datetime objects in pandas support calculations, logical operations and convenient date-related properties using the dt accessor.

3.A DatetimeIndex contains these date-related properties and supports convenient slicing.

4.Resample is a powerful method to change the frequency of a time series.
'''

import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt

data_path = "./datas/air_quality_no2_long.csv"
air_quality_df:DataFrame = pd.read_csv(data_path)
air_quality_df.rename(columns={"date.utc":"datetime"},inplace=True)
print(air_quality_df.head(5))
# 使用to_datetime方法，将原来str类型的，转换为datetime64类型的，后面可以使用datetime的相关方法进行计算
air_quality_df['datetime'] = pd.to_datetime(air_quality_df['datetime'])
# Name: datetime, dtype: datetime64[ns, UTC]
print('\nto_datetime:\n',air_quality_df['datetime'].head(5))

# 也可以在读取时间序列相关的数据时，设置parse_dates参数
air_quality_df:DataFrame = pd.read_csv(data_path,parse_dates=["date.utc"])
air_quality_df.rename(columns={"date.utc":"datetime"},inplace=True)
print('\nto_datetime2:\n',air_quality_df['datetime'].head(5))

# max min
print('max,min:',air_quality_df['datetime'].max(),air_quality_df['datetime'].min(),air_quality_df['datetime'].max()-air_quality_df['datetime'].min())
# 从datetime列中解析month,week等信息
air_quality_df['month'] = air_quality_df['datetime'].dt.month
air_quality_df['week'] = air_quality_df['datetime'].dt.week
air_quality_df['hour'] = air_quality_df['datetime'].dt.hour
air_quality_df['dayofweek'] = air_quality_df['datetime'].dt.dayofweek
air_quality_df['date'] = air_quality_df['datetime'].dt.date



print(air_quality_df.head(5))
print(air_quality_df['week'].value_counts(),air_quality_df['month'].value_counts(),
      air_quality_df['hour'].value_counts(),air_quality_df['date'].value_counts())

# fig,ax = plt.subplots(3,2)
# air_quality_df['date'].value_counts().sort_index().plot(ax=ax[0,0])
# air_quality_df['hour'].value_counts().sort_index().plot(ax=ax[0,1])
# air_quality_df['month'].value_counts().sort_index().plot(ax=ax[1,0])
# air_quality_df['week'].value_counts().sort_index().plot(ax=ax[1,1])
# air_quality_df['dayofweek'].value_counts().sort_index().plot(ax=ax[2,0])
# plt.show()

print(air_quality_df.groupby(["dayofweek","location"])["value"].mean())

# 以datetime为行，location为列，将同一各datetime下的所有location聚合成一行
datetime_group = air_quality_df.pivot(index='datetime',columns="location",values=['value'])
print(datetime_group.head(10))
# datetime_group的index为datetime,现在变成了一个时间索引 column为location
print('time index:',datetime_group.index.year,datetime_group.index.weekday)
# 时间时间索引切片
print('time slice index:',datetime_group["2019-05-20":"2019-05-21"])
datetime_group["2019-05-20":"2019-05-21"].plot()
plt.show()

# rule:DateOffset, Timedelta or str
'''
resample方法：
* it provides a time-based grouping, by using a string (e.g. M, 5H,…) that defines the target frequency
* it requires an aggregation function such as mean, max,…
'''
time_groupby = datetime_group.resample("24H").max()
print("time_groupby:\n",time_groupby)
print(time_groupby.index.freq)