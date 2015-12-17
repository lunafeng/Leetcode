#!/usr/bin/python
import collections

class Solution(object):
	def deleteDuplicates(self, head):
		numbers = []
		point = head
		while(point != None):
			value = point.val
			numbers.append(value)
			point = point.next
		counter = dict(collections.Counter(numbers))
		duplicates = [k for k in counter if counter[k] > 1]
		point = head
		while(point != None and point.val in duplicates):
			point = point.next
		if point is None:
			return point
		else:	
			head = ListNode(point.val)		
			newpoint = head
			point = point.next
			while(point != None):
				current = point.val
				if current not in duplicates:
					newpoint.next = ListNode(point.val)
					newpoint = newpoint.next
					point = point.next
				else:
					point = point.next
			return head


class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

	def printNode(self, head):
		point = head
		while(point != None):
			print point.val , "->",
			point = point.next

			
				
