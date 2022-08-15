#Exercise 8.8: Decide if a game is fair

import random
import sys

N = int(sys.argv[1]) #number of games
r = int(sys.argv[2]) #award for win

win = 0 #initial wins
money = 0 #initial money
cost = 1.0 #cost of one game

for i in range(N): #for loop for game played N times
	dice = 0 #initial eyes on dice
	money -= cost #cost reduces money for every game played 
	for i in range(4): #for loop for n dice for every throw
		die = random.randint(1,6) #random interger from one to six
		dice = dice + die #adding eyes of dice thrown
	print dice
	if dice < 9: #if eyes of dice are less than 9
		win += 1 #add 1 to number of wins
		money += r #money increases by r

earned = (win * r) - (N * cost) #Money earned in N games 	
prob = float(win)/N #probability of winning a game

print "Wins: %d" %win
print "Money: %d " %money
print "Probability: %f" %prob
print "Money Earned: %f " %earned

"""
terminal >> python sum_4dice.py 10000 10
7
11
16
12
12
20
22
...
7
13
10
15
16
7
Wins: 560
Money: -4400 
Probability: 0.056000
Money Earned: 5040.000000 
"""