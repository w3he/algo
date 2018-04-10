import random
from players.player import Player


class NovicePlayer(Player):

    def __init__(self, color):
        super().__init__(color)

    def compute(self, board):
        moves = self.get_moves(board)
        if not moves:
            raise Exception("No more legal moves to play.")
        idx = random.randint(0, len(moves)-1)
        return moves[idx]
