# store it as a matrix of 1 and 0's
import sys


box = lambda ch : int(ch == ' ')

with open(sys.argv[1],"r+") as file:
    crossword = [[box(ch) for ch in line[:-1]] for line in file.readlines() if len(line) > 0][:-1]


for row in crossword:
    print(row)
