
#Exercise 5.41

import numpy as np
import matplotlib.pyplot as plt

T = 2*np.pi
i = 1
t = np.linspace(0,T,100) #generates 100 coordinates in [0,T]

def S(t,n,T): #approximate function by sum of sines
	S1 = 0 #starting value for S1, for loop
	for i in range(1, n+1): #values of i from 1 to n, including n 
		#for loop for arithmetic sequence
		S1 = S1 + (4/np.pi)*(1/((2*i)-1))*np.sin((2*(2*i - 1)*np.pi*t)/T)
		#S1 redefined every time the program runs through the loop	
	return S1

def C(t,T): #function we want to approximate
	f = t
	for i in range(0,len(f)): 
	#runs i from 0 to number of elements in list f, remember f = t
		if f[i] < (T/2): #tests every element in list f
			f[i] = 1
		else:
			f[i] = -1
	return f
	
plt.plot(S(t,1,T))
plt.plot(S(t,3,T))
plt.plot(S(t,20,T))
plt.plot(S(t,200,T))
plt.plot(C(t,T))
#plotting functions in same plot

plt.xlabel('t')
plt.ylabel('S')
#labeling x and y axis
plt.title('sinesum1_plot')

plt.show()

"""
terminal>> python sinesum1_plot.py 

"""

