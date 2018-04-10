import random

from players.player import Player, COLS, ROWS, EMPTY


class DefensivePlayer(Player):

    def compute(self, board):

        if not self.all_moves:  # that's first move
            return 3

        (row_played, col_played, _) = self.all_moves[-1]

        if 2 < row_played < ROWS-1:
            return col_played  # follow suit

        moves = self.get_moves(board)

        # find another column to play
        r = random.randint(0, len(moves)-1)
        return moves[r]


