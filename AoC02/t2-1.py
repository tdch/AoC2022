# A-rock B-paper C-scissor
# X-rock Y-paper Z-scissor

win = [('A', 'Y'), ('B', 'Z'), ('C', 'X')]
eq = [('A', 'X'), ('B', 'Y'), ('C', 'Z')]
shapes = {'X': 1, 'Y': 2, 'Z': 3}

score = 0
with open("input.txt") as file:
    for game in [tuple(line.split()) for line in file]:
        score += shapes[game[1]]
        if game in win:
            score += 6
        if game in eq:
            score += 3

print(score)
