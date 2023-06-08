#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 14:33:57 2023

@author: ruben
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
res = np.array([1, 2, 5, 10])
max_values={}
for resolution in res:
    for profile in list(map(chr,range(ord('A'),ord('D')+1))):
        rP = pd.read_csv('/home/ruben/Research-project/Grounding_line_positions_thule_FULL/groundingLines'+str(resolution)+'kmfull_Caprona'+profile+'.csv')
        print('In the direction of the profile Caprona', profile, ', the grounding line position for', resolution, 'km resolution is:', rP['distance'][np.argmax(rP['groundingline'])])
        max_value=rP['distance'][np.argmax(rP['groundingline'])]
        max_values[(profile, resolution)]=max_value

mean_values = {}
max_values_res = {}
min_values_res = {}

for resolution in res:
    max_values_res[resolution] = max([max_values[(profile, resolution)] for profile in list(map(chr,range(ord('A'),ord('D')+1)))])
    min_values_res[resolution] = min([max_values[(profile, resolution)] for profile in list(map(chr,range(ord('A'),ord('D')+1)))])
    mean_values[resolution] = np.mean([max_values[(profile, resolution)] for profile in list(map(chr,range(ord('A'),ord('D')+1)))])
    
for resolution in res:
    print("resolution: ", resolution, "km")
    print("mean value: ", mean_values[resolution])
    print("max value: ", max_values_res[resolution])
    print("min value: ", min_values_res[resolution])
    
y_error=res*1000/2
res=-res
plt.scatter(res*1000, list(mean_values.values()), color="k")
plt.scatter(res*1000, list(max_values_res.values()), color="red")
plt.scatter(res*1000, list(min_values_res.values()), color="blue")
plt.xticks(res*1000, -res)
plt.errorbar(res*1000, list(mean_values.values()), yerr=y_error, fmt="o")
plt.show()