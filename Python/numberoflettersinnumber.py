# Codingame challenge
# Name : Number of letters in a number - binary
# Category : Community puzzles
# URL : https://www.codingame.com/training/community/number-of-letters-in-a-number---binary
# Selected programming language : Python 3.5.3

'''
-----------------------------------------------------------------------------------	
Find the nth term in the sequence starting with S(0) = start and defined by the rule:

Given a term in the sequence, S(i), the next term, S(i+1) can be found by counting the letters (ignoring whitespace) in the spelled-out binary representation of S(i).

As an example, starting from 5 (S(0) = 5), we convert to the binary representation, 101, then spell it out as an English string "one zero one", and count the letters which yields 10 (S(1) = 10).
Input
Line 1: integers start and n, separated by a space
Output
Line 1: the nth term in the sequence, expressed as an integer
Constraints
1 ≤ n ≤ 10^18
1 ≤ start ≤ 10^18
Example
Input
5 2
Output
14
-----------------------------------------------------------------------------------	
'''
start, n = [int(i) for i in input().split()]
ZERO_LENGTH, ONE_LENGTH = 4, 3

sequenceoutput = start
for i in range(n):
    binaryrepresentation = bin(sequenceoutput)[2:]  # remove the 0b prefix of 0b0110110
    nbletters = binaryrepresentation.count('0')*ZERO_LENGTH + binaryrepresentation.count('1')*ONE_LENGTH
    # there is a moment, when n is big, where sequence == nbletters undefinitely
    if sequenceoutput != nbletters:
        sequenceoutput = nbletters
    else:
        break
    
print(sequenceoutput)
