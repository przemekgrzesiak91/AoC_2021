pos = []
instructions = []

with open('data\day13.txt') as f:
    x = 1
    for line in f:
        if line == '\n': x = 0
        elif x: pos.append(line.strip().split(','))
        elif not x: instructions.append(line.strip())

max_x = max([int(x[0]) for x in pos ]) +1
# change this !
max_y = max([int(y[1]) for y in pos ]) +6
# !!
print(max_x, max_y)

paper = [['.'] * max_x for _ in range(max_y)]
for row in pos:
    x,y = int(row[0]), int(row[1])
    paper[y][x] = '#'



def print_paper(paper):
    for line in paper:
        line = ''.join(line)
        print(line)

def count(paper):
    sum = 0
    for row in paper:
        for x in row:
            if x == "#": sum+=1
    print(sum)

#folds
for fold in instructions:
    #print_paper(paper)
    how,value = fold.split(' ')[2].split('=')
    value = int(value)
    print('-----')
    print(how,value)
    print('max',max_x,max_y)
    if how == 'x':
        new_paper = [['.'] * (value) for _ in range(max_y)]
        for j in range(max_y-1,-1,-1):
            for i in range(value-1,-1,-1):
                #print(i, max_x-1-i,j)
                if paper[j][i] == '#' or paper[j][max_x-1-i] == '#' and i != max_x-1-i:
                    new_paper[j][i] = '#'
                else:
                    new_paper[j][i] = ' '
        paper = new_paper
        max_x = value
    elif how == 'y':
        new_paper = [['.'] * max_x for _ in range(value)]
        for j in range(value-1,-1,-1):
            for i in range(max_x-1,-1,-1):
                #print(j, max_y-1-j, i)
                if paper[j][i] == '#' or paper[max_y-1-j][i] == '#' and j != max_y-1-j:
                    new_paper[j][i] = '#'
                else:
                    new_paper[j][i] = ' '
        paper = new_paper
        max_y = value
    count(paper)

print_paper(paper)