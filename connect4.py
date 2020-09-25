class connect4:
    def __init__(self, height=6, width=7):
        self.height = height
        self.width = width
        self.board = [['' for x in range(width)] for i in range(height)]

    def return_board(self):
        return self.board

    def get_column(self, index):
        return [i[index] for i in self.board]

    def get_row(self, index):
        return self.board[index]

    def get_diagonals(self):
        diagonals = []
        for p in range(self.height + self.width - 1):
            diagonals.append([])
            for q in range(max(p - self.height + 1, 0),
                           min(p + 1, self.height)):
                diagonals[p].append(self.board[self.height - p + q - 1][q])
        for p in range(self.height + self.width - 1):
            diagonals.append([])
            for q in range(max(p - self.height + 1, 0),
                           min(p + 1, self.height)):
                diagonals[p].append(self.board[p - q][q])
        return diagonals

    def make_move(self, team, col):
        if '' not in self.get_column(col):
            return self.board
        i = self.height - 1
        while self.board[i][col] != '':
            i -= 1
        self.board[i][col] = team
        return self.board

    def check_win(self):
        for i in range(self.height):  # check rows
            for x in range(self.width - 3):
                if self.get_row(i)[x:x + 4] in [['0', '0',
                                                 '0', '0'], ['1', '1', '1', '1']]:
                    return self.board[i][x]
        for i in range(self.width):  # check columns
            for x in range(self.height - 3):
                if self.get_column(
                        i)[x:x + 4] in [['0', '0', '0', '0'], ['1', '1', '1', '1']]:
                    return self.board[x][i]
        for i in self.get_diagonals():
            for x in range(len(i)):
                if i[x:x + 4] in [['0', '0', '0', '0'], ['1', '1', '1', '1']]:
                    return i[x]

        return None