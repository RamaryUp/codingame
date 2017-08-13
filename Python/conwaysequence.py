# Codingame challenge
# Name : Conway Sequence
# Category : Classic puzzle - medium level
# URL : https://www.codingame.com/training/medium/conway-sequence
# Selected programming language : Python 3.5.3

from itertools import groupby

row, l = input(), int(input())

for i in range (1, l):
    digitslist = list(map(int, row.split()))
    groupeddigits=[(len(list(cs)), c) for c, cs in groupby(digitslist)]
    row = ' '.join(str(item[0]) + ' ' + str(item[1]) for item in groupeddigits)
print(row.strip())
