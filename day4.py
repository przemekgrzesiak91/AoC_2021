#import numpy as np

with open('data/day4.txt') as f:
    data = f.read().split('\n')

def search_num(num, boards):
    for board in boards:
        for row in board:
            if num in row:
                i = row.index(num)
                row[i] = 'x'
                if check_win(board,row, i):
                    i_board = boards.index(board)
                    if i_board in n_board:
                        print(board)
                        print(num, i_board)
                        print(num * sum_board(board))
                        n_board.remove(i_board)

def check_win(board,row, i):
    column = [row[i] for row in board]

    if row == ['x','x','x','x','x'] or column == ['x','x','x','x','x']:
        return 1

def sum_board(board):
    sum = 0

    for row in board:
        for num in row:
            if num != 'x': sum += num
    return sum


numbers = [int(x) for x in data[0].split(',')]
data_boards = data[1:]
boards = []
board = []

for row in data_boards:
    if row == '':
        if board != []: boards.append(board)
        board = []
    else:
        board.append([int(x) for x in row.split(' ') if x != ''])

# 4.1
n_board = list(range(0,99))

for num in numbers:
    search_num(num, boards)


