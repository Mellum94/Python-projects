#Exercise 8.6: Estimate the probability in a dice game
import random
import sys

M = 0 									#starting with zero outcomes of desired result
N = int(sys.argv[1]) 					#number of experiments
n = int(sys.argv[2]) 					#number of dice

for i in range(N): 						#for loop for running experiment several times
	for i in range(n):  				#for loop for throwing several dice at once
		outcome = random.randint(1, 6)  #throwing die, possible outcomes in interval [1,6] 
		if outcome == 6:
			M += 1 						#counts success
			break 						#1 success per throw, because they're asking 
										#for at least one six on every throw

N = float(N)

#Comparing Monte Carlo simulation to exact solution:
print "Probability: %f Difference: %f" % (float(M/N), abs(float(M/N)-(11/36.0)))
#Difference being difference between exact solution and Mone Carlo simulation

"""
terminal >> python one6_ndice.py 1000000 2
Probability: 0.305338 Difference: 0.000218 
"""