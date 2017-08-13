# Codingame challenge
# Name : Minimal number of swaps
# Category : Community puzzles
# URL : https://www.codingame.com/training/easy/minimal-number-of-swaps
# Selected programming language : Python 3.5.3

'''
-----------------------------------------------------------------------------------
	Goal

Given a list of 1 and 0, you must regroup all the 1 at the begin of the list in a minimum number of steps.
A step is the interchange of two elements located at different positions.

The expected result is the minimum number of steps required to obtain a sorted list.
Input
Line 1: an integer N.
Line 2: a list of N numbers that can take the values 0 or 1.
Output
Line 1 : The minimum number of steps to regroup all the 1 at the beginning of the list.
Constraints
1 ≤ N < 500
Example
Input
5
1 0 1 0 1
Output
1
-----------------------------------------------------------------------------------	
'''

n, l = int(input()), input().split()

nb1 = l.count('1')
# The nummber of swaps required is equal to the number of "1" that are not yet grouped in the target block of "1"
nbexchanges = l[nb1:].count('1')

print(nbexchanges)
