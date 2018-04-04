import sys

maze = [
    [1, 1, 1, 1, 1, 0, 1],
    [0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0],
    [1, 0, 1, 1, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1]
]

ROWS = len(maze)
COLS = len(maze[0])


def check_next(r, c, visited):
    return 0 <= c < COLS and 0 <= r < ROWS and maze[r][c] and (r, c) not in visited


def solve(moves, path, visited):
    for (r, c) in moves:

        if c == COLS - 1 and r == ROWS - 1:  # reaching exit
            path.append((r, c))
            return True

        visited.append((r, c))

        next_moves = []
        if check_next(r, c + 1, visited):  # right
            next_moves.append((r, c + 1))
        if check_next(r + 1, c, visited):  # down
            next_moves.append((r + 1, c))
        if check_next(r, c - 1, visited):  # left
            next_moves.append((r, c - 1))
        if check_next(r - 1, c, visited):  # up
            next_moves.append((r - 1, c))

        if next_moves:
            path.append((r, c))
            result = solve(next_moves, path, visited)
            if result:
                return True
    # back tracking
    path.pop()
    return False


def print_path(path, visited):
    for r in range(ROWS):
        for c in range(COLS):
            if not maze[r][c]:
                print(" o", end='')
            elif (r, c) in path:
                print(" -", end='')
            elif (r, c) in visited:
                print(" *", end='')
            else:
                print("  ", end='')
        print('')


def main():
    visited = []
    path = []
    moves = [(0, 0)]
    solve(moves, path, visited)

    print_path(path, visited)


if __name__ == "__main__":
    sys.exit(int(main() or 0))
