import sys
import pygame

pygame.init()

class GUI:

	def __init__(self):

		# load all images
		self.grid_img = pygame.image.load('images/grid.png')
		self.grid_rect = self.grid_img.get_rect()
		self.light_token_img = pygame.image.load('images/light_token2.png')
		self.light_transparent_img = pygame.image.load('images/light_transparent2.png')
		self.dark_transparent_img = pygame.image.load('images/dark_transparent.png')
		self.dark_token_img = pygame.image.load('images/dark_token.png')
		self.back_img = pygame.image.load('images/background.png')
		self.back_rect = self.back_img.get_rect()

		# keeps track of turn order and players 
		self.color = 1 
		self.winner = 0
		self.lightIsHuman = True
		self.darkIsHuman = True

		# used for rendering text
		self.font = pygame.font.SysFont("comicsansms", 34)

		# sets up screen
		pygame.display.set_icon(self.light_token_img)
		self.screen = pygame.display.set_mode((800, 600))
		self.screen.fill((255, 255, 255))	

		# restart button
		self.restart_img = pygame.image.load('images/restart.png')
		self.restart_rect = self.restart_img.get_rect()
		self.restart_rect.center = [self.screen.get_width() / 2, self.screen.get_height() / 2]

	# event loop for when game is over	
	def end_menu(self, board, lightScore, darkScore):

		# the game loop
		done = False
		while not done:

			# the event loop
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()	
				
				# mouse click event	drop token
				if event.type == pygame.MOUSEBUTTONDOWN:
					x, y = event.pos
					
					# check to see if restart button is pressed
					if x > self.restart_rect.left and x < self.restart_rect.right:
						if y > self.restart_rect.top and y < self.restart_rect.bottom:
						
							# restart the game	
							done = True	
							self.winner = 0

			# draws board and tokens
			self.draw_board(board, 0, lightScore, darkScore)

			# draws restart button
			self.screen.blit(self.restart_img, self.restart_rect)
			
			pygame.display.flip()


	def draw_background(self):	
		self.back_rect.left = -400
		self.back_rect.top = 0
		self.screen.blit(self.back_img, self.back_rect)
	
	def draw_board(self, board, color, lightScore, darkScore):

		# erase old screen
		#self.screen.fill((255,255,255))

		self.draw_background()
		self.draw_potential_move(board, color)

		# draws the tokens
		self.grid_rect.center = (int(self.screen.get_width() / 2), int(self.screen.get_height() / 2))
		token_rect = self.light_token_img.get_rect()
		for row in range(0, len(board.data)):
			for col in range(0, len(board.data[0])):
				start = 12
				size = 80
				token_rect.left = self.grid_rect.left + start + size * col 
				token_rect.bottom = self.grid_rect.bottom - start - size * (len(board.data) - row - 1)
				if board.data[row][col] == 0:
					continue
				elif board.data[row][col] == 1:
					self.screen.blit(self.light_token_img, token_rect)
				else:
					self.screen.blit(self.dark_token_img, token_rect)

		# draws the grid
		self.screen.blit(self.grid_img, self.grid_rect)

		# informs users of a winner
		if self.winner != 0:
			winner = "Green Wins!"
			if self.winner == 2:
				winner = "Black Wins!"
			txt = self.font.render(winner, True, (0, 0, 0))
			rect = txt.get_rect()
			rect.centerx = self.screen.get_width() / 2
			rect.top = 8 
			self.screen.blit(txt, rect)

		# displays score
		light_txt = self.font.render(str(lightScore), True, (0, 255, 0))
		light_rect = light_txt.get_rect()
		light_rect.left = 20 
		light_rect.top = self.screen.get_height() / 2 - 100
		self.screen.blit(light_txt, light_rect)
		buff_txt = self.font.render("-", True, (0, 0, 0))
		buff_rect = buff_txt.get_rect()
		buff_rect.centerx = light_rect.centerx
		buff_rect.top = light_rect.bottom - 20 
		self.screen.blit(buff_txt, buff_rect)
		dark_txt = self.font.render(str(darkScore), True, (0, 0, 0))
		dark_rect = dark_txt.get_rect()
		dark_rect.centerx = light_rect.centerx 
		dark_rect.top = buff_rect.bottom - 20 
		self.screen.blit(dark_txt, dark_rect)
		

		# displays changes
		pygame.display.flip()

		'''token_rect.left = self.grid_rect.left
		token_rect.bottom = self.grid_rect.bottom
		screen.blit(self.light_token_img, token_rect)'''


	def draw_potential_move(self, board, color):

		# skip display if no player is moving
		if color == 0:
			return

		# selects light or dark
		if color == 1:
			img = self.light_transparent_img
		else:
			img = self.dark_transparent_img

		# gets column 
		col = self.col_from_mouse()
		
		# gets row
		if board.allowsMove(col):
			row = len(board.data) - 1
			while board.data[row][col] != 0:
				row -= 1
			rect = self.light_token_img.get_rect()
			start = 12
			size = 80
			rect.left = self.grid_rect.left + start + size * col 
			rect.bottom = self.grid_rect.bottom - start - size * (len(board.data) - row - 1)
			self.screen.blit(img, rect)
		else:
			return	



	def place_token(self, board, color):

		# if winner already found don't allow moves 
		if self.winner != 0:
			return False

		col = self.col_from_mouse()
		if board.allowsMove(col):
			board.dropToken(col, color)
			if color == 1:
				color = 2
			else:
				color = 1
			print(board.record)
			return True
	
		return False
			


	
	def col_from_mouse(self):

		x, y = pygame.mouse.get_pos()
		size = 82
		col = int((x - self.grid_rect.left) / size)
		return col
	




if __name__ == "__main__":
	
	game = Game()
	game.run()


