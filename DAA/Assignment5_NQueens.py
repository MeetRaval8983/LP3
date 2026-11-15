
# Assignment No. 5: N-Queens Using Backtracking
# Aim: To place N queens on an N x N chessboard so that
# no two queens attack each other, with the first queen fixed.

def print_board(board, n):
    print("\nFinal N-Queens Matrix:")
    for row in range(n):
        print(" ".join(str(board[row][col]) for col in range(n)))


def is_safe(board, row, col, n):
    # Check the same column in previous rows
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve_n_queens(board, row, n):
    # All queens have been placed
    if row == n:
        return True

    # Try each column in the current row
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1

            if solve_n_queens(board, row + 1, n):
                return True

            # Backtrack if this position leads to no solution
            board[row][col] = 0

    return False


def main():
    n = int(input("Enter the value of N: "))

    if n < 1:
        print("N must be at least 1.")
        return

    board = [[0] * n for _ in range(n)]

    # Place the first queen at the top-left corner
    board[0][0] = 1

    print("\nInitial Matrix (first queen fixed at row 1, column 1):")
    for row in board:
        print(" ".join(map(str, row)))

    # Solve by placing the remaining queens
    if solve_n_queens(board, 1, n):
        print_board(board, n)
        print("\nSolution found!")
    else:
        print("\nNo solution exists with the first queen fixed at (1, 1).")


if __name__ == "__main__":
    main()
