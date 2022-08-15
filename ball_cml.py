#Exercise 4.10

import sys

"""
sys.argv: automatically makes a list of strings 
representing the arguments (as separated by spaces)
on the command-line.
Takes the 1st and 2nd argument after filename, command line argument.

"""

if len(sys.argv) < 2:
    print "You need to provide a command line argument for t and v0."
    sys.exit()

"""
number of elements in list made by sys.argv has to be greater than 2,
one value for t and one for v0.  

"""

g = 9.81


t = sys.argv[1]
t = float(t)

v0 = sys.argv[2]
v0 = float(v0)


y = v0*t - 0.5*g*t**2

print "When the initial velocity is %.2f meters per seconds,\
the ball will have reached the height of %.2f meters\
 after %.2f seconds." %(v0,y,t)


 """
No command-line argument:

terminal >> python ball_cml_qa.py
No command line argument.
t = 2
v0 = 40
When the initial velocity is 40.00 meters per seconds,
the ball will have reached the height of 60.38 meters after 2.00 seconds.

With command-line argument:

terminal >> python ball_cml_qa.py 2 40
When the initial velocity is 40.00 meters per seconds,
the ball will have reached the height of 60.38 meters after 2.00 seconds.

"""
