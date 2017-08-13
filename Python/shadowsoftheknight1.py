# Codingame challenge
# Name : Shadows of the Knight - Episode 1
# Category : Classic puzzle - medium level
# URL : https://www.codingame.com/training/medium/shadows-of-the-knight-episode-1
# Selected programming language : Python 3.5.3

'''
-----------------------------------------------------------------------------------	
	The Goal

Batman will look for the hostages on a given building by jumping from one window to another using his grapnel gun. Batman's goal is to jump to the window where the hostages are located in order to disarm the bombs. Unfortunately he has a limited number of jumps before the bombs go off...
 	Rules

Before each jump, the heat-signature device will provide Batman with the direction of the bombs based on Batman current position: 
U (Up)
UR (Up-Right)
R (Right)
DR (Down-Right)
D (Down)
DL (Down-Left)
L (Left)
UL (Up-Left)

Your mission is to program the device so that it indicates the location of the next window Batman should jump to in order to reach the bombs' room as soon as possible.

Buildings are represented as a rectangular array of windows, the window in the top left corner of the building is at index (0,0).
 	Note

For some tests, the bombs' location may change from one execution to the other: the goal is to help you find the best algorithm in all cases.

The tests provided are similar to the validation tests used to compute the final score but remain different.
 	Game Input

The program must first read the initialization data from standard input. Then, within an infinite loop, read the device data from the standard input and provide to the standard output the next movement instruction.
Initialization input
Line 1 : 2 integers W H. The (W, H) couple represents the width and height of the building as a number of windows.

Line 2 : 1 integer N, which represents the number of jumps Batman can make before the bombs go off.

Line 3 : 2 integers X0 Y0, representing the starting position of Batman.

Input for one game turn
The direction indicating where the bomb is.
Output for one game turn
A single line with 2 integers X Y separated by a space character. (X, Y) represents the location of the next window Batman should jump to. X represents the index along the horizontal axis, Y represents the index along the vertical axis. (0,0) is located in the top-left corner of the building.
Constraints
1 ≤ W ≤ 10000
1 ≤ H ≤ 10000
2 ≤ N ≤ 100
0 ≤ X, X0 < W
0 ≤ Y, Y0 < H
Response time per turn ≤ 150ms
Response time per turn ≤ 150ms
Example
Initialization input
10 10     Building has 100 windows (10x10)
6         Batman has 6 jumps to find the bombs
2 5       Batman starts at position (2,5)
 
No output expected
Input for turn 1
UR
Hostages are in the upward-right direction
 
Output for turn 1
5 4
Batman jumps to window (5,4)
Input for turn 2
R
Hostages are located to the right of Batman
 
Output for turn 2
7 4
Batman jumps to window (7,4)
 
Batman found the hostages. He can defuse the bombs in time. You win!
-----------------------------------------------------------------------------------	
'''

import sys
# w: width of the building.
# h: height of the building.
w, h = map(int, input().split())
n = int(input())  # maximum number of turns before game over.
x0, y0 = map(int, input().split())
xmin = ymin = 0
xmax, ymax = w-1, h-1

xmin_update_when = ['U',' D', 'UR', 'DR', 'R']
xmax_update_when = ['U', 'D', 'UL', 'DL', 'L']
ymin_update_when = ['D', 'L', 'R','DL', 'DR' ]
ymax_update_when = ['U', 'L', 'R', 'UL', 'UR']

xadd_int = {'U':0, 'D':0, 'UR':1, 'R':1, 'DR':1, 'UL':-1, 'L':-1, 'DL':-1}
yadd_int = {'U':-1, 'D':1, 'UR':-1, 'R':0, 'DR':1, 'UL':-1, 'L':0, 'DL':1}

while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)

    print('bomb_dir={}'.format(bomb_dir), file=sys.stderr)
    if bomb_dir in xmin_update_when:
        xmin = x0 + xadd_int[bomb_dir]
    if bomb_dir in xmax_update_when:
        xmax = x0 + xadd_int[bomb_dir]
    if bomb_dir in ymin_update_when:
        ymin = y0 + yadd_int[bomb_dir]
    if bomb_dir in ymax_update_when:
        ymax = y0 + yadd_int[bomb_dir]
    
    x0 = (xmax + xmin) // 2
    y0 = (ymax + ymin) // 2 

    # the location of the next window Batman should jump to.
    print('{} {}'.format(x0, y0))
