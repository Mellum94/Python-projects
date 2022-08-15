#Exercise 5.22
#a)

import numpy as np
import matplotlib.pyplot as plt

with open('pos.dat', 'r') as infile: 
	s = infile.readline() 
	#storing first line in file as variable s (time interval)
	
	x_values = []
	y_values = []
	#creating lists to store and seperate the x and y GPS coordinates
	
	for line in infile: #using for loop to go through all lines in file
		values = line.split() 
		# splitting each line and storing elements in list

		x = float(values[0]) #converting first element in list to float 
							 #and storing it as variable x 
		y = float(values[1]) #converting second element in list to float
							 #and storing it as variable y 
		x_values.append(x) 
		y_values.append(y)
		#adding x and y variables to respectively x and y lists
	

x = np.array(x_values) 
y = np.array(y_values)
#converting x and y lists to arrays for plot

print s
#checking if s variable is correct for b)

plt.plot(x,y)
#plotting x and y array

plt.xlabel('x')
plt.ylabel('y')
#labeling axis

plt.show()

#b)

vx_values = []
vy_values = []
#making lists for velocities in x and y direction

time = [] #list for time

def vx(t): #function for velocities in x direction
	
	for k in range(0, len(x)-1): #for loop for numerical differentiation
		t = k*s #adding 15 sec interval for time
		time.append(t) # adding new time values to time list
		x_ = x[k]
		vx = (x_*(t[k+1])-x_*t[n])/s
		vx_values.append(vx) #adding new velocities to vx_values list
	
	return vx_values


def vy(t): #function for velocities in y direction
	
	for k in range(0,len(y)-1): #for loop for numerical differentiation
		y_ = y[k]
		vy = (y_*t[k+1]-y_*t[k])/s
		vy_values.append(vy) #adding new velocities to vy_values list
		
	return vy_values

        
vel_x = np.array(vx_values)
vel_y = np.array(vy_values)
#converting velocity lists to arrays
time = np.array(time)
#converting time list to array

plt.plot(time, vel_x)
plt.plot(time, vel_y)
#plotting velocities in y and x direction versus time
plt.xlabel('time in seconds')
plt.ylabel('velocity')
#lebeling x and y axis
plt.show()

"""
terminal>>python position2velocity.py  15


Ingen graf paa b). 
Skjonner ikke helt hva jeg har gjordt feil.
"""
