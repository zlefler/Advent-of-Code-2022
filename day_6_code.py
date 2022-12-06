def marker_start() -> int:  # Function for Part One
    '''...It needs to report the number of characters from the beginning of the buffer to the end of the first such four-character marker.'''
    frequency_map = {}
    left = 0
    with open('day_6_input.txt') as f:
        text = f.read()
        for right in range(len(text)):
            frequency_map[text[right]] = frequency_map.get(text[right], 0) + 1
            if right == 3 and len(frequency_map) == 4:
                return left
            elif right > 3:
                frequency_map[text[left]] -= 1
                if frequency_map[text[left]] == 0:
                    del frequency_map[text[left]]
                left += 1
                if len(frequency_map) == 4:
                    return left + 4

    # set left and right sides of window
    # move right side k times, add letters to map
    # check if all discrete
    # if not, move right and add, move left and subtract
    # check again, when all discrete, return left


print(f'answer to Part One: {marker_start()}')
