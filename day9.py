
with open('data/day9.txt') as f:
    data = f.read().split('\n')

#poprawić wczytanie
for i in range(0,len(data)):
    data[i] = list(map(int,data[i]))

n = len(data)
m = len(data[0])

low_points = []

def basin(data,x,y):
    #print('start',x,y)
    visited = []
    to_check = [[x,y]]
    n_to_check = 1

    while to_check:
        current = to_check.pop(0)
        c_x, c_y = current
        if current not in visited:
            visited.append(current)

            if c_x-1 >= 0 and data[c_x-1][c_y] < 9 and [c_x-1,c_y] not in visited and [c_x-1,c_y] not in to_check:
                to_check.append([c_x-1,c_y])
                n_to_check += 1
            if c_x+1 <= n-1 and data[c_x+1][c_y] < 9 and [c_x+1,c_y] not in visited and [c_x+1,c_y] not in to_check:
                to_check.append([c_x+1,c_y])
                n_to_check += 1
            if c_y-1 >= 0 and data[c_x][c_y-1] < 9 and [c_x,c_y-1] not in visited and [c_x,c_y-1] not in to_check:
                to_check.append([c_x,c_y-1])
                n_to_check += 1
            if c_y+1 <= m-1 and data[c_x][c_y+1] < 9 and [c_x,c_y+1] not in visited and [c_x,c_y+1] not in to_check:
                to_check.append([c_x,c_y+1])
                n_to_check += 1

    return(n_to_check)


basins = []

for i in range(0,n):
    for j in range(0,m):

        value = data[i][j]
        cond = 0
        if i-1 >= 0 and data[i-1][j] <= value: cond += 1
        if i+1 <= n-1 and data[i+1][j] <= value: cond += 1
        if j-1 >= 0 and data[i][j-1] <= value: cond += 1
        if j+1 <= m-1 and data[i][j+1] <= value: cond += 1

        if cond == 0:
            basins.append(basin(data, i, j))

            low_points.append(value)

print(sum([x+1 for x in low_points]))

result = 1
for x in range(3):
    a = max(basins)
    basins.remove(a)
    result *= a

print(result)


