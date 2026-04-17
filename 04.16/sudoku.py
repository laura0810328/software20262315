dic = {}
puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

def is_valid(h, v, key, puzzle):
    dic[key] = [1,2,3,4,5,6,7,8,9]

    for i in range(9):
        if puzzle[h][i] in dic[key]:
            dic[key].remove(puzzle[h][i])
        if puzzle[i][v] in dic[key]:
            dic[key].remove(puzzle[i][v])

    nh = (h // 3) * 3
    nv = (v // 3) * 3

    for i in range(3):
        for j in range(3):
            if puzzle[nh+i][nv+j] in dic[key]:
                dic[key].remove(puzzle[nh+i][nv+j])

    return dic[key]


def solve_sudoku(n, m, board):
    if m == 9:
        return solve_sudoku(n+1, 0, board)
    if n == 9:
        return True

    if board[n][m] != 0:
        return solve_sudoku(n, m+1, board)

    key = n*10 + m
    candidates = is_valid(n, m, key, board)

    for num in candidate:
        board[n][m] = num

        if solve_sudoku(n, m+1, board):
            return True
        board[n][m] = 0

    return False

def print_board(board):
    for i in board:
        print(i)

if solve_sudoku(0, 0, puzzle)!=False:
    print_board(puzzle)
else:
    print("해답을 찾을 수 없습니다.")
