
#Exercise 7.4
from math import pi, sqrt

class Rectangle(object):
	def __init__(self, x0, y0, W, H): #x0 and y0 are coordinates of corner of rectangle
		self.x0 =x0
		self.y0 = y0
		self.W = W #width
		self.H = H #height

	def area(self):
		return self.W*self.H #area = width*height

	def perimeter(self):
		return 2*self.H + 2*self.W #perimeter = 2*width + 2*height

r1 = Rectangle(2, -1, 5, 4) #making an 'instance'
print r1.perimeter()
print r1.area()

class Triangle(object):
	def __init__(self, v1, v2, v3): 
	#v1, v2 and v3 are tuples with x and y coordinates or triangle corners
		self.v1 = v1
		self.v2 = v2
		self.v3 = v3

	def area(self):
		v1 = self.v1
		v2 = self.v2
		v3 = self.v3
		return 0.5*abs(v1[0]*(v2[1]-v3[1]) + v2[0]*(v3[1]-v1[1]) + v3[1]*(v1[1]-v2[1]))
		#area of triangle with coordinates points

	def perimeter(self):
		v1 = self.v1
		v2 = self.v2
		v3 = self.v3
		return (sqrt(((v2[0]-v1[0])**2)+(v2[1]-v1[1])**2)) +\
		(sqrt(((v2[0]-v3[0])**2)+(v2[1]-v3[1])**2)) +\
		(sqrt(((v3[0]-v1[0])**2)+(v3[1]-v1[0])**2))
		#perimeter of triangle (by adding hypotenuses)

t1 = Triangle((0, 0), (3, 0), (0, 4))
print t1.perimeter()
print t1.area()

def test_func_Rectangle():
	expected_per = 18
	expected_area = 20
	computed_per = r1.perimeter()
	computed_area = r1.area()
	tol = 1E-14
	success = abs(expected_area-computed_area) < tol and abs(expected_per-computed_per) < tol
	msg = 'expected does not equal computed'
	assert success, msg
	print 'test function works'

test_func_Rectangle()

def test_func_Triangle():
	expected_per = 12
	expected_area = 6
	computed_per = t1.perimeter()
	computed_area = t1.area()
	tol = 1E-14
	success = abs(expected_area-computed_area) < tol and abs(expected_per-computed_per) < tol
	msg = 'expected does not equal computed'
	assert success, msg
	print 'test function works'

test_func_Triangle()

"""
terminal>> python geometric_shapes.py 
18
20
12.0
6.0
test function works
test function works

"""




