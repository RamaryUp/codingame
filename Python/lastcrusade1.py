# Codingame challenge
# Name : The Last Crusade - Episode 1
# Category : Classic puzzle - medium level
# URL : https://www.codingame.com/training/medium/the-last-crusade-episode-1
# Selected programming language : Python 3.5.3

import sys

# TOP means From TOP, LEFT means from LEFT, RIGHT means from RIGHT
# (0,1) means go down, (1,0) means go right, (-1, 0) means go left

directions={}
directions[0] = {'TOP':(0,0),'LEFT':(0,0),'RIGHT':(0,0) }
directions[1] = {'TOP':(0,1),'LEFT':(0,1),'RIGHT':(0,1) } # From Left : Go to right, From Right : go to left
directions[2] = {'TOP':(0,0),'LEFT':(1,0),'RIGHT':(-1,0) } # From Left : Go to right, From Right : Go to left
directions[3] = {'TOP':(0,1),'LEFT':(0,0),'RIGHT':(0,0) }
directions[4] = {'TOP':(-1,0),'LEFT':(0,0),'RIGHT':(0,1) }
directions[5] = {'TOP':(1,0),'LEFT':(0,1),'RIGHT':(0,0) }
directions[6] = {'TOP':(0,0),'LEFT':(1,0),'RIGHT':(-1,0) }
directions[7] = {'TOP':(0,1),'LEFT':(0,0),'RIGHT':(0,1) }
directions[8] = {'TOP':(0,0),'LEFT':(0,1),'RIGHT':(0,1) }
directions[9] = {'TOP':(0,1),'LEFT':(0,1),'RIGHT':(0,0) }
directions[10] = {'TOP':(-1,0),'LEFT':(0,0),'RIGHT':(0,0) }
directions[11] = {'TOP':(1,0),'LEFT':(0,0),'RIGHT':(0,0) }
directions[12] = {'TOP':(0,0),'LEFT':(0,0),'RIGHT':(0,1) }
directions[13] = {'TOP':(0,0),'LEFT':(0,1),'RIGHT':(0,1) }

tunnel=[]

# w: number of columns.
# h: number of rows.
w, h = [int(i) for i in input().split()]
for i in range(h):
    #line = input()  # represents a line in the grid and contains W integers. Each integer represents one room of a given type.
    rooms = [int(x) for x in input().split()]
    tunnel.append(rooms)
    
ex = int(input())  # the coordinate along the X axis of the exit (not useful for this first mission, but must be read).
# game loop
while True:
    xi, yi, pos = input().split()
    xi = int(xi)
    yi = int(yi)
    roomtype = tunnel[yi][xi]

    # One line containing the X Y coordinates of the room in which you believe Indy will be on the next turn.
    print("{} {}".format(xi + directions[roomtype][pos][0], yi + directions[roomtype][pos][1]))
