#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 22 14:24:05 2023

@author: ruben
"""

### python nuevoElementos.py /bettik/garcicru/ElmerConfigs/07Feb2023-CalvingMIP/CONE/OUTPUT_FILES_quarter/ elem_250m_exp1_Ao9_C001_rhoi917_rhow1028-7
import numpy as np
import matplotlib.pyplot as plt
import sys
l = int(sys.argv[2])
base=(sys.argv[1])
ini=int(sys.argv[3])
cone250={}
fig = plt.figure()
ax = plt.gca()

for i in range (ini,l) :
    print(i)
    cone250[i] = np.genfromtxt(base+'250m-'+str(i)+'.txt', delimiter=' ')

for i in range (ini+1,l) :
    cone250[i][0]+=np.max(cone250[i-1][0])
for i in range (ini,l) :
    #plt.yscale("log")
    ax.set_yscale("log")
    ax.scatter(cone250[i][0],cone250[i][1],color='r')
#plt.show()
