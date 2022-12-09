board = [
    ["5", ".", ".",".", "4", ".", ".", ".", "9"],
    [".", "2", ".", ".", "1", ".", "6", "8", "."],
    [".", ".", "9", "8", "7", ".", "1", ".", "."],
    [".", ".", "6", "7", ".", ".", "2", ".", "."],
    [".", "9", ".", "3", "5", "4", ".", "6", "."],
    ["3", ".", ".", ".", ".", ".", ".", ".", "1"],
    ["9", ".", ".", ".", "6", ".", "8", ".", "2"],
    [".", "1", "4", ".", "3", ".", ".", "5", "7"],
    [".", ".", "5", ".", "8", "7", ".", ".", "."]
]
print(board)
def resolver(board):
    while True:
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    for k in range(1, 10):
                        if str(k) not in board[i]:
                            if str(k) not in [board[x][j] for x in range(9)]:
                                if str(k) not in [board[x][y] for x in range((i//3)*3, (i//3)*3+3) for y in range((j//3)*3, (j//3)*3+3)]:
                                    board[i][j] = str(k)
                                    break
                    else:
                        return False
                    break
            else:
                continue
            break
        else:
            return True
            



                    
resolver_sudoku = resolver(board)
print(resolver_sudoku)


            