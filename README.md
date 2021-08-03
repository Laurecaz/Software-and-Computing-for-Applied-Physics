# Atomic Orbitals of Hydrogen
The hydrogen wave function can be written as,

![equation1](https://latex.codecogs.com/gif.latex?\phi_{n,l,m}(r)&space;=&space;Y_{l,m}(\theta,\phi)e^{-r/na_{1}}(\frac{r}{a_{1}})^{l}L_{n-l-1}(r))
- ![equation2](https://latex.codecogs.com/gif.latex?Y_{l,m}(\theta,\phi)), spherical harmonic,
- ![equation3](https://latex.codecogs.com/gif.latex?L_{n-l-1}(r)), a Laguerre polynomial.

The aim of the program is to simulate the possible electrons' position of the hydrogen atom in different states. The main steps of the program for each states are :
- An 3D arbitrary grid is created.
- The hydrogen wavefunction is calculated for each portion of space. The positive part is separated from the negative one, and their probability are determined separetly.
- The electrons' coordinates are generated randomly following these two different probability law. The one following the negative law will have its electrons "return" in the space i.e. every coordinates will change sign, in order to reproduce the "negativity" of there wavefunction.
- Then, the electron's coordinates correponding to a probability of presence less than 25% are deleted, and the rest are plot with a color code revealing the most likely electron's positions.

Thanks to this approach, we can observe that the electrons will form atomic orbitals that we can compare to the theory.
This project is divided into four blocks :
- In the file [functions](https://github.com/Laurecaz/Software-and-Computing-for-Applied-Physics/blob/210eff060e604a76519aac8830f16862f5375748/functions.py) all our functions are stocked. They are tools used for the construction of our data.
- In the file [TEST](https://github.com/Laurecaz/Software-and-Computing-for-Applied-Physics/blob/210eff060e604a76519aac8830f16862f5375748/TEST.py), the functions are tested, to ensure as much as possible that the program is working properly.
- In the file [configuration](https://github.com/Laurecaz/Software-and-Computing-for-Applied-Physics/blob/102bd30c6aaa54a23c2e705d57a4043867b9b39f/configuration.txt) there are the definitions of the parameters used in the simulation file : the specific orbital (n,l,m) and the number of coordinates we want to simulate. The latter must be chosen with attention : the computing time increase with it. As default, it is settle as ![equation3](https://latex.codecogs.com/gif.latex?10^{6}), nottice that is must be much larger for the level n = 1.
- In the file [simulation](https://github.com/Laurecaz/Software-and-Computing-for-Applied-Physics/blob/210eff060e604a76519aac8830f16862f5375748/simulation.py) there is the main part of the code. It reproduces all the steps descibe earlier relying on the functions designed on purpose.
- In the file [plots](https://github.com/Laurecaz/Software-and-Computing-for-Applied-Physics/blob/210eff060e604a76519aac8830f16862f5375748/plots.py) the data produced by the simulation file are plotted in 3 dimension using matplotlib.pyplot.
