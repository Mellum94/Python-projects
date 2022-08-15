

def f(x):
    return x + 1

print f(2)


def test_noe():
    expected = 4
    computed = f(2)
    tol = 1E-14
    success = abs(expected - computed) < tol
    msg = "computed=%g != %g (expected)" %(computed, expected)
    assert success, msg

test_noe()

"""
terminal>>> python noe.py 
3
Traceback (most recent call last):
  File "noe.py", line 16, in <module>
    test_noe()
  File "noe.py", line 14, in test_noe
    assert success, msg
AssertionError: computed=3 != 4 (expected)

"""

