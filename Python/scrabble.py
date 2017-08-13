# Codingame challenge
# Name : Scrabble
# Category : Classic puzzle - medium level
# URL : https://www.codingame.com/training/medium/scrabble
# Selected programming language : Python 3.5.3

from itertools import groupby

# INITIALIZATION --------------------------------------------------------
points={}
points[1]='eaionrtlsu'
points[2]='dg'
points[3]='bcmp'
points[4]='fhvwy'
points[5]='k'
points[8]='jx'
points[10]='qz'

lettersval={}
for i in list(points.keys()):
    for letter in points[i]:
        lettersval[letter] = i

n = int(input())
words = [input() for i in range(n)]
letters = list(input())

# PROCESSING --------------------------------------------------------
letters.sort()
countrandomletters={c: len(list(cs)) for c,cs in groupby(letters)}

bestscore = -1

for candidate in words:
    letters = list(candidate)
    letters.sort()
    countcandidateletters={c: len(list(cs)) for c,cs in groupby(letters)}
    
    total = 0
    for letter, count in countcandidateletters.items():
        try:
            if count <= countrandomletters[letter]:
                total += count * lettersval[letter]
            else:
                total = -1
                break
        except KeyError:
            total = -1
            break
    if total > bestscore:
        bestword = candidate
        bestscore = total

print(bestword)
