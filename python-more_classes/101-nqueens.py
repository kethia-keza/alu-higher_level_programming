#!/usr/bin/python3
"""
N Queens Problem Solver

Finds and prints all valid solutions for placing N non-attacking queens
on an N x N chessboard using backtracking.
"""
import sys


def print_usage_and_exit():
    """Prints usage error message and exits with status 1."""
    print("Usage: nqueens N")
    sys.exit(1)


def parse_args():
    """
    Validates command-line arguments.

    Returns:
        int: The size of the board N if valid.
    """
    if len(sys.argv) != 2:
        print_usage_and_exit()

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    return n


def solve_nqueens(n, row, cols, pos_diag, neg_diag, board):
    """
    Recursive helper function that places queens using backtracking.

    Args:
        n (int): Board dimensions (N x N).
        row (int): Current row being evaluated.
        cols (set): Set of columns already occupied.
        pos_diag (set): Set of positive diagonals (row + col) under attack.
        neg_diag (set): Set of negative diagonals (row - col) under attack.
        board (list): Current list of queen coordinates [[r, c], ...].
    """
    if row == n:
        print(board)
        return

    for col in range(n):
        if col in cols or (row + col) in pos_diag or (row - col) in neg_diag:
            continue

        # Place queen
        cols.add(col)
        pos_diag.add(row + col)
        neg_diag.add(row - col)
        board.append([row, col])

        # Recurse to next row
        solve_nqueens(n, row + 1, cols, pos_diag, neg_diag, board)

        # Backtrack (remove queen)
        cols.remove(col)
        pos_diag.remove(row + col)
        neg_diag.remove(row - col)
        board.pop()


def main():
    """Main execution function."""
    n = parse_args()
    solve_nqueens(n, 0, set(), set(), set(), [])


if __name__ == "__main__":
    main()
