#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 11:08:25 2023

@author: ruben
"""
##THIS CODE WORKS TO COMPUTE THE MAXIMUM, MINIMUM AND MEAN VALUES OF THE POSITION OF THE
## GROUNDING LINE PER EACH RESOLUTION#####

##READING THE FILE AND COMPUTING THE VALUE OF THE GROUNDING LINE PER EACH PROFILE FOR EACH RESOLUTION

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
res = np.array([1, 2, 5, 10])
max_values={}
for resolution in res:
    for profile in list(map(chr,range(ord('A'),ord('C')+1))):
        rP2 = pd.read_csv('/home/ruben/Documents/Grounding_line_positions_cone/groundingLines'+str(resolution)+'km_profile'+profile+'.csv')
        print('In the direction of the profile', profile, ', the grounding line position for', resolution, 'km resolution is:', rP2['distance'][np.argmax(rP2['groundingline'])])
        max_value=rP2['distance'][np.argmax(rP2['groundingline'])]
        max_values[(profile, resolution)]=max_value
        
        
## Calculating mean, max, and min
mean_values = {}
max_values_res = {}
min_values_res = {}

for resolution in res:
    max_values_res[resolution] = max([max_values[(profile, resolution)] for profile in list(map(chr,range(ord('A'),ord('C')+1)))])
    min_values_res[resolution] = min([max_values[(profile, resolution)] for profile in list(map(chr,range(ord('A'),ord('C')+1)))])
    mean_values[resolution] = np.mean([max_values[(profile, resolution)] for profile in list(map(chr,range(ord('A'),ord('C')+1)))])

##Print the results

for resolution in res:
    print("resolution: ", resolution, "km")
    print("mean value: ", mean_values[resolution])
    print("max value: ", max_values_res[resolution])
    print("min value: ", min_values_res[resolution])

##PLOT OF THE MEAN, MAXIMUM AND MINIMUM VALUE FOR EACH RESOLUTION##
    
#plt.plot(res, list(mean_values.values()), 'o-', label='Mean')
#plt.plot(res, list(max_values_res.values()), 'o-', label='Max')
#plt.plot(res, list(min_values_res.values()), 'o-', label='Min')
#plt.xlabel('Resolution (km)')
#plt.ylabel('Grounding line position (m)')
#plt.legend()
#plt.show()

y_error=res*1000/2
res=-res
plt.scatter(res*1000, list(mean_values.values()), color="k")
plt.scatter(res*1000, list(max_values_res.values()), color="red")
plt.scatter(res*1000, list(min_values_res.values()), color="blue")
plt.xticks(res*1000, -res)
plt.errorbar(res*1000, list(mean_values.values()), yerr=y_error, fmt="o")
plt.show()
