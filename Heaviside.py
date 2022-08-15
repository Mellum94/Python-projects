#Exercise 3.29

#a)

def H(x):
    if x < 0:
        return 0
    else:
        return 1

print "H(x)=%g" %(H(2))



#b)

def test_H():
    liste = [-10, -10**15, 0, 10**(-15), 10]
    expected = [0, 0, 1, 1, 1]
    computed = [H(liste[0]), H(liste[1]), H(liste[2]), H(liste[3]), H(liste[4])]
    success = expected == computed
    msg = "computed != expected"
    assert success, msg
    print "it's working!"

test_H()
    
"""
terminal >> python Heaviside.py 
H(x)=1
it's working!

"""
