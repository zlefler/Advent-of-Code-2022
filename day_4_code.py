import re

with open('day_4_input.txt') as f:
    overlaps = 0
    for line in f.read().splitlines():
        assignments = re.split('-|,', line)
        if int(assignments[0]) <= int(assignments[2]) and int(assignments[1]) >= int(assignments[3]):
            overlaps += 1
        elif int(assignments[0]) >= int(assignments[2]) and int(assignments[1]) <= int(assignments[3]):
            overlaps += 1
            print(assignments)
print(f'answer to Part One: {overlaps}')
