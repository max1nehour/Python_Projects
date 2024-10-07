def check(board, row, col, num):
    if num in board[row]:
        return False
    if num in [board[i][col] for i in range(4)]:
        return False
    row_0, col_0 = 2 * (row // 2), 2 * (col // 2)
    for i in range(row_0, row_0 + 2):
        for j in range(col_0, col_0 + 2):
            if board[i][j] == num:
                return False
    
    return True

def solve(board):
    for row in range(4):
        for col in range(4):
            if board[row][col] == 0:
                for num in range(1, 5):
                    if check(board, row, col, num):
                        board[row][col] = num
                        if solve(board):
                            return True
                        board[row][col] = 0 
                return False
    return True

def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))


board = []
for i in range(4):
    row = list(map(int, input().split())) 
    board.append(row) 
solve(board)
print_board(board)
