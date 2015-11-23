#!/usr/bin/python

class Solution:
	def isValidSudoku(self,board):
		for row in board:
			rowHash = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
			for num in row:
				try:
					num = int(num)
					rowHash[num] += 1
				except:
					pass
			print rowHash
			if self.validation(rowHash) == False:
				return False
		print "row is ok"
		for i in range(9):
			column = []
			columnHash =  {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
			for row in board:
				column.append(row[i])
			for num in column :
				try:
					num = int(num)
					columnHash[num] += 1
				except:
					pass
			if self.validation(columnHash) == False:
				return False
		print "column is ok"
		for i in range(3):
			rows = board[i*3:i*3+3]
			print "rows:",rows
			for j in range(3):
				square = []
				squareHash =  {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
				for row in rows:
					square += row[j*3:j*3+3]
				print square
				for num in square :
					try:
						num = int(num)
						squareHash[num] += 1
					except:
						pass
				print squareHash
				if self.validation(squareHash) == False:
					return False
		print "square is ok"
		return True	

	def validation(self,hash):
		for num in hash:
			if hash[num] > 1:
				return False
		return True
			
			
#board = [".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]
board = ["....5..1.",".4.3.....",".....3..1","8......2.","..2.7....",".15......",".....2...",".2.9.....","..4......"]
test = Solution()
print test.isValidSudoku(board)




	
