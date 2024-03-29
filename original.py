import numpy as np
import math
import random
##############################
# NF-subset or NF-supset?
##############################
def issubset(a,b):
    count = 0
    for i in range(len(a)):
        if (a[i][0] <= b[i][0]) and (a[i][1] <= b[i][1]) and (a[i][2] >= b[i][2]) and (a[i][3] >= b[i][3]):
            count += 1
    if count == len(a):
        return 1
    else:
        return 0
##############################
# Operations on NF-set
##############################
def complement(a):
    out = []
    for i in range(len(a)):
        temp = []
        for j in range(4):
            if j%2 == 0:
                temp.append(round(1-a[i][j],2))
            elif j == 1:
                temp.append(round(a[i][3],2))
            else:
                temp.append(round(a[i][1],2))
        out.append(temp)
    return out
#########
def intersection(a,b):
    out = []
    for i in range(len(a)):
        temp = []
        for j in range(4):
            if j < 2:
                temp.append(min(a[i][j],b[i][j]))
            else:
                temp.append(max(a[i][j],b[i][j]))
        out.append(temp)
    return out
#########
def union(a,b):
    out = []
    for i in range(len(a)):
        temp = []
        for j in range(4):
            if j < 2:
                temp.append(max(a[i][j],b[i][j]))
            else:
                temp.append(min(a[i][j],b[i][j]))
        out.append(temp)
    return out