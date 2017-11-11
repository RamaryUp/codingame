# Codingame challenge
# Name : Game of life
# Category : Community puzzles
# URL : https://www.codingame.com/training/community/game-of-life
# Selected programming language : Python 3.5.3

'''
-----------------------------------------------------------------------------------	
You are given a board with width * height cells in which each cell has an initial state: live '1' or dead '0'. Each cell interacts with its eight neighbors (horizontally, vertically and diagonally) using the following four rules:

1. Any live cell with fewer than two live neighbors dies, as if caused by under-population.
2. Any live cell with two or three live neighbors lives on to the next generation.
3. Any live cell with more than three live neighbors dies, as if by over-population..
4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

Write a program to compute the next state (after one update) of the board given its current state.
Input
Line 1: Two space separated integers width and height, respectively the width and height of the board
Next height lines: width characters ('0' or '1') each representing an initial cell state.
Output
height lines: width characters ('0' or '1') each representing an updated cell state.
Constraints
1 ≤ width, height ≤ 100
Example
Input
3 3
000
111
000
Output
010
-----------------------------------------------------------------------------------	
'''
import sys

# define virtual dead cells surrounding actual board
LIVE_CELL='1'
DEAD_CELL='0'

'''
Initialize the board dedicated to couting live cells of the superboard
'''
def init_superboard_counters(width, height):
    super_width = width + 2
    super_height = height + 2
    
    newboard = [[0] * super_width for _ in range(super_height)]
    return newboard

'''
Increment the counter of live cells of neighbors of a cell
'''
def update_board_counters(sboard_counters, x, y):
    sboard_counters[x-1][y-1] += 1
    sboard_counters[x-1][y] += 1
    sboard_counters[x-1][y+1] += 1
    sboard_counters[x][y-1] += 1
    sboard_counters[x][y+1] += 1
    sboard_counters[x+1][y-1] += 1
    sboard_counters[x+1][y] += 1
    sboard_counters[x+1][y+1] += 1


'''
returns a superboard of counters of live neighbors
the dimention of this superboard is (width+2) x (height+2)
'''
def count_live_neighbours(sboard_cells, width, height):
    sboard_counters = init_superboard_counters(width, height)
    
    print("count_live_neighbours sboard_cells={}".format(sboard_cells), file=sys.stderr)
    for vertical_index in range(1, height+1):
        for horizontal_index in range(1, width+1):
            if sboard_cells[vertical_index][horizontal_index] == LIVE_CELL:
                update_board_counters(sboard_counters, vertical_index, horizontal_index)
    
    return sboard_counters

'''
returns a width x height board containing the next state of the board given its current state
'''
def compute_next_state(sboard_cells, sboard_counters, width, height):
    nextboard_cells = [[DEAD_CELL] * width for _ in range(height)]

    for vertical_index in range(1, height+1):
        for horizontal_index in range(1, width+1):
            if sboard_cells[vertical_index][horizontal_index] == LIVE_CELL:                
                if sboard_counters[vertical_index][horizontal_index] < 2:
                    # dies due to under-population
                    nextboard_cells[vertical_index-1][horizontal_index-1] = DEAD_CELL
                elif 2 <= sboard_counters[vertical_index][horizontal_index] <=3:
                    # keeps living
                    nextboard_cells[vertical_index-1][horizontal_index-1] = LIVE_CELL
                else:
                    # dies to over-population
                    nextboard_cells[vertical_index-1][horizontal_index-1] = DEAD_CELL                    
            else:
                # any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
                if sboard_counters[vertical_index][horizontal_index] == 3:
                    nextboard_cells[vertical_index-1][horizontal_index-1] = LIVE_CELL

    return nextboard_cells


# the superboard is the board + the surrouding border of virtual dead cells
# the width of the superboard is (width+2) x (height+2)

superboard = []
width, height = [int(i) for i in input().split()]
superboard_width = width + 2
superboard_height = height + 2


ROW_SUPERBOARD_BORDER = DEAD_CELL * superboard_width

# add upper row first
superboard.append(ROW_SUPERBOARD_BORDER)

for _ in range(height):
    line = input()
    print("line : {}".format(line), file=sys.stderr)
    superboard_row = DEAD_CELL + line + DEAD_CELL
    superboard.append(superboard_row)

# add bottom row
superboard.append(ROW_SUPERBOARD_BORDER)

counters = count_live_neighbours(superboard, width, height)
next_state = compute_next_state(superboard, counters, width, height)

# output results
for row in next_state:    
    print(''.join(row))
    