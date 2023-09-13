#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 00:08:05 2023

@author: ruben
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
res = np.array([1, 5, 10])
max_values_complete={}
for resolution in res:
    for profile in list(map(chr,range(ord('A'),ord('D')+1))):
        rP = pd.read_csv('/home/ruben/Research-project/Grounding_line_positions_thule_FULL/groundingLines'+str(resolution)+'kmfull_Halbrane'+profile+'.csv')
        #print('In the direction of the profile Caprona', profile, ', the grounding line position for', resolution, 'km resolution is:', rP['distance'][np.argmax(rP['groundingline'])])
        max_value_complete=rP['distance'][np.argmax(rP['groundingline'])]
        max_values_complete[(profile, resolution)]=max_value_complete

mean_values_complete = {}
max_values_res_complete = {}
min_values_res_complete = {}

for resolution in res:
    max_values_res_complete[resolution] = max([max_values_complete[(profile, resolution)] for profile in list(map(chr,range(ord('A'),ord('D')+1)))])
    min_values_res_complete[resolution] = min([max_values_complete[(profile, resolution)] for profile in list(map(chr,range(ord('A'),ord('D')+1)))])
    mean_values_complete[resolution] = np.mean([max_values_complete[(profile, resolution)] for profile in list(map(chr,range(ord('A'),ord('D')+1)))])

#####################################################
max_values_quarter={}
for resolution in res:
    rP4=pd.read_csv('/home/ruben/Documents/Grounding_line_positions_thule/groundingLines'+str(resolution)+'km_HalbraneB.csv')
    max_values_quarter[resolution]=rP4['distance'][np.argmax(rP4['groundingline'])]

####################################################
y_error=res*1000/2
res=-res
plt.rc('font', size=30)
plt.scatter(res*1000, list(max_values_quarter.values()), color='black', label='Quarter domain', s=80 )
plt.scatter(res*1000, list(max_values_res_complete.values()), color='red', label='Max. value domain complete', s=80)
plt.scatter(res*1000, list(mean_values_complete.values()), color='blue', label='Mean value domain complete', s=80)
plt.scatter(res*1000, list(min_values_res_complete.values()), color='green', label='Min. value domain complete', s=80)
plt.xticks(res*1000, -res)
plt.errorbar(res*1000, list(mean_values_complete.values()), yerr=y_error, fmt='o')
plt.errorbar(res*1000, list(max_values_quarter.values()), yerr=y_error, fmt='o')
plt.ylabel('Grounging line position (m)')
plt.xlabel('Resolution (km)')
plt.legend()
plt.show()