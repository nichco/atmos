from smt.surrogate_models import RMTB
import numpy as np
import matplotlib.pyplot as plt

def standard_atmosphere(z):

    # constants for standard atmosphere model
    g = 9.806 # m/(s^2)
    Ts = 288.16 # deg K @ sea level
    Ps = 1.01325E5 # Pascals at sea level
    rhoS = 1.225 # kg/m^3 at sea level
    R = 287 # J/(Kg-K) gas constant
    P11 = 2.2629E04
    P25 = 2.4879E03
    rho11 = 0.3639
    rho25 = 0.0400

    # standard atmosphere model
    if z <= 11000:
        a = -6.5E-3 # K/m
        temperature = Ts + a*z
        pressure = Ps*((temperature/Ts)**((-g)/(a*R)))
        density = rhoS*((temperature/Ts)**(-((g/(a*R)) + 1)))
    elif z > 11000 and z <= 25000:
        temperature = 216.6 # isothermal region
        pressure = P11*(np.exp(-(g/(R*temperature))*(z - 11000)))
        density = rho11*(np.exp(-(g/(R*216.66))*(z - 11000)))
    elif z > 25000: # and z <= 47000:
        a = 3E-3
        temperature = 216.66 + a*(z - 25000)
        pressure = P25*((temperature/216.66)**((-g)/(a*R)))
        density = rho25*((temperature/216.66)**(-((g/(a*R)) + 1)))

    return temperature, pressure, density


def training():

    # generate (x, y) training data pairs for the standard atmosphere model
    max = 47000
    step = 1000
    size = int(max/step)

    xt_temperature = np.zeros(size)
    xt_pressure = np.zeros(size)
    xt_density = np.zeros(size)

    yt_temperature = np.zeros(size)
    yt_pressure = np.zeros(size)
    yt_density = np.zeros(size)
    index = 0
    for z in range(0,max,step):
        xt_temperature[index] = 1*z
        xt_pressure[index] = 1*z
        xt_density[index] = 1*z

        t,p,r = standard_atmosphere(z)
        yt_temperature[index] = 1*t
        yt_pressure[index] = 1*p
        yt_density[index] = 1*r

        index += 1

    return xt_temperature, xt_pressure, xt_density, yt_temperature, yt_pressure, yt_density

def surrogate():

    return


xt_t,xt_p,xt_d,yt_t,yt_p,yt_d = training()

plt.plot(xt_t,yt_t)
plt.show()

plt.plot(xt_p,yt_p)
plt.show()

plt.plot(xt_d,yt_d)
plt.show()