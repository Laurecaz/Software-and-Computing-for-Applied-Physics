import numpy as np
import matplotlib.pyplot as plt
from functions import hydrogen_wf, separation_by_probability




#choice of orbital
#print('What orbitals do you want to plot ? ')
n = 7#input('n = ')
l = 1#input('l = ')
m = 0#input('m = ')

#construction of arbitrary coordinates grid
dz=0.5
zmin=-10
zmax=10
x = np.arange(zmin,zmax,dz)
y = np.arange(zmin,zmax,dz)
z = np.arange(zmin,zmax,dz)


#Calculation of the probability

data = []
for i in range(len(x)) :
    for i in range(len(y)) :
        for i in range(len(z)) :
            data.append(hydrogen_wf(n,l,m,x[i],y[i],z[i]))

#data = [abs(i)**2 for i in data]
#sum_data = sum(data)
#data = [i/sum_data for i in  data]

data = [i.real for i in data]
positive = []
negative = []

for i in range(len(data)):
    if data[i] >= 0 :
        positive.append(data[i])
    else :
        negative.append(data[i])
        

positive = [abs(i)**2 for i in positive]
sum_pos = sum(positive)
positive = [i/sum_pos for i in  positive]

negative = [abs(i)**2 for i in negative]
sum_neg = sum(negative)
negative = [i/sum_neg for i in  negative]



x_pos = np.linspace(zmin,zmax,len(positive))
y_pos = np.linspace(zmin,zmax,len(positive))
z_pos = np.linspace(zmin,zmax,len(positive))

x_neg = np.linspace(zmin,zmax,len(negative))
y_neg = np.linspace(zmin,zmax,len(negative))
z_neg = np.linspace(zmin,zmax,len(negative))




#NEGATIVE

x_coords = np.random.choice(x_neg, size=1000000, replace=True, p=negative)
y_coords = np.random.choice(y_neg, size=1000000, replace=True, p=negative)
z_coords = np.random.choice(z_neg, size=1000000, replace=True, p=negative)

#re-injection of the coordinates in the probability
data = hydrogen_wf(n,l,m,x_coords,y_coords,z_coords)  #changer le nom



#boudanry definition
maximum = max(data)

quarter = 0.25*maximum
half = 0.5*maximum
three_quarter = 0.9*maximum

#signe and symmetries
sign_x = -1
sign_y = -1
sign_z = -1

#separation of the data according to the probability of each coordinates
coord_quarter = separation_by_probability(0, quarter, sign_x*x_coords, sign_y*y_coords, sign_z*z_coords, data)#
coord_half = separation_by_probability(quarter, half, sign_x*x_coords, sign_y*y_coords, sign_z*z_coords, data)
coord_three_quarter = separation_by_probability(half, three_quarter, sign_x*x_coords, sign_y*y_coords, sign_z*z_coords, data)
coord_last_quarter = separation_by_probability(three_quarter, maximum, sign_x*x_coords, sign_y*y_coords, sign_z*z_coords, data)


#plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(coord_last_quarter[0],coord_last_quarter[1],coord_last_quarter[2], alpha=0.05, s=2,color='r')
ax.scatter(coord_three_quarter[0],coord_three_quarter[1],coord_three_quarter[2], alpha=0.05, s=2,color='r')
ax.scatter(coord_half[0],coord_half[1],coord_half[2], alpha=0.05, s=2,color='r')
#ax.scatter(coord_quarter[0],coord_quarter[1],coord_quarter[2], alpha=0.05, s=2,color='r')


#POSITVE


x_coords = np.random.choice(x_pos, size=1000000, replace=True, p=positive)
y_coords = np.random.choice(y_pos, size=1000000, replace=True, p=positive)
z_coords = np.random.choice(z_pos, size=1000000, replace=True, p=positive)


#re-injection of the coordinates in the probability
data = hydrogen_wf(n,l,m,x_coords,y_coords,z_coords)  #changer le nom



#boudanry definition
maximum = max(data)
print(maximum)

quarter = 0.25*maximum
half = 0.5*maximum
three_quarter = 0.9*maximum


#separation of the data according to the probability of each coordinates
coord_quarter = separation_by_probability(0, quarter, x_coords, y_coords, z_coords, data)#
coord_half = separation_by_probability(quarter, half, x_coords, y_coords, z_coords, data)
coord_three_quarter = separation_by_probability(half, three_quarter, x_coords, y_coords, z_coords, data)
coord_last_quarter = separation_by_probability(three_quarter, maximum, x_coords, y_coords, z_coords, data)


#plotting
#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
ax.scatter(coord_last_quarter[0],coord_last_quarter[1],coord_last_quarter[2], alpha=0.05, s=2,color='b')
ax.scatter(coord_three_quarter[0],coord_three_quarter[1],coord_three_quarter[2], alpha=0.05, s=2,color='b')
ax.scatter(coord_half[0],coord_half[1],coord_half[2], alpha=0.05, s=2,color='b')
#ax.scatter(coord_quarter[0],coord_quarter[1],coord_quarter[2], alpha=0.05, s=2,color='b')

plt.xlabel('x')
plt.ylabel('y')



