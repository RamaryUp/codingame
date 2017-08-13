# Codingame challenge
# Name : Kolakoski Sequence
# Category : Community puzzles
# URL : https://www.codingame.com/training/community/kolakoski-sequence

'''
-----------------------------------------------------------------------------------	
	Goal

A Kolakoski sequence, named after William Kolakoski, is an infinite sequence of digits whose run lengths reduce to the sequence itself.

For example, the Kolakoski sequence for the numbers 1 and 2 is
1,2,2,1,1,2,1,2,2,1,2,2,1,1,2,1,1,2,2,1,2,1,1,2,1,2,2,1,1…
because, when writing down the successive run lengths of 1s and 2s, you get the same sequence back:

Sequence:    1  2 2  1 1  2  1  2 2  1  2 2 …
             ↕   ↕    ↕   ↕  ↕   ↕   ↕   ↕
Run lengths: 1   2    2   1  1   2   1   2  …  ← same sequence
Your goal is to output the first N elements of the Kolakoski sequence given its first two distinct digits A and B.
Input
Line 1: The number N of digits to output
Line 2: The digits A and B which will form the sequence, in that order
Output
The Kolakoski sequence, without any separator.
Constraints
1 ≤ N ≤ 1000
1 ≤ A ≤ 9
1 ≤ B ≤ 9
A ≠ B
Example
Input
10
1 2
Output
1221121221
-----------------------------------------------------------------------------------	
'''

class Finished(Exception):
    pass

n = int(input())
pair =[int(i) for i in input().split()]

alternateseqidx = 0
nextruns = []
idxrun = 0
runlength = c = pair[0]

try:
    while True:
        for length in range(runlength):
            nextruns.append(pair[alternateseqidx])
            if len(nextruns) >= n:
                raise Finished  # it's a way to break both the inner for loop and while loop
        alternateseqidx = (alternateseqidx + 1) % 2    
        idxrun += 1
        c = pair[alternateseqidx]                

        if idxrun == len(nextruns):
            nextruns.append(c)
            runlength = c-1
        else:
            runlength = nextruns[idxrun]

except Finished:
    print(''.join(map(str, nextruns)))
    pass
