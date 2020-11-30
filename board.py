import numpy as np
from helpers import checkConsecutive

# In Board data matrix(list of lists): data[row][col]
# Top row is at index = 0
# leftmost column is at index = 0
class Board:
    def __init__(self, height, width):
        self.width = width
        self.height = height
        # Data location is of the form data[row][col]
        # From top-left
        self.data = []
        self.record = []
        # Creat height x width matrix using nested lists
        for row in range(height):
            boardRow = []
            for col in range(width):
                boardRow.append(0)
            self.data.append(boardRow)

    def __repr__(self):
        s = ""
        for row in self.data:
            s += str(row) + "\n"
        return s

    # Prints board
    def printBoard(self):
        print(self)

    # Check if move is allowed (bounds check and col capacity check)
    def allowsMove(self, col):
        # Check bounds
        if col < 0 or col >= self.width:
            print("Move not allowed: Column", col, "out of Bounds")
            return False
        # Check column capacity
        if self.data[0][col] != 0:
            print("Move not allowed: Column", col, "is full")
            return False
        return True

    # Drop token id (int) into specified column
    def dropToken(self, col, id):
        if self.allowsMove(col):
            self.record.append(col)
            for rowN in range(1, self.height):
                if self.data[rowN][col] != 0:
                    self.data[rowN-1][col] = id
                    return True
            self.data[self.height-1][col] = id
            return True
        # Token could not be dropped (not allowed)
        return False

    # Returns the token id (int) of winner. 
    # A return value of 0 indicates no win
    def checkWinner(self):
        # Check for row of 4
        for row in self.data:
            ret = checkConsecutive(row, 4) # check if row contains 4 consecutive non-zeroes
            if ret != 0:
                return ret
        # Check for column of 4
        for colN in range(self.width):
            aList = []
            for row in self.data:
                aList.append(row[colN])
            ret = checkConsecutive(aList, 4) # check if aList contains 4 consecutive non-zeroes
            if ret != 0:
                return ret
        # Check for diagonal of 4
        arr = np.array(self.data)
        # top-left to bot-right diagonals
        diags = [arr.diagonal(i) for i in range(-self.height+1, self.width)]
        for aList in diags:
            ret = checkConsecutive(aList, 4) # check if aList contains 4 consecutive non-zeroes
            if ret != 0:
                return ret
        # reverse rows, then get top-left to bot-right diagonals
        diags = [arr[::-1, :].diagonal(i) for i in range(-self.height+1, self.width)]
        for aList in diags:
            ret = checkConsecutive(aList, 4) # check if aList contains 4 consecutive non-zeroes
            if ret != 0:
                return ret
		#check for possible move 
        for row in self.data:
            for element in row:
                if element == 0:
                    return 0			
		# its a tie if no possible move found
        return -1 
