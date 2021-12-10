
with open('data\day10.txt') as f:
    data = f.read().split('\n')

close_chunks = [')',']','}','>']
pairs = {')' : ['(',3],
         ']' : ['[',57],
         '}' : ['{',1197],
         '>' : ['<',25137]}

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

print(sum)







