import sys
import players
import argparse
import time

from players import *


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
    board = []
    for r in range(ROWS):
        board.append([])
        for c in range(COLS):
            board[r].append(' ')
    return board


def select_player(name, color):
        return {
            'Novice': NovicePlayer(color),
            'Defensive': DefensivePlayer(color),
            'Naive': NaivePlayer(color)
        }.get(name, ManualPlayer(color, name))


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
