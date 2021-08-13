# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 14:26:03 2021
@author: laurecazals
"""

import numpy as np
import matplotlib.pyplot as plt
from functions import modelisation
from matplotlib.collections import PathCollection
from matplotlib.legend_handler import HandlerPathCollection, HandlerLine2D
import configparser
import random


config = configparser.ConfigParser()

#Choice of the specific configuration
chosen_text = input('Choose your plot configuration text : ')
chosen_text = str(chosen_text)
config.read(chosen_text)

n = int(config.get('settings', 'n'))
l = int(config.get('settings', 'l'))
m = int(config.get('settings', 'm'))

numberCoord = int(config.get('settings', 'numberCoord')) # need to be increase for n = 1

zmin = int(config.get('settings', 'zmin'))
zmax = int(config.get('settings', 'zmax'))

low = float(config.get('settings', 'low_prob'))
middle = float(config.get('settings', 'middle_prob'))
high = float(config.get('settings', 'high_prob'))

random.seed(config.get('settings','NumbSeed'))

#import the data created in the simulation file
source1 = config.get('paths','positive_prob')
source2 = config.get('paths','negative_prob')

destination = config.get('paths',f'orbitals_{n}{l}{m}_pic')



positive_prob = np.load(source1)
negative_prob = np.load(source2)

#Arbitrary coordinates with the same size as our positive and negative probability, usefull to create our random coordinates following our probability
coord_pos = np.linspace(zmin,zmax,len(positive_prob))
coord_neg = np.linspace(zmin,zmax,len(negative_prob))


# Creation of our coordinates generated randomly following the probability (either "positive" or "negative one) trend + Separation of the coordinates for different probability range.
#"Positive" coordinates :

low_prob_positive = modelisation(positive_prob,coord_pos,n,l,m,numberCoord,1,low,middle,high)[0]
middle_prob_positive = modelisation(positive_prob,coord_pos,n,l,m,numberCoord,1,low,middle,high)[1]
high_prob_positive = modelisation(positive_prob,coord_pos,n,l,m,numberCoord,1,low,middle,high)[2]

#"Negative" coordinates :
low_prob_negative = modelisation(negative_prob,coord_neg,n,l,m,numberCoord,-1,low,middle,high)[0]
middle_prob_negative = modelisation(negative_prob,coord_neg,n,l,m,numberCoord,-1,low,middle,high)[1]
high_prob_negative = modelisation(negative_prob,coord_neg,n,l,m,numberCoord,-1,low,middle,high)[2]


def update(handle, orig):
    """ This method is used to set the marker transparency. 
    Only solution find on internet to handle this issue.
    """
    handle.update_from(orig)
    handle.set_alpha(1)


#Plotting
def graphPlot():

    
    #plotting
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    #Positive wavefunction data: 
        
    ax.scatter(low_prob_positive[0],low_prob_positive[1],low_prob_positive[2], alpha=0.05, s=2,color='cornflowerblue',label=f'Between {low*100}% and {middle*100}%')
    ax.scatter(middle_prob_positive[0],middle_prob_positive[1],middle_prob_positive[2], alpha=0.05, s=2,color='blue',label=f'Between {middle*100}% and {high*100}%')
    ax.scatter(high_prob_positive[0],high_prob_positive[1],high_prob_positive[2], alpha=0.05, s=2,color='red', label=f'More than {high*100}%')

    #Negative wavefunction data:
    ax.scatter(low_prob_negative[0],low_prob_negative[1],low_prob_negative[2], alpha=0.05, s=2,color='cornflowerblue')
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
