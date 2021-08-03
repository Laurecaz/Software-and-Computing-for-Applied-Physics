# Atomic Orbitals of Hydrogen
The hydrogen wave function can be written as,

![equation1](https://latex.codecogs.com/gif.latex?\phi_{n,l,m}(r)&space;=&space;Y_{l,m}(\theta,\phi)e^{-r/na_{1}}(\frac{r}{a_{1}})^{l}L_{n-l-1}(r))
- ![equation1](https://latex.codecogs.com/gif.latex?Y_{l,m}(\theta,\phi)), spherical harmonic,
- ![equation1](https://latex.codecogs.com/gif.latex?L_{n-l-1}(r)), a Laguerre polynomial.

The aim of the program is to simulate the possible electrons' position of the hydrogen atom in different states. The main steps of the program for each states are :
- An 3D arbitrary grid is created.
- The hydrogen wavefunction is calculated for each portion of space. The positive part is separated from the negative one, and their probability are determined separetly.
- The electrons' coordinates are generated randomly following these two different probability law. The one following the negative law will have its electrons "return" in the space i.e. every coordinates will change sign, in order to reproduce the "negativity" of there wavefunction.
- Then, the electron's coordinates correponding to a probability of presence less than 25% are deleted, and the rest are plot with a color code revealing the most likely electron's positions.

Thanks to this approach, we can observe that the electrons will form atomic orbitals that we can compare to the theory.
This project is divided into four blocks :
- In the file [functions](https://github.com/Laurecaz/Software-and-Computing-for-Applied-Physics/blob/210eff060e604a76519aac8830f16862f5375748/functions.py)
