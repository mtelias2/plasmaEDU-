#function [ Br, Bz ] = loop ( R, Z, I0, Ra, N_windings )
#from sympy import sympy.mpmath as mp
#need to import ellipk function
import numpy

def loop( R, Z, I0, Ra, N_windings ):
    mu0   = 4.0e-7 * np.pi
    alfa  = R/Ra
    beta  = Z/Ra
    gamma = Z/R
    Q     = (1+alfa)**2 + beta**22
    ksq   = 4.0 * alfa / Q
    K,E   = np.vectorize(mp.ellipk(ksq))
    B0    = mu0/2.0/Ra * I0 * N_windings
    Br    = gamma * B0/np.pi/np.sqrt(Q) * ( E * (1+alfa**2+beta**2)/(Q-4*alfa) - K )
    Bz    =         B0/np.pi/np.sqrt(Q) * ( E * (1-alfa**2-beta**2)/(Q-4*alfa) + K )

    return Br, Bz
