#!/usr/bin/python

class Solution():
	def getHint(self, secret, guess):
		length = len(secret)
		secretNew = ""
		guessNew = ""
		same = []
		for i in range(length):
			s = secret[i]
			g = guess[i]
			if s != g:
				secretNew += s
				guessNew += g
			else:
				same.append(s)
		secretHash = {}
		for l in secretNew:
			if l not in secretHash:
				secretHash[l] = 1
			else:
				secretHash[l] += 1
		diff = []
		for i in range(len(secretNew)):
			g = guessNew[i]
			if g in secretHash and secretHash[g] > 0:
				diff.append(g)
				secretHash[g] -= 1
		sameNum = len(same)
		diffNum = len(diff)
		return str(sameNum) + "A" + str(diffNum) + "B"

				
			

				
