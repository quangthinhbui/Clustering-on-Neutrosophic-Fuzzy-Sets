import numpy as np
from input import *
from similarity import *
######### measure matrix #########
def mmat(m,mes):
    measure = {"mmm":sim_mmm,"rmm":sim_rmm,"mrmm":sim_mrmm,
               "mms":sim_mms,"mrms":sim_mrms,"dbs":sim_dbs,"dbd":sim_dbd,
               "d11":sim_d11,"d12":sim_d12,"d71":sim_d71,"d72":sim_d72,
               "s1":s1,"s2":s2,"s3":s3,"s4":s4,"s5":s5,"s6":s6,"s7":s7,"s8":s8,"s9":s9}
    out = []
    for i in range(len(m)):
        temp = []
        for j in range(len(m)):
            temp.append(round(measure[mes](m[i],m[j]),3))
        out.append(temp)
    return out
######### composition matrix #########
def cmat(m):
    out = []
    for i in range(len(m)):
        temp = []
        for j in range(len(m)):
            t = [min(m[i][k],m[k][j]) for k in range(len(m))]
            temp.append(max(t))
        out.append(temp)
    return out
######### equivalent composition matrix #########
def eqv(m):
    count = 0
    for i in range(len(m)):
        temp = []
        for j in range(len(m)):
            t = [min(m[i][k],m[k][j]) for k in range(len(m))]
            if max(t) <= m[i][j]:
                temp.append(1)
            else:
                temp.append(0)
        count += sum(temp)
    return count == len(m)**2
#####
def emat(m):
    while eqv(m) == 0:
        m = cmat(m)
    return m