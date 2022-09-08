import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt

data_path = "./datas/linkflow_data_sample.csv"
sample_data:DataFrame = pd.read_csv(data_path,header=None,names=['user_id','action','fre'])
#sample_data.plot()

#sample_data['fre'].plot()
#sample_data.plot.scatter(x='action',y='fre',alpha=0.5)
#sample_data.plot.box()
# I want each of the columns in a separate subplot.
# axs = sample_data.plot.area(figsize=(12, 4), subplots=True)

# customize, extend or save the resulting plot.
fig, axs = plt.subplots(figsize=(12, 4))
sample_data.plot.area(ax=axs)
axs.set_ylabel("NO$_2$ concentration")
#fig.savefig("no2_concentrations.png")


plt.show()
