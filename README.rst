1D Semiconductor Physics Equations
==================================

Drift-diffusion Model
---------------------

Equations are here (4):

http://certik.github.com/theoretical-physics/book/src/elmag/elmag.html#equations

This is called a drift-diffusion model and can model
any semiconductor. For example pn-junctions:

http://en.wikipedia.org/wiki/P-n_junction

transistors:

http://en.wikipedia.org/wiki/Transistor

or thin films of silicon, very simplified model is here:

http://certik.github.com/theoretical-physics/book/src/elmag/elmag.html#example-1

The last two equations (and read the assumptions above that had to be
made). The 3 nonlinear PDEs is a way more general and precise model,
that also gives the charges at the boundaries etc.

1D Case
-------

For the 1D pn-junction, the equations are here:

http://certik.github.com/theoretical-physics/book/src/elmag/elmag.html#example-3

it's a set of 6 nonlinear first-order ODEs. The boundary conditions
are not exactly clear to me yet, but here is what I should get:

http://www.nextnano.de/nextnano3/tutorial/1Dtutorial_pn_junction.htm

so I tried to solve it using the Euler method (for ODEs), see the
attached python script. But unfortunately, p(x) explodes, but it
should go to zero, as x->320nm. So either the equations are wrong, or
I am setting the model constants wrong.

The constants (in the code) are:

Constants (SI units)
--------------------

Basic::

    q: 1.6022e-19
    k_b: 1.3806503e-23
    eps_0: 8.854187817e-12
    T: 298.0

GaAs::

    eps_r: 12.93
    mu_p: 0.045
    mu_n: 0.14
    D_p: 0.00115556862583
    D_n: 0.00359510239146
    N_A: 5e+23
    N_D: 2e+24
