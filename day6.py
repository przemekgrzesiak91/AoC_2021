
with open('data/day6.txt') as f:
    data = f.read().split(',')
data = [int(x) for x in data]

def count_fishes(data,days):
    counter = {0:0, 1:0, 2:0, 3:0, 4:0,
               5:0, 6:0, 7:0, 8:0}

    for i in data:
        counter[i] += 1
    print(data)
    while days > 0:
        print(counter)
        counter_list = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for key, value in counter.items():
            if key == 0:
                counter_list[6] += value
                counter_list[8] += value
            else:
                counter_list[key - 1] += value

        for i in range(0,len(counter_list)):
            counter[i] = counter_list[i]
        days -= 1

    sum = 0
    for key,value in counter.items():
        sum += value

    return sum




# Day 6.1
print(count_fishes(data,80))
# Day 6.2
print(count_fishes(data,256))