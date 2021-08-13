#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 10:52:14 2021
@author: laurecazals
"""

import numpy as np
from functions import hydrogen_wf, From_wf_to_probability, sign_separation
import configparser




config = configparser.ConfigParser()

#Choice of the specific configuration
chosen_text = input('Choose your simulation configuration text : ')
chosen_text = str(chosen_text)
config.read(chosen_text)

n = int(config.get('settings', 'n'))
l = int(config.get('settings', 'l'))
m = int(config.get('settings', 'm'))

numberCoord = int(config.get('settings', 'numberCoord')) # need to be increase fo n = 1


#Path where the final data generate by this simulation while be saved
destination1 = config.get('paths','positive_prob')
destination2 = config.get('paths','negative_prob')


#Construction of arbitrary 3D coordinates grid
dz = float(config.get('settings', 'dz'))  #if reduce, the time calculation can quickly increase
zmin = int(config.get('settings', 'zmin'))
zmax = int(config.get('settings', 'zmax'))

coordinate = np.arange(zmin,zmax,dz)




#Calculation of the wavefunction for each poitn in the 3D grid
wave_function = []
for i in range(len(coordinate)) : #3 DIMENSION GRID
    for i in range(len(coordinate)) :
        for i in range(len(coordinate)) :
            wave_function.append(hydrogen_wf(n,l,m,coordinate[i],coordinate[i],coordinate[i])) #Value of the wavefunction in each point of the grid

wave_function= [i.real for i in wave_function] # real part of the wavefunction only

#Separation of positive and negative probability
wave_function = sign_separation(wave_function)

#Calculation of the probability 
positive_prob = From_wf_to_probability(wave_function[0])
negative_prob = From_wf_to_probability(wave_function[1])
 



#Save the data created by this simulation file
np.save(destination1,positive_prob)
np.save(destination2,negative_prob)

