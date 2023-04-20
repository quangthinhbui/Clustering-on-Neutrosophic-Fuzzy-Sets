import numpy as np
from input import *
from similarity import *
from matrix import *
######### lambda-cutting #########
def lbd(m):
    temp = []
    for i in range(len(m)):
        temp += m[i]
    out = sorted(list(set(temp)))
    return out
######### lambda-cutting matrix #########
def lcmat(m,l):
    out = []
    for i in range(len(m)):
        temp = []
        for j in range(len(m)):
            if m[i][j] >= l:
                temp.append(1)
            else:
                temp.append(0)
        out.append(temp)
    return out
######### clustering label #########
def label(m):
    out = [0]*len(m)
    gr = 0
    dele = []
    for i in range(len(m)):
        if i in dele:
            for j in range(len(m)):
                if (j>i) and (m[i][j] == 1):
                    dele.append(j)
                    out[j] = out[i]
        if i not in dele:
            out[i] = gr
            for j in range(len(m)):
                if (j>i) and (m[i][j] == 1):
                    dele.append(j)
                    out[j] = out[i]
            gr += 1
    return out
######### clusters #########
def cluster(m):
    out = []
    for i in range(max(m)+1):
        temp = []
        for j in range(len(m)):
            if m[j] == i:
                temp.append(j)
        out.append(temp)
    return out
