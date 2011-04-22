#from scipy.integrate import odeint
from numpy import arange, pi, arctan, array, zeros
atan = arctan
from pylab import plot, show, legend

def euler(derivs, y_0, t_list):
    """
    It has the same interface as odeint, but uses a simple Euler method, so
    that it's robust.
    """
    R = zeros((len(t_list), len(y_0)))
    y = array(y_0)
    R[0, :] = y
    for i, t in enumerate(t_list[:-1]):
        delta_t = t_list[i+1]-t_list[i]
        yp = array(derivs(y, t))
        y += yp*delta_t
        R[i+1, :] = y
    return R


# everything in SI units:
nm = 1e-9
cm = 1e-2

q = 1.6022e-19
k_b = 1.3806503e-23
T = 298.
eps_0 = 8.854187817e-12
R = 0.

N_A = 0.5*1e18 * cm**(-3)
N_D = 2.0*1e18 * cm**(-3)
eps_r = 12.93
eps = eps_r*eps_0
mu_n = 1400 * cm**2
mu_p = 450 * cm**2
D_n = mu_n * k_b * T/q
D_p = mu_p * k_b * T/q
print "1D pn-junction simulation"
print
print "Constants (SI units)"
print "--------------------"
print "Basic:"
print "q:", q
print "k_b:", k_b
print "eps_0:", eps_0
print "T:", T
print
print "GaAs:"
print "eps_r:", eps_r
print "mu_p:", mu_p
print "mu_n:", mu_n
print "D_p:", D_p
print "D_n:", D_n
print "N_A:", N_A
print "N_D:", N_D

def C(t):
    return (N_D+N_A)*(atan((t-150*nm)/(10*nm))/pi +0.5) - N_A

def deriv(y, t):
    yp = [0, 0, 0, 0, 0, 0]
    yp[5] = -q/eps * (y[2] - y[0] + C(t))
    yp[0] = y[1]
    yp[1] = R/D_n+mu_n/D_n * (y[1]*y[5]+y[0]*yp[5])
    yp[2] = y[3]
    yp[3] = R/D_p-mu_p/D_p * (y[3]*y[5]+y[2]*yp[5])
    yp[4] = y[5]
    return yp

t = arange(0, 30*nm, 300*nm/200)
_eps = N_A/1.e3
y = euler(deriv, [0., 0., N_A, 0., 0., 0.], t)
n = y[:, 0]
n_p = y[:, 1]
p = y[:, 2]
p_p = y[:, 3]
phi = y[:, 4]
phi_p = y[:, 5]
plot(t, n, "r-", label="n")
plot(t, p, "b-", label="p")
#plot(t, p_p, "bx", label="p_p")
plot(t, phi, "k-", label="phi")
plot(t, C(t), "g+", label="C")
legend()
show()