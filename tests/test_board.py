import unittest, sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) # Parent Dir
from board import Board

class test_board(unittest.TestCase):
	def setUp(self):
		self.board = Board(6, 7)

	def test_printBoard(self):
		self.board.printBoard()

	def test_allows_legal_move(self):
		self.assertTrue(self.board.allowsMove(2))

	def test_allows_out_of_bounds_move(self):
		self.assertFalse(self.board.allowsMove(-1))
		self.assertFalse(self.board.allowsMove(7))

	def test_allows_move_on_full_column(self):
		self.board.dropToken(3, 1)
		self.board.dropToken(3, 1)
		self.board.dropToken(3, 1)
		self.board.dropToken(3, 1)
		self.board.dropToken(3, 1)
		self.board.dropToken(3, 1)
		self.assertFalse(self.board.allowsMove(3))

	def test_legal_drop_token(self):
		self.assertTrue(self.board.dropToken(4, 2))

	def test_drop_token_out_of_bounds(self):
		self.assertFalse(self.board.dropToken(-1, 1))
		self.assertFalse(self.board.dropToken(8, 1))

	def test_drop_token_on_full_column(self):
		self.board.dropToken(5, 1)
		self.board.dropToken(5, 1)
		self.board.dropToken(5, 1)
		self.board.dropToken(5, 1)
		self.board.dropToken(5, 1)
		self.board.dropToken(5, 1)
		self.assertFalse(self.board.dropToken(5,1))

	def test_check_winner_empty(self):
		self.assertEqual(0, self.board.checkWinner())

	def test_check_winner_vertical(self):
		self.board.dropToken(5, 1)
		self.board.dropToken(5, 1)
		self.board.dropToken(5, 1)
		self.board.dropToken(5, 1)
		self.assertEqual(1, self.board.checkWinner())

	def test_check_winner_horizontal(self):
		self.board.dropToken(2, 1)
		self.board.dropToken(3, 1)
		self.board.dropToken(4, 1)
		self.board.dropToken(5, 1)
		self.assertEqual(1, self.board.checkWinner())

	def test_check_winner_diagonal_1(self):
		# Padding
		self.board.dropToken(3, 2)
		self.board.dropToken(4, 2)
		self.board.dropToken(4, 2)
		self.board.dropToken(5, 2)
		self.board.dropToken(5, 2)
		self.board.dropToken(5, 2)
		# Diagonal
		self.board.dropToken(2, 1)
		self.board.dropToken(3, 1)
		self.board.dropToken(4, 1)
		self.board.dropToken(5, 1)

		self.assertEqual(1, self.board.checkWinner())

	def test_check_winner_diagonal_2(self):
		# Padding
		self.board.dropToken(2, 2)
		self.board.dropToken(2, 2)
		self.board.dropToken(2, 2)
		self.board.dropToken(3, 2)
		self.board.dropToken(3, 2)
		self.board.dropToken(4, 2)

		# Diagonal
		self.board.dropToken(2, 1)
		self.board.dropToken(3, 1)
		self.board.dropToken(4, 1)
		self.board.dropToken(5, 1)

		self.assertEqual(1, self.board.checkWinner())
