print("N-Queen Problem")

def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 1:
            return False

    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def solve_nqueen(board, row, n):
    if row == n:
        for i in board:
            print(i)
        return True

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            if solve_nqueen(board, row+1, n):
                return True
            board[row][col] = 0
    return False

n = 4
board = [[0]*n for i in range(n)]
solve_nqueen(board, 0, n)