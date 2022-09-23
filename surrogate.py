from smt.surrogate_models import RMTB
import numpy as np
import matplotlib.pyplot as plt

def standard_atmosphere(z):

    Ts = 288.16 # deg K @ sea level

    if z <= 11000:
        a = -6.5E-3 # K/m
        temperature = Ts + a*z
    elif z > 11000 and z <= 25000:
        temperature = 216.6 # isothermal region
    elif z > 25000 and z <= 47000:
        a = 3E-3
        temperature = 216.66 + a*(z - 25000)

    return temperature


def training():
    # temperature

    # density
    return

def surrogate():

    return


# temperature model test
max = 40000
temp = np.zeros(max)
for i in range(1,max):
    temp[i] = standard_atmosphere(i)

plt.plot(temp)