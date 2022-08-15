#Exerise E.30: Implement a 2nd-order Runge-Kutta; function


import numpy as np
import matplotlib.pyplot as plt

def RungeKutta(f, U0, T, n):
	t = np.zeros(n+1) #t and k as arrays
	u = np.zeros(n+1)  # u[k] is the solution at time t[k]
	u[0] = U0 #initial u value set as first element in u array
	t[0] = 0 #initial t value set as first element in t array
	dt = T/float(n) #difference in t[k] and t[k+1] value
	for k in range(n): #generates u and t coordinates using Runge Kutta approximation
		t[k+1] = t[k] + dt
		k1 = dt * f(u[k], t[k])
		k2 = dt * f(u[k] + 0.5*k1, t[k] + 0.5*dt)
		u[k+1] = u[k] + dt*f(u[k], t[k])
	return u, t

def f(x, t):
	return x

def expo(t): #exact solution
	return np.exp(t)

U0 = 1 #initial value
T = 2 #t max
n = 50 #spacing

a, t = RungeKutta(f, U0, T, n) #u and t coordinates in variables a and t for plot
b = expo(t) # exact function coordinate in variable b for plot
plt.plot(t, b) #plotting exact
plt.plot(t, a) #plotting approximate
plt.show()

"""
terminal >>

"""
