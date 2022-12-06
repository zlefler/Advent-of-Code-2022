from string import ascii_lowercase, ascii_uppercase

# Part One

'''The list of items for each rucksack is given as characters all on a single line. A given rucksack always has the same number of items in each of its two compartments, so the first half of the characters represent items in the first compartment, while the second half of the characters represent items in the second compartment.
To help prioritize item rearrangement, every item type can be converted to a priority:

Lowercase item types a through z have priorities 1 through 26.
Uppercase item types A through Z have priorities 27 through 52.
Find the item type that appears in both compartments of each rucksack. What is the sum of the priorities of those item types?'''


i = 1
priority_map = {}
for char in ascii_lowercase:
    priority_map[char] = i
    i += 1
for char in ascii_uppercase:
    priority_map[char] = i
    i += 1

priority_sum = 0
with open('day_3_input.txt') as f:
    for line in f.read().splitlines():
        frequency_map = {}
        mid = len(line) // 2
        first = line[:mid]
        second = line[mid:]
        for char in first:
            frequency_map[char] = True
        for char in second:
            i = 0
            if char in frequency_map:
                priority_sum += priority_map[char]
                break

print(f'Solution to Part One: {priority_sum}')

# Part Two

with open('day_3_input.txt') as f:
    groups = []
    group = []
    sum = 0
    for line in f.read().splitlines():
        if len(group) < 3:
            group.append(line)
        else:
            groups.append(group)
            group = []
            group.append(line)
    for group in groups:
        frequency_map = {}
        for i in range(len(group)):
            for char in group[i]:
                if i == 0:
                    frequency_map[char] = i
                else:
                    if char in frequency_map and frequency_map[char] == i-1:
                        frequency_map[char] = i
        for key, val in frequency_map.items():
            if val == 2:
                sum += priority_map[key]
print(sum)
