import numpy as np
from input import *
######### mean min-max #########
def abd(a,b):
    return sum([min(a[i],b[i]) for i in range(4)])
def abu(a,b):
    return sum([max(a[i],b[i]) for i in range(4)])
def sim_mmm(a,b):
    temp = []
    for i in range(len(a)):
        temp.append(abd(a[i],b[i])/abu(a[i],b[i]))
    out = np.mean(temp)
    return out
######### ratio min-max #########
def sim_rmm(a,b):
    mi = []
    ma = []
    for i in range(len(a)):
        mi.append(abd(a[i],b[i]))
        ma.append(abu(a[i],b[i]))
    out = sum(mi)/sum(ma)
    return out
######### mean ratio min-max #########
def mr(a,b):
    temp = [min(a[i],b[i])/max(a[i],b[i]) for i in range(4)]
    print(temp)
    out = np.mean(temp)
    return out
def sim_mrmm(a,b):
    temp = []
    for i in range(len(a)):
        temp.append(mr(a[i],b[i]))
    out = np.mean(temp)
    return out
######### mean max square #########
def sq(a,b):
    temp = [abs(a[i]**2-b[i]**2) for i in range(4)]
    out = (1-max(temp))/(1+max(temp))
    return out
def sim_mms(a,b):
    temp = []
    for i in range(len(a)):
        temp.append(sq(a[i],b[i]))
    out = np.mean(temp)
    return out
######### mean ratio max square #########
def sim_mrms(a,b):
    temp = []
    for i in range(len(a)):
        temp.append(mr(a[i],b[i]))
    out = np.mean(temp)
    return out