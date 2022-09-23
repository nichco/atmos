from smt.surrogate_models import RMTB
import numpy as np
import matplotlib.pyplot as plt

def standard_atmosphere(z):

    g = 9.806 # m/(s^2)
    Ts = 288.16 # deg K @ sea level
    Ps = 1.01325E5 # Pascals at sea level
    rhoS = 1.225 # kg/m^3 at sea level
    R = 287 # J/(Kg-K) gas constant
    P11 = 2.2629E04
    P25 = 2.4879E03
    rho11 = 0.3639
    rho25 = 0.0400

    if z <= 11000:
        a = -6.5E-3 # K/m
        temperature = Ts + a*z
        pressure = Ps*((temperature/Ts)**((-g)/(a*R)))
        density = rhoS*((temperature/Ts)**(-((g/(a*R)) + 1)))
    elif z > 11000 and z <= 25000:
        temperature = 216.6 # isothermal region
        pressure = P11*(np.exp(-(g/(R*temperature))*(z - 11000)))
        density = rho11*(np.exp(-(g/(R*216.66))*(z - 11000)))
    elif z > 25000 and z <= 47000:
        a = 3E-3
        temperature = 216.66 + a*(z - 25000)
        pressure = P25*((temperature/216.66)**((-g)/(a*R)))
        density = rho25*((temperature/216.66)**(-((g/(a*R)) + 1)))

    return temperature, pressure, density


def training():
    # temperature

    # density
    return

def surrogate():

    return


# temperature model test
max = 40000
t = np.zeros(max)
p = np.zeros(max)
r = np.zeros(max)
for i in range(0,max):
    t[i],p[i],r[i] = standard_atmosphere(i)

plt.plot(t)
plt.show()
plt.plot(p)
plt.show()
plt.plot(r)
plt.show()