#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 14:19:20 2023

@author: ruben
"""
from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import pandas as pd
import sys
file="/home/ruben/Documents/emptydirectory/CONE/OUTPUT_FILES_quarter/elem_10km/elem_10km_exp1_Ao9_C001_rhoi917_rhow1028-3_2980-2989.nc"
def groundingline(filename=file,sampling=10):
    nc=Dataset(filename, 'r')
    bed=nc.variables['bedrock_elem'][0,:]
    zb=nc.variables['zb_elem'][::sampling]
    mask=np.where(bed-zb==0,nc.variables['cell_area'][::sampling],0)
    t=nc.variables['time_instant'][::sampling]
    nc.close()
    t-=t[0]
    integral=np.sum(mask, axis=1)
    gl=np.sqrt(integral/np.pi)
    return(t,gl)

def multiplefilesgroundingline(path="/home/ruben/Documents/emptydirectory/CONE/OUTPUT_FILES_quarter/elem_10km/"):
    l=0
    for filename in Path(path).glob('elem_1km_exp1_Ao9_C001_rhoi917_rhow1028_quarter-3*09.nc'):
        l+=1
    gl=np.zeros(l)
    t=np.zeros(l)
    l=0
    for filename in Path(path).glob('elem_1km_exp1_Ao9_C001_rhoi917_rhow1028_quarter-3*09.nc'):
        print(filename)
        (myt,mygl)=groundingline(filename=filename, sampling=1)
        t[l]=int(str(filename).split("-")[-1].split(".")[0])
        gl[l]=mygl
        l+=1
    return(t,gl)

def groundedarea(filename=file, sampling=100):
    nc=Dataset(filename,'r')
    bed=nc.variables['bedrock_elem'][0,:]
    zb=nc.variables['zb_elem'][::sampling]
    mask=np.where(bed-zb==0,nc.variables['cell_area'][::sampling],0)
    t=nc.variables["time_instant"][::sampling]
    nc.close()
    t-=t[0]
    integral=np.sum(mask,axis=1)
    #gl=np.sqrt(integral/np.pi)
    return(t,integral)

def multipleFilesGroundingarea(path="/home/ruben/Documents/emptydirectory/CONE/OUTPUT_FILES_quarter/elem_10km"):
    l=0
    for filename in Path(path).glob('elem_500m_exp3_Ao9_C001_rhoi917_rhow1028-3_*.nc') :
        l+=1
    gl=np.zeros(l)
    t=np.zeros(l)
    l=0
    for filename in Path(path).glob('elem_500m_exp3_Ao9_C001_rhoi917_rhow1028-3_*.nc') :
        print(filename)
        (myt,mygl)=groundedarea(filename=filename,sampling=1)
        t[l]=int(str(filename).split("-")[-1].split(".")[0])
        gl[l]=mygl
        l+=1
    return(t,gl)
def GroundedVolume(filename=file,sampling=100,variable='h_elem') :
    nc=Dataset(filename,'r')
    bed=nc.variables['bedrock_elem'][0,:]
    zb=nc.variables['zb_elem'][::sampling]
    mask=np.where(bed-zb==0,nc.variables['cell_area'][::sampling]*nc.variables[variable][::sampling],0)
    t=nc.variables["time_instant"][::sampling]
    nc.close()
    t-=t[0]
    integral=np.sum(mask,axis=1)
    #gl=np.sqrt(integral/np.pi)
    return(t,integral)
def multipleFilesVol(path="home/ruben/Documents/emptydirectory/CONE/OUTPUT_FILES_quarter/elem_5km"):
    l=0
    for filename in Path(path).glob('elem*9.nc') :
        l+=1
    gl=np.zeros(l)
    t=np.zeros(l)
    l=0
    for filename in Path(path).glob('elem*9.nc') :
        print(filename)
        (myt,mygl)=GroundedVolume(filename=filename,sampling=1)
        t[l]=int(str(filename).split("-")[-1].split(".")[0])
        gl[l]=mygl
        l+=1
    return(t,gl)


def multipleFilesVolSerie(path="/home/ruben/Documents/emptydirectory/CONE/OUTPUT_FILES_quarter/elem_10km"):
    l=0
    for filename in Path(path).glob('elem*[0,2,4,6,8]0.nc') :
        l+=1
        #print(filename)
    gl=np.zeros(l)
    t=np.zeros(l)
    l=0
    for filename in Path(path).glob('elem*[0,2,4,6,8]0.nc') :
        print(filename)
        (myt,mygl)=GroundedVolume(filename=filename,sampling=1)
        t[l]=int(str(filename).split("_")[-1].split(".")[0])
        gl[l]=mygl
        l+=1
    return(t,gl)


def IceThickness(filename=file,sampling=100,variable='h_elem') :
    nc=Dataset(filename,'r')
    pvar=nc.variables['pvar'][::sampling]
    mask=np.where(pvar==0,nc.variables[variable][::sampling],0)
    t=nc.variables["time_instant"][::sampling]
    nc.close()
    t-=t[0]
    integral=np.sum(mask,axis=1)
    #gl=np.sqrt(integral/np.pi)
    return(t,integral)
def multipleFilesH(path="/home/ruben/Documents/emptydirectory/CONE/OUTPUT_FILES_quarter/elem_10km"):
    l=0
    for filename in Path(path).glob('elem_1km_exp1_Ao9_C001_rhoi917_rhow1028-2*09.nc') :
        l+=1
    gl=np.zeros(l)
    t=np.zeros(l)
    l=0
    for filename in Path(path).glob('elem_1km_exp1_Ao9_C001_rhoi917_rhow1028-2*09.nc') :
        print(filename)
        (myt,mygl)=IceThickness(filename=filename,sampling=1)
        t[l]=int(str(filename).split("-")[-1].split(".")[0])
        gl[l]=mygl
        l+=1
    return(t,gl)



###############################################################################################


