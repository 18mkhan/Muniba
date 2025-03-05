from random import *
player1 = input("player1 name- ")
rounds = 1
while rounds <= 13:	
	dice1 = randint(1,6)
	dice2 = randint(1,6)
	dice3 = randint(1,6)
	dice4 = randint(1,6)
	dice5 = randint(1,6)
	dice6 = randint(1,6)
	print(dice1)
	print(dice2)
	print(dice3)
	print(dice4)
	print(dice5)
	print(dice6)
	print("round num", rounds, "-player1")
	rounds = rounds + 1
player2 = input("player2 name- ")
rounds = 1
while rounds <=13:
	dice1 = randint(1,6)
	dice2 = randint(1,6)
	dice3 = randint(1,6)
	dice4 = randint(1,6)
	dice5 = randint(1,6)
	dice6 = randint(1,6)
	print(dice1)
	print(dice2)
	print(dice3)
	print(dice4)
	print(dice5)
	print(dice6)
	print("round num", rounds, "-player2")
	rounds = rounds + 1


