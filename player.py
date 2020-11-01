import pygame


'''
Base CLass for Player. It will split into human and AI implementations
'''
class BasePlayer:
	def __init__(self, name, color):
		self.name = name
		self.color = color

	def __repr__(self):
		return str(self.name)

	def play(self, board):
		return True



# sorry I'm not super comfortable with inheritance so I just made a seperate human player
# feel free to change this if you want!
class HumanPlayer:
	
	def __init__(self, color):
	
		self.color = color	
	
	
	def move(self, board, gui):

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

			gui.draw_board(board, self.color)
