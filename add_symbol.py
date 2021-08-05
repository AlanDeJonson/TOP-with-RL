'''
date: 2021/08/01
function: 将坐标数据转换成适合于MATLAB读取的50*2数组
author: He R.G.
'''


import pandas as pd
import numpy as np
import os

os.chdir('/Users/explor/Desktop/Traveling_Officer_Problem/data_set')
nodes = pd.read_csv('50_vio_nodes.csv')
a = np.empty(30,dtype='object')
for i in range(30):
    for j in range(100):
        if j%2 == 0:
            a[i] = str(a[i]) + str(nodes.iloc[i][j]) + ','
        else:
            a[i] = str(a[i]) + str(nodes.iloc[i][j]) + ';'
