
#Exercise 1.11: Compute the air resistance on a football


from math import pi


Cd = 0.4 #Drag coefficient, no units.

V1 = 120/3.6 # Velocity 1 of ball (hard kick), m s^-1
V2 = 30/3.6 # Velocity 2 of ball (soft kick), m s^-1

rho = 1.2 # Air density, kg m^-3
g =  9.81 # Acceleration of gravity, m s^-2 
a = 0.11 # Radius of ball, m
m = 0.43 # Mass of ball, kg

A = pi*a**2 # Cross sectional area of ball, m^2
Fg = m*g # Force of gravity, N
Fd1 = (1.0/2.0)*Cd*rho*A*V1**2 # Drag force due to air resistance with V1, N
Fd2 = (1.0/2.0)*Cd*rho*A*V2**2 # Drag force due to air resistance with V2, N

ratio1 = Fd1/Fg
ratio2 =Fd2/Fg

print "The force of gravity on the ball is %2f." %Fg

print "The drag force due to air resistance on ball\
 with velocity of 120 km/h is %2f N." %Fd1
print "The drag force due to air resistance on ball\
 with velocity of 30 km/h is %2f N." %Fd2

print "The ratio of the drag force on the ball with velocity equal\
 to 120 km/h and the force of gravity on the ball is %2f." %ratio1
print "The ratio of the drag force on the ball with velocity equal\
 to 30 km/hand the force of gravity on the ball is %2f." %ratio2

"""
terminal>>python kick.py
The force of gravity on the ball is 4.218300.
The drag force due to air resistance on ball with velocity of 120 km/h is 10.136872 N.
The drag force due to air resistance on ball with velocity of 30 km/h is 0.633555 N.
The ratio of the drag force on the ball with velocity equal to 120 km/h and the force of gravity on the ball is 2.403071.
The ratio of the drag force on the ball with velocity equal to 30 km/hand the force of gravity on the ball is 0.150192.

"""

