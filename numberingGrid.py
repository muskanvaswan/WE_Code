def print_grid(grid):
     for line in grid:
        print(line)


def read_grid(file_name: str):
    file = open(file_name, 'r')
    grid = []
    for line in file.readlines():
        grid.append(line.split())
    return grid
    

def add_row_padding(grid):
    grid.insert(0, ['X'] * (len(grid[1])))
    grid.append(['X'] * (len(grid[1])))
    return grid


def add_column_padding(grid):
    for line in grid:
        line.insert(0, 'X')
        line.append('X')
    return grid


def is_across(grid, row: int, col: int) -> bool:
    return grid[row][col - 1] == 'X' and grid[row][col + 1] == '.'


def is_down(grid, row: int, col: int) -> bool:
    return grid[row - 1][col] == 'X' and grid[row + 1][col] == '.'


def remove_padding(grid):
    grid.pop(0)
    grid.pop(-1)
    for line in grid:
        line.pop(0)
        line.pop(-1)
    return grid


def number_grid(file_name: str):
    grid = add_row_padding(add_column_padding(read_grid(file_name)))
    
    number = 1
    for row in range(1, len(grid) - 1):
        for col in range(1, len(grid) - 1):
            if grid[row][col] != 'X' and (is_across(grid, row, col) or is_down(grid, row, col)):
                grid[row][col] = str(number)
                number += 1
                
    return remove_padding(grid)

print_grid(number_grid("crossword_grid.txt"))
