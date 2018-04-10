import random

ROWS = 6
COLS = 7
EMPTY = ' '


class Player:

    _color = None
    _results = ([], [], [])
    _all_moves = []

    def __init__(self, color):
        self._color = color

    @property
    def color(self):
        return self._color

    @property
    def name(self):
        return self.__class__.__name__

    @property
    def all_moves(self):
        return self._all_moves

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
                self._all_moves.append((row, col, self.color))
                return self.check(board, self.color)

        raise Exception("No more legal moves. It's a DRAW!")

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
                elif connected:  # horizontally, empty means interrupt
                    connected = []  # reset
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
                elif board[row][col] == EMPTY:  # vertically, empty means top
                    break
            if connected and color == self.color:
                self.add_results(connected)

        # check diagonal - UP
        # start from one off from lower left corner
        # we need two-off to for up diagonal line starting (2,0) position
        for c in range(-2, 4):
            col = c
            connected = []
            # row, col both increments
            for row in range(ROWS):
                if 0 <= col < COLS and board[row][col] == color:
                    connected.append((row, col))
                    if len(connected) == 4:
                        return connected
                elif connected:
                    connected = []  # reset
                col += 1

            if connected and color == self.color:
                self.add_results(connected)

        # check diagonal - DOWN
        # start from middle lower, ends two-off to include down line ends in (2,6) position
        for c in range(3, COLS + 2):
            connected = []
            col = c
            # row increments, while col decrements
            for row in range(ROWS):
                if 0 <= col < COLS and board[row][col] == color:
                    connected.append((row, col))
                    if len(connected) == 4:
                        return connected
                elif connected:
                    connected = []  # reset
                col -= 1

            if connected and color == self.color:
                self.add_results(connected)

        return None

    def print_board(self, board):
        for r in range(ROWS):
            row = ROWS - r - 1
            print(row, board[row])
        print("")




