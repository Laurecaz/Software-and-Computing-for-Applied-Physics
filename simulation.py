#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 10:52:14 2021

@author: laurecazals
"""

import numpy as np
import matplotlib.pyplot as plt
from functions import hydrogen_wf, From_wf_to_probability, sign_separation, modelisation
import configparser


#Choice of orbital
config = configparser.ConfigParser()
config.read('configuration.txt')

n = int(config.get('settings', 'n'))
l = int(config.get('settings', 'l'))
m = int(config.get('settings', 'm'))

numberCoord = int(config.get('settings', 'numberCoord'))


#Construction of arbitrary 3D coordinates grid
dz=0.5 #if reduce, the time calculation can quickly increase
zmin=-10
zmax=10
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

#Avoid a bug due to the fact that the wavefunction have only one sign i.e. n = 1, l = 0, m = 0
if positive_prob == []:
    positive  = [1]
if negative_prob == []:
    negative_prob  = [1]

#Arbitrary coordinates with the same size as our positive and negative probability
#Usefull to create our random coordinates following our probability
coord_pos = np.linspace(zmin,zmax,len(positive_prob))
coord_neg = np.linspace(zmin,zmax,len(negative_prob))


# Creation of our coordinates generated randomly following the probability (either "positive" or "negative one) trend.
#Separation of the coordinates for different probability range.
#"Positive" coordinates :
low_prob_positive = modelisation(positive_prob,coord_pos,n,l,m,numberCoord)[0]
middle_prob_positive = modelisation(positive_prob,coord_pos,n,l,m,numberCoord)[1]
high_prob_positive = modelisation(positive_prob,coord_pos,n,l,m,numberCoord)[2]

#"Negative" coordinates :
low_prob_negative = modelisation(negative_prob,coord_neg,n,l,m,numberCoord)[0]
middle_prob_negative = modelisation(negative_prob,coord_neg,n,l,m,numberCoord)[1]
high_prob_negative = modelisation(negative_prob,coord_neg,n,l,m,numberCoord)[2]



