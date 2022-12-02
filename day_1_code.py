'''Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?'''

# Part One
current_weight = 0
max_weight = 0
with open('day_1_input.txt') as f:
    for line in f.readlines():
        if line == '\n':
            max_weight = max(current_weight, max_weight)
            current_weight = 0
        else:
            current_weight += int(line)
print(f'answer to part one: {max_weight}')

# Part Two

all_weights = []
current_weight = 0
with open('day_1_input.txt') as f:
    for line in f.readlines():
        if line == '\n':
            all_weights.append(current_weight)
            current_weight = 0
        else:
            current_weight += int(line)

all_weights.sort()
top_three = 0
for i in range(-1, -4, -1):
    top_three += all_weights[i]
print(f'answer to part two: {top_three}')
