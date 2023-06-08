#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 17:10:56 2023

@author: ruben
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
res = np.array([1, 2, 5, 10])
max_values_complete={}
for resolution in res:
    for profile in list(map(chr,range(ord('A'),ord('H')+1))):
        rP = pd.read_csv('/home/ruben/Research-project/Grounding_line_positions_cone_full/groundingLines'+str(resolution)+'kmfull_'+profile+'.csv')
        #print('In the direction of the profile Caprona', profile, ', the grounding line position for', resolution, 'km resolution is:', rP['distance'][np.argmax(rP['groundingline'])])
        max_value_complete=rP['distance'][np.argmax(rP['groundingline'])]
        max_values_complete[(profile, resolution)]=max_value_complete
        
mean_values_complete = {}
max_values_res_complete = {}
min_values_res_complete = {}

for resolution in res:
    max_values_res_complete[resolution] = max([max_values_complete[(profile, resolution)] for profile in list(map(chr,range(ord('A'),ord('H')+1)))])
    min_values_res_complete[resolution] = min([max_values_complete[(profile, resolution)] for profile in list(map(chr,range(ord('A'),ord('H')+1)))])
    mean_values_complete[resolution] = np.mean([max_values_complete[(profile, resolution)] for profile in list(map(chr,range(ord('A'),ord('H')+1)))])

max_values_quarter={}
for resolution in res:
    for profile in list(map(chr,range(ord('A'),ord('C')+1))):
        rP4 = pd.read_csv('/home/ruben/Documents/Grounding_line_positions_cone/groundingLines'+str(resolution)+'km_profile'+profile+'.csv')
        max_value_q=rP4['distance'][np.argmax(rP4['groundingline'])]
        max_values_quarter[(profile, resolution)]=max_value_q

mean_quarter={}
max_quarter={}
min_quarter={}
 
for resolution in res:
    max_quarter[resolution] = max([max_values_quarter[(profile, resolution)] for profile in list(map(chr,range(ord('A'),ord('C')+1)))])
    mean_quarter[resolution] = np.mean([max_values_quarter[(profile, resolution)] for profile in list(map(chr,range(ord('A'),ord('C')+1)))])
    min_quarter[resolution] = min([max_values_quarter[(profile, resolution)] for profile in list(map(chr,range(ord('A'),ord('C')+1)))])


y_error=res*1000/2
res=-res
plt.rc('font', size=30)
plt.scatter(res*1000, list(mean_values_complete.values()), color='k', label='mean value domain complete', s=80)
plt.scatter(res*1000, list(min_values_res_complete.values()), color='red', label='min value domain complete', s=80)
plt.scatter(res*1000, list(max_values_res_complete.values()), color='blue', label='max value domain complete', s=80)
plt.scatter(res*1000, list(mean_quarter.values()), color='green', label='mean value quarter', s=80)
plt.scatter(res*1000, list(max_quarter.values()), color='brown', label='max value quarter', s=80)
plt.scatter(res*1000, list(min_quarter.values()), color='purple', label='min value quarter', s=80)
plt.xticks(res*1000, -res)
plt.errorbar(res*1000, list(mean_values_complete.values()), yerr=y_error, fmt='o')
plt.errorbar(res*1000, list(mean_quarter.values()), yerr=y_error, fmt='o')
plt.ylabel('Grounging line position (m)')
plt.xlabel('Resolution (km)')
plt.legend()
plt.show()