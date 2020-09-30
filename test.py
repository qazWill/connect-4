'''
William was using this to test some functions
'''

from helpers import *

board = init_board()
board[2][0] = 1
board[2][1] = 1
board[2][2] = 1
board[2][3] = 1

print(get_winner(board))

board = init_board()
board[2][0] = 2 
board[3][1] = 2
board[4][2] = 2
board[5][3] = 2


# get winner testing, will delete
print(get_winner(board))
