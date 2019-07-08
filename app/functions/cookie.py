import random

def getAFortune():
	fortuneList = open("app/functions/Fortune_data.txt").readlines()
	fortune = random.choice(fortuneList)
	return fortune
