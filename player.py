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

