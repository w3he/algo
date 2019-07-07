import sys
import argparse
import time

from players import *

ROWS = 6
COLS = 7
EMPTY = ' '
connections = {'Y': [], 'R': []}


def parse_args():
    """Parse the command-line arguments."""
    parser = argparse.ArgumentParser()

    parser.add_argument('--player1', '-1',
                        help='specify first player name',
                        default="Novice")
    parser.add_argument('--player2', '-2',
                        help='specify second player name',
                        default="")
    parser.add_argument("-v", "--version",
                        action='store_true',
                        help="Print app version and exit")

    return parser.parse_args()


def init():
    # 2-D matrix as array or arrays
    board = []
    for r in range(ROWS):
        board.append([])
        for c in range(COLS):
            board[r].append(EMPTY)
    return board


def select_player(name, color):
    return {
        'Novice': NovicePlayer(color),
        'Defensive': DefensivePlayer(color),
        'Naive': NaivePlayer(color)
    }.get(name, ManualPlayer(color, name))


def add_blank(row, col, connect):
    if not connect or connect[-1] != EMPTY:
        connect.append((row, col, EMPTY))
    elif connect[0] == EMPTY:
        connect[0] = (row, col, EMPTY)


def play(board, color, col):
    my_row = 0
    for row in range(ROWS):
        if board[row][col] == EMPTY:
            my_row = row
            break

    for connection in connections:



    def check_row(self, board, color):
        # check for 2s with open ends, and 3s with one end open
        connect_rows = {}
        for row in range(ROWS):
            myConnect = []
            connect = []
            for col in range(COLS):
                if board[row][col] == EMPTY:
                    self.add_blank(row, col, connect)
                    self.add_blank(row, col, myConnect)
                elif board[row][col] == color:
                    pass
                elif board[row][col] != color:
                    connect.append((row, col))
                    if len(connect) == 4:
                        return connect
                elif connect:  # horizontally, empty means interrupt
                    connect = []  # reset
            if connect and color == self.color:
                self.add_results(connect)
        return None

    def check_column(self, board, color):
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
        return None

    def check_diag_up(self, board, color):
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
        return None

    def check_diag_down(self, board, color):
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

def main():

    args = parse_args()

    board = init()
    done = []
    while not done:
        for player in (select_player(args.player1, "Y"), select_player(args.player2, "R")):
            time.sleep(.25)
            done = player.play(board)
            if done:
                print("Congrats, you win.", player.name, player.color)
                break
            else:
                player.print_board(board)

    # print final results
    for r in range(ROWS):
        row = ROWS - r - 1
        print(board[row])
        for col in range(COLS):
            if (row, col) in done:
                print("  ^  ", end="")
            else:
                print("     ", end="")
        print("")


if __name__ == "__main__":
    sys.exit(int(main() or 0))
