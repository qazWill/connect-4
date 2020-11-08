from board import Board
from player import * 
from gui import GUI

board = Board(6, 7)
gui = GUI()

# sets up players
lightPlayer = HumanPlayer(1)
#darkPlayer = HumanPlayer(2)
darkPlayer = RandomComputerPlayer(2)
player = lightPlayer

# repeat until winner is found
while board.checkWinner() == 0:

	player.move(board, gui)

	# switches player for next move
	if player == lightPlayer:
		player = darkPlayer
	else:
		player = lightPlayer

	gui.draw_board(board, player.color)

# after game is over show end menu
# this will have an option to restart or exit
gui.end_menu(board)
