
with open('data/day8.txt') as f:
    data = f.read().split('\n')


sum = 0
for row in data:
    four_digits = row.split('|')[1].split(' ')
    for digit in four_digits:
        if len(digit) in (2,3,4,7): sum+=1

print(sum)

sum = 0
for row in data:
    signal_patterns = row.split('|')[0].split(' ')
    new_signals = {}

    for signal in signal_patterns:
        if len(signal) == 2: new_signals[1] = ''.join(sorted(signal))
        elif len(signal) == 3: new_signals[7] = ''.join(sorted(signal))
        elif len(signal) == 7: new_signals[8] = ''.join(sorted(signal))
        elif len(signal) == 4: new_signals[4] = ''.join(sorted(signal))

    sig1 = list(new_signals[1])
    sig2 = [x for x in new_signals[4] if x not in sig1]
    sig3 = [x for x in new_signals[7] if x not in sig1]
    sig4 = [x for x in new_signals[8] if x not in sig1 and x not in sig2 and x not in sig3]


    for signal in signal_patterns:
        if sig1[0] in signal and sig1[1] in signal:
            if len(signal) == 5: new_signals[3] = ''.join(sorted(signal))
            elif len(signal) == 6:
                if sig2[0] in signal and sig2[1] in signal: new_signals[9] = ''.join(sorted(signal))
                if sig4[0] in signal and sig4[1] in signal: new_signals[0] = ''.join(sorted(signal))
        if sig2[0] in signal and sig2[1] in signal:
            if len(signal) == 5: new_signals[5] = ''.join(sorted(signal))
            elif len(signal) == 6 and sig4[0] in signal and sig4[1] in signal:
                new_signals[6] = ''.join(sorted(signal))

        if len(signal) == 5 and sig4[0] in signal and sig4[1] in signal:
            new_signals[2] = ''.join(sorted(signal))


    num = ''
    four_digits = row.split('|')[1].split(' ')[1:]

    for digit in four_digits:
        digit = ''.join(sorted(digit))
        for key, value in new_signals.items():
            if digit == value: num += str(key)
    if num != '':
        sum += int(num)

print(sum)