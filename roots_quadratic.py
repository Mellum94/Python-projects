#Exercise 3.8: Write a function for solving ax^2 + bx + c = 0


print "a)"

from numpy.lib.scimath import sqrt

def roots(a, b, c):
    return (-b - sqrt(b**2 - 4*a*c))/(2*a), (-b + sqrt(b**2 - 4*a*c))/(2*a)


print roots(1,10,29)

"""
terminal>>python roots_quadratic.py 
((-5-2j), (-5+2j)))

"""

print "b)"


def test_roots_float():
    expected = [-2.0, -0.5]
    computed = roots(2, 5, 2)
    tol = 1E-14
    success = abs(expected[0] - computed[0]) < tol
    msg = "computed roots = %g != %g (expected)" %(computed[0], expected[0])
    assert success, msg
    success_2= abs(expected[1] - computed[1]) < tol
    msg_2 = "computed roots = %g != %g (expected)" %(computed[1], expected[1])
    assert success_2, msg_2
    print "it's working"

test_roots_float()


from cmath import sqrt

j = sqrt(-1)
def test_roots_complex():
    expected = [-5-2j, -5+2j]
    computed = roots(1, 10, 29)
    tol = 1E-14
    success = abs(expected[0] - computed[0]) < tol
    msg =  "computed roots = %f+%f != %f+%f (expected)" %(computed[0].real, computed[0].imag, expected[0].real, expected[0].imag)
    assert success, msg # erstatter if setningen, sjekk, forsikrer
    success_2= abs(expected[1] - computed[1]) < tol
    msg_2 = "computed roots = %f%f != %f+%f (expected)" %(computed[1].real, computed[1].imag, expected[1].real, expected[1].imag)
    assert success_2, msg_2
    print "this one is also working"

test_roots_complex()


"""
terminal>> python roots_quadratic.py 
a)
((-5-2j), (-5+2j))
b)
it's working
this one is also working

"""
