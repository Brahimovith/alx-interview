#!/usr/bin/python
def canUnlockAll(boxes):
    s = []
    for i in boxes:
        for j in i:
            s.append(j)
    
    l = set(s)
    print(l)
    for i in range(1,len(boxes)):
        if(i in l):
            continue
        return False
    return True
        

