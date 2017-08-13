# Codingame challenge
# Name : Dwarfs standing on the shoulders of giants
# Category : Classic puzzle - medium level
# URL : https://www.codingame.com/training/medium/dwarfs-standing-on-the-shoulders-of-giants
# Selected programming language : Python 3.5.3

def saverelationship(dico, x, y):
    if x in dico:
        dico[x].append(y)
    else:
        dico[x]=[y]
    if y not in dico:
        dico[y]=[]

def getfarthest(dico, dicolongest, node):
    # longest distance is cached in memory from node to farthest suceeding node
    if node in dicolongest:
        return dicolongest[node]

    nearfarthest = 0
    
    for nextnode in dico[node]:
        dicolongest[nextnode] = getfarthest(dico, dicolongest, nextnode) 
        if dicolongest[nextnode] > nearfarthest:
            nearfarthest = dicolongest[nextnode]
    
    return 1 + nearfarthest

# longest relationship from x to the farthest influenced by x
# if distance == 1, it means it is a leaf of the graph
def getlongestrelationship(dico):
    return max(longest for longest in [getfarthest(dico, {}, node) for node in list(dico.keys())])
            
n = int(input())  # the number of relationships of influence
dico={}
for i in range(n):
    # x: a relationship of influence between two people (x influences y)
    x, y = [int(j) for j in input().split()]
    saverelationship(dico, x, y)
    longest = getlongestrelationship(dico)

print(longest)
