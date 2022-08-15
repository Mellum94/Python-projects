#Exercise 8.17: Vectorize a probability computation

import random
import numpy as np

for i in [1,2,3,6]:
	N = 10**i #N value to higher exponent for every round through loop
	r = np.random.uniform(0,1,size=N) #size = number of times

	M = np.sum(np.logical_and(r>=0.5, r<=0.6)) #sum of elements, compund boolean statement
	prob = float(M)/N #probabilty
	print prob
	
"""
terminal>> python compute_prob_vec.py 
0.2
0.11
0.108
0.099879
"""