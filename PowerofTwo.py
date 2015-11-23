#!/usr/bin/python

class Solution:
	def isPowerOfTwo(self,n):
		power = 0
		while(1):
			if 2**power == n:
				return True
			elif 2**power > n:
				return False
			power += 1

test = Solution()
print test.isPowerOfTwo(8)	
