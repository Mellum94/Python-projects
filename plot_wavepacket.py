
#Exercise 5.28

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return (np.e**(-(x-3*t)**2))*np.sin(3*np.pi*(x - t))

t = 0
x = np.linspace(-4.0, 4.0, 10000)
#generating 10 000 coordinates in interval [-4,4]
y = f(x)


plt.plot(x, y) #plotting function

plt.xlabel('x')
plt.ylabel('y')
#labeling x and y axis
plt.legend('f(x,t)')
#labeling function
plt.title('plot_wavepacket')
#labeling graph
plt.show()

"""
terminal>> python plot_wavepacket.py 

"""
