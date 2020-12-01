import sys
import pygame
import random
import time

class RandomComputerPlayer:

	def __init__(self, color):

		self.color = color    

	def move(self, board, gui, lightScore, darkScore):
		remainCols = []
		for x in range(board.width):
			if board.allowsMove(x):
				remainCols.append(x)

		if not remainCols:
			return
		else:
			n = random.randint(0,len(remainCols)-1)
			col = remainCols[n]
			if board.allowsMove(col):
				board.dropToken(col, self.color)

class HardComputerPlayer:

	def __init__(self, color, depth):

		self.color = color    
		self.depth = depth

	def move(self, board, gui, lightScore, darkScore):

		nextColor = 1 
		if self.color == 1:
			nextColor = 2

		#self.gui = gui

		best = -999999
		best_col = None
		remainCols = []
		for x in range(board.width):
			if board.allowsMove(x):
				remainCols.append(x)
		for col in remainCols:
			board.dropToken(col, self.color)
			score = -self.ratePosition(board, nextColor, self.depth)
			board.undoMove()
			#print("Score: " + str(score))
			if score > best:
				best = score 
				best_col = col
			elif score == best:
				if random.random() > 0.5:
					best = score 
					best_col = col
		if board.allowsMove(best_col):
			board.dropToken(best_col, self.color)	
	
	def ratePosition(self, board, color, depth):

		'''if depth != 0:
			self.gui.draw_board(board, color, 0, 0)
			print("depth: " + str(depth))
			print(str(board.record))
			time.sleep(1)'''

		nextColor = 1 
		if color == 1:
			nextColor = 2

		# max depth base case
		if depth == 0:
			return 0	

		# end of game base cases
		if board.checkWinner() != 0:
	
			# check for tie	base case worth 0
			if board.checkWinner() == -1:
				return 0

			# check for win base case worth 1000
			if board.checkWinner() == color:
				return 1000
			
			# check for lose base case worth -1000
			if board.checkWinner() != color:
				return -1000
	
		# rates moves	
		else:
			best = -99999999
			remainCols = []
			for x in range(board.width):
				if board.allowsMove(x):
					remainCols.append(x)
			for col in remainCols:
				board.dropToken(col, color)
				score = -self.ratePosition(board, nextColor, depth - 1)
				#print("inner score: " + str(score))
				board.undoMove()
				if score > best:
					best = score 

			return best
				



# sorry I'm not super comfortable with inheritance so I just made a seperate human player
# feel free to change this if you want!
class HumanPlayer:
	
	def __init__(self, color):
	
		self.color = color	
	
	
	def move(self, board, gui, lightScore, darkScore):

		# waits for user selection		
		done = False
		while not done:	

			# the event loop
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()	
				
				# mouse click event	drop token
				if event.type == pygame.MOUSEBUTTONDOWN:
					if (gui.place_token(board, self.color)):
						done = True

			gui.draw_board(board, self.color, lightScore, darkScore)
