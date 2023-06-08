#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 11:38:55 2023

@author: ruben
"""
##  HALBRANE ##
###COMPARAISON ENTRE LES DEUX CONFIGURATIONS COMPLETE ET QUART DU DOMAINE##
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
## ON PRENDS LE DATA QUI CORRESPOND A LE DOMAINE COMPLETE POUR CAPRONA###
res = np.array([1, 5, 10])
max_values_complete={}
for resolution in res:
    for profile in list(map(chr,range(ord('A'),ord('D')+1))):
        rP = pd.read_csv('/home/ruben/Research-project/Grounding_line_positions_thule_FULL/groundingLines'+str(resolution)+'kmfull_Halbrane'+profile+'.csv')
        #print('In the direction of the profile Halbrane', profile, ', the grounding line position for', resolution, 'km resolution is:', rP['distance'][np.argmax(rP['groundingline'])])
        max_value_complete=rP['distance'][np.argmax(rP['groundingline'])]
        max_values_complete[(profile, resolution)]=max_value_complete

mean_values_complete = {}
max_values_res_complete = {}
min_values_res_complete = {}

####ON CALCULE LA MOYENNE, LE MAX ET MIN DE LA POSITION DE LA GROUNDING LINE POUR CHAQUE RESOLUTION####

for resolution in res:
    max_values_res_complete[resolution] = max([max_values_complete[(profile, resolution)] for profile in list(map(chr,range(ord('A'),ord('D')+1)))])
    min_values_res_complete[resolution] = min([max_values_complete[(profile, resolution)] for profile in list(map(chr,range(ord('A'),ord('D')+1)))])
    mean_values_complete[resolution] = np.mean([max_values_complete[(profile, resolution)] for profile in list(map(chr,range(ord('A'),ord('D')+1)))])



##ON PRENDS LE DATA QUI CORRESPOND A LE QUART DU DOMAINE POUR CAPRONA#######
max_values_quarter={}
for resolution in res:
    rP4=pd.read_csv('/home/ruben/Documents/Grounding_line_positions_thule/groundingLines'+str(resolution)+'km_HalbraneB.csv')
    max_values_quarter[resolution]=rP4['distance'][np.argmax(rP4['groundingline'])]
## ON FAIT LA FIGURE DE CHAQUE RESOLUTION ET LA POSITION DE LA LIGNE D'ECHOUAGE POUR LE QUART DU DOMAINE ET 
## DU DOMAINE COMPLETE AVEC DES ERREURS 


markers = ['o', 's', 'D']
colors = ['red', 'green', 'blue']

for i, resolution in enumerate(res):
    plt.scatter(resolution*1000, mean_values_complete[resolution], color="k")
    plt.scatter(resolution*1000, max_values_res_complete[resolution], color=colors[i])
    plt.scatter(resolution*1000, min_values_res_complete[resolution], color=colors[i])
    
    if resolution in max_values_quarter:
        # Use dashed error bar lines for quarter domain
        plt.errorbar(resolution*1000, max_values_quarter[resolution], yerr=resolution*1000/2, fmt=markers[i], linestyle='dashed', color=colors[i])
    else:
        # Use solid lines for complete domain
        plt.errorbar(resolution*1000, mean_values_complete[resolution], yerr=resolution*1000/2, fmt=markers[i], linestyle='solid', color=colors[i])
        

# Set x-axis labels and title
plt.xticks(res*1000, res)
plt.xlabel('Resolution (km)')
plt.ylabel('Grounding Line Position (m)')
plt.title('Comparison of Grounding Line Positions')

# Add legend for error bar colors and marker styles
legend_labels = ['Mean', 'Max/Min']
errorbar_labels = ['Error Bars (Complete)', 'Error Bars (Quarter)']
handles = [plt.Line2D([0], [0], marker=marker, color='w', markerfacecolor='black', markersize=5) for marker in markers]
plt.legend(handles, errorbar_labels, title='Error Bars', loc='best')
plt.show()