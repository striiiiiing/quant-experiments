import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
df = pd.read_csv('516390.csv').dropna()
# df['开盘'][30:].plot()
temp = sm.tsa.seasonal_decompose(df['开盘'][-365:].dropna(),
                                period=34,
                                model="mul")
np.abs(temp.seasonal).plot()
np.abs(temp.resid).plot()
np.abs(temp.trend).plot()
plt.show()
#平滑20天，否则23
#29