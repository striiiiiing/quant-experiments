import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
df = pd.read_csv('516390.csv').dropna()
# df['weight'] = df['weight'].rolling(window=23,center=True).mean()
ls = []
for i in range(2,150):
    res = sm.tsa.seasonal_decompose(df['开盘'][-365:].dropna(),
                                period=i,
                                model="mul")
    # df['trend']=df['weight']- res.seasonal
    ls.append(np.sort(np.abs(res.resid - 1))[-i - 3] / abs(np.max(res.seasonal - 1)) )
pd.DataFrame(ls).plot()
# print(ls)
# plt.legend(labels=['Effect fitting diagram during Day 0 to Day 199'])
# sm.tsa.seasonal_decompose(ls,model="add",period=7).plot()
plt.show()
#平滑20天，否则23