
with open('data/day2.txt') as f:
    data = f.read().split('\n')

def calc_pos(data):

    h_pos = 0
    depth = 0

    for row in data:
        direction,value = row.split(' ')
        if direction == 'forward': h_pos += int(value)
        elif direction == 'down': depth += int(value)
        elif direction == 'up': depth -= int(value)

    return h_pos*depth

print(calc_pos(data))

#2.2
def calc_pos2(data):

    h_pos = 0
    depth = 0
    aim = 0

    for row in data:
        direction,value = row.split(' ')
        if direction == 'forward':
            h_pos += int(value)
            depth += int(value) * aim
        elif direction == 'down': aim += int(value)
        elif direction == 'up': aim -= int(value)

    return h_pos*depth

print(calc_pos2(data))