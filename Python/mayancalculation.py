# Codingame challenge
# Name : Mayan Calculation
# Category : Classic puzzle - medium level
# URL : https://www.codingame.com/training/medium/mayan-calculation
# Selected programming language : Python 3.5.3

'''
-----------------------------------------------------------------------------------
	The Goal

Upon discovering a new Maya site, hundreds of mathematics, physics and astronomy books have been uncovered.

The end of the world might arrive sooner than we thought, but we need you to be sure that it doesn't!

Thus, in order to computerize the mayan scientific calculations, you're asked to develop a program capable of performing basic arithmetical operations between two mayan numbers.
 	Rules

The mayan numerical system contains 20 numerals going from 0 to 19. Here's an ASCII example of their representation:
0	1	2	3	4	5	6	7	8	9
.oo.
o..o
.oo.
....	o...
....
....
....	oo..
....
....
....	ooo.
....
....
....	oooo
....
....
....	....
----
....
....	o...
----
....
....	oo..
----
....
....	ooo.
----
....
....	oooo
----
....
....
10	11	12	13	14	15	16	17	18	19
....
----
----
....	o...
----
----
....	oo..
----
----
....	ooo.
----
----
....	oooo
----
----
....	....
----
----
----	o...
----
----
----	oo..
----
----
----	ooo.
----
----
----	oooo
----
----
---- A mayan number is divided into vertical sections. Each section contains a numeral (from 0 to 19) representing a power of 20. The lowest section corresponds to 200, the one above to 201 and so on.

Thereby, the example below is : (12 x 20 x 20) + (0 x 20) + 5 = 4805



To spice the problem up, the mayans used several dialects, and the graphical representation of the numerals could vary from one dialect to another.
 
The representation of the mayan numerals will be given as the input of your program in the form of ASCII characters. You will have to display the result of the operation between the two given mayan numbers. The possible operations are *, /, +, -
 	Game Input

Input
Line 1: the width L and height H of a mayan numeral.

H next lines: the ASCII representation of the 20 mayan numerals. Each line is (20 x L) characters long.

Next line: the amount of lines S1 of the first number.

S1 next lines: the first number, each line having L characters.

Next line: the amount of lines S2 of the second number.

S2 next lines: the second number, each line having L characters.

Last line: the operation to carry out: *, /, +, or -

Output
The result of the operation in mayan numeration, H lines per section, each line having L characters.
Constraints
0 < L, H < 100
0 < S1, S2 < 1000
The remainder of a division is always 0.
The mayan numbers given as input will not exceed 263.
Example
Input
4 4
.oo.o...oo..ooo.oooo....o...oo..ooo.oooo____o...oo..ooo.oooo____o...oo..ooo.oooo
o..o................____________________________________________________________
.oo.........................................____________________________________
................................................................________________
4
o...
....
....
....
4
o...
....
....
....
+
Output
oo..
....
....
....

-----------------------------------------------------------------------------------
'''

import math

def getmayanumber(H):
    s = int(input())
    nbmayadigits = s // H
    mayanb = [ [] for x in range(nbmayadigits) ]
    for i in range(s):
        num_line = input()
        digitpower = nbmayadigits - (i // H) - 1
        mayanb[digitpower].append(num_line)
    return mayanb


def mayatointdigits(ref, mayanb):
    intdigits = [0 for x in range(len(mayanb))]
    for i, elem in enumerate(mayanb):
        intdigits[i] = ref.index(elem)
    return intdigits

def intdigitstointvalue(intdigits):
    total = 0
    for i, value in enumerate(intdigits):
        total += value * (20 ** i)
    return total

def operateint(operator, intvalue1, intvalue2): 
    return intvalue1 * intvalue2 if operator == '*' \
        else intvalue1 // intvalue2 if operator == '/' \
        else intvalue1 + intvalue2 if operator == '+' \
        else intvalue1 - intvalue2 if operator == '-' \
        else 0

def inttoserializedmaya(intvalue):
    power = 0
    temp = intvalue
    serializedmaya=[]

    while True:
        modulo = temp % (20 ** (power + 1))
        multiplier = modulo // (20 ** power)
        serializedmaya.append(multiplier)
        
        if temp == modulo:
            break
        power += 1
        temp = temp - modulo
    return serializedmaya
    
def printserializedmaya(ref, serializedmaya):
    # at index N there is the maya digit power N
    for mayadigit in serializedmaya[::-1]:
        for line in ref[mayadigit]:
            print(line)

def operatemaya(ref, operator, mayanb1, mayanb2):
    intdigits1 = mayatointdigits(ref, mayanb1)
    intvalue1 = intdigitstointvalue(intdigits1)
    intdigits2 = mayatointdigits(ref, mayanb2)
    intvalue2 = intdigitstointvalue(intdigits2)
    intresult = operateint(operator, intvalue1, intvalue2)
    return inttoserializedmaya(intresult)


L, H = [int(i) for i in input().split()]

# initialize the Maya references
ref = [ [] for x in range(20) ]
# feed the Maya dictionary
for i in range(H):
    numeral = input()
    for mayadigit in range(20):
        part = numeral[L * mayadigit: L * (mayadigit+1)]
        ref[mayadigit].append(part)
        
mayanb1 = getmayanumber(H)
mayanb2 = getmayanumber(H)
operation = input()
serializedmayaresult = operatemaya(ref, operation, mayanb1, mayanb2)
printserializedmaya(ref, serializedmayaresult)