
#Exercise 1.10: Evaluate the Gaussian Function

from math import e, sqrt, pi

x = 1.0
m = 0.0
s = 2.0

function = (1.0/(sqrt(2.0*pi)*2.0))*(e**((-1.0/2.0)*((x-m)/s)**2))

print "The bell-shaped Gaussian function is equal \
to %5f when x=1, m=0 and s=2." %function



print function

"""
terminal>> python gaussian1.py
The bell-shaped Gaussian function is equal to 0.176033 when
x=1, m=0 and s=2.

0.176032663382

"""

