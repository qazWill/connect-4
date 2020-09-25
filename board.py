class Board:
#adds board
   def __init__(self, width, height):
        self.width = width
        self.height = height
        self.data = [] 
    
        for row in range( self.height ):
            boardRow = []
            for col in range( self.width ):
                boardRow += [' ']
            self.data += [boardRow]
        
        
def __repr__(self):
        s = ''
        for row in range( self.height ):
            s += '|'
            for col in range( self.width ):
                s += self.data[row][col] + '|'
            s += '\n'
            
        s += '--'*self.width + '-\n'
        
        for col in range( self.width ):
            s += ' ' + str(col % 10)
        s += '\n'
        
        return s

# TODO: compare diff with __repr__
def printBoard(self):
	s = ''
	for row in self.data:
		for entry in row:
			print("|" + str(entry))
		print("|\n")
                                    
def addMove( self,col,ox ):
        if self.allowsMove(col):
            for row in range( self.height ):
                if self.data[row][col] != ' ':
                    self.data[row-1][col] = ox
                    return
            self.data[self.height-1][col] = ox #if empty column, place piece at the bottom
#check if move is allowed,
def allowsMove( self,col ):
        if 0 <= col < self.width:
            return self.data[0][col] == ' '
        else:
            print "try a valid number"

def getWinner(self):	

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
				
		
#move

#check for valid move
#print board
