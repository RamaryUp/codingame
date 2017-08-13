# Codingame challenge
# Name : DDCG Mapper
# Category : Community puzzles
# URL : https://www.codingame.com/training/community/ddcg-mapper

import sys

def getrow (couples, idx):
    resultrow = ['0' for i in range(len(couples[0][0]))]	# ['0','0','0','0']
    for couple in couples:
        tempo = couple[1]
        if idx % tempo == 0:
            pattern = couple[0]
            for i, character in enumerate(pattern):
                resultrow[i] = max(resultrow[i], character)	# Indeed, max('X','0') returns 'X'
    
    separator = ''    
    return separator.join(resultrow)

# Initialize	
nblines = int(input())
nbcouples = int(input())
couples = []

for i in range(nbcouples):
    pattern, tempo = input().split()
    tempo = int(tempo)
    couples.append((pattern, tempo))

# card motifs are written from bottom to top, so reverse order
for i in range(nblines, 0, -1):    
    print(getrow(couples, i))
