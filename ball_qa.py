g = 9.81


t = raw_input("Select a value for t:")
t = float(t)

#raw_input - asks user for values in terminal

v0 = raw_input("Select a value for v0:")
v0 = float(v0)

y = v0*t - 0.5*g*t**2

print "When the initial velocity is %.2f meters per seconds,\
the ball will have reached the height of %.2f meters\
 after %.2f seconds." %(v0,y,t)


"""
terminal>> python ball_qa.py
Select a value for t:2
Select a value for v0:40
When the initial velocity is 40.00 meters per seconds,
the ball will have reached the height of 60.38 meters after 2.00 seconds.

"""