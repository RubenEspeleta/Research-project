#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 14:46:29 2023

@author: ruben
"""

from netCDF4 import Dataset
filename="10km_exp1_Ao9_C001_rhoi917_rhow1028-3_2500.nc"
path="/home/ruben/Documents/emptydirectory/CONE/OUTPUT_FILES_quarter/10km"
import numpy as np
import os
from pathlib import Path
import matplotlib.pyplot as plt
def distance(x=1,y=1) :
    '''This function computes the distance to the origin
     takes as argument x and y arrays'''
    return(np.sqrt(x**2+y**2))

def funcion(myfile=filename) :
    ''' Computes the grounding line position along the Profile A. TO BE IMPROVED.
         usage:
             '''
    nc=Dataset(filename,'r')
    bedrock=nc.variables['bedrock'][:]
    ground=nc.variables['groundedmask'][:]
    mymask=-bedrock*ground
    x=np.squeeze(nc.variables['x'][0,:])
    y=np.squeeze(nc.variables['y'][0,:])
    x0=np.argmin(np.abs(x))
    y0=np.argmin(np.abs(y))
    profileA=np.where(x==np.argmin(np.abs(x)),mymask,np.nan)
    profileA=np.where(y>=0,profileA,np.nan)
    Amax=np.nanargmax(profileA)
    Amax=distance(x[Amax],y[Amax])
    profileE=np.where(y<=0,profileA,np.nan)
    Emax=np.nanargmax(profileE)
    Emax=distance(x[Emax],y[Emax])

    return(filename,Amax,Emax)


filenames = []
Amax_list = []
Emax_list = []
time = np.arange(51)
for filename in Path(path).glob('10km_exp1*-*.nc') :
     #print(filename)
     (a,b,c)=funcion(myfile=filename)
     print(a,b,c)
     filenames.append(a)
     Amax_list.append(b)

plt.figure()
plt.plot(time, Amax_list, 'o', label='Amax')
plt.xlabel('Timestep')
plt.ylabel('Distance')
plt.legend()
plt.title('Amax and Emax for each filename')
plt.show()
