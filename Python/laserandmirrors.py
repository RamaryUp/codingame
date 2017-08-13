# Codingame challenge
# Name : Laser and mirrors
# Category : Community puzzles
# URL : https://www.codingame.com/training/community/laser-and-mirrors

'''
 	Goal

You find yourself in a corner of a gigantic dark room. You don't see anything at a distance, only the cold surface of both corner walls. On the floor you see something shining.
It's a strange small gold cylinder.
You pick it, observe it, and discover a small button on the side. You press it, and ghosh! You had a blight red light flashing into your eyes.

After some times, when the surprise is past, you understand that this small cylinder is a laser. You try it in your room, and discovers by pointing to different angles (0°, 90°, 180° and 270°) that the laser beam goes back at you. It probably means that this room is a rectangle, and that all sides are covered by a reflecting surface.

But at some angles you do not get back your beam. Maybe the corners are not reflexive? Maybe there are other people on each corner, and the laser beam stops at them?

If you knew the size UxV of the rectangle, could you guess at which corner the laser beam stopped and the length of the beam?

Note: for simplicity, the angle is 45°. If the angle was different (except for 0° and 90°), it would be the same problem as with an angle of 45° and a different shape (but probably not integers). And you can also forget the square root of 2 from the length.

Examples: (S is the starting corner, where you are)
U=V=2 => corner=B length=2
A██B
█ /█
█/ █
S██C



U=2 V=3 => corner=A length=6
 A███B
U█\/\█
 █/\/█
 S███C
   V


U=2 V=4 => corner=C length=4
 A████B
U█ /\ █
 █/  \█
 S████C
   V
Input
One line: Two integers U and V for the size of the rectangle.
Output
One line: The corner (A or B or C) at which the laser beam stopped, and the length (divided by √2) of the beam.
Constraints
1 ≤ U, V ≤ 100 000
length ≤ UxV
Example
Input
2 2
Output

'''

U, V = 'U', 'V'

T={}
T[U] = {U : 1, V : -1}
T[V] = {U : -1, V :1}


u, v = [int(i) for i in input().split()]
LAT={(U,-1):0, (U, 1): u, (V,-1):0, (V,1): v}

CORNER={(0,0):'A', (0,u):'S',(v,0):'B',(v,u):'C'}

MIRROR={(V,0):u, (V,u):0, (U,0):v, (U,v):0}

cur = V
side = u
pos = 0

vector = {U:-1, V:1}
ORTH={'U':'V','V':'U'}
length = 0


while True:
    newside = MIRROR[cur, side]
    distopposed = newside - side
    newpos = LAT[cur, vector[cur]]
    distlateral = newpos - pos
    
    
    if abs(distopposed) == abs(distlateral):
        length += abs(distopposed)
        if cur == V:
            corner = (newpos, newside)
        else:
            corner = (newside, newpos)
        break
    elif abs(distopposed) < abs(distlateral):
        # laser beam gets to the opposed wall
        side = newside
        pos += vector[cur] * abs(distopposed)
        length += abs(distopposed)

    else:
        # laser beam gets to the lateral wall
        cur=ORTH[cur]
        pos = side + (vector[cur] * abs(distlateral))
        side = newpos
        length += abs(distlateral)
    
    vector = {U:vector[U] * T[cur][U], V:vector[V] * T[cur][V]}

print("{} {}".format(CORNER[corner], length) )
