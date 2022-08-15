
#Exercise 7.5

import math
import cmath
import numpy as np

class Quadratic(object):

	def __init__(self, a, b, c):
		self.a = a
		self.b = b
		self.c = c

	def value(self, x):
		a = self.a
		b = self.b
		c = self.c
		return a*x**2 + b*x + c
	
	def table(self, L, R, n):
		self.L = L #left 
		self.R = R #right
		self.n = n #spacing, interval

		x = np.linspace(L,R,n) #array of x values

		for i in x:
			print 'x: %.2f | f(x): %.2f '\
			 %(i, self.value(i))

	def roots(self):
		a = self.a
		b = self.b
		c = self.c
		if (b**2)-4.0*a*c < 0: #testing for negative in sqrt
			return (-b+(cmath.sqrt(b**2-(4*a*c))))/(2*a),\
			 (-b-(cmath.sqrt(b**2-(4*a*c))))/(2*a)
			 #if negative, we use cmath for complex numbers
		else:
			return (-b-(math.sqrt(b**2-(4*a*c))))/(2*a),\
			(-b-(math.sqrt(b**2-(4*a*c))))/(2*a)
			#if positive, we use math

q = Quadratic(1,-2,1) #making 'instance'		

def test_func_value():
	tol = 1E-14
	expected = 0
	computed = q.value(1)
	success = abs(expected-computed)<tol
	msg = 'expected does not equal computed'
	assert success, msg
	print 'test function works'

def test_func_roots():
	tol = 1E-14
	expected = 1.0, 1.0
	computed = q.roots()
	success = abs(expected[0]-computed[0])<tol and abs(expected[1]-computed[1])<tol
	msg = 'expected does not equal computed'
	assert success, msg
	print 'test function works'		


print q.roots()
print q.value(1)
q.table(5,14,10)
test_func_value()
test_func_roots()

"""
terminal>> python Quadratic.py 
(1.0, 1.0)
0
x: 5.00 | f(x): 16.00 
x: 6.00 | f(x): 25.00 
x: 7.00 | f(x): 36.00 
x: 8.00 | f(x): 49.00 
x: 9.00 | f(x): 64.00 
x: 10.00 | f(x): 81.00 
x: 11.00 | f(x): 100.00 
x: 12.00 | f(x): 121.00 
x: 13.00 | f(x): 144.00 
x: 14.00 | f(x): 169.00 
test function works
test function works
"""
