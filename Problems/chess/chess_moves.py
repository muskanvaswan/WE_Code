from collections import namedtuple
import itertools as it

square = namedtuple('square', 'file rank')
move = namedtuple('move', 'start end')
RANKS = '12345678'
FILES = 'ABCDEFGH'

RULES =  {
    'knight': [(1, 2), (2, 1), (-1, 2), (2, -1), (1, -2), (-2, 1), (-2, -1), (-1, -2)],
    'bishop': [i for p in [it.permutations([n, n, -n, -n], 2) for n in range(8)] for i in p],
    'king': [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (1, 1), (1, -1), (-1, 1)],
    'queen': [(i * j[0], i * j[1]) for i in range(1, 7) for j in [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (1, 1), (1, -1), (-1, 1)]],
    'rook': [(i * j[0], i * j[1]) for i in range(1, 7) for j in [(0, 1), (1, 0), (0, -1), (-1, 0)]],
}

def file_diff(start: square, end: square) -> int:
    return ord(start.file) - ord(end.file)

def rank_diff(start: square, end: square) -> int:
    return int(start.rank) - int(end.rank)

def sq_diff(start: square, end: square) -> [int, int]:
    return file_diff(start, end), rank_diff(start, end)

def valid_move(start: square, end: square, piece: str) -> bool:
    return sq_diff(start, end) in RULES[piece]

def move_file_by(file: str, by: int):
    return chr(ord(file) + by) if chr(ord(file) + by).upper() in FILES else None

def move_rank_by(rank: str, by: int):
    return str(int(rank) + by) if str(int(rank) + by) in RANKS else None

def make_move_from_square(start: square, by):
    return move(move(None, start), square(move_file_by(start.file, by[0]), move_rank_by(start.rank, by[1])))

def make_move_from_move(start: move, by):
    return move(start, square(move_file_by(start.end.file, by[0]), move_rank_by(start.end.rank, by[1])))

def possible_moves(start, piece) -> [move]:
    return [moved for moved in [(make_move_from_square(start, m) if type(start) == square else make_move_from_move(start, m)) for m in RULES[piece]] if all(moved.end)]

def build_path(node: move) -> [square]:
    path = []
    while node != None:
        path.append(node.end)
        node = node.start
    return path[::-1]

def track_path(start: square, end: square, piece: str) -> [square]:
    # perform a depth first search where nodes are edges are moves and we are searching for end square 
    frontier, visited = [], []
    frontier.append(move(None, start))
    while frontier != []:
        node = frontier.pop(0)
        if valid_move(node.end, end, piece):
            return build_path(move(node, end))
        if node.end not in visited:
            visited.append(node.end)
            for moved in possible_moves(node, piece):
                frontier.append(moved)


print(track_path(square('a', '8'), square('a', '1'), 'king'))
#print(possible_moves_knight(square('d', '4')))
