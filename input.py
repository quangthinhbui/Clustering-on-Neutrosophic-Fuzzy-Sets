import numpy as np
######### File #########
def f(m):
    with open(m) as fm:
        content = fm.readlines()
        n = [x.strip() for x in content]
    s = [int(k) for k in n[0].split()]
    for j in range(1,s[0]+1):
        t = [float(k) for k in n[j].split()]
        out = np.resize(t,(s[1],4)).tolist()
    return out
def file(m):
    with open(m) as fm:
        content = fm.readlines()
        n = [x.strip() for x in content]
    s = [int(k) for k in n[0].split()]
    out = []
    for j in range(1,s[0]+1):
        t = [float(k) for k in n[j].split()]
        out.append(np.resize(t,(s[1],4)).tolist())
    return out
######### Random #########
def random(o,c):
#    o = int(input("Number of objects: "))
#    c = int(input("Number of criteria: "))
#    s = int(input("Seed: "))
    random.seed(7)
    out = []
    for i in range(c):
        out_c = []
        for j in range(o):
            out_o = []
            for k in range(4):
                if k == 0:
                    out_o.append(random.randint(1,9)/10)
                else:
                    out_o.append(random.randint(1,9)/10)
            out_c.append(out_o)
        out.append(out_c)
    return out