import random

def getAFortune():
	fortuneList = open("Fortune_data.txt").readlines()
	fortune = random.choice(fortuneList)
	return fortune