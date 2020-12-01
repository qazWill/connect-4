import sys
from board import Board
from player import * 
from gui import GUI

def playerSelection(gui):

	lightNum, darkNum = gui.sel_menu()
	
	if lightNum == 0:
		lightPlayer = HumanPlayer(1)
	elif lightNum == 1:
		lightPlayer = RandomComputerPlayer(1)

	if darkNum == 0:
		darkPlayer = HumanPlayer(2)
	elif darkNum == 1:
		darkPlayer = RandomComputerPlayer(2)
	return lightPlayer, darkPlayer

board = Board(6, 7)
gui = GUI()

# sets up players
lightPlayer, darkPlayer = playerSelection(gui)
player = lightPlayer

lightScore = 0
darkScore = 0

# loop for playing multiple games
while True:

	#print board

	# repeat until winner is found
	while board.checkWinner() == 0:

		player.move(board, gui, lightScore, darkScore)

		# switches player for next move
		if player == lightPlayer:
			player = darkPlayer
		else:
			player = lightPlayer

		gui.draw_board(board, player.color, lightScore, darkScore)

	# updates winner
	if board.checkWinner() == 1:
		gui.winner = 1
		lightScore += 1
	elif board.checkWinner() == 2:
		gui.winner = 2
		darkScore += 1
	else:
		gui.winner = -1

	# after game is over show end menu
	# this will have an option to restart or exit
	gui.end_menu(board, lightScore, darkScore)

	# delete old board and make new one
	# in case user wants to play again
	board = Board(6, 7)
	
	# make new player selections
	#lightPlayer = HumanPlayer(1)
	#darkPlayer = RandomComputerPlayer(2)
	player = lightPlayer
