# Codingame challenge
# Name : The Last Crusade - Episode 1
# Category : Classic puzzle - medium level
# URL : https://www.codingame.com/training/medium/the-last-crusade-episode-1
# Selected programming language : Python 3.5.3
'''
-----------------------------------------------------------------------------------
	The Goal

Your objective is to write a program capable of predicting the route Indy will take on his way down a tunnel. Indy is not in danger of getting trapped in this first mission.
 	Rules

The tunnel consists of a patchwork of square rooms of different types.The rooms can be accessed and activated by computer using an ancient RS232 serial port (because Mayans
aren't very technologically advanced, as is to be expected...).

There is a total of 14 room types (6 base shapes extended to 14 through rotations).

[See the complete rules on Codingame]
-----------------------------------------------------------------------------------
'''
# Where do I come from
FROMTOP, FROMLEFT, FROMRIGHT ='TOP', 'LEFT', 'RIGHT'

# Where do I go
GODOWN, GOLEFT, GORIGHT = (0,1), (-1,0), (1,0)

DONTMOVE=(0,0)

directions={}
directions[0] = {FROMTOP:DONTMOVE,FROMLEFT:DONTMOVE,FROMRIGHT:DONTMOVE }
directions[1] = {FROMTOP:GODOWN,FROMLEFT:GODOWN,FROMRIGHT:GODOWN } # From top : Go down, From Left : Go down, From Right : Go down
directions[2] = {FROMTOP:DONTMOVE,FROMLEFT:GORIGHT,FROMRIGHT:GOLEFT } # From Top : Can't move, From Left : Go to right, From Right : Go to left
directions[3] = {FROMTOP:GODOWN,FROMLEFT:DONTMOVE,FROMRIGHT:DONTMOVE }
directions[4] = {FROMTOP:GOLEFT,FROMLEFT:DONTMOVE,FROMRIGHT:GODOWN }
directions[5] = {FROMTOP:GORIGHT,FROMLEFT:GODOWN,FROMRIGHT:DONTMOVE }
directions[6] = {FROMTOP:DONTMOVE,FROMLEFT:GORIGHT,FROMRIGHT:GOLEFT }
directions[7] = {FROMTOP:GODOWN,FROMLEFT:DONTMOVE,FROMRIGHT:GODOWN }
directions[8] = {FROMTOP:DONTMOVE,FROMLEFT:GODOWN,FROMRIGHT:GODOWN }
directions[9] = {FROMTOP:GODOWN,FROMLEFT:GODOWN,FROMRIGHT:DONTMOVE }
directions[10] = {FROMTOP:GOLEFT,FROMLEFT:DONTMOVE,FROMRIGHT:DONTMOVE }
directions[11] = {FROMTOP:GORIGHT,FROMLEFT:DONTMOVE,FROMRIGHT:DONTMOVE }
directions[12] = {FROMTOP:DONTMOVE,FROMLEFT:DONTMOVE,FROMRIGHT:GODOWN }
directions[13] = {FROMTOP:DONTMOVE,FROMLEFT:GODOWN,FROMRIGHT:GODOWN }

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
