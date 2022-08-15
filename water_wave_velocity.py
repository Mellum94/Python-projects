#Exercise 5.31

import numpy as np
import matplotlib.pyplot as plt

s = 7.9*10**(-2) #N/m, air-water surface tension
g = 9.81 #m/s**2, acceleration of gravity
rho = 1000 #kg/m**3, density of water
h = 50 #m, water depth

x = np.linspace(1,2000,100)
#x = wavelength

#y = np.sqrt((g*x)/(2*np.pi)*(1 + s*(4*np.pi**2)/(rho*g*x**2))*(np.tanh)*((2*np.pi*h)/x))
#splitting function into variables:
a = (g*x)/(2*np.pi)
b = (1 + s*(4*np.pi**2)/(rho*g*x**2))
c = np.tanh((2*np.pi*h)/x)

y = np.sqrt(a*b*c)

plt.plot(x, y) #plotting function

plt.xlabel('x') #naming x-axis
plt.ylabel('c(x)') #naming y-axis
plt.legend(['y']) #function label
plt.title('water_wave_velocity') #graph title

plt.show() 

"""
Run with x = np.linspace(1,2000,100): (large wavelength)
terminal >>python water_wave_velocity.py

Run with x = np.linspace(0.001,0.01,100): (small wavelength)
terminal>>python water_wave_velocity.py

"""


