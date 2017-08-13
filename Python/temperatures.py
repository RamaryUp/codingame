# Codingame challenge
# Name : Temperatures
# Category : Classic puzzle - easy
# URL : https://www.codingame.com/training/easy/temperatures
# Selected programming language : Python 3.5.3
'''
-----------------------------------------------------------------------------------
 	The Goal

In this exercise, you have to analyze records of temperature to find the closest to zero.

	
Sample temperatures
Here, -1 is the closest to 0.
 	Rules

Write a program that prints the temperature closest to 0 among input data. If two numbers are equally close to zero, positive integer has to be considered closest to zero (for instance, if the temperatures are -5 and 5, then display 5).
 	Game Input

Your program must read the data from the standard input and write the result on the standard output.
Input
Line 1: N, the number of temperatures to analyze

Line 2: A string with the N temperatures expressed as integers ranging from -273 to 5526

Output
Display 0 (zero) if no temperatures are provided. Otherwise, display the temperature closest to 0.
Constraints
0 ≤ N < 10000
Example
Input
5
1 -2 -8 4 5
Output
-----------------------------------------------------------------------------------
'''
import math

n = int(input())  # the number of temperatures to analyse
temps = input().split()  # the n temperatures expressed as integers ranging from -273 to 5526
best = int(temps[0]) if n > 0 else 0

for temp in [int(i) for i in temps[1:]]:    
    if abs(temp) < abs(best):           
        best = temp

    elif best < 0 and best == -temp:
        best = temp
print(best)
