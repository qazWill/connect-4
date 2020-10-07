import sys
import pygame
from board import Board

pygame.init()

class Game:

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


	# sets up board and runs game loop	
	def run(self):


		# test drops, DELETE
		self.board = Board(6, 7)

		# sets up pygame window
		pygame.display.set_icon(self.light_token_img)
		screen = pygame.display.set_mode((800, 600))
		screen.fill((255, 255, 255))	
		

		# the game loop
		while True:

			# the event loop
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()	
			
				
				# mouse click event	drop token
				if event.type == pygame.MOUSEBUTTONDOWN:
					self.place_token()

			# erase screen
			screen.fill((255,255,255))

			# draws board and tokens
			self.draw_background(screen)
			self.draw_potential_move(screen)
			self.draw_board(screen)

			# displays changes
			pygame.display.flip()

	def draw_background(self, screen):	
		self.back_rect.left = -400
		self.back_rect.top = 0
		screen.blit(self.back_img, self.back_rect)
	
	def draw_board(self, screen):

		# draws the tokens
		self.grid_rect.center = (int(screen.get_width() / 2), int(screen.get_height() / 2))
		token_rect = self.light_token_img.get_rect()
		for row in range(0, len(self.board.data)):
			for col in range(0, len(self.board.data[0])):
				start = 12
				size = 80
				token_rect.left = self.grid_rect.left + start + size * col 
				token_rect.bottom = self.grid_rect.bottom - start - size * (len(self.board.data) - row - 1)
				if self.board.data[row][col] == 0:
					continue
				elif self.board.data[row][col] == 1:
					screen.blit(self.light_token_img, token_rect)
				else:
					screen.blit(self.dark_token_img, token_rect)
				

		# draws the grid
		screen.blit(self.grid_img, self.grid_rect)

		'''token_rect.left = self.grid_rect.left
		token_rect.bottom = self.grid_rect.bottom
		screen.blit(self.light_token_img, token_rect)'''


	def draw_potential_move(self, screen):

		# selects light or dark
		if self.color == 1:
			img = self.light_transparent_img
		else:
			img = self.dark_transparent_img

		# gets column 
		col = self.col_from_mouse()
		
		# gets row
		if self.board.allowsMove(col):
			row = len(self.board.data) - 1
			while self.board.data[row][col] != 0:
				row -= 1
			rect = self.light_token_img.get_rect()
			start = 12
			size = 80
			rect.left = self.grid_rect.left + start + size * col 
			rect.bottom = self.grid_rect.bottom - start - size * (len(self.board.data) - row - 1)
			screen.blit(img, rect)
		else:
			return	

	def place_token(self):

		# if winner already found don't allow moves 
		if self.winner != 0:
			return

		col = self.col_from_mouse()
		if self.board.allowsMove(col):
			self.board.dropToken(col, self.color)
			if self.color == 1:
				self.color = 2
			else:
				self.color = 1
			self.winner = self.board.checkWinner()
			


	
	def col_from_mouse(self):

		x, y = pygame.mouse.get_pos()
		size = 82
		col = int((x - self.grid_rect.left) / size)
		return col
	




if __name__ == "__main__":
	
	game = Game()
	game.run()


