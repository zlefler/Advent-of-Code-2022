# Part One

stacks = {1: ['Z', 'P', 'M', 'H', 'R'], 2: ['P', 'C', 'J', 'B'], 3: ['S', 'N', 'H', 'G', 'L', 'C', 'D'], 4: ['F', 'T', 'M', 'D', 'Q', 'S', 'R', 'L'], 5: [
    'F', 'S', 'P', 'Q', 'B', 'T', 'Z', 'M'], 6: ['T', 'F', 'S', 'Z', 'B', 'G'], 7: ['N', 'R', 'V'], 8: ['P', 'G', 'L', 'T', 'D', 'V', 'C', 'M'], 9: ['W', 'Q', 'N', 'J', 'F', 'M', 'L']}

with open('day_5_input.txt') as f:
    i = 0
    for unsplit_line in f.read().splitlines():
        if i < 10:
            i += 1
            continue
        line = unsplit_line.split()
        crates_moved = int(line[1])
        start_stack = int(line[3])
        end_stack = int(line[5])
        for _ in range(crates_moved):
            stacks[end_stack].append(stacks[start_stack].pop())

stack_tops = ''
for stack in stacks.values():
    stack_tops += stack[-1]

print(f'answer to Part One: {stack_tops}')

# Part Two

stacks = {1: ['Z', 'P', 'M', 'H', 'R'], 2: ['P', 'C', 'J', 'B'], 3: ['S', 'N', 'H', 'G', 'L', 'C', 'D'], 4: ['F', 'T', 'M', 'D', 'Q', 'S', 'R', 'L'], 5: [
    'F', 'S', 'P', 'Q', 'B', 'T', 'Z', 'M'], 6: ['T', 'F', 'S', 'Z', 'B', 'G'], 7: ['N', 'R', 'V'], 8: ['P', 'G', 'L', 'T', 'D', 'V', 'C', 'M'], 9: ['W', 'Q', 'N', 'J', 'F', 'M', 'L']}

with open('day_5_input.txt') as f:
    i = 0
    for unsplit_line in f.read().splitlines():
        if i < 10:
            i += 1
            continue
        line = unsplit_line.split()
        crates_moved = int(line[1])
        start_stack = int(line[3])
        end_stack = int(line[5])
        crates_to_move = []
        for _ in range(crates_moved):
            crates_to_move.insert(0, stacks[start_stack].pop())
        for crate in crates_to_move:
            stacks[end_stack].append(crate)

stack_tops = ''
for stack in stacks.values():
    stack_tops += stack[-1]

print(f'Answer to Part Two: {stack_tops}')
