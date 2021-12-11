
with open('data\day10.txt') as f:
    data = f.read().split('\n')

close_chunks = [')',']','}','>']
pairs = {')' : ['(',3,1],
         ']' : ['[',57,2],
         '}' : ['{',1197,3],
         '>' : ['<',25137,4]}
pairs2 = {'(' : 1,
         '[' : 2,
         '{' : 3,
         '<' : 4}

incomplete = []
sum = 0
for row in data:
    row = list(row)
    checked = []
    cond = True

    while cond:
        cond = False
        for i in range(0,len(row)):
            if row[i] in close_chunks:
                cond = True
                if pairs[row[i]][0] == row[i-1]:
                    row.pop(i)
                    row.pop(i-1)
                    break
                else:
                    sum += pairs[row[i]][1]
                    cond = False
                    break
            if i == len(row) - 1:
                incomplete.append(row)
print(sum)


sum2 = []
for row in incomplete:
    #print(row[::-1])
    sum = 0
    for chunk in row[::-1]:
        sum *= 5
        sum += pairs2[chunk]
    sum2.append(sum)

middle = int(len(sum2)/2)
sum2 = sorted(sum2)
print(sum2[middle])







