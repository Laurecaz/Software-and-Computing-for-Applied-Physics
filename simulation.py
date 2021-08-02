import numpy as np
import matplotlib.pyplot as plt
from functions import hydrogen_wf, From_wf_to_probability, sign_separation, modelisation




#Choice of orbital
n = 4
l = 2
m = 0

#Construction of arbitrary 3D coordinates grid
dz=0.5
zmin=-10
zmax=10
coordinate = np.arange(zmin,zmax,dz)

#Calculation of the wavefunction
wave_function = []
for i in range(len(coordinate)) : #3 DIMENSION GRID
    for i in range(len(coordinate)) :
        for i in range(len(coordinate)) :
            wave_function.append(hydrogen_wf(n,l,m,coordinate[i],coordinate[i],coordinate[i])) #Value of the wavefunction in each point of the grid

wave_function= [i.real for i in wave_function]

#Separation of positive and negative probability
wave_function = sign_separation(wave_function)

#Definition of the probability
positive = From_wf_to_probability(wave_function[0])
negative = From_wf_to_probability(wave_function[1])

#Avoid a bug due to the fact that the wavefunction have only one sign i.e. n = 1, l = 0, m = 0
if positive == []:
    positive  = [1]
if negative == []:
    negative  = [1]

coord_pos = np.linspace(zmin,zmax,len(positive))
coord_neg = np.linspace(zmin,zmax,len(negative))



#Positive :
low_prob_positive = modelisation(positive,coord_pos,n,l,m,+1)[0]
middle_prob_positive = modelisation(positive,coord_pos,n,l,m,+1)[1]
high_prob_positive = modelisation(positive,coord_pos,n,l,m,+1)[2]

#Negative :
low_prob_negative = modelisation(negative,coord_neg,n,l,m,-1)[0]
middle_prob_negative = modelisation(negative,coord_neg,n,l,m,-1)[1]
high_prob_negative = modelisation(negative,coord_neg,n,l,m,-1)[2]




