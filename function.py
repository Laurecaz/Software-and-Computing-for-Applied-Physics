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

# From wavefunction (list) to probabaility (list)
def From_wf_to_probability(wave_function):
    wave_function = [abs(i)**2 for i in wave_function]
    sum_wf = sum(wave_function)
    wave_function = [i/sum_wf for i in  wave_function]
    return wave_function


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
    
    
#creation of our coordinates and separation of them for different probability range 
def modelisation(Probability,coordinates,n,l,m,sign) : 
    x_coords = np.random.choice(coordinates, size=1000000, replace=True, p=Probability)
    y_coords = np.random.choice(coordinates, size=1000000, replace=True, p=Probability)
    z_coords = np.random.choice(coordinates, size=1000000, replace=True, p=Probability)

    #re-injection of the coordinates in the probability
    wave_function = hydrogen_wf(n,l,m,x_coords,y_coords,z_coords)
    wave_function= [i.real for i in wave_function]
    Probability = From_wf_to_probability(wave_function)
    
    #boundary constant
    maximum = max(Probability)

    low_prob = 0.25*maximum
    middle_prob = 0.5*maximum
    high_prob = 0.9*maximum
    
    #separation of the data according to the probability of each coordinates and sign according to the wavefunction
    low = separation_by_probability(low_prob,middle_prob, sign*x_coords, sign*y_coords, sign*z_coords, Probability)
    middle = separation_by_probability(middle_prob,high_prob, sign*x_coords, sign*y_coords, sign*z_coords, Probability)
    high = separation_by_probability(high_prob, maximum, sign*x_coords, sign*y_coords, sign*z_coords, Probability)

    return low, middle, high
