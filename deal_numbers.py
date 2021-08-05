'''
date: 2021/08/01
function: 将MATLAB保存的数组储存到python的list里，并且用逗号隔开
author: Huang J.H.

'''


import numpy as np
import pandas as pd
import os
os.chdir('/Users/explor/Documents/MATLAB')
filename = 'shortest_route.txt' # txt文件和当前脚本在同一目录下，所以不用写具体路径
pos = []
Efield = []
with open(filename, 'r') as file_to_read:
    while True:
        lines = file_to_read.readline() # 整行读取数据
        if not lines:
            break
            pass
        p_tmp = [float(i) for i in lines.split()] # 将整行数据分割处理，如果分割符是空格，括号里就不用传入参数，如果是逗号， 则传入‘，'字符。
        pos.append(p_tmp)  # 添加新读取的数据
        pass
    pos = np.array(pos) # 将数据从list类型转换为array类型。
    pass

