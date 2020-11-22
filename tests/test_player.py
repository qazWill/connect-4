import unittest, sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) # Parent Dir
from board import Board
from player import * 
from gui import GUI

class test_computer_player(unittest.TestCase):
	def setUp(self):
		self.board = Board(6, 7)
		self.gui = GUI()
		self.humanPlayer = HumanPlayer(1)
		self.randomComputerPlayer = RandomComputerPlayer(2)

	def test_random_computer_move(self):
		self.randomComputerPlayer.move(self.board, 
			self.gui, self.humanPlayer, self.randomComputerPlayer)
		self.assertNotEqual(Board(6, 7), self.board)