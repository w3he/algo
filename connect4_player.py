import random

ROWS = 6
COLS = 7
EMPTY = ' '


class Player:

    _color = None
    _results = ([], [], [])

    def __init__(self, color):
        self._color = color

    @property
    def color(self):
        return self._color

    @property
    def results(self):
        return self._results

    @results.setter
    def results(self, value):
        if value is not None:
            self._results = value

    def reset_results(self):
        self.results = ([], [], [])

    def get_moves(self, board):
        moves = []
        for col in range(COLS):
            if board[ROWS-1][col] == EMPTY:
                moves.append(col)
        return moves

    def compute(self, board):
        moves = self.get_moves(board)
        if not moves:
            raise Exception("No more legit moves")
        for key in (2, 1, 0):
            for result in self.results[key]:
                for row, col in result:
                    if col in moves:
                        return col

        idx = random.randint(0, len(moves) - 1)

        # print(idx, len(moves))

        return moves[idx]

    def play(self, board):
        # reset previous results
        self.reset_results()
        col = self.compute(board)
        for row in range(ROWS):
            if board[row][col] == EMPTY:
                board[row][col] = self.color
                return self.check(board, self.color)

        # No more legal moves
        raise Exception("It's a DRAW")

    def add_results(self, result):
        l = len(result)
        if not l:
            return
        self.results[l-1].append(result)

    def check(self, board, color):
        # do we have 4 in a row
        for row in range(ROWS):
            connected = []
            for col in range(COLS):
                if board[row][col] == color:
                    connected.append((row, col))
                    if len(connected) == 4:
                        return connected
                elif board[row][col] != EMPTY and connected:
                    connected = []  # reset
                elif board[row][col] == EMPTY:
                    break
            if connected and color == self.color:
                self.add_results(connected)

        # do we have 4 in a column
        for col in range(COLS):
            connected = []
            for row in range(ROWS):
                if board[row][col] == color:
                    connected.append((row, col))
                    if len(connected) == 4:
                        return connected
                elif board[row][col] != EMPTY and connected:
                    connected = []  # reset
                elif board[row][col] == EMPTY:
                    break
            if connected and color == self.color:
                self.add_results(connected)

        # check diagonal - UP
        # row, col both increments
        for c in range(1 + COLS // 2):
            col = c - 1
            connected = []
            for row in range(ROWS):
                col += 1
                if col >= COLS:
                    continue
                if board[row][col] == color:
                    connected.append((row, col))
                    if len(connected) == 4:
                        return connected
                elif board[row][col] != EMPTY and connected:
                    connected = []  # reset
                elif board[row][col] == EMPTY:
                    break
            if connected and color == self.color:
                self.add_results(connected)

        # check diagonal - DOWN
        # row decrements while col increments
        for c in range(1 + COLS // 2):
            connected = []
            col = c - 1
            row = ROWS
            for r in range(ROWS):
                row -= 1
                col += 1
                if row < 0 or col >= COLS:
                    continue

                if board[row][col] == color:
                    connected.append((row, col))
                    if len(connected) == 4:
                        return connected
                elif board[row][col] != EMPTY and connected:
                    connected = []  # reset
                elif board[row][col] == EMPTY:
                    break
            if connected and color == self.color:
                self.add_results(connected)

        return None
