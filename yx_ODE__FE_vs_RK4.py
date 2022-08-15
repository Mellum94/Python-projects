#Exercise E.23: Compare ODE methods

from ODESolver import RungeKutta4, ForwardEuler
from math import sqrt
import matplotlib.pyplot as plt
import numpy as np 

eps = 0.001 # epsilon value
y0 = 1 + np.sqrt(eps) # initial value

g = lambda x: 1 + np.sqrt(x + eps) # exact function
f = lambda y,x: (1.0)/(2*(y-1)) # approximate function

r = [4**x for x in range(1,6)] # to reduce step size repeatedly

for k in r: # for loop to reduce step size repeatedly
	t = np.linspace(0,4,k) # k being step number of the most recently computed solution
	# array of time values, form 0 to 4, with spacing k

	# Runge Kutta MEthod
	rk = RungeKutta4(f) # creating instance (RungeKutta4 from ODESolver)
	rk.set_initial_condition(y0) # set_initial_condition from ODESolver
	uRK4, tRK4 = rk.solve(t) #two values as output

	# Forward Euler MEthod
	fe = ForwardEuler(f) # creating instance (ForwardEuler from ODESolver)
	fe.set_initial_condition(y0) 
	uFE, tFE = fe.solve(t)
	
	#PLot
	plt.subplot(121) #for plot in same figure
	plt.plot(tRK4, uRK4) #RungeKutta
	plt.subplot(122) #for plot in same figure
	plt.plot(tFE, uFE) #ForwardEuler

t = np.linspace(0,4,100) # for plotting exact solution

#Plot
plt.subplot(121) #plot in same figure and plot in same plot as RungeKutta
plt.axis([0,4,0,25]) #range and domain of plot
plt.plot(t, g(t)) # Exact solution
plt.subplot(122) #plot in same figure and plot in same plot as ForwardEuler
plt.axis([0,4,0,25]) #range and domain of plot
plt.plot(t, g(t)) #Exact solution

plt.show()

"""
terminal >> python yx_ODE__FE_vs_RK4.py 


"""