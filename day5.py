import re

with open('data/day5.txt') as f:
    data = f.read().split('\n')

def create_board(x):
    board = [[0] * x for _ in range(x)]
    return board

board = create_board(1000)

for row in data:
    row = row.replace('->',',').split(',')
    x1,y1,x2,y2 = [int(x) for x in row]
    #print(x1,y1,x2,y2)
    if x1 == x2:
        if y1 > y2: y1, y2 = y2, y1
        for i in range(y1,y2+1):
            board[i][x1] += 1
    elif y1 == y2:
        if x1>x2: x1,x2 = x2,x1
        for i in range(x1,x2+1):
            board[y1][i] += 1
    else:
        dir_x = 1 if(x2 - x1) > 0 else -1
        dir_y = 1 if(y2 - y1) > 0 else -1

        for i in range(abs(y2-y1)+1):
            new_x, new_y = x1+i*dir_x, y1+i*dir_y
            board[new_y][new_x] += 1

def sum_board(board):
    sum = 0
    for row in board:
        for i in row:
            if i >= 2: sum += 1
    return sum



print(sum_board(board))
