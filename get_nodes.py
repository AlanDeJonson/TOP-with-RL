
'''
date 2021/08/01
function: get usable nodes from 50.1.csv
author: He R.G.
'''


import pandas as pd
import numpy as np

event = pd.read_csv('50.1.csv')
nodes = pd.DataFrame(np.ones((30,100)))

for i in range(30):
    for j in range(50):
        nodes[2*j][i] = event.lat_truth[j+50*i]
        nodes[2*j+1][i] = event.lon_truth[j+50*i]

        
