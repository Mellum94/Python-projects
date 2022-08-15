#Exercise 9.11: Implement a new sub-class for differentiation


from math import e
import numpy as np

class Diff:
	def __init__(self, f, h=1E-5):
		self.f = f
		self.h = float(h)

class Backward1(Diff): #inheriting from Diff
	def __call__(self, x):
		f, h = self.f, self.h
		return (f(x) - f(x-h))/h

class Backward2(Diff): #inheriting from Diff
	def __call__(self, x):
		f, h = self.f, self.h
		return (f(x-2*h)-4*f(x-h)+3*f(x))/(2*h)

def g(t):
	return e**(-t)

for k in range(0,15):
	h = 2**(-k) #increasing k for smaller and smaller h
	func1 = Backward1(g,h)
	func2 = Backward2(g,h)
	deriv1 = func1(0)
	deriv2 = func2(0)
	#Table:
	print 'func1(0): %10.5f   func2(0): %10.5f  Difference: %10.5f' %(deriv1, deriv2, abs(deriv1 - deriv2))

"""
terminal >> python Backward2.py 
func1(0):   -1.71828   func2(0):   -0.24204  Difference:    1.47625
func1(0):   -1.29744   func2(0):   -0.87660  Difference:    0.42084
func1(0):   -1.13610   func2(0):   -0.97476  Difference:    0.16134
func1(0):   -1.06519   func2(0):   -0.99427  Difference:    0.07091
func1(0):   -1.03191   func2(0):   -0.99864  Difference:    0.03328
func1(0):   -1.01579   func2(0):   -0.99967  Difference:    0.01612
func1(0):   -1.00785   func2(0):   -0.99992  Difference:    0.00794
func1(0):   -1.00392   func2(0):   -0.99998  Difference:    0.00394
func1(0):   -1.00196   func2(0):   -0.99999  Difference:    0.00196
func1(0):   -1.00098   func2(0):   -1.00000  Difference:    0.00098
func1(0):   -1.00049   func2(0):   -1.00000  Difference:    0.00049
func1(0):   -1.00024   func2(0):   -1.00000  Difference:    0.00024
func1(0):   -1.00012   func2(0):   -1.00000  Difference:    0.00012
func1(0):   -1.00006   func2(0):   -1.00000  Difference:    0.00006
func1(0):   -1.00003   func2(0):   -1.00000  Difference:    0.00003

"""