#Exercise 2.11: Compute a mathematical sum
# Identifying the error in the code given in the assigment. The correct code is given below. 

print "First version:"

s = 0.0           #Error 1) s, k, and M must be decimal numbers to avoid integer devision.
k = 1.0
M = 100.0

eps = 1e-10

while k < M+eps:      #Error 3) did not include 1/100 in the sum
    print k
    s += (1/k)     
    k+=1           #Error 2) k cannot be a constant
    print s
  
"""
terminal>> python sum_while.py 
1.0
1.0
2.0
1.5
3.0
1.83333333333
4.0
2.08333333333
5.0

...

99.0
5.17737751764
100.0
5.18737751764

"""
print
    
print "Second version:"

s = 0.0           #Error 1) s, k, and M must be decimal numbers to avoid integer devision.
k = 1.0
M = 100.0

list_k = [ ]
list_s = [ ]

eps = 1e-10

while k < M+eps:      #Error 3) k has to be les than or equal to M to include 1/100 in the sum
    list_k.append(k)
    s += (1/k)     
    k+=1           #Error 2) k cannot be a constant
    list_s.append(s)

print "When k = %.2f" % list_k[-1]
print "the sum = %.4f" % list_s[-1]


#s = s+1/k, increment is 1/k
#The sum should be equal to 5.187377517639621 (from calculator)


"""

terminal>> python sum_while.py 
When k = 100.00
the sum = 5.1874

"""
