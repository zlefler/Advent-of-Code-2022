forest = []
with open('day_8_input.txt') as f:
    for line in f.read().splitlines():
        row = []
        for tree in line:
            row.append(tree)
        forest.append(row)
