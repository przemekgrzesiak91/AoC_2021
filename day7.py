
with open('data/day7.txt') as f:
    data = f.read().split(',')


print(data)
data = [int(x) for x in data]

n_pos = len(data)

# 7.1
sum_move1 = []
sum_move2 = []

for i in range(0,n_pos):
    cost1 = [abs(x-i) for x in data]
    cost2 = [sum(range(1,abs(x-i)+1)) for x in data]
    sum_move1.append(sum(cost1))
    sum_move2.append(sum(cost2))
print(min(sum_move1))
print(min(sum_move2))


