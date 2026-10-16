import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random
import time
import math as mt


ans = np.array([0] * 100)
N = 5
l = ['300339','002829','601698','516110','513050','300722','002253','002362','000592','003000','603321','516390']
dff = [pd.read_csv(i + '.csv').dropna()['开盘'].values for i in l]
www = [pd.read_csv(i + '.csv').dropna()['收盘'].values for i in l]
rg = np.linspace(0.9,1.1,100)
for T in range(N) :
    random.seed(time.time() + T)
    ls = []
    for j in np.nditer(rg):
        wallet = 10000
        stock=[0] * len(l)
        flag = [1] * len(l)
        date = [0] * len(l)
        def lb(data,pt,wallet,j):
            global date
            if (int(dff[k][-data] < dff[k][-data-7] * j) ^ int(j > 1)) and date[k] > 0:
                date[k] += 1
                stock[pt] += wallet // (dff[k][data] * 100) * 100
                wallet %=  dff[k][data] * 100
                flag[pt] = 0
            else:
                wallet += stock[pt] * dff[k][data]\
                    * 0.9975
                stock[pt] = 0
                flag[pt] = 1
                if date[k] > 0: date[k] -= 1
                else :date[k] += 1
            return wallet
        for i in range(365,1,-1):
            lt = list(range(len(l)))
            random.shuffle(lt)
            for k in lt:
                wallet =lb(i,k,wallet,j,)
                # except:
                #     print(k)
                    # exit()
        sum = 0
        for k in range(len(l)):
            sum += stock[k] * dff[k][-1]
        ls.append(sum + wallet)
    ans = ans + np.array(ls)

plt.plot(rg,ans / N)
plt.show()
