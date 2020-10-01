from board import Board

'''
Base CLass for Player. It will split into human and AI implementations

token_id (int) is the token used to represent this player's token on the board
'''
class BasePlayer:
	def __init__(self, name, color, token_id):
		self.name = name
		self.color = color
		self.token_id = token_id

	def __repr__(self):
		return str(self.name)

	def playMove(self, board, col):
		if board.dropToken(col, self.token_id):
			return True
		return False
