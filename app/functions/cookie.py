import random

#function to get random fortune from text file, returns string
def getAFortune(test=False):
	if test: #check if function call is for test to determine appropriate path name to text file
		fortuneList = open("./Fortune_data.txt").readlines()
	else:
		fortuneList = open("app/functions/Fortune_data.txt").readlines()
	fortune = random.choice(fortuneList)
	return fortune

#function to return string of random numbers
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


