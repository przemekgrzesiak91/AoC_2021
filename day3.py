with open('data/day3.txt') as f:
    data = f.read().split('\n')


gamma_rate = ''
epsilon_rate = ''
n = len(data)
n_binary = len(data[0])

sum_binary = [0] * (n_binary)

for b_number in data:
    for i in range(0, n_binary):
        if b_number[i] == '1': sum_binary[i] += 1

for pos in sum_binary:
    if pos > n / 2:
        gamma_rate += '1'
        epsilon_rate += '0'
    else:
        gamma_rate += '0'
        epsilon_rate += '1'

#Day 3.2
oxygen_generator = ''
CO2_scrubber = ''

print(gamma_rate[0])
data_oxy = [i for i in data if i[0] == gamma_rate[0]]
data_CO2 = [i for i in data if i[0] == epsilon_rate[0]]

for i in range(1, n_binary):
    sum_bit = 0
    for b_number in data_oxy:
        if b_number[i] == "1": sum_bit +=1
    if sum_bit >= len(data_oxy)/2:
        data_oxy = [x for x in data_oxy if x[i] == '1']
    else:
        data_oxy = [x for x in data_oxy if x[i] == '0']
    if len(data_oxy) == 1: break



for i in range(1, n_binary):
    sum_bit = 0
    for b_number in data_CO2:
        if b_number[i] == "1": sum_bit += 1

    if sum_bit < len(data_CO2) / 2:
        data_CO2 = [x for x in data_CO2 if x[i] == '1']
    else:
        data_CO2 = [x for x in data_CO2 if x[i] == '0']
    if len(data_CO2) == 1: break


print(data_oxy)
print(data_CO2)
oxygen_generator = data_oxy[0]
CO2_scrubber = data_CO2[0]

#Day 3.1
power_consumption = int(gamma_rate,2) * int(epsilon_rate,2)
print(power_consumption)
#Day 3.2
life_support = int(oxygen_generator,2) * int(CO2_scrubber,2)
print(life_support)