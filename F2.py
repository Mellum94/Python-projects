#Exercise 7.11
from math import e, sin

class F(object):

	def __init__(self, a, w): #special method
		self.a = a
		self.w = w
		
	def __str__(self): #special method, to see function as string
		return 'e**(-a*x)*sin(w*x)'
		
	def __call__(self, x): #special method, calling function
		a = self.a
		w = self.w
		return e**(-a*x)*sin(w*x)

"""
terminal>> python
Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
[GCC 5.4.0 20160609] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> from F2 import F
>>> f =F(a=1.0, w=0.1)
>>> from math import pi
>>> print f(x=pi)
0.013353835137
>>> f.a = 2
>>> print f(pi)
0.00057707154012
>>> print f
e**(-a*x)*sin(w*x)
>>> exit()
"""
	
