import sys

box = lambda ch : ch == ' '

def read_crossword(file) -> [[int]]:
    # maybe make a seperate func for adding the boundary ?¿
    with open(file,"r+") as file:
        crossword = [[False] + [box(ch) for ch in line[:-1]] + [False] for line in file.readlines() if len(line) > 0][:-1]
    crossword.insert(0, [False]*len(crossword[0]))
    crossword.append([False]*len(crossword[0]))
    return crossword

crossword = read_crossword(sys.argv[1])

def find_starts(matrix: [[int]], width: int, height: int) -> [(int, int)]:
    return sorted(find_across_starts(flatten_across(matrix), width) + find_down_starts(flatten_down(matrix), height))

def find_across_starts(row_flat: [int], width: int) -> [(int, int)]:
    return [(int(i / width), (i % width)) for i in range(1, len(row_flat) - 1) if row_flat[i] and not row_flat[i - 1] and row_flat[i + 1]]

def find_down_starts(column_flat: [int], height: int) -> [(int, int)]:
    return [(i % height, int(i / height )) for i in range(1, len(column_flat) - 1) if column_flat[i] and not column_flat[i - 1] and column_flat[i + 1]]

def flatten_across(matrix: [[int]]) -> [int]:
    return flatten(matrix)

def flatten_down(matrix: [[int]]) -> [int]:
    return flatten([list(elem[0]) for elem in zip(matrix)])

def flatten(matrix: [[int]]) -> [int]:
    return [element for row in matrix for element in row]

def format_grid(grid: [[int]], starts = []) -> str:
    result = ''
    for i, row in enumerate(crossword):
        for j, cell in enumerate(row):
            result += ('_' if (i, j) in starts else ' ') if cell else 'X'
        result += '\n'
    return result


# DRIVER CODE
print(len(set(starts)))
print(format_grid(crossword))
starts = find_starts(crossword, len(crossword[0]), len(crossword))
print(format_grid(crossword, starts))
