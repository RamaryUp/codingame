# Codingame challenge
# Name : Stock Exchange Losses
# Category : Classic puzzle - medium level
# URL : https://www.codingame.com/training/medium/stock-exchange-losses
# Selected programming language : Python 3.5.3

'''
-----------------------------------------------------------------------------------	
	The Goal

A finance company is carrying out a study on the worst stock investments and would like to acquire a program to do so. The program must be able to analyze a chronological series of stock values in order to show the largest loss that it is possible to make by buying a share at a given time t0 and by selling it at a later date t1. The loss will be expressed as the difference in value between t0 and t1. If there is no loss, the loss will be worth 0.
 	Game Input

Input
Line 1: the number n of stock values available.

Line 2: the stock values arranged in order, from the date of their introduction on the stock market v1 until the last known value vn. The values are integers.

Output
The maximal loss p, expressed negatively if there is a loss, otherwise 0.
Constraints
0 < n < 100000
0 < v < 231
Examples

Input
6
3 2 4 2 1 5
Output
-3

Input
6
5 3 4 2 3 1
Output
-4

Input
5
1 2 4 4 5
Output
-----------------------------------------------------------------------------------
'''

max_loss = 0
n = int(input())

numbers = [int(i) for i in input().split()]
prev_max = prev_min = numbers[0]

for i in range(1, n):
    v = numbers[i]
    if v > prev_max:
        prev_max = prev_min = v
    elif v < prev_min:
            prev_min = v
            max_loss = min(max_loss, prev_min - prev_max)
print(max_loss)
