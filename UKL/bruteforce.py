import itertools
import pandas as pd
import csv
import matplotlib.pyplot as plt
import os

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def genAllPermutations(series):
    return itertools.permutations(series);

tree_branches_counter = {}

perm_counter = {}

def slow_sort(perm):
    c_perm = list(perm)
    sortd = False
    steps = 0;
    s_type = -1
    time = 0
    # sort type finding time
    s_t_f_t = -1
    if perm[0] == len(perm):
        s_t_f_t = 0
        s_type = 3
    while not sortd:
        p = "".join(map(lambda x: str(x), c_perm))
        if p in perm_counter.keys():
            perm_counter[p]+=1
        else:
            perm_counter[p]=1
        if c_perm[0] == 1:
            if sorted(c_perm) == c_perm:
                if s_type == -1:
                    s_t_f_t = time
                    s_type = 2
                sortd=True
                break
        time+=1
        if c_perm[0] != 1:
            _temp = c_perm.index(c_perm[0]-1)
            steps+=_temp
            if _temp in tree_branches_counter.keys():
                tree_branches_counter[_temp]+=1
            else:
                tree_branches_counter[_temp]=1
            c_perm.remove( c_perm[0]-1 )
            c_perm.insert(0, c_perm[0]-1)
        else:
            _temp = c_perm.index(N)
            steps+=_temp
            if _temp in tree_branches_counter.keys():
                tree_branches_counter[_temp]+=1
            else:
                tree_branches_counter[_temp]=1
            c_perm.remove(N)
            c_perm.insert(0, N)
        if c_perm[0]==len(perm):
            s_t_f_t = time
            s_type = 1
        
    return (steps, s_type, s_t_f_t, time)
 
N = int(input("Podaj n: "))

def calcDistance( base, perm ):
    pos = {}
    for i in range(0, N):
        pos[base[i]] = i
    val = 0
    for i in range(0, N):
        val += abs(pos[ perm[i] ] - i)
    return val

# counter = {}

# sm=0
# if not os.path.isfile("./data-for-"+str(N)+".csv"):
ctr = []
tst = [ 0 ] * (N+1)
typeCounter = [ 0, 0, 0, 0 ] 
s_o_a = 0
sg = [0,0,0,0]

for i in genAllPermutations(range(1,N+1)):
    ss, s_t, s_t_f_t, time = slow_sort(i)
    # if ss in counter:
    #     counter[ss] += 1
    # else:
    #     counter[ss] = 1
# data = ""
# for k in sorted(counter.keys()):
#     data += str(k) +";" + str(counter[k]) + "\n"
    # print(ss, ": ", i, " - ", calcDistance(list(range(1, N+1)), i) )
    dst = calcDistance(list(range(1, N+1)), i)
    # if ss in ctr:
    #     ctr[ss] += dst
    # else:
    #     ctr[ss] = dst
    # with open("data-for-"+str(N)+".csv", "a") as file:
    #     file.write(data)
    #     file.close()
    tst[ i[0] ] += ss
    typeCounter[s_t] += ss
    s_o_a += ss
    ctr.append( (ss, i, dst, s_t, s_t_f_t, time) )
    if i[0] == N:
        sg[1] += ss
    elif i[0] == N-1:
        sg[2] += ss
    elif i[0] == 1:
        sg[0] += ss
    else:
        sg[3] += ss

colrs = [bcolors.OKGREEN, bcolors.FAIL, bcolors.OKCYAN, bcolors.WARNING, bcolors.OKBLUE]



# f_data = ""

# for i in typeCounter:
#     f_data += str(i) + ";"

# with open("typeCounter-"+str(N)+".csv", "a+") as file:
#     file.write(f_data)



def translate_sort_type(i):
    if i==1:
        return "Starting perm is not p[0]=N but transfers to p[0]=N"
    if i==2:
        return "Transforms noramly"
    if i==3:
        return "Starts with p[0]=N"
    return "other"
    
def short(s):
    if len(s) > 16:
        return s[0:16]+"..."
    return s

sb= [  ]

for i in range(0, N+1):
    sb.append([0] * (N+1))
print("Operations:\tPerm:\tDst.\t     Sort Type\t\t\t\tstft.\ttime")
for i in sorted(ctr):
    perm = ""
    for c in i[1]:
        perm += colrs[ c % len(colrs) ] + ""  + str(c) + ""
    # sb[i[3]][ i[1][0] ] += i[2]
    # if i[0] >= (N-3)*(N-1) and i[0] <= N*(N+1):
    # print(i[0], ": \t\t", perm, "\t", bcolors.ENDC, i[2], "\t", "(",i[3],")" ,short(translate_sort_type( i[3] )), "\t\t", i[4], "\t", i[5] )
print(sb)
print(s_o_a)
print(tst)
print(typeCounter)
print(sg)
# print(perm_counter)
sorted_perm_counter = {k: v for k, v in sorted(perm_counter.items(), key=lambda item: item[1])}
for i in sorted_perm_counter:
    if sorted_perm_counter[i] > 1:
        print(i,": ",sorted_perm_counter[i])
# for i in sorted(tree_branches_counter.keys()):
#     print(i,": ",tree_branches_counter[i])

# for i in sorted(ctr.keys()):
#     print(i, ": ", ctr[i])

    # print('Saved data as "'+"data-for-"+str(N)+".csv"+'"')
    # df = pd.read_csv("data-for-"+str(N)+".csv", names=["ilosc operacji","ilosc permutacji"], delimiter=";")
    # plt.plot(df["ilosc operacji"], df["ilosc permutacji"] )
    # plt.savefig("graphs/data-for-"+str(N)+".png")
