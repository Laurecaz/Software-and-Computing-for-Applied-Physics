# Atomic Orbitals of Hydrogen
The hydrogen wave function can be written as,

![equation1](https://latex.codecogs.com/gif.latex?\phi_{n,l,m}(r)&space;=&space;Y_{l,m}(\theta,\phi)e^{-r/na_{1}}(\frac{r}{a_{1}})^{l}L_{n-l-1}(r))
- ***Y<sub><l,m***, spherical harmonic,
- ***L<sub>n-l-1 ***, a Laguerre polynomial.

The aim of the program is to simulate the electrons' position of the hydrogen atom in different states. To do so, for each states, the wavefunction is calculated. The positive part is separated from the negative one, and their probability are determined separelty. The electrons' coordinates are generated randomly following these two differents probability law. The one following the negative law will have its electrons "return" in the space i.e. every coordinates will change sign, in order to reproduce the negativity of there wavefunction. Then, the electron's coordinates correponding to a probability of presence less than 25% are deleted, and the rest are plot with a color code revealing the most likely electron's positions. Thanks to this approach, we can observe that all the electrons will form atomic orbitals that we can compare to the theory.
