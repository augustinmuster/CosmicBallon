#!/usr/bin/python


# """
# Bethe Bloch equation and calculation of energy loss along trajectory

# author: Bob Wimmer
# date: April 27, 2011
# email: wimmer@physik.uni-kiel.de

# """

from math import *

adia=False

#Define some natural constants

mp = 1.672621637e-27        #kg
me = 9.1093821499999992e-31 #kg
qe = 1.602176487e-19        #C
na = 6.02214179e23          #mol^-1
eps0 = 8.854187817e-12      #F/m
c = 299792458               #m/s


#and nnow some problem specific ones

E = 0.2e9*qe              #2Gev in J
m0   = 207*me                   #mass of projectile
Z1   = 1                    #nuclear charge of projectile


# Electron density  and mean exitation potential part
Z= 7.6                     #atomic number (effective) for water
A=28.97                        #mass number (in g/mol)
EB   = 10*Z*qe              #compute mean exitation potential

# constants for adiabatic athmosphere
# molar mass
M=0.029
# gaz constants
R=8.314
# sea level pressure
p0=101325
# sea level temperature
T0=288.15
# temperature lapse temperature
L=0.0065
# gravitational acceleration
g=9.81
# creation altitude
h0=15000


# function for adiabatic athmosphere
def rho(h):
    term1=(p0*M)/(R*T0)
    term2=1-(L*h)/T0
    term3=(g*M)/(R*L)-1
    return 1000*term1*term2**term3 #in g/m^3

# electron density function
def ne(h):
    if(adia):
        return (na*Z*rho(h))/A         #compute electron density of medium in m^-3
    else:
        return (na*Z*1.06e3)/A

def beta(v):
    return v/c

def gamma(v):               #Lorentz gamma
    return 1./sqrt(1-v*v/c/c)

def v_of_Ekin_m0(Ekin, m0): #invert kinetic energy, E_kin, for speed, v.
    b2 = 1.-1./(1.+Ekin/m0/c/c)**2
    return sqrt(b2)*c

def dEdx(Z1,Ekin,m0,EB,ne): #Bethe-Bloch equation
    v = v_of_Ekin_m0(Ekin, m0)
    b2 = beta(v)**2
    C = Z1**2*qe**4/4/pi/eps0**2/me
    ln_term = log(2.*me*v**2/EB)
    return C/v**2*ne*(ln_term  - log(1.-b2) - b2)

bbf = open('stopping_altitude_no_adia','w')
    #initialize position, energy loss, and dx
while E<100.e9*qe:
    x=0         #position in m
    dE = 0.     #energy loss
    dx = 1  #1m
    Ekin=E
    while Ekin > 0:
        dE = dEdx(Z1,Ekin,m0,EB,ne(h0-x))*dx     #units J/m*dx
        x = x+dx
        Ekin = Ekin - dE

    print("Energy: "+str(E)+", Stopping_altitude: "+str((x)))
    E=E+0.5e9*qe

bbf.close()
