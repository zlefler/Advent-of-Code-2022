# Part One

'''"The first column is what your opponent is going to play: A for Rock, B for Paper, and C for Scissors. The second column--" Suddenly, the Elf is called away to help with someone's tent.

The second column, you reason, must be what you should play in response: X for Rock, Y for Paper, and Z for Scissors. Winning every time would be suspicious, so the responses must have been carefully chosen.

The winner of the whole tournament is the player with the highest score. Your total score is the sum of your scores for each round. The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).'''

throw_scores = {'X': 1, 'Y': 2, 'Z': 3}

matchup_scores = {'A X': 3, 'A Y': 6, 'A Z': 0, 'B X': 0, 'B Y': 3, 'B Z': 6, 'C X': 6,
                  'C Y': 0, 'C Z': 3}

total_score = 0
with open('day_2_input.txt') as f:
    for line in f.read().splitlines():
        total_score += matchup_scores[line]
        total_score += throw_scores[line[-1]]

print(f'Answer to Part One: {total_score}')

# Part Two
