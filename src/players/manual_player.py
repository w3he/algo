from players.player import Player, COLS, ROWS, EMPTY


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
