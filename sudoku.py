import sys
import time

N = 9


def get_nset():
    nums = set()
    for n in range(1, N+1):
        nums.add(n)
    return nums


def is_acceptable(row):
    count = set()
    for n in row:
        if n and n not in count:
            count.add(n)
        elif n and n in count:
            return False
    return True


def get_empty(sudoku):
    for r in range(N):
        for c in range(N):
            if not sudoku[r][c]:
                return r, c
    return None


def get_missing(row):
    vals = get_nset()
    for n in row:
        if n:
            vals.remove(n)
    return vals


def get_column(sudoku, c):
    column = []
    for r in range(N):
        column.append(sudoku[r][c])
    return column


def get_square(sudoku, row, col):
    row = int(row / 3) * 3
    col = int(col / 3) * 3
    square = []
    for r in range(int(N/3)):
        for c in range(int(N/3)):
            square.append(sudoku[row + r][col + c])
    return square


def print_solution(sudoku):

    for r in range(len(sudoku)):
        if r > 0 and not r % 3:
            print("-" * 27)
        for s in (0, 3, 6):
            print(sudoku[r][s:s+3], end="")
        print("")


depth = []


def solve(sudoku):
    depth.append(len(depth) +1)

    print("")
    print(depth)
    print_solution(sudoku)
    print("")
    time.sleep(.25)

    empty = get_empty(sudoku)
    if not empty:
        return True
    r, c = empty

    # get a list of numbers not in the row
    vals = get_missing(sudoku[r])
    for v in vals:
        sudoku[r][c] = v
        # check to see if it will collide in column or small 3x3 square
        if is_acceptable(get_column(sudoku, c)) and is_acceptable(get_square(sudoku, r, c)):
            if solve(sudoku):
                return True
    sudoku[r][c] = 0
    depth.pop()
    return False


def main():
    sudoku = [
        [3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]
    ]

    solve(sudoku)
    print_solution(sudoku)


if __name__ == "__main__":
    sys.exit(int(main() or 0))
