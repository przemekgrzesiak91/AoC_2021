
with open ('data/day1.txt') as f:
    data = f.read().split('\n')

data = [int(x) for x in data]

def count_increased(data):
    n_incresead = 0
    start = data[0]
    
    for i in range(1,len(data)):
        if data[i] > start: n_incresead += 1
        start = data[i]

    return n_incresead

# 1.1

print(count_increased(data))

# 1.2
#data = [1,1,1,2,2,2,3,3,3]
new_data = []

for i in range(2,len(data)):
    new_data.append((data[i-2]+data[i-1]+data[i]))

print(count_increased(new_data))