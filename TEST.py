import pytest
from functions import maximum_3array
import numpy as np


#Test of maximum_3array
def test_max3array() :
    #Does it work at it should be :
    assert maximum_3array([6,0,1],[1,2,4],[1,6,3]) == 6
    #Does it work with different array lenghts :
    assert maximum_3array([1,6],[1],[1,6,3]) == 6
