# Codingame challenge
# Name : ASCII Art
# Category : Classic puzzle - easy
# URL : https://www.codingame.com/training/easy/ascii-art
# Selected programming language : Python 3.5.3

IDX_QUESTION_MARK = 26

l = int(input())
h = int(input())
text = input()
dict = {}

for i in range(h):
    row = input()
    for j, character in enumerate(row):
        dict[i,j] = character

line = {}        
for i in range(h):        
    line[i]=''
    for character in text.upper():
        base_index = l * (ord(character) - ord('A')) if 'A' <= character <= 'Z' else l * IDX_QUESTION_MARK
        for j in range(l):
            line[i] += dict[i, base_index+j]

for i in range(h):
    print(line[i])
