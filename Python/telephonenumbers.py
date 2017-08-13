# Codingame challenge
# Name : Telephone numbers
# Category : Classic puzzle - medium level
# URL : https://www.codingame.com/training/medium/telephone-numbers
# Selected programming language : Python 3.5.3

import math

# returns : the number of new memory cell created
def queuedigits(contacts, remainingnumbers):
    createdcell = 0
    if len(remainingnumbers) == 0:
        return createdcell

    key = remainingnumbers[0]

    if key not in contacts:
        contacts[key] = {}
        createdcell = 1
        
    return createdcell + queuedigits(contacts[key], remainingnumbers[1:])
    
n = int(input())
contacts = {}
count = 0
for i in range(n):
    telephone = input()
    count += queuedigits(contacts, telephone)

print(count)
