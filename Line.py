
#Exercise 7.6

class Line(object):
	def __init__(self, p1, p2):
		self.p1 = p1
		self.p2 = p2
		
	def value(self, x):
		p1 = self.p1
		p2 = self.p2
		
		if p2[0] != p1[0]: #testing if we get 0 in denominator
			a = (p2[1]-p1[1])/float(p2[0]-p1[0])
			b = p1[1] - a*p1[0]
			return a*x + b
		else:
			b = p1[1]
			return b
		
l = Line((0,-1),(2,4)) #making 'instance'
print l.value(1)

def test_func_line():
	tol = 1E-14
	expected = 1.5
	computed = l.value(1)
	success = abs(expected - computed) < tol
	msg = 'expected does not equal computed'
	assert success, msg
	print 'test function works'
	
test_func_line()

"""
terminal>> python Line.py 
1.5
test function works

"""

