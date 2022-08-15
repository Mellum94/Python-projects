

#Exercise 3.22


from math import sqrt, e, pi

m = 0

s = 2

n = 11


def gaussian(m,s,n,x):
    return (1.0/(sqrt(2.0*pi)*2.0))*(e**((-1.0/2.0)*((x-m)/s)**2))


print "   x   Gaussian   "


for x in range(m-5*s, m+5*s, 1):
    print "   %g  %.10f  " %(x, gaussian(m,s,n,x))
    
#prints from 0 to 19 (20-1), with increment of 1

"""

termial>> python gaussian2.py
   x   Gaussian   
   0  0.0000007434  
   1  0.0000007434  
   2  0.0000669151  
   3  0.0000669151  
   4  0.0022159242  
   5  0.0022159242  
   6  0.0269954833  
   7  0.0269954833  
   8  0.1209853623  
   9  0.1209853623  
   10  0.1994711402  
   11  0.1994711402  
   12  0.1209853623  
   13  0.1209853623  
   14  0.0269954833  
   15  0.0269954833  
   16  0.0022159242  
   17  0.0022159242  
   18  0.0000669151  
   19  0.0000669151

"""
