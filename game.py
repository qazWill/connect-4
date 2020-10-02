import sys
import pygame
from board import Board

class Game:

	def __init__(self):

		# load all images
		self.grid_img = pygame.image.load('grid.png')
		self.grid_rect = self.grid_img.get_rect()
		self.light_token_img = pygame.image.load('light_token.png')
		self.dark_token_img = pygame.image.load('dark_token.png')
		self.back_img = pygame.image.load('background.png')
		self.back_rect = self.back_img.get_rect()
	
	def run(self):

		self.board = Board(6, 7)
		self.board.dropToken(0, 1)
		self.board.dropToken(0, 2)
		self.board.dropToken(1, 2)
		self.board.dropToken(1, 1)
		self.board.dropToken(6, 1)
		self.board.dropToken(6, 1)
		self.board.dropToken(6, 1)
		self.board.dropToken(6, 1)
		self.board.dropToken(6, 1)

		print(self.board)
		

		screen = pygame.display.set_mode((800, 600))
		screen.fill((255, 255, 255))	
		

		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					print("Quit")
					sys.exit()

			screen.fill((255,255,255))
			self.draw_board(screen)
			pygame.display.flip()

		
	def draw_board(self, screen):
		
		# draws the background
		self.back_rect.left = -400
		self.back_rect.top = 0
		screen.blit(self.back_img, self.back_rect)

		# draws the tokens
		self.grid_rect.center = (float(screen.get_width() / 2), float(screen.get_height() / 2))
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



if __name__ == "__main__":
	
	game = Game()
	game.run()


