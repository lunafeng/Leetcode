#!/usr/bin/python

class Solution:
	def isHappy(self,n):
		numStr = str(n)
		nextNum = numStr
		appeared = []
		while(int(nextNum) != 1):
			if nextNum in appeared:
				return False
			else:
				sum = 0
				for num in nextNum:
					sum += int(num)**2
				appeared.append(nextNum)
				nextNum = str(sum)
				print "next:",nextNum
		return True

test = Solution()
print test.isHappy(11)
