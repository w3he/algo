import sys

# board dimension
N = 4


def is_safe(q, queens):
    """ test new q against placed ones """
    l = len(queens)
    for r in range(l):
        c = queens[r]
        if q == c:  # same column
            return False
        elif abs(l-r) == abs(q-c):  # diagonal
            return False
    return True


def solve(queens):
    if len(queens) == N:
        return True  # we are done
    for c in range(N):
        if is_safe(c, queens):
            queens.append(c)
            if solve(queens):
                return True
            queens.pop()
    return False


def print_solution(queens):
    for r in range(N):
        print(" ." * queens[r], "Q", ". " * (N - queens[r] -1))


def main():
    solutions = []
    for r in range(N):
        queens = [r]
        if solve(queens):
            solutions.append(queens)

    print("There may be {0} valid solution(s) for {1}".format(len(solutions), N))

    for n in range(len(solutions)):
        print("sol: ", n)
        print_solution(solutions[n])

if __name__ == "__main__":
    sys.exit(int(main() or 0))
