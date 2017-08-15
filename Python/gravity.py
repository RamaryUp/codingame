# Codingame challenge
# Name : Gravity
# Category : Community puzzles
# URL : https://www.codingame.com/training/community/gravity

'''
-----------------------------------------------------------------------------------	
The program:
The program must output the given map, making the # fall to the bottom of the grid.

The map is composed of '.' and '#'.

INPUT:
Line 1 : Two integers: The map width width and height height.
height next lines : width characters: (. or #).

OUTPUT:
height lines : width characters where the # are at the bottom of the grid.

CONSTRAINTS:
0 < width < 100
0 < height < 10

EXAMPLE:
Input
17 5
...#...#.#.#...#.
.#..#...#....#...
..........#......
..###...###..##..
#################
Output
.................
.................
...##...###..#...
.####..#####.###.
#################
-----------------------------------------------------------------------------------	
'''
SHARP_CHAR='#'
POINT_CHAR='.'
width, height = [int(i) for i in input().split()]
counters = [0 for i in range(width)]
for i in range(height):
    line = input()
    for j in range(width):
        counters[j] += 1 if line[j] == SHARP_CHAR else 0

for i in range(height , 0, -1):
    line = ""
    for j in range(width):
        line += SHARP_CHAR if counters[j] >= i else POINT_CHAR
    print(line)