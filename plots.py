# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 14:26:03 2021

@author: laurecazals
"""

import matplotlib.pyplot as plt
from simulation import low_prob_negative, low_prob_positive, middle_prob_negative, middle_prob_positive, high_prob_negative, high_prob_positive, n, l, m
from functions import update
from matplotlib.collections import PathCollection
from matplotlib.legend_handler import HandlerPathCollection, HandlerLine2D


#plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

#Positive : 
ax.scatter(low_prob_positive[0],low_prob_positive[1],low_prob_positive[2], alpha=0.05, s=2,color='lightsteelblue',label='Less than 50%')
ax.scatter(middle_prob_positive[0],middle_prob_positive[1],middle_prob_positive[2], alpha=0.05, s=2,color='blue',label='Less than 75%')
ax.scatter(high_prob_positive[0],high_prob_positive[1],high_prob_positive[2], alpha=0.05, s=2,color='red', label='More than 75%')

#Negative : 
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

plt.show()

