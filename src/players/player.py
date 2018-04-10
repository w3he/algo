import random
import copy

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
    def name(self):
        return self.__class__.__name__

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
            col = c - 1
            connected = []
            # row, col both increments
            for row in range(ROWS):
                col += 1
                if col < 0 or col >= COLS:
                    continue
                if board[row][col] == color:
                    connected.append((row, col))
                    if len(connected) == 4:
                        return connected
                elif connected:
                    connected = []  # reset
            if connected and color == self.color:
                self.add_results(connected)

        # check diagonal - DOWN
        # start from middle lower, ends two-off to include down line ends in (2,6) position
        for c in range(3, COLS + 2):
            connected = []
            col = c + 1
            # row increments, while col decrements
            for row in range(ROWS):
                col -= 1
                if row < 0 or col >= COLS:
                    continue

                if board[row][col] == color:
                    connected.append((row, col))
                    if len(connected) == 4:
                        return connected
                elif connected:
                    connected = []  # reset
            if connected and color == self.color:
                self.add_results(connected)

        return None

    def print_board(self, board):
        for r in range(ROWS):
            row = ROWS - r - 1
            print(row, board[row])
        print("")


class NovicePlayer(Player):

    def __init__(self, color):
        super().__init__(color)

    def compute(self, board):
        moves = self.get_moves(board)
        if not moves:
            raise Exception("No more legal moves to play.")
        idx = random.randint(0, len(moves)-1)
        return moves[idx]


class NaivePlayer(Player):

    def __init__(self, color):
        super().__init__(color)

    def compute(self, board):
        for col in (3, 2, 4, 1, 5, 0, 6):
            for row in range(ROWS):
                if board[row][col] == EMPTY:
                    return col
        raise Exception("No more legal moves to play.")


class DefensivePlayer(Player):

    _board = None

    def get_last_move(self, board):
        if self._board:
            for r in range(ROWS, 0, -1):
                row = r - 1
                for col in range(0, COLS):
                    if self._board[row][col] != board[row][col]:
                        return row, col
        else:
            return 0, 3

    def check(self, board, color):
        if color == self.color:  # remember the board as I played
            self._board = copy.deepcopy(board)
        return super().check(board, color)

    def compute(self, board):
        (row_payed, col_played) = self.get_last_move(board)

        moves = self.get_moves(board)
        for col in moves:
            if col == col_played:
                # play like a copycat
                return col_played

        for col in moves:
            if row_payed > 0:
                if board[row_payed][col] == EMPTY and board[row_payed-1][col] != EMPTY:
                    return col
            elif board[row_payed][col] == EMPTY:
                return col

        # find another column to play
        r = random.randint(0, len(moves)-1)
        return moves[r]


class ManualPlayer(Player):

    def __init__(self, color, name="You"):
        super().__init__(color)
        self._name = name

    @property
    def name(self):
        return self._name

    def play(self, board):
        for t in range(3):
            try:
                inp = input("Your move [col]:")
                col = int(inp)
                if 0 <= col < COLS:
                    played = self.manual_play(board, col)
                    if played:
                        done = self.check(board, self.color)
                        if done:
                            print("Congrats! You win.", done)
                            return done
                        break  # no need to retry
                    else:
                        print("Invalid move. Please try again...")
                else:
                    print("Invalid move. Please try again...")
            except ValueError:
                print("Please enter a number.")

        return None

    def manual_play(self, board, col):

        if col is not None:
            for r in range(ROWS):
                if board[r][col] == EMPTY:
                    board[r][col] = self.color
                    return True  # played
        # no legal move
        return False


