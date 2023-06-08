#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 10:49:31 2023

@author: ruben
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
rP=pd.read_csv('/home/ruben/Documents/emptydirectory/python_codes/Simulation_times_CONE_full.csv')
rP2=pd.read_csv('/home/ruben/Documents/emptydirectory/python_codes/Simulation_times_THULE_full.csv')
estimated_time = rP['Estimated time for 50000 y']
estimated_time_thule = rP2['Estimated time for 50000 y']
n_nodes = rP['nodes']
n_nodes_thule = rP2['nodes']
fig= plt.figure()
ax=plt.gca()
plt.rc('font', size=10)
plt.xlabel('Number of nodes', fontsize=30)
plt.ylabel('Estimated time for 50000 y (s)', fontsize=30)
plt.title('Estimated Time vs. Number of nodes', fontsize=30)
ax.scatter(n_nodes, estimated_time, marker='o', s=100, label='Cone')
ax.scatter(n_nodes_thule, estimated_time_thule, marker='o', s=100, label='Thule')
ax.set_yscale("log")
ax.set_xscale("log")
plt.legend(fontsize=30)
plt.tick_params(axis='x', labelsize=30)
plt.tick_params(axis='y', labelsize=30)
plt.show()