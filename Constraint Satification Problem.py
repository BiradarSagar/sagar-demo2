def is_safe(board, row, col, n):
    for i in range(row):
        if board[i] == col or \
           abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve_nqueens(board, row, n, solutions):
    if row == n:
        solutions.append(board.copy())
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve_nqueens(board, row + 1, n, solutions)
            board[row] = -1  # backtrack

def print_solution(board):
    n = len(board)
    for row in board:
        print(" ".join("Q" if i == row else "." for i in range(n)))
    print()

def n_queens(n):
    board = [-1] * n
    solutions = []
    solve_nqueens(board, 0, n, solutions)
    for solution in solutions:
        print_solution(solution)
    print(f"Total solutions: {len(solutions)}")

# Example usage
n = 8
n_queens(n)
