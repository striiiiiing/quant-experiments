import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('516390.csv').dropna()['开盘'].values
w = pd.read_csv('516390.csv').dropna()['收盘'].values
ls = []
rg = np.linspace(0.9,1.1,100)
for j in np.nditer(rg):
    wallet = 10000
    stock = 0
    flag = 1
    for i in range(df.shape[0]-365,df.shape[0]):
        if (df[i] < w[i-1] * j) ^ (j >= 1.0):
            stock += wallet // (df[i] * 100) * 100
            wallet %=  df[i] * 100
            flag = 0
        else:
            wallet += stock * df[i]\
                * 0.998
            stock = 0
            flag = 1
    ls.append(wallet+stock * df[-1])
plt.plot(rg,ls)

ls = []
rg = np.linspace(0.9,1.1,100)
for j in np.nditer(rg):
    wallet = 10000
    stock = 0
    flag = 1
    for i in range(df.shape[0]-365,df.shape[0]):
        if (df[i] < df[i-1] * j) ^ (j >= 1.0):
            stock += wallet // (df[i] * 100) * 100
            wallet %=  df[i] * 100
            flag = 0
        else:
            wallet += stock * df[i]\
                * 0.998
            stock = 0
            flag = 1
    ls.append(wallet+stock * df[-1])
plt.plot(rg,ls)


ls = []
rg = np.linspace(0.9,1.1,100)
for j in np.nditer(rg):
    wallet = 10000
    stock = 0
    flag = 1
    for i in range(df.shape[0]-365,df.shape[0]):
        if (w[i] < df[i] * j) ^ (j >= 1.0):
            stock += wallet // (w[i] * 100) * 100
            wallet %=  w[i] * 100
            flag = 0
        else:
            wallet += stock * w[i]\
                * 0.998
            stock = 0
            flag = 1
    ls.append(wallet+stock * w[-1])
plt.plot(rg,ls)


ls = []
rg = np.linspace(0.9,1.1,100)
for j in np.nditer(rg):
    wallet = 10000
    stock = 0
    flag = 1
    for i in range(df.shape[0]-365,df.shape[0]):
        if (w[i] < df[i-1] * j) ^ (j >= 1.0):
            stock += wallet // (w[i] * 100) * 100
            wallet %=  w[i] * 100
            flag = 0
        else:
            wallet += stock * w[i]\
                * 0.998
            stock = 0
            flag = 1
    ls.append(wallet+stock * w[-1])
plt.plot(rg,ls)

ls = []
rg = np.linspace(0.9,1.1,100)
for j in np.nditer(rg):
    wallet = 10000
    stock = 0
    flag = 1
    for i in range(df.shape[0]-365,df.shape[0]):
        if (w[i] < w[i-1] * j) ^ (j >= 1.0):
            stock += wallet // (w[i] * 100) * 100
            wallet %=  w[i] * 100
            flag = 0
        else:
            wallet += stock * w[i]\
                * 0.998
            stock = 0
            flag = 1
    ls.append(wallet+stock * w[-1])
plt.plot(rg,ls)
plt.show()
