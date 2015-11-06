#!/usr/bin/python

class Solution(object):
	def wordPattern(self, pattern, str):
		patternList = list(pattern)
		patternListUnique = []
		for p in patternList:
			if p not in patternListUnique:
				patternListUnique.append(p)
		strList = str.split(" ")
		strListUnique = []
		for p in strList:
			if p not in strListUnique:
				strListUnique.append(p)
		if len(patternListUnique) != len(strListUnique):
			return False
		else:
			mapping = {}
			for i in range(len(patternListUnique)):
				mapping[strListUnique[i]] = patternListUnique[i]
			image = []
			for word in str.split(" "):
				image.append(mapping[word])
			return image == list(pattern)
	





test = Solution()
pattern = "ab"
str = "b c"
print test.wordPattern(pattern, str)	
