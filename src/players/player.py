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

    # get available moves as list of column indices
    def get_moves(self, board):
        moves = []
        for col in range(COLS):
            if board[ROWS-1][col] == EMPTY:
                moves.append(col)
        return moves

    # select a legit move as column index
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

    # make a legit move by adding a colored piece to the selected column
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
        return self.check_row(board, color) or self.check_column(board, color) or self.check_diag_up(board, color) or self.check_diag_down(board, color)





