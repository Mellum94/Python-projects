#Exercise 8.15: Compute probabilities of throwing two dice

import numpy as np

N = 100 #number of throws
probabilities = []
pairs = np.random.randint(1,7,(N,2))
sum1 = np.sum(pairs, axis=1)
print sum1

for k in range(2,13):
	m = np.count_nonzero(sum1==k)

print m


"""
terminal>>

"""