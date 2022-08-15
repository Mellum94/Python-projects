#Exercise E.16: Simulate radioactive decay

from math import log, e
import numpy as np
import matplotlib.pyplot as plt

class Decay:
	def __init__(self, a):
		self.a = a
	def __call__(self, u, t):	
		return -a*u #right-side of diffential equation

a = log(2)/5600.0 #1/y
f = Decay(a) #creating instance
T = 20000 #t max
dt = 500 #difference in t[k] and t[k+1] value
n = T/dt #spacing
t = np.linspace(0, T, n+1) #array of t values from 0 to T (t max)
u = np.zeros(n+1)  #array of u values
u[0] = 1 #initial value

for i in range(n):
	u[i+1] = u[i] + dt*f(u[i], t[i])

final_u = u[-1] #last element added to u array
exact = e**(-a*T) #exact value

print final_u
print exact
print abs(exact-final_u) #difference between final_u and exact

#PLot
plt.plot(t,u)
plt.show()

"""
terminal>> python radioactive_decay.py 
0.0776577923652
0.0841187620395
0.00646096967434

"""

