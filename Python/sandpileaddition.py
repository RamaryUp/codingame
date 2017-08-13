# Codingame challenge
# Name : Sandpile addition
# Category : Community puzzles
# URL : https://www.codingame.com/training/community/sandpile-addition

'''
-----------------------------------------------------------------------------------	
	Goal

A sandpile is a square matrix of natural numbers between 0 and 3, representing how many grains of sand there is on each square
To add two sandpiles, just start by adding the two matrices element by element. Except the matrix you generate might not be a sandpile, if one of its element is higher than 3 you must transform this matrix into a sandpile, and this is how it is done :
- If a square has 4 grains of sand or more, it "loses" four and distributes it to its four neighbors (if the square touches an edge, the grain of sand is lost)
- Keep doing that to all the squares with 4 grains or more until all the squares have 3 grains or less

Example :
000   000   000    010
020 + 020 = 040 -> 101
000   000   000    010
Input
Line 1 : An integer n, the size of the two sandpiles
2*n next lines : The two sandpiles
Output
n lines representing the resulting sandpile
Constraints
2 ≤ N ≤ 10
Example
Input
3
121
202
121
020
202
020
Output
313
101
313
-----------------------------------------------------------------------------------	
'''

import sys
import math

def addOne(newsquare, x, y):
    length = len(newsquare)
    if 0 <= x < length and 0 <= y < length:
        newsquare[x][y] += 1

def translate(square):    
    length = len(square)
    newsquare = [[0] * length for _ in range(length)]
    for x in range(length):
        for y in range(length):
            if square[x][y] >= 4:
                addOne(newsquare, x-1, y)
                addOne(newsquare, x+1, y)
                addOne(newsquare, x, y-1)
                addOne(newsquare, x, y+1)
                newsquare[x][y] += square[x][y] - 4
            else:
                newsquare[x][y] += square[x][y]
    return newsquare
    
def isSandPile(square):
    length = len(square)
    for x in range(length):
        for y in range(length):
            if square[x][y] >= 4:
                return False
    return True
                
# INITIALIZATION
n = int(input())
square1=[]
square2=[]
for i in range(n):
    square1.append([int(x) for x in input()])
for i in range(n):
    square2.append([int(x) for x in input()])

# PROCESSING
# summing the squares
square = [[square1[x][y]+square2[x][y] for y in range(n) ] for x in range(n)]

while not isSandPile(square):
    square = translate(square)

# PRINTING SANDPILE RESULT
for i in range(n):
    print(''.join(str(x) for x in square[i]))