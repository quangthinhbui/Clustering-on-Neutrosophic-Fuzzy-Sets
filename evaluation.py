import numpy as np
from sklearn.metrics import davies_bouldin_score
from sklearn.metrics import silhouette_score
from input import *
from measure import *
from matrix import *
from clustering import *
######### embedding #########
def emb(v):
    out = []
    for i in range(len(v)):
        for j in range(4):
            out.append(v[i][j])
    return out
def obj(m):
    out = []
    for i in range(len(m)):
        out.append(emb(m[i]))
    return out
