#!/usr/bin/python


# """
# Bethe Bloch equation and calculation of energy loss along trajectory

# author: Bob Wimmer
# date: April 27, 2011
# email: wimmer@physik.uni-kiel.de

# """

from math import *

#Define some natural constants

mp = 1.672621637e-27        #kg
me = 9.1093821499999992e-31 #kg
qe = 1.602176487e-19        #C
na = 6.02214179e23          #mol^-1
eps0 = 8.854187817e-12      #F/m
c = 299792458               #m/s


#and nnow some problem specific ones

Ekin = 6.e9*qe              #2Gev in J
m0   = 207*me                   #mass of projectile
Z1   = 1                    #nuclear charge of projectile


# Electron density  and mean exitation potential part
rho= 1.060e3                  #density in g/m^3
Z= 7.6                     #atomic number (effective) for water
A=28.97                        #mass number (in g/mol)
ne   = (na*Z*rho)/A         #compute electron density of medium in m^-3
EB   = 10*Z*qe              #compute mean exitation potential


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


#Energy loss in first layer
print str(dEdx(1,Ekin,m0,EB,ne)/(qe*1.e9)) + ' in MeV/mm'

#initialize position, energy loss, and dx
x=0         #position in m
dE = 0.     #energy loss
dx = 1.e-1  #1cm
bbf = open('bb_in_air.csv','w')
# while Ekin > 0:
while x<15000:
    string = str(x) + ', ' + str(Ekin/(qe*1e6)) + ', ' + str(dE/(qe*1.e9)/dx) + '\n'
    #print x, Ekin/(qe*1e6), dE/(qe*1.e9)/dx
    print string
    bbf.write(string)
    dE = dEdx(Z1,Ekin,m0,EB,ne)*dx     #units J/m*dx
    x = x+dx
    Ekin = Ekin - dE

bbf.close()
