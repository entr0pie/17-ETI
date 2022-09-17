from random import shuffle
from copy import deepcopy

def array(string):
    array = []
    for char in string:
        array.append(char)
    return array

def toString(array) -> str:
    string = ""
    for char in array:
        string += char
    return string

line = str(input(">> ")).lower().strip()
original = array(line)

pos = []
for i in range(1000):
    copy = deepcopy(original)
    shuffle(copy)
    new_pos = toString(copy) 
    if new_pos not in pos:
        pos.append(new_pos)

for p in pos:
    print(p)
