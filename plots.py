# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 14:26:03 2021

@author: laurecazals
"""

import numpy as np
import matplotlib.pyplot as plt
from functions import update, modelisation
from matplotlib.collections import PathCollection
from matplotlib.legend_handler import HandlerPathCollection, HandlerLine2D
import configparser
from simulation import positive_prob, negative_prob



config = configparser.ConfigParser()
config.read('configuration.txt')

n = int(config.get('settings', 'n'))
l = int(config.get('settings', 'l'))
m = int(config.get('settings', 'm'))

numberCoord = int(config.get('settings', 'numberCoord')) # need to be increase fo n = 1

zmin = int(config.get('settings', 'zmin'))
zmax = int(config.get('settings', 'zmax'))


destination = config.get('paths',f'orbitals_{n}{l}{m}_pic')




#Arbitrary coordinates with the same size as our positive and negative probability, usefull to create our random coordinates following our probability
coord_pos = np.linspace(zmin,zmax,len(positive_prob))
coord_neg = np.linspace(zmin,zmax,len(negative_prob))


# Creation of our coordinates generated randomly following the probability (either "positive" or "negative one) trend + Separation of the coordinates for different probability range.
#"Positive" coordinates :
low_prob_positive = modelisation(positive_prob,coord_pos,n,l,m,numberCoord)[0]
middle_prob_positive = modelisation(positive_prob,coord_pos,n,l,m,numberCoord)[1]
high_prob_positive = modelisation(positive_prob,coord_pos,n,l,m,numberCoord)[2]

#"Negative" coordinates :
low_prob_negative = modelisation(negative_prob,coord_neg,n,l,m,numberCoord)[0]
middle_prob_negative = modelisation(negative_prob,coord_neg,n,l,m,numberCoord)[1]
high_prob_negative = modelisation(negative_prob,coord_neg,n,l,m,numberCoord)[2]




#Plotting
def graphPlot():

    
    #plotting
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    #Positive wavefunction data: 
    ax.scatter(low_prob_positive[0],low_prob_positive[1],low_prob_positive[2], alpha=0.05, s=2,color='lightsteelblue',label='Less than 50%')
    ax.scatter(middle_prob_positive[0],middle_prob_positive[1],middle_prob_positive[2], alpha=0.05, s=2,color='blue',label='Less than 75%')
    ax.scatter(high_prob_positive[0],high_prob_positive[1],high_prob_positive[2], alpha=0.05, s=2,color='red', label='More than 75%')

    #Negative wavefunction data: 
    ax.scatter(low_prob_negative[0],low_prob_negative[1],low_prob_negative[2], alpha=0.05, s=2,color='lightsteelblue')
    ax.scatter(middle_prob_negative[0],middle_prob_negative[1],middle_prob_negative[2], alpha=0.05, s=2,color='blue')
    ax.scatter(high_prob_negative[0],high_prob_negative[1],high_prob_negative[2], alpha=0.05, s=2,color='red')

    #Axis
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    
    #Title
    ax.set_title(f'Hydrogen Orbital (n = {n}, l = {l}, m = {m})')
    
    #Legend
    plt.legend(handler_map={PathCollection : HandlerPathCollection(update_func= update), plt.Line2D : HandlerLine2D(update_func = update)},markerscale = 4)
    
    #save
    plt.savefig(destination)

    


graphPlot()
