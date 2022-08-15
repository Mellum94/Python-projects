#Exercise 8.2: Compute a Probability

import random

for n in [1,2,3,6]:
	M = 0 #starting with zero outcomes in desired interval [0.5,0.6]
	N = 10**n #N value to higher exponent for every round through loop
	for i in range(N):
		outcome = random.random() #generates a random number in the half open interval [0,1)
		if 0.5 <= outcome <= 0.6: #if test for whether outcome is in desired interval [0.5,0.6]
			M += 1 # adds to M every time outcome is in interval [0.5,0.6]
	print float(M)/N #print probability for every N

"""
terminal>> python compute_prob.py 
0.1
0.09
0.106
0.100015

"""