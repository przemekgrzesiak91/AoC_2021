with open('data\day14.txt') as f:
    template, d_pairs = f.read().split('\n\n')

#print(template)
#print(d_pairs)
pairs = {}
for pair in d_pairs.split('\n'):
    x,y = pair.split(' -> ')
    pairs[x] = y

def counter(pair_count):
    counts = {}
    for key,value in pair_count.items():
        char = key[1]

        if char not in counts.keys():
            counts[char] = value
        else:
            counts[char] += value

    counts['N'] += 1
    return(counts)

pair_count = {}
for i in range(0, len(template) - 1):
    pair = template[i:i + 2]
    if not pair in pair_count.keys():
        pair_count[pair] = 1
    else:
        pair_count[pair] += 1

step = 1
#while step <= 10:
while step <= 40:
    print(step)
    new_pair_count = {}
    for key,value in pair_count.items():
        x,y = list(key)[0] + pairs[key], pairs[key] + list(key)[1]
        if x not in new_pair_count.keys():
            new_pair_count[x] = value
        else:
            new_pair_count[x] += value

        if y not in new_pair_count.keys():
            new_pair_count[y] = value
        else:
            new_pair_count[y] += value

    pair_count = new_pair_count.copy()
    step += 1

counts = counter(pair_count)
max_x = max([value for value in counts.values()])
min_x = min([value for value in counts.values()])
print(max_x - min_x)