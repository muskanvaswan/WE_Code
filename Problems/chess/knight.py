from collections import namedtuple
import queue

square = namedtuple('square', 'file rank')
move = namedtuple('move', 'start end')
RANKS = '12345678'
FILES = 'ABCDEFGH'

KNIGHT_MOVES =  [(1, 2), (2, 1), (-1, 2), (2, -1), (1, -2), (-2, 1), (-2, -1), (-1, -2)]

def file_diff(start: square, end: square) -> int:
    return ord(start.file) - ord(end.file)

def rank_diff(start: square, end: square) -> int:
    return int(start.rank) - int(end.rank)

def sq_diff(start: square, end: square) -> [int, int]:
    return file_diff(start, end), rank_diff(start, end)

def valid_knight_move(start: square, end: square) -> bool:
    return sq_diff(start, end) in KNIGHT_MOVES

def move_file_by(file: str, by: int):
    return chr(ord(file) + by) if chr(ord(file) + by).upper() in FILES else None

def move_rank_by(rank: str, by: int):
    return str(int(rank) + by) if str(int(rank) + by) in RANKS else None

def make_move_from_square(start: square, by):
    return move(move(None, start), square(move_file_by(start.file, by[0]), move_rank_by(start.rank, by[1])))

def make_move(start: move, by):
    return move(start, square(move_file_by(start.end.file, by[0]), move_rank_by(start.end.rank, by[1])))

def possible_moves_knight(start) -> [move]:
    # using the type function seems icky
    return [moved for moved in [make_move(start, m) for m in KNIGHT_MOVES] if all(moved.end)]

def build_path(node: move) -> [square]:
    path = []
    while node != None:
        path.append(node.end)
        node = node.start
    return path[::-1]


# Non recursive approach
def track_path_knight(start: square, end: square) -> [square]:
    # perform a depth first search on nodes
    frontier = []
    aux_board = {key.lower(): [False]*8 for key in FILES}
    frontier.append(move(None, start))
    while frontier != []:
        node = frontier.pop(0)
        if valid_knight_move(node.end, end):
            return build_path(move(node, end))
        if not aux_board[node.end.file][int(node.end.rank) - 1]:
            aux_board[node.end.file][int(node.end.rank) - 1] = True
            for moved in possible_moves_knight(node):
                frontier.append(moved)



# Recursive approach
frontier = []
aux_board = {key.lower(): [False]*8 for key in FILES}

def knight_path(start: move, end: square) -> [square]:
    global frontier, aux_board
    if valid_knight_move(start.end, end):
        return build_path(move(start, end))
    if not aux_board[start.end.file][int(start.end.rank) - 1]:
        frontier += possible_moves_knight(start)
        aux_board[start.end.file][int(start.end.rank) - 1] = True
    return knight_path(frontier.pop(0), end)



print(track_path_knight(square('e', '8'), square('e', '3')))
print(knight_path(move(None, square('e', '8')), square('e', '3')))
