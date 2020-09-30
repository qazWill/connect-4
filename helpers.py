'''
This module will contain useful functions classes
for use in the connect 4 game

'''

# Returns whether there are n consecutive non-zero tokens
# Returns token id (int) if found, else returns 0
def checkConsecutive(aList, n):
    if len(aList) < n:
        return 0
    # Set 1st element as prev
    count = 1
    prev = aList[0]  
    for i in range(1, len(aList)):
        curr = aList[i]
        if curr == 0:
            count = 0
        elif prev != curr:
            count = 1
        else:
            count += 1
        # Check Count
        if count >= n:
            return prev
        # Set new prev
        prev = curr
    return 0


# returns winner if found
# returns 0 if no winner is found
def get_winner(board):
		

	# checks for row of 4
	for y in range(0, 6):
		count = 0
		target = 1
		for x in range(0, 7):
			if board[x][y] == 0:
				count = 0
			elif board[x][y] == target:
				count += 1
			else:
				count = 1
				target = board[x][y]

			if count == 4:
				return target

	# checks for column of 4
	for x in range(0, 7):
		count = 0
		target = 1
		for y in range(0, 6):
			if board[x][y] == 0:
				count = 0
			elif board[x][y] == target:
				count += 1
			else:
				count = 1
				target = board[x][y]

			if count == 4:
				return target

	# checks for diagonal of 4
	for x_start in range(0, 7):
		for y_start in range(0, 6):
			
			x = x_start
			y = y_start	
			target = board[x][y]
			
			# skip 0's
			if target == 0:
				continue

			found = True
			for i in range(0, 3):
				x += 1
				y += 1
				if x >= 7 or y >= 6 or board[x][y] != target:
					found = False
					break
			
			if found:
				return target

			x = x_start
			y = y_start	
			target = board[x][y]
			found = True
			for i in range(0, 3):
				x += 1
				y -= 1
				if x >= 7 or y < 0 or board[x][y] != target:
					found = False
					break

			if found:
				return target

	# return 0 if no 4 in a row was found
	return 0					




# initializes board with blank spaces
# 0 represents blank space
# 1 represents red occupation
# 2 represents black occupation
# board[x][y], x is column, y is row
# feel free to flip these coords if it feels weird
def init_board():
	board = []
	for x in range(0, 7): # 7 columns
		board.append([])
		for y in range(0, 6): # 6 rows
			board[-1].append(0)
	return board

