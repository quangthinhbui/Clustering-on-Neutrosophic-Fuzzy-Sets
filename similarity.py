import numpy as np
import math
from input import *
######### mean min-max #########
def sim_mmm(a,b):
    temp = 0
    for i in range(len(a)):
        mi = sum([min(a[i][j],b[i][j]) for j in range(4)])
        ma = sum([max(a[i][j],b[i][j]) for j in range(4)])
        temp += mi/ma
    out = temp/len(a)
    return out
######### ratio min-max #########
def sim_rmm(a,b):
    num = 0
    den = 0
    for i in range(len(a)):
        mi = sum([min(a[i][j],b[i][j]) for j in range(4)])
        ma = sum([max(a[i][j],b[i][j]) for j in range(4)])
        num += mi
        den += ma
    out = num/den
    return out
######### mean ratio min-max #########
def sim_mrmm(a,b):
    temp = 0
    for i in range(len(a)):
        temp += sum([min(a[i][j],b[i][j])/max(a[i][j],b[i][j]) for j in range(4)])/4
    out = temp/len(a)
    return out
######### mean max square #########
def sim_mms(a,b):
    temp = 0
    for i in range(len(a)):
        t = max([abs(a[i][j]**2-b[i][j]**2) for j in range(4)])
        temp += (1 - t) / (1 + t)
    out = temp/len(a)
    return out
######### mean ratio max square #########
def sim_mrms(a,b):
    num = 0
    den = 0
    for i in range(len(a)):
        t = max([abs(a[i][j]**2-b[i][j]**2) for j in range(4)])
        num += 1 - t
        den += 1 + t
    out = num/den
    return out
######### distance-based #########
def dp(p,a,b):
    temp = 0
    for i in range(len(a)):
        t = sum([abs(a[i][j]-b[i][j])**p for j in range(4)])/4
        temp += t
    out = (temp/len(a))**(1/p)
    return out
def dvc(a,b):
    temp = 0
    for i in range(len(a)):
        t = max([abs(a[i][j]-b[i][j]) for j in range(4)])
        temp += t
    out = (temp/len(a))
    return out
def sim_dbs(a,b):
    out = 1 - dp(2,a,b)
    return out
def sim_dbd(a,b):
    out = (1 - dp(2,a,b))/(1 + dp(2,a,b))
    return out
def sim_d11(a,b):
    out = 1 - dp(1,a,b)
    return out
def sim_d12(a,b):
    out = (1 - dp(1,a,b))/(1 + dp(1,a,b))
    return out
def sim_d71(a,b):
    out = 1 - dp(7,a,b)
    return out
def sim_d72(a,b):
    out = (1 - dp(7,a,b))/(1 + dp(7,a,b))
    return out
def sim_dvc1(a,b):
    out = 1 - dvc(a,b)
    return out
def sim_dvc2(a,b):
    out = (1 - dvc(a,b))/(1 + dvc(a,b))
    return out
##############################
# Similarity
##############################
def s1(a,b):
    temp = 0
    for i in range(len(a)):
        t = [math.sqrt(2)*math.cos((a[i][j]-b[i][j])*math.pi/4) for j in range(4)]
        temp += (math.sqrt(2)+1)/4*(sum(t)-4)
    out = temp/len(a)
    return out
#########
def s2(a,b):
    temp = 0
    for i in range(len(a)):
        t = [abs(a[i][j]-b[i][j]) for j in range(4)]
        temp += 1-sum(t)/len(t)
    out = temp / len(a)
    return out
#########
def s3(a,b):
    temp = 0
    for i in range(len(a)):
        t = [abs(a[i][j]-b[i][j]) for j in range(4)]
        temp += math.log(2-sum(t)/len(t),2)
    out = temp / len(a)
    return out
#########
def s4(a,b):
    temp = 0
    for i in range(len(a)):
        t = [abs(a[i][j]-b[i][j]) for j in range(4)]
        temp += 1-math.log(1+sum(t)/len(t),2)
    out = temp / len(a)
    return out
#########
def s5(a,b):
    temp = 0
    for i in range(len(a)):
        t = [abs(a[i][j]-b[i][j]) for j in range(4)]
        temp += (math.exp(-sum(t)/len(t))-math.exp(-1))/(1-math.exp(-1))
    out = temp / len(a)
    return out
#########
def s6(a,b):
    temp = 0
    for i in range(len(a)):
        t = [abs(a[i][j]-b[i][j]) for j in range(4)]
        temp += 1-math.sin(sum(t)*math.pi/8)
    out = temp / len(a)
    return out
#########
def s7(a,b):
    temp = 0
    for i in range(len(a)):
        t = [abs(a[i][j]-b[i][j]) for j in range(4)]
        temp += math.cos(sum(t)*math.pi/8)
    out = temp / len(a)
    return out
#########
def s8(a,b):
    temp = 0
    for i in range(len(a)):
        t = [abs(a[i][j]-b[i][j]) for j in range(4)]
        temp += 1-math.tan(sum(t)*math.pi/16)
    out = temp / len(a)
    return out
#########
def s9(a,b):
    temp = 0
    for i in range(len(a)):
        t = [abs(a[i][j]-b[i][j]) for j in range(4)]
        temp += math.cos(math.pi/4+sum(t)*math.pi/16)/math.sin(math.pi/4+sum(t)*math.pi/16)
    out = temp / len(a)
    return out