#!/usr/bin/env
import sys
import time

def get_rows(board):
    return len(board)

def get_cols(board):
    return len(board[0])

def print_board(board):
    print "+" + "-" * get_cols(board) + "+"
    for row in board:
        output_str = "|"
        for c in row:
            if c:
                output_str += "X"
            else:
                output_str += " "
        output_str += "|"
        print output_str
    print "+" + "-" * get_cols(board) + "+"

def correct(value, max):
    if value == max:
        return 0
    elif value == -1:
        return max - 1
    else:
        return value

def get_neighbors(row, col, board):
    board_rows = get_rows(board)
    board_cols = get_cols(board)
    neighbors = 0

    if board[correct(row + 1, board_rows)][correct(col + 1, board_cols)]:
        neighbors += 1
    if board[correct(row - 1, board_rows)][correct(col + 1, board_cols)]:
        neighbors += 1
    if board[correct(row, board_rows)][correct(col + 1, board_cols)]:
        neighbors += 1
    if board[correct(row + 1, board_rows)][correct(col - 1, board_cols)]:
        neighbors += 1
    if board[correct(row, board_rows)][correct(col - 1, board_cols)]:
        neighbors += 1
    if board[correct(row - 1, board_rows)][correct(col - 1, board_cols)]:
        neighbors += 1
    if board[correct(row + 1, board_rows)][correct(col, board_cols)]:
        neighbors += 1
    if board[correct(row - 1, board_rows)][correct(col, board_cols)]:
        neighbors += 1
    return neighbors

def create_board_size(rows, cols):
    # For reference board[row][column]
    board = [[False for x in xrange(cols)] for y in xrange(rows)]
    return board

def read_board_file(file):
    with open(file) as f:
        content = f.readlines()
        board = create_board_size(len(content), len(content[0].split(',')))
        for r, row in enumerate(content):
            for c, cell in enumerate(row.split(',')):
                if cell is 'X' or cell is 'X\n':
                    board[r][c] = True
                else:
                    board[r][c] = False
        return board

def run(board):
    new_board = create_board_size(get_rows(board), get_cols(board))
    for r, row in enumerate(board):
        for c, cell in enumerate(row):
            n = get_neighbors(r, c, board)
            if cell:
                if n < 2:
                    new_board[r][c] = False
                elif n <= 3:
                    new_board[r][c] = True
                else:  # n <= 4
                    new_board[r][c] = False  # unneeded, but kept for readability
            else:
                if n == 3:
                    new_board[r][c] = True
                else:
                    new_board[r][c] = False  # unneeded, again kept for readability
    return new_board

board = [[]]
try:
    BOARD_FILE = sys.argv[1]
except IndexError:
    print "No Board File provided"
    quit()

board = read_board_file(BOARD_FILE)
print_board(board)

while True:
    board = run(board)
    print_board(board)
    time.sleep(.1)
