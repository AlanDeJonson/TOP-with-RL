import numpy as np
from datetime import timedelta
from dateutil.parser import parse
import pandas as pd
from math import radians, sin, cos, sqrt, asin
import math

def LLs2Dist(lat1, lon1, lat2, lon2):    # 根据经纬度计算两点间的距离（米）
    lat_diff = (lat1 - lat2)*111000      # 纬度差值（米）
    lon_diff = (lon1 - lon2)*111000*math.cos((lat1+lat2)/2*math.pi/180) # 经度差值（米）
    distance = math.sqrt(lat_diff*lat_diff+lon_diff*lon_diff) # 用勾股定理算距离
    return distance


def t2s(t):  #将时分秒格式的时间转换为秒数
    h,m,s = t.strip().split(":")
    return (int(h) * 3600 + int(m) * 60 + int(s))

tour_ = [[0, 1, 5, 4, 6, 8, 2, 9, 3, 7, 12, 11, 13, 10, 15, 16, 14, 17, 18, 19],
         [19, 18, 12, 11, 17, 16, 13, 15, 14, 10, 8, 7, 9, 3, 6, 4, 5, 1, 2, 0],
         [0, 4, 3, 1, 9, 6, 2, 7, 8, 10, 11, 12, 14, 15, 5, 17, 13, 16, 18, 19],
         [18, 19, 13, 17, 16, 12, 15, 14, 10, 11, 5, 4, 8, 6, 7, 3, 2, 0, 1, 9],
         [19, 16, 15, 18, 17, 14, 13, 12, 9, 7, 6, 8, 11, 4, 5, 3, 10, 2, 1, 0],
         [19, 8, 9, 16, 11, 10, 7, 15, 12, 18, 17, 13, 4, 14, 6, 5, 3, 1, 0, 2],
         [2, 6, 0, 10, 7, 1, 3, 4, 9, 5, 11, 15, 12, 14, 13, 8, 17, 16, 18, 19],
         [6, 0, 1, 7, 4, 3, 5, 2, 9, 8, 10, 11, 13, 14, 12, 16, 15, 18, 19, 17],
         [0, 1, 2, 3, 4, 5, 6, 7, 8, 11, 10, 9, 12, 13, 14, 15, 16, 17, 18, 19],
         [17, 18, 16, 19, 14, 12, 11, 8, 15, 6, 10, 7, 5, 4, 3, 9, 2, 1, 13, 0],
         [17, 19, 1, 11, 15, 18, 16, 14, 12, 13, 10, 0, 8, 9, 7, 6, 5, 4, 3, 2],
         [15, 18, 16, 17, 19, 14, 11, 10, 13, 12, 9, 6, 7, 8, 5, 4, 3, 2, 1, 0],
         [18, 17, 19, 15, 14, 10, 12, 13, 16, 11, 9, 8, 7, 5, 6, 2, 1, 3, 0, 4],
         [4, 2, 3, 1, 6, 8, 5, 7, 9, 10, 14, 15, 16, 13, 11, 12, 17, 18, 19, 0],
         [18, 1, 19, 14, 17, 16, 13, 15, 12, 10, 11, 0, 9, 7, 8, 5, 6, 2, 3, 4],
         [1, 2, 0, 3, 5, 4, 7, 6, 8, 9, 10, 11, 13, 12, 14, 16, 17, 15, 18, 19],
         [11, 17, 16, 14, 18, 15, 19, 13, 12, 9, 7, 10, 8, 6, 5, 2, 3, 4, 0, 1],
         [19, 18, 0, 16, 17, 14, 15, 13, 12, 11, 10, 8, 9, 7, 6, 5, 4, 3, 2, 1],
         [2, 6, 4, 1, 0, 3, 5, 9, 8, 12, 10, 13, 7, 14, 11, 16, 15, 17, 18, 19],
         [0, 1, 5, 3, 2, 4, 6, 7, 8, 10, 12, 9, 13, 14, 15, 16, 11, 18, 17, 19],
         [0, 1, 5, 7, 3, 9, 4, 2, 8, 10, 6, 12, 15, 11, 14, 13, 17, 18, 19, 16],
         [16, 19, 0, 14, 3, 15, 4, 1, 10, 5, 17, 18, 13, 11, 6, 7, 2, 12, 8, 9],
         [5, 2, 0, 1, 3, 4, 6, 9, 8, 10, 12, 11, 7, 15, 14, 13, 16, 17, 18, 19],
         [18, 19, 16, 15, 17, 13, 12, 14, 11, 10, 9, 8, 7, 4, 6, 5, 2, 3, 1, 0],
         [4, 2, 6, 3, 5, 10, 7, 8, 13, 12, 1, 9, 14, 15, 17, 11, 16, 18, 19, 0],
         [3, 4, 0, 1, 5, 2, 13, 7, 6, 12, 8, 9, 10, 11, 15, 16, 17, 18, 14, 19],
         [18, 15, 19, 17, 16, 14, 11, 13, 10, 7, 6, 5, 12, 8, 9, 4, 3, 2, 1, 0],
         [19, 18, 17, 14, 11, 12, 16, 15, 13, 10, 9, 8, 7, 6, 4, 2, 3, 5, 0, 1],
         [0, 1, 7, 5, 3, 6, 2, 4, 8, 10, 9, 14, 11, 12, 13, 15, 16, 17, 18, 19],
         [19, 18, 11, 14, 16, 12, 17, 15, 13, 9, 10, 5, 8, 7, 6, 4, 3, 1, 2, 0]]
# 20nodes violation

tour = [[19, 39, 18, 17, 15, 37, 14, 16, 38, 12, 36, 11, 10, 13, 33, 35, 34, 32, 31, 9, 49, 7, 30, 5, 4, 8, 29, 44, 2, 3, 6, 23, 48, 45, 47, 22, 1, 41, 42, 26, 43, 28, 46, 27, 25, 24, 0, 21, 20, 40],
        [30, 11, 31, 33, 10, 34, 32, 14, 13, 16, 35, 4, 36, 12, 15, 17, 37, 0, 19, 18, 1, 6, 7, 42, 2, 3, 38, 39, 20, 22, 41, 23, 24, 21, 5, 40, 46, 29, 8, 25, 26, 9, 43, 44, 28, 45, 27, 47, 48, 49],
        [39, 37, 38, 35, 19, 15, 36, 16, 17, 18, 34, 33, 9, 27, 10, 29, 47, 26, 13, 25, 28, 32, 49, 30, 45, 22, 11, 31, 48, 46, 7, 41, 42, 14, 3, 0, 8, 20, 21, 24, 4, 5, 44, 12, 6, 2, 23, 1, 43, 40],
        [29, 8, 9, 7, 49, 28, 27, 5, 6, 4, 48, 26, 3, 47, 24, 23, 25, 46, 2, 45, 44, 21, 22, 43, 42, 41, 20, 19, 40, 1, 0, 18, 17, 39, 38, 15, 16, 37, 35, 36, 14, 13, 12, 33, 31, 11, 34, 32, 30, 10],
        [2, 42, 5, 1, 24, 11, 9, 48, 6, 21, 23, 7, 0, 4, 40, 41, 43, 22, 8, 47, 49, 46, 44, 45, 25, 20, 28, 13, 29, 10, 26, 27, 3, 14, 30, 32, 12, 16, 39, 15, 17, 31, 34, 33, 18, 19, 35, 36, 37, 38],
        [31, 13, 41, 11, 12, 32, 34, 16, 10, 35, 30, 0, 4, 38, 33, 14, 17, 36, 40, 18, 1, 15, 37, 39, 24, 25, 47, 44, 2, 19, 46, 23, 20, 43, 42, 21, 22, 45, 3, 8, 48, 7, 5, 6, 49, 9, 26, 27, 28, 29],
        [42, 17, 18, 39, 38, 16, 37, 14, 15, 19, 36, 35, 9, 11, 31, 10, 32, 13, 33, 44, 26, 46, 49, 2, 45, 47, 7, 24, 28, 25, 27, 48, 43, 4, 5, 29, 30, 40, 12, 34, 21, 23, 22, 3, 6, 8, 0, 41, 1, 20],
        [29, 9, 49, 8, 47, 28, 27, 48, 7, 45, 5, 44, 26, 25, 43, 6, 42, 46, 3, 23, 40, 4, 21, 24, 41, 19, 39, 20, 0, 2, 38, 1, 36, 37, 17, 35, 18, 22, 32, 34, 11, 33, 16, 31, 12, 15, 30, 10, 13, 14],
        [22, 42, 7, 0, 1, 24, 6, 23, 27, 26, 10, 20, 2, 21, 4, 44, 43, 41, 8, 45, 25, 3, 29, 28, 46, 5, 40, 48, 47, 33, 32, 9, 30, 34, 31, 35, 13, 36, 14, 15, 49, 12, 11, 37, 39, 38, 19, 16, 17, 18],
        [49, 9, 48, 29, 8, 28, 27, 46, 7, 47, 6, 45, 3, 44, 43, 42, 23, 4, 5, 0, 22, 26, 41, 1, 25, 40, 39, 21, 20, 24, 18, 17, 19, 38, 36, 16, 15, 2, 35, 14, 13, 10, 37, 33, 11, 32, 12, 34, 30, 31],
        [19, 18, 17, 16, 14, 13, 39, 12, 36, 37, 49, 15, 8, 11, 35, 9, 34, 48, 5, 26, 38, 29, 46, 7, 33, 6, 47, 32, 31, 45, 2, 41, 27, 30, 28, 44, 4, 21, 24, 0, 20, 43, 40, 10, 3, 23, 25, 42, 22, 1],
        [10, 9, 8, 7, 6, 27, 28, 49, 48, 25, 26, 5, 29, 4, 3, 47, 24, 46, 1, 0, 2, 22, 23, 45, 21, 43, 41, 42, 44, 20, 19, 39, 17, 40, 18, 38, 15, 14, 13, 16, 31, 35, 37, 33, 11, 12, 34, 36, 32, 30],
        [39, 17, 16, 15, 38, 13, 14, 37, 36, 12, 19, 11, 35, 33, 32, 31, 10, 9, 28, 29, 18, 34, 49, 30, 21, 47, 27, 8, 46, 45, 48, 25, 6, 22, 7, 44, 40, 3, 2, 26, 41, 24, 23, 42, 1, 5, 43, 4, 20, 0],
        [29, 28, 9, 6, 27, 8, 7, 5, 24, 26, 25, 4, 48, 23, 46, 49, 22, 43, 47, 21, 1, 0, 3, 44, 42, 2, 45, 39, 40, 41, 19, 20, 38, 18, 37, 16, 17, 36, 15, 14, 33, 35, 34, 31, 12, 13, 11, 10, 32, 30],
        [39, 38, 37, 36, 35, 34, 33, 18, 17, 16, 12, 41, 6, 8, 7, 46, 29, 28, 15, 0, 1, 11, 10, 22, 9, 27, 4, 45, 49, 44, 47, 19, 32, 40, 20, 26, 23, 25, 3, 2, 21, 48, 24, 42, 31, 5, 43, 13, 30, 14],
        [13, 12, 15, 11, 34, 19, 42, 32, 30, 10, 45, 14, 33, 31, 36, 35, 16, 0, 17, 37, 39, 38, 1, 18, 40, 41, 3, 44, 20, 8, 24, 43, 2, 48, 21, 23, 6, 22, 5, 46, 7, 4, 47, 25, 49, 9, 26, 27, 29, 28],
        [39, 37, 38, 36, 35, 19, 34, 33, 18, 32, 17, 14, 15, 16, 13, 31, 12, 11, 9, 10, 30, 8, 7, 29, 6, 28, 27, 49, 48, 26, 45, 5, 47, 46, 25, 43, 23, 22, 24, 44, 42, 4, 21, 3, 2, 1, 20, 41, 0, 40],
        [11, 31, 15, 13, 10, 35, 16, 36, 12, 18, 33, 14, 17, 37, 32, 38, 34, 1, 30, 23, 20, 19, 0, 41, 39, 24, 4, 42, 25, 43, 21, 40, 2, 45, 46, 22, 44, 3, 47, 48, 5, 26, 27, 9, 28, 29, 6, 49, 7, 8],
        [0, 41, 5, 6, 21, 2, 20, 40, 42, 7, 29, 14, 9, 4, 1, 3, 23, 24, 43, 22, 10, 26, 8, 45, 27, 48, 12, 13, 28, 11, 25, 33, 44, 46, 47, 19, 30, 16, 15, 18, 31, 49, 36, 32, 34, 35, 17, 37, 38, 39],
        [13, 30, 31, 35, 10, 12, 38, 32, 40, 16, 11, 22, 39, 37, 36, 18, 21, 34, 23, 20, 41, 15, 33, 14, 19, 17, 2, 0, 1, 43, 25, 26, 24, 42, 29, 4, 6, 5, 7, 45, 8, 27, 28, 3, 44, 46, 47, 9, 48, 49],
        [19, 18, 39, 17, 14, 15, 36, 12, 35, 34, 9, 16, 31, 10, 32, 33, 38, 11, 13, 6, 5, 27, 28, 29, 37, 49, 0, 2, 26, 24, 25, 48, 4, 42, 1, 46, 41, 47, 40, 3, 23, 43, 22, 20, 30, 44, 7, 8, 45, 21],
        [30, 31, 12, 13, 10, 14, 32, 33, 35, 11, 34, 37, 36, 18, 19, 0, 16, 38, 15, 2, 1, 39, 17, 40, 41, 42, 20, 3, 21, 4, 43, 23, 22, 44, 6, 5, 49, 45, 46, 24, 25, 47, 9, 7, 48, 26, 27, 8, 29, 28],
        [0, 22, 12, 1, 3, 29, 46, 42, 23, 20, 40, 26, 6, 7, 2, 4, 28, 24, 41, 5, 25, 21, 27, 10, 32, 43, 11, 30, 9, 31, 44, 15, 8, 47, 17, 18, 48, 45, 33, 13, 49, 14, 35, 34, 16, 36, 38, 39, 37, 19],
        [9, 29, 8, 7, 28, 6, 49, 5, 48, 4, 3, 43, 1, 0, 47, 46, 2, 26, 27, 25, 44, 41, 45, 24, 23, 42, 22, 40, 21, 20, 39, 36, 38, 18, 19, 35, 37, 13, 15, 34, 33, 12, 16, 14, 17, 32, 30, 31, 11, 10],
        [0, 24, 26, 25, 2, 5, 29, 3, 44, 13, 1, 4, 41, 42, 27, 30, 31, 47, 22, 21, 46, 43, 40, 23, 20, 49, 28, 37, 7, 32, 6, 8, 48, 45, 33, 35, 17, 9, 38, 10, 39, 11, 12, 34, 36, 14, 15, 16, 18, 19],
        [10, 13, 30, 33, 34, 11, 36, 42, 3, 14, 40, 16, 15, 1, 17, 31, 45, 35, 41, 19, 18, 38, 37, 49, 0, 48, 39, 25, 23, 5, 27, 12, 47, 28, 7, 2, 26, 8, 29, 24, 9, 32, 43, 22, 4, 44, 6, 21, 20, 46],
        [1, 21, 43, 6, 9, 40, 0, 22, 44, 48, 4, 5, 46, 20, 26, 7, 3, 24, 2, 41, 49, 45, 23, 47, 42, 27, 8, 10, 25, 29, 30, 32, 14, 31, 33, 28, 11, 12, 15, 17, 39, 13, 35, 16, 34, 37, 36, 38, 19, 18],
        [10, 29, 28, 27, 26, 25, 49, 24, 48, 47, 23, 22, 21, 8, 7, 45, 6, 5, 44, 19, 42, 43, 4, 3, 15, 2, 18, 16, 9, 1, 17, 46, 20, 41, 39, 32, 0, 40, 35, 11, 34, 33, 14, 30, 31, 36, 38, 37, 13, 12],
        [0, 26, 4, 45, 42, 22, 20, 5, 1, 2, 41, 46, 44, 9, 6, 40, 21, 3, 10, 23, 19, 7, 49, 8, 11, 12, 47, 48, 14, 43, 25, 24, 15, 13, 16, 17, 33, 27, 28, 18, 30, 29, 31, 32, 35, 39, 34, 36, 37, 38],
        [10, 49, 48, 29, 28, 47, 27, 26, 25, 24, 9, 23, 22, 8, 20, 21, 19, 46, 7, 6, 5, 45, 18, 4, 3, 44, 2, 1, 0, 17, 16, 42, 43, 41, 36, 14, 15, 34, 37, 38, 39, 35, 40, 13, 31, 32, 33, 11, 12, 30]]

loc = pd.read_csv('50.1.CSV')
i = 0        # tsp遍历的节点
n = 30        # 抓捕成功的节点数
l = 0        # 测试集含小列表数
speed = 1.5   # 速度
add = 0      # 增加的时间

for l in range(30):
    j = 0
    for i in range(49):
        time_number = t2s(format(parse(loc.DepartureTime[tour[l][i+1]+50*l])-parse(loc.ArrivalTime[tour[l][i+1]+50*l])))  # 车辆停留时间
        lat1 = loc.lat_truth[tour[l][j]+50*l]
        lon1 = loc.lon_truth[tour[l][j]+50*l]
        lat2 = loc.lat_truth[tour[l][i+1]+50*l]
        lon2 = loc.lon_truth[tour[l][i+1]+50*l]

        duration = LLs2Dist(lat1, lon1, lat2, lon2)/speed+add
        if duration<time_number:
            n = n+1
        
        add = duration
        j = i + 1
rate = n/(50*30)
print(rate)

