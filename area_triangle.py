
#Exercise 3.16


x_1 = 0.0
x_2 = 1.0
x_3 = 0.0

y_1 = 0.0
y_2 = 0.0
y_3 = 2.0


v1 = (x_1,y_1); v2 = (x_2,y_2); v3 = (x_3,y_3)

vertices = [v1, v2, v3]

def triangle_area (vertices):
    return (1.0/2.0)*abs((x_2*y_3)-(x_3*y_2)-(x_1*y_3)+(x_3*y_1)+(x_1*y_2)-(x_2*y_1))

print "The area of the triangle is %.2f ." %(triangle_area(vertices))

"""
terminal >> python area_triangle.py 
The area of the triangel is 1.00 .

"""

def test_triangle_area():
    v1 = (0,0); v2 = (1,0); v3 = (0,2)
    vertices = [v1, v2, v3]
    expected = 1
    computed = triangle_area (vertices)
    tol = 1e-14
    success = abs(expected-computed) < tol
    msg = 'computed area =%g != %g (expected)' % (computed,expected)
    assert success, msg
    print "It's working!"

test_triangle_area()


"""
terminal>> python area_triangle.py 
The area of the triangel is 1.00 .
It's working!

"""

 

