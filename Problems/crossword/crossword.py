# store it as a matrix of 1 and 0's
# store as a matrix of true or false ?¿
import sys

box = lambda ch : ch == ' '

def read_crossword(file) -> [[int]]:
    # maybe make a seperate func for adding the boundary ?¿
    with open(file,"r+") as file:
        crossword = [[False] + [box(ch) for ch in line[:-1]] + [False] for line in file.readlines() if len(line) > 0][:-1]
    crossword.insert(0, [False]*len(crossword[0]))
    crossword.append([False]*len(crossword[0]))
    return crossword

def is_shallow(x, y, crossword) -> bool:
    # TODO: fix
    if crossword[x + 1][y]:
        return crossword[x - 1][y]
    if crossword[x][y + 1]:
        return crossword[x][y - 1]
    return True

def is_bounded(x, y, crossword) -> bool:
    return (not crossword[x - 1][y]) or (not crossword[x][y - 1])

def is_starter(x, y, crossword) -> bool:
    # TODO: improve
    if x == 0 or y == 0 or x == len(crossword) - 1 or y == len(crossword) - 1:
        return False
    return crossword[x][y] and (not is_shallow(x, y, crossword)) and is_bounded(x, y, crossword)

def assign_starters(crossword) -> [int]:
    # do I need this function ?¿¿¿
    return [(i, j) for (i, row) in enumerate(crossword) for (j, cell) in enumerate(row) if is_starter(i, j, crossword)]


def resulting(crossword):
    content, count = '', 0
    for (i, row) in enumerate(crossword):
        for (j, cell) in enumerate(row):
            if is_starter(i, j, crossword):
                content += '.'
            else:
                content += ' ' if cell else 'X'
            count += 1
        content += '\n'
    return content

crossword = read_crossword(sys.argv[1])
print(resulting(crossword))
print(crossword[1][2])
print(is_starter(1, 2, crossword))

# put this inside function
for row in crossword:
    for cell in row:
        print(' ' if cell else 'X', end="")
    print()
