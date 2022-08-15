#Exercise 4.14

#a)

import random

t_values = [] 
#list for t-values

def y(): 
	# Open the file that you want the program to read.	
	with open('ball.dat', 'r') as infile:
		lst = infile.readline()
		lst = lst.split()
		v0 = float(lst[1])
		# Read first line and split and get the v0 value from index 1

		infile.readline()
		# Skip the next line (t:)

		for line in infile:	# for every line in file
			lst = line.split()
			#create list, split number in file and put them in a list

			for i in lst: #for every element in list
				i = float(i)

				t_values.append(i)
				#float element and put in new list


	return t_values, v0

print y()
#call function


#b)

def ballwritetest ():

	
	with open('ballwritetest.dat', 'w') as outfile:
		#creating new file to write in
		outfile.write("v0: 3.00\nt:  \n0.5987  0.4926  0.9786  \n2.593  6.34876  2.9954  1.9872  \n 0.3928  0.8743")         
		#wrinting v0 value and random t values in file
    
	y = []
	
	for i in ballwrite:
   		y.append(type(i))

   	return ballwritetest, y

print ballwritetest()
		
print
print

#c)

def y():
	
	with open('ballwrite.txt', 'w') as outfile:
		outfile.write('t_value          y_value\n')
		#variable name heading
		g = 9.81
		t_values = sorted(t_values[1])
		#sorting list of t values from a)
		for t in t_values: #loop finding f value for all t values in t_values list
			f = v0*t - 0.5*g*t**2
			outfile.write("%5.2f   %5.2f\n" %(t, f) 
			#two nicely formatted columns

print y()


"""
terminal >> python ball_file_read_write.py
([0.15592, 0.28075, 0.36807889, 0.35, 0.57681501876, 
	0.21342619, 0.0519085, 0.042, 0.27, 0.50620017, 0.528, 
	0.2094294, 0.1117, 0.53012, 0.372985, 0.39325246, 
	0.21385894, 0.3464815, 0.57982969, 0.10262264, 
	0.29584013, 0.17383923], 3.0)


ballwrite.txt:

v0: 3.00
t:  
0.5987  0.4926  0.9786  
2.593  6.34876  2.9954  1.9872  
 0.3928  0.8743


Strevde med både b) og c) denne uka. Fikk det ikke til å bli riktig, derfor heller ingen terminal utskrift.
Løsningsforslag hadde vært fint.

"""
















