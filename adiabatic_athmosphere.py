import matplotlib.pyplot as plt
import numpy as np



#------------- constants-------------------
# -----------------------------------------

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

# --------------function-------------------
# -----------------------------------------

def rho(h):
    term1=(p0*M)/(R*T0)
    term2=1-(L*h)/T0
    term3=(g*M)/(R*L)-1
    return term1*term2**term3



alt=np.linspace(1,20000,10)
dens=rho(alt)
print(alt)
print(dens)
plt.plot(alt,dens)

plt.show()
