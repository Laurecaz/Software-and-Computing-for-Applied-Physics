#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 12:33:42 2021

@author: laurecazals
"""
import scipy.special
from scipy.special import sph_harm
import numpy as np
import math



#FUNCTION FILE

#Generate the hydrogen wave function for a specific orbital and x, y and z coordinates (which can represent either a point or a 3D grid)
def hydrogen_wf(n,l,m,X,Y,Z):
    R = np.sqrt(X**2+Y**2+Z**2)
    Theta = np.arccos(Z/R)
    Phi = np.arctan2(Y,X)
    
    rho = 2.*R/n
    s_harm=sph_harm(m, l, Phi, Theta)
    l_poly = scipy.special.genlaguerre(n-l-1,2*l+1)(rho)
    
    prefactor = np.sqrt((2./n)**3*math.factorial(n-l-1)/(2.*n*math.factorial(n+l)))
    wf = prefactor*np.exp(-rho/2.)*rho**l*s_harm*l_poly
    wf = np.nan_to_num(wf,nan = 0.001)
    return wf # same size as a coordinate




#separation of the 3 direction coordinates for different range of probability
def separation_by_probability(prob_min,prob_max,x,y,z,prob): 
    x_reduc = []
    y_reduc = []
    z_reduc = []
    prob_min = min(prob_min,prob_max) #if by mistake prob_max is smaller than prob_min
    prob_max = max(prob_min,prob_max)
    for i in range(len(prob)):
        if prob_min < prob[i] < prob_max :
            x_reduc.append(x[i])
            y_reduc.append(y[i])
            z_reduc.append(z[i])
    return x_reduc, y_reduc, z_reduc

# From wavefunction (list) to probability (list)
def From_wf_to_probability(wave_function):
    probability = [abs(i)**2 for i in wave_function]
    sum_prob = sum(probability)
    probability = [i/sum_prob for i in  probability]
    return probability #same size as the wave_function in entry


#Separation between positive and negative data 
def sign_separation(data):
    positive = []
    negative = []
    for i in range(len(data)):
        if data[i] >= 0 :
            positive.append(data[i])
        else :
            negative.append(data[i])
    return [positive,negative]
    
    
#creation of our coordinates and separation of them for different probability range.
def modelisation(Probability,coordinates,n,l,m) : 
    if Probability == 'positive': #difference orientation in space for positive and negative wavefunction
        sign = +1
    else :
        sign = -1
    
    x_coords = np.random.choice(coordinates, size=1000000, replace=True, p=Probability)#creation of our random coordinates following the behaviour of the hydrogen probability
    y_coords = np.random.choice(coordinates, size=1000000, replace=True, p=Probability)
    z_coords = np.random.choice(coordinates, size=1000000, replace=True, p=Probability)

    #re-injection of the coordinates in the probability in order to separate them correctly
    wave_function = hydrogen_wf(n,l,m,x_coords,y_coords,z_coords)
    wave_function = [i.real for i in wave_function]
    Probability = From_wf_to_probability(wave_function)
    
    #boundary constant
    maximum = max(Probability)

    low_prob = 0.25*maximum
    middle_prob = 0.5*maximum
    high_prob = 0.9*maximum
    
    #separation of the data according to the probability of each coordinates (and sign according to the wavefunction)
    low_coord = separation_by_probability(low_prob,middle_prob, sign*x_coords, sign*y_coords, sign*z_coords, Probability)
    middle_coord = separation_by_probability(middle_prob,high_prob, sign*x_coords, sign*y_coords, sign*z_coords, Probability)
    high_coord = separation_by_probability(high_prob, maximum, sign*x_coords, sign*y_coords, sign*z_coords, Probability)

    return low_coord, middle_coord, high_coord
