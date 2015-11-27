#!/usr/bin/python
from itertools import combinations

class Solution(object):
	def subsets(self,num):
		length = len(num)
		subsets = []
		for i in range(length + 1):
			com = list(combinations(num, i))
			for c in com:
				cList = list(c)
				cList.sort()
				subsets.append(cList)
		return subsets



num = [1,2]
test = Solution()
print test.subsets(num)
