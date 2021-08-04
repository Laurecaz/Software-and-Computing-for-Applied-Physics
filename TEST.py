#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 15:24:26 2021

@author: laurecazals
"""

from functions import From_wf_to_probability, sign_separation, separation_by_probability, hydrogen_wf
import numpy as np
import random
import math
from simulation import positive_prob


def test_hydrogen_wf():
    # check that some specific case that we know
    assert hydrogen_wf(2,1,0,0,0,0) == (1e-12+1e-12j) 
    assert hydrogen_wf(2,1,1,0,0,0) == (1e-12+1e-12j)
    assert hydrogen_wf(3,1,0,0,0,0) == (1e-12+1e-12j)
    assert hydrogen_wf(3,2,1,0,0,0) == (1e-12+1e-12j)


def test_separation_by_probability():
    # test that the output have the same lenght
    coord = np.linspace(-10,10,len(positive_prob))
    maximum = max(positive_prob)
    x, y, z = separation_by_probability(0.25*maximum,0.50*maximum,coord,coord,coord,positive_prob)
    assert len(x) == len(y)
    assert len(y) == len(z)
    
    
def test_wf_to_probability():
    # sum of all the data equals to one to check that it returns a probability
    assert round(sum(From_wf_to_probability(np.random.random(1000))),10) == 1
    # all the data are positive to check that it returns  a probability
    for i in range(1000):
        assert From_wf_to_probability(np.random.random(1000))[i] >= 0
        
        
def test_sign():
    # test for the 0
    assert sign_separation([-1,-2,45,5,0,-9.78,0.01]) == [[45,5,0,0.01],[-1,-2,-9.78]]
    

if __name__ == "main":
    pass 


