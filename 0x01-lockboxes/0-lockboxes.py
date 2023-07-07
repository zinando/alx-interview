#!/usr/bin/python3

def canUnlockAll(boxes):
     new = []
     for x in box:
        if len(x)>0:
           for i in x:
              if i not in new:
                 new.append(i)

     for k in range(len(box)):
        if k not in new and k !=0:
           return False
     return True
