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
import configparser




config = configparser.ConfigParser()
config.read('configuration.txt')

low = float(config.get('settings', 'low_prob'))
middle = float(config.get('settings', 'middle_prob'))
high = float(config.get('settings', 'high_prob'))

#FUNCTION FILE

#Generate the hydrogen wave function for a specific orbital and x, y and z coordinates (which can represent either a point or a 3D grid)
def hydrogen_wf(n,l,m,X,Y,Z):
    """This method calculates the wavefunction for a specific orbital i.e. n,l and m, at points X, Y and Z (which can represent either a point or a 3D grid).
    Parameters
        n : principal quantum number.
        l : azimuthal quantum number.
        m : magnetic quantum number.
        X, Y, Z : float or array of coordinates. 
    
    Returns:
        The wavefunction of the specific orbitals for each coordinate.
        
    Raise:
        ValueError if n is less than 1, if l is negative or more than n-1 and if the absolute value of m is more than l ."""
    
    R = np.sqrt(X**2+Y**2+Z**2)
    Theta = np.arccos(Z/R)
    Phi = np.arctan2(Y,X)
    
    rho = 2.*R/n
    s_harm=sph_harm(m, l, Phi, Theta)
    l_poly = scipy.special.genlaguerre(n-l-1,2*l+1)(rho)
    
    prefactor = np.sqrt((2./n)**3*math.factorial(n-l-1)/(2.*n*math.factorial(n+l)))
    wf = prefactor*np.exp(-rho/2.)*rho**l*s_harm*l_poly
    wf = np.nan_to_num(wf,nan = 1e-12)
    return wf # same size as a coordinate




def separation_by_probability(prob_min,prob_max,x,y,z,prob): 
    """This method separates the coordinates according to the range of probability they belong to.
       
    Parameters
        prob_min and prob_max : the boundaries which select the probability range
        x, y and z : the coordinates we want to separate
        prob : array which describe the probability law 
    
    Returns:
        The coordinates x, y and z which correspond to the probability range selected.
    
    Raise:
        ValueError if x, y, z and prob are not iterable."""
    
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


def From_wf_to_probability(wave_function):
    """This method generates the probability corresponding to a given wavefunction.
       
    Parameters
        wave_function : the wave_function 
    
    Returns:
        The corresponding probability 
        
    Raise:
        ValueError if wave_function is not iterable."""
    
    probability = [abs(i)**2 for i in wave_function]
    sum_prob = sum(probability)
    probability = [i/sum_prob for i in  probability]
    return probability #same size as the wave_function in entry


 
def sign_separation(data):
    """This method separate the positive values and the negative one from an initial iterable object.
       
    Parameters
        data : array or list of one dimension composed by numbers.
    
    Returns:
        A 2D list composed separetly by the positive and negative values.
        
    Raise:
        ValueError if data is not iterable and not composed by numbers"""
    
    positive = []
    negative = []
    for i in range(len(data)):
        if data[i] >= 0 :
            positive.append(data[i])
        else :
            negative.append(data[i])
    return [positive,negative]
    
    

def modelisation(Probability,coordinates,n,l,m,numberCoord,sign) : 
    """This method creates the coordinates following the Probability law and separate them for different probability range.
       
    Parameters
        Probability : list with coordinates that represent the probability law.
        coordinates : list with the same lenght as Probability.
        n, l and m : quantum numbers.
        numberCoord : size of the coordinates we create.
        
    Returns:
        3 list in 3D which are the coordinates for different probability range 
        
    Raise:
        ValueError if coordinates and Probability do not have the same size, if numberCoord is negative"""

    #creation of our random coordinates following the behaviour of the hydrogen probability
    x_coords = np.random.choice(coordinates, size=numberCoord, replace=True, p=Probability)# size is increased when n = 1, otherwise no need and the time of caculation increases
    y_coords = np.random.choice(coordinates, size=numberCoord, replace=True, p=Probability)
    z_coords = np.random.choice(coordinates, size=numberCoord, replace=True, p=Probability)

    #re-injection of the coordinates in the probability in order to separate them correctly
    wave_function = hydrogen_wf(n,l,m,x_coords,y_coords,z_coords)
    wave_function = [i.real for i in wave_function]
    Probability = From_wf_to_probability(wave_function)
    
    #boundary constant
    maximum = max(Probability)
    
   
    low_prob = low*maximum
    middle_prob = middle*maximum
    high_prob = high*maximum
    
    #separation of the data according to the probability of each coordinates (and sign according to the wavefunction)
    low_coord = separation_by_probability(low_prob,middle_prob, sign*x_coords, sign*y_coords, sign*z_coords, Probability)
    middle_coord = separation_by_probability(middle_prob,high_prob, sign*x_coords, sign*y_coords, sign*z_coords, Probability)
    high_coord = separation_by_probability(high_prob, maximum, sign*x_coords, sign*y_coords, sign*z_coords, Probability)

    return low_coord, middle_coord, high_coord #contained the three direction coordinates in each 
    

#Function used to set the marker transparency
def update(handle, orig):
    handle.update_from(orig)
    handle.set_alpha(1)
    
