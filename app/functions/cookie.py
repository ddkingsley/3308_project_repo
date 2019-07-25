import random

def getAFortune(test=False):
	if test:
		fortuneList = open("./Fortune_data.txt").readlines()
	else:
		fortuneList = open("app/functions/Fortune_data.txt").readlines()
	fortune = random.choice(fortuneList)
	return fortune

def getLuckyNumbers():
	numlist = []
	for i in range(5):
		num = random.randrange(1, 70)
		numlist.append(num)
	num = random.randrange(1, 27)
	numlist.append(num)
	numstring = ""
	for i in numlist:
		numstring = numstring + str(i) + " "
	return numstring


