import sys
from connect4_player import Player, NovicePlayer, DefensivePlayer


ROWS = 6
COLS = 7
EMPTY = ' '


def init():
    board = []
    for r in range(ROWS):
        board.append([])
        for c in range(COLS):
            board[r].append(' ')
    return board


def print_board(board):
    for r in range(ROWS):
        row = ROWS - r - 1
        print(row, board[row])


def manual_play(board, color, col):

    if col is not None:
        for r in range(ROWS):
            if board[r][col] == EMPTY:
                board[r][col] = color
                return True  # played
    # no legal move
    return False


def main():
    board = init()
    done = []
    computer = DefensivePlayer('B')
    while not done:
        done = computer.play(board)
        print_board(board)
        if done:
            print("Sorry, you lost.", done)
            break

        # allow three attempts
        for t in range(3):
            try:
                inp = input("Your move [col]:")
                col = int(inp)
                if 0 <= col < COLS:
                    played = manual_play(board, 'R', col)
                    if played:
                        done = computer.check(board, 'R')
                        if done:
                            print("Congrats! You win.", done)
                            break
                    else:
                        print("Invalid move. Please try again...")
                        continue
                    break
                else:
                    print("Invalid move. Please try again...")
                    continue
            except ValueError:
                print("Please enter a number.")

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
