class Board:

	def __init__(self):

		self.board = # to do initialize board


	def getWinner(self):	

		# checks for row of 4
		for y in range(0, 6):
			count = 0
			target = 1
			for x in range(0, 7):
				if board[x][y] == 0:
					count = 0
				elif board[x][y] == target:
					count += 1
				else:
					count = 1
					target = board[x][y]

				if count == 4:
					return target

		# checks for column of 4
		for x in range(0, 7):
			count = 0
			target = 1
			for y in range(0, 6):
				if board[x][y] == 0:
					count = 0
				elif board[x][y] == target:
					count += 1
				else:
					count = 1
					target = board[x][y]

				if count == 4:
					return target

		# checks for diagonal of 4
		for x_start in range(0, 7):
			for y_start in range(0, 6):
				
				x = x_start
				y = y_start	
				target = board[x][y]
				
				# skip 0's
				if target == 0:
					continue

				found = True
		
