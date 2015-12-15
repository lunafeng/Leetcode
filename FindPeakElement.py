#!/usr/bin/python
from decimal import Decimal

class Solution(object):
	def findPeakElement(self,nums):
		neg_inf = Decimal('-Infinity')
		front = []
		front.append(neg_inf)
		front += nums
		nums = front
		nums.append(neg_inf)
		for i in range(len(nums)):
			try:
				fir = nums[i]
				mid = nums[i+1]
				sec = nums[i+2]
				if fir < mid and sec < mid:
					return i
			except:
				pass
		return 0



			
