import numpy as np
import random

namelist = open('names_prepped.txt', "r").read()

corpus = namelist.split()

charpair_dict = {}

#makes a dictionary of dictionaries - letters key paired letters key number of occurrences of said paired letter
for word in corpus:
	for i in range(len(word)-1):
		if word[i] in charpair_dict.keys():
			keychar = word[i]
			pairee_dict = charpair_dict[keychar]
			if word[i+1] in pairee_dict.keys():
				pairee_dict[word[i+1]] += 1
			else:
				pairee_dict[word[i+1]] = 1
			charpair_dict[keychar] = pairee_dict
		else:
			pairee_dict = {}
			pairee_dict[word[i+1]] = 1
			charpair_dict[word[i]] = pairee_dict

#print charpair_dict

#this block generates the first character
starts = 0
getstarts = charpair_dict["^"]
startcheck = 0
for char in getstarts.keys():
	starts += getstarts[char]
seed = random.randint(1, starts)
for char in getstarts.keys():
	startcheck +=getstarts[char]
	if startcheck >= seed:
		firstchar = char
		break
lastchar = firstchar

#this block generates the rest of the name
name = [firstchar]

while True:
	numpairs = 0 #counts how many pairs total the key letter has
	check = 0 #if this number exceeds the random number, correct letter has been found
	getnum = charpair_dict[lastchar]
	for char in getnum.keys():
		numpairs += getnum[char]
	nextchar_num = random.randint(1,numpairs)
	for char in getnum.keys():
		check += getnum[char]
		if check >= nextchar_num:
			nextchar = char
			break
	name.append(nextchar)
	if name[-1] == "/":
		if len(name) > 3:
			break
		else:
			name = name[:-1]
	lastchar = name[-1]

finalname = ''.join(name)
finalname = finalname[:-1]

print finalname