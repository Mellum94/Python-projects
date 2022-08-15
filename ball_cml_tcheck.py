#Exercise 4.12 

import sys

g = 9.81

def y(t):
	return v0*t - 0.5*g*t**2

try:	
	t = sys.argv[1]
	t = float(t)

	v0 = sys.argv[2]
	v0 = float(v0)

except:
	print "No command line argument."
	t = raw_input("t = ")
	v0 = raw_input("v0 = ")
	
	try:
		t = float(t)
		v0 = float(v0)
	except:
		print "Cannot convert to float."
		sys.exit()
		
if 0 < t < (2.0*v0)/g:
	print "t is in range"
else:
	print "t is out of range"
	sys.exit()	

print "When the initial velocity is %.2f meters per seconds, \
the ball will have reached the height of %.2f meters\
 after %.2f seconds." %(v0,y(t),t)


"""
No command-line argument:

terminal >> python ball_cml_tcheck.py
No command line argument.
t = 2
v0 = 40
t is in range
When the initial velocity is 40.00 meters per seconds,
the ball will have reached the height of 60.38 meters after 2.00 seconds.

With command-line argument:

terminal >> python ball_cml_tcheck.py 2 40
t is in range
When the initial velocity is 40.00 meters per seconds,
the ball will have reached the height of 60.38 meters after 2.00 seconds.

"""

