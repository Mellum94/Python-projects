#Exercise 8.9: Adjust a game to make it fair

import random
import sys

N = int(sys.argv[1]) #number of games
r = int(sys.argv[2]) #award for win
n = int(sys.argv[3]) #number of dice

win = 0 #initial wins
money = 0 #initial money
cost = 1.0 #cost of one game

for i in range(N): #for loop for game played N times
	dice = 0 #initial eyes on dice
	money -= cost #cost reduces money for every game played 
	for i in range(n): #for loop for n dice for every throw
		die = random.randint(1,6) #random interger from one to six
		dice = dice + die #adding eyes of dice thrown
	if dice < 9: #if eyes of dice are less than 9
		win += 1 #add 1 to number of wins
		money += r #money increases by r

prob = float(win)/N #probability of winning a game
fair = cost/float(prob) #r for a fair game
earned = (win * r) - (N * cost) #money earned in N games	

print "Fair game award: %f" % fair
print "Wins: %d" %win
print "Money: %d " % money
print "Probability: %f" %prob
print "Money Earned: %f " %earned

"""
terminal >> python sum_ndice_fair.py 100000 10 4
Fair game award: 18.419598
Wins: 5429
Money: -45710 
Probability: 0.054290
Money Earned: -45710.000000 

"""
