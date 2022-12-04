# A-rock B-paper C-scissor
# X-rock Y-paper Z-scissor
# X-loose Y-draw Z-win

moves = {('A', 'X'):'Z', ('A','Y'):'X', ('A','Z'):'Y',
        ('B','X'):'X', ('B','Y'):'Y', ('B','Z'):'Z',
        ('C','X'):'Y', ('C','Y'):'Z', ('C','Z'):'X'}
shapes = {'X': 1, 'Y': 2, 'Z': 3}
wins = {'X':0, 'Y':3, 'Z':6}

score = 0
with open("input.txt") as file:
    for game in [tuple(line.split()) for line in file]:
        score += shapes[moves[game]] + wins[game[1]]
        
print(score)
