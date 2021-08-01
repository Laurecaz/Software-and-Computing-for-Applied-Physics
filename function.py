import math
import numpy as np
import scipy.special
from scipy.special import sph_harm


#hydrogen wave function
def hydrogen_wf(n,l,m,X,Y,Z):
    R = np.sqrt(X**2+Y**2+Z**2)
    Theta = np.arccos(Z/R)
    Phi = np.arctan2(Y,X)
    
    rho = 2.*R/n
    s_harm=sph_harm(m, l, Phi, Theta)
    l_poly = scipy.special.genlaguerre(n-l-1,2*l+1)(rho)
    
    prefactor = np.sqrt((2./n)**3*math.factorial(n-l-1)/(2.*n*math.factorial(n+l)))
    wf = prefactor*np.exp(-rho/2.)*rho**l*s_harm*l_poly
    wf = np.nan_to_num(wf)
    return wf

#separation of the data for different range of probability
def separation_by_probability(prob_min,prob_max,x,y,z,prob): 
    x_reduc = []
    y_reduc = []
    z_reduc = []
    for i in range(len(prob)):
        if prob_min < prob[i] < prob_max :
            x_reduc.append(x[i])
            y_reduc.append(y[i])
            z_reduc.append(z[i])
    return x_reduc, y_reduc, z_reduc
