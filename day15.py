
with open('data\day15.txt') as f:
    board = (f.read().split('\n'))

for i in range(0,len(board)):
    board[i] = list(map(int,board[i]))

x,y = 0,0
end_x,end_y = len(board)-1,len(board[0])-1

while x != end_x and y != end_y:
    board[x][y] = 0
    if y+1 <= end_y:
        right = board[x][y+1]
    if x+1 <= end_x:
        down = board[x+1][y]
    print(right,down)
    if right < down:
        y = y+1
    else:
        x = x+1

for row in board:
    print(row)