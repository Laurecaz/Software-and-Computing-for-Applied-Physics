#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 15:24:26 2021
@author: laurecazals
"""

from functions import From_wf_to_probability, sign_separation, separation_by_probability, hydrogen_wf
import numpy as np
import random


def test_hydrogen_wf():
    # check that some specific case that we know
    assert hydrogen_wf(2,1,0,0,0,0) == (1e-12+1e-12j) 
    assert hydrogen_wf(2,1,1,0,0,0) == (1e-12+1e-12j)
    assert hydrogen_wf(3,1,0,0,0,0) == (1e-12+1e-12j)
    assert hydrogen_wf(3,2,1,0,0,0) == (1e-12+1e-12j)


def test_separation_by_probability():
    
    random.seed(0.5)
    random_prob = np.random.random(1000)
    
    coord = np.linspace(-10,10,len(random_prob))
    maximum = max(random_prob)
    
     # test that the output have the same lenght
    x, y, z = separation_by_probability(0.25*maximum,0.50*maximum,coord,coord,coord,random_prob)
    assert len(x) == len(y)
    assert len(y) == len(z)

    
def test_wf_to_probability():
    
    random.seed(23)
    random_values = From_wf_to_probability(np.random.random(1000)*1000-500)
    
    # sum of all the data equals to one to check that it returns a probability
    assert round(sum(random_values),10) == 1
    assert round(sum(From_wf_to_probability(np.random.random(1000))),10) == 1 #only positive values for the wavefunction
    assert round(sum(From_wf_to_probability(np.random.random(1000)*(-1))),10) == 1 #only positive values for the wavefunction
    
    # all the data are positive to check that it returns a probability
    for i in range(1000):
        assert From_wf_to_probability(random_values)[i] >= 0
 
    # special case of n = 1, l = 0 and m = 0 (no negative wave function but the sum of the probability cannot be 0)
    assert sum(From_wf_to_probability([])) == 1
    
    # input and output lists must be the same 
    assert len(random_values) == len(From_wf_to_probability(random_values))

 

def test_sign():
    # test for the 0
    assert sign_separation([-1,-2,45,5,0,-9.78,0.01]) == [[45,5,0,0.01],[-1,-2,-9.78]]
    
    # test is there is only positive or negative numbers
    assert sign_separation([1,2,3,4,5]) == [[1,2,3,4,5],[]]
    assert sign_separation([-1,-2,-3,-4,-5]) == [[],[-1,-2,-3,-4,-5]]

    # test if th einput is an empty lisy
    assert sign_separation([]) == [[], []]



if __name__ == "main":
    pass
