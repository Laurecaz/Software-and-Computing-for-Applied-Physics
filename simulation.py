import numpy as np
import matplotlib.pyplot as plt
from functions import hydrogen_wf, separation_by_probability


#choice of orbital
#print('What orbitals do you want to plot ? ')
n = 2#input('n = ')
l = 0#input('l = ')
m = 0#input('m = ')

#construction of arbitrary coordinates grid
dz=0.01
zmin=-10
zmax=10
x = np.arange(zmin,zmax,dz)
y = np.arange(zmin,zmax,dz)
z = np.arange(zmin,zmax,dz)

#Calculation of the probability 
data = hydrogen_wf(n,l,m,x,y,z) 
data = (abs(data)**2)/sum(abs(data)**2)

#Getting electron coordinates based on the probability shape

#Getting electron coordinates based on the probability shape
x_coords = np.random.choice(x, size=100000, replace=True, p=data)
y_coords = np.random.choice(y, size=100000, replace=True, p=data)
z_coords = np.random.choice(z, size=100000, replace=True, p=data)

#re-injection of the coordinates in the probability
data = hydrogen_wf(n,l,m,x_coords,y_coords,z_coords)  #changer le nom
data = (abs(data)**2)/sum(abs(data)**2)

#boudanry definition
maximum = max(data)

quarter = 0.25*maximum
half = 0.5*maximum
three_quarter = 0.75*maximum

#separation of the data according to the probability of each coordinates
coord_quarter = separation_by_probability(0, quarter, x_coords, y_coords, z_coords, data)
coord_half = separation_by_probability(quarter, half, x_coords, y_coords, z_coords, data)
coord_three_quarter = separation_by_probability(half, three_quarter, x_coords, y_coords, z_coords, data)
coord_last_quarter = separation_by_probability(three_quarter, maximum, x_coords, y_coords, z_coords, data)


#plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(coord_last_quarter[0],coord_last_quarter[1],coord_last_quarter[2], alpha=0.05, s=2,color='b')
ax.scatter(coord_three_quarter[0],coord_three_quarter[1],coord_three_quarter[2], alpha=0.05, s=2,color='m')
ax.scatter(coord_half[0],coord_half[1],coord_half[2], alpha=0.05, s=2,color='g')
ax.scatter(coord_quarter[0],coord_quarter[1],coord_quarter[2], alpha=0.05, s=2,color='r')




