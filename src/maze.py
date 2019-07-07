from __future__ import print_function
import sys

N = 6
maze = [
    [1, 1, 1, 0, 1, 1],
    [0, 1, 0, 0, 1, 0],
    [1, 1, 1, 0, 1, 0],
    [1, 0, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0],
    [1, 1, 1, 1, 1, 1]
]


def solve(moves, visited, path):

    for (r, c) in moves:
        visited.append((r, c))

        next_moves = []
        if c < N-1 and (r, c+1) and maze[r][c+1]:
            next_moves.append((r, c+1))
        if r < N-1 and (r+1, c) not in visited and maze[r+1][c]:
            next_moves.append((r+1, c))
        if c > 0 and (r, c-1) not in visited and maze[r][c-1]:
            next_moves.append((r, c-1))
        if r > 0 and (r-1, c) not in visited and maze[r-1][c]:
            next_moves.append((r-1, c))
        if next_moves:
            path.append((r, c))
            result = solve(next_moves, visited, path)
            if result:
                return True
        elif c == N-1 and r == N-1:
            path.append((r, c))
            return True
    path.pop()
    return False


def print_path(path, visited):
    for r in range(N):
        for c in range(N):
            if not maze[r][c]:
                print(" o", end='')
            elif (r, c) in path:
                print(" -", end='')
            elif (r, c) in visited:
                print(" *", end='')
            else:
                print(" 1", end='')
        print('')


def main():
    visited = []
    path = []
    moves = [(0, 0)]
    solve(moves, visited, path)

    print_path(path, visited)

if __name__ == "__main__":
    sys.exit(int(main() or 0))