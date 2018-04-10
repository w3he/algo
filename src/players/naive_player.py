from players.player import Player, ROWS, EMPTY


class NaivePlayer(Player):

    def __init__(self, color):
        super().__init__(color)

    def compute(self, board):
        for col in (3, 2, 4, 1, 5, 0, 6):
            for row in range(ROWS):
                if board[row][col] == EMPTY:
                    return col
        raise Exception("No more legal moves to play.")
