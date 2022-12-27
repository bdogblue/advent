# --- Day 2: Rock Paper Scissors --- 

infile = open('input.txt', 'r')

guide = infile.read()

infile.close()

stratagy_list = [line.split(" ") for line in guide.splitlines()]

your_score = 0

for case in stratagy_list:
    if case[0] == 'A':
        if case[1] == 'Y':
            your_score += 3 + 1
        if case[1] == 'X':
            your_score += 0 + 3
        if case[1] == 'Z':
            your_score += 6 + 2 
    if case[0] == 'B':
        if case[1] == 'Y':
            your_score += 3 + 2 
        if case[1] == 'X':
            your_score += 0 + 1
        if case[1] == 'Z':
            your_score += 6 + 3
    if case[0] == 'C':
        if case[1] == 'Y':
            your_score += 3 + 3
        if case[1] == 'X':
            your_score += 0 + 2
        if case[1] == 'Z':
            your_score += 6 + 1

print("This is your score:", your_score)