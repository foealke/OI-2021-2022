import igraph
from igraph import layout
from igraph import Graph
import time
import os


input_path = input("Podaj path: ")
input_data = ""
with open(input_path, "r") as file:
    input_data = file.readlines()[1].replace("\n","")


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


def calc(dt):
    data = []

    data = dt.split(" ")
    data = list(map(int,data))

    sol = [[]] * len(data)
    sol[1] = data[0]
    sol[len(data)-2] = data[len(data)-1]
    sol[0] = [data[1]]
    sol[len(data)-1] = [data[len(data)-2]]
    taken = [False] * (len(data)+1)
    taken[data[len(data)-1]] = True
    taken[data[0]] = True


    for i in range(2, len(sol)-2):
        sol[i] = [ data[i-1], data[i+1] ]

    for i in range(2, len(sol)-2):
        if sol[i][0] == sol[i][1]:
            taken[sol[i][0]] = True
            sol[i] = sol[i][0]

    for i in range(2, len(sol)-2):
        if type(sol[i-2]) == int:
            if sol[i-2] != data[i-1]:
                sol[i] = data[i-1]
        if type(sol[i+2]) == int:
            if sol[i+2] != data[i+1]:
                sol[i] = data[i+1]

    # ctr = [0] * len(sol)

    for i in range(0, len(sol)):
        if type(sol[i]) == int:
            taken[sol[i]] = True

    for i in range(0, len(sol)):
        if type(sol[i]) == list:
            sol[i] = list(filter(lambda x: not taken[x], sol[i]))

    counter = [0] * (len(sol)+1)
    for i in range(0, len(sol)):
        if type(sol[i]) == int:
            counter[ sol[i] ] += 1 
        else:
            for x in sol[i]:
                counter[x] += 1
    
    updated = True
    while updated:
        updated = False
        for i in range(0, len(sol)):
            if type(sol[i] ) == list:
                for x in range(0, len(sol[i])):
                    if counter[ sol[i][x] ] == 1:
                        if len(sol[i]) > 1:
                            counter[ sol[i][not x] ] -= 1
                        sol[i] = sol[i][x] 
                        updated = True
                        continue
    
    sForPrint = ""
    for i in sol:
        if type(i) == int:
            sForPrint += "D"
            # sForPrint += bcolors.FAIL + "D" + bcolors.ENDC
        if type(i) == list:
            if len(i) == 2:
                sForPrint += "C"
                # sForPrint+= bcolors.OKGREEN + "C" + bcolors.ENDC
            if len(i) == 1:
                sForPrint += "B"
                # sForPrint+= bcolors.OKCYAN + "B" + bcolors.ENDC
            if len(i) == 0:
                sForPrint += "A"
                # sForPrint+= bcolors.OKBLUE + "A" + bcolors.ENDC

    return sForPrint

calculated = calc( input_data )

with open("output-bf.txt", "w") as file:
    file.write(calculated)

# print( calculated[0] )
# print( calculated[1] )
# taken = [ False ] * (len(calculated[0])+1)

# # [ text : parent ]
# tree = { "X":"X" }

# for i in range(0, len(calculated[0])):
#     if type(calculated[0][i]) == int:
#         taken[calculated[0][i]] = True

# recalculated = []

# for i in range(0,len(calculated[0])):
#     recalculated.append( calculated[0][i] )
#     if type(calculated[0][i]) != int:
#         recalculated[i] += calculated[1]

# def generateTree( index, taken, parent ):
#     idx = index
#     if ( idx >= len(recalculated) ): 
#             return
#     while type(recalculated[idx]) == int: 
#         idx+=1
#         if ( idx >= len(recalculated) ): 
#             return
#     for r in recalculated[idx]:
#         if not taken[r]:
#             t_c = taken.copy()
#             t_c[r] = True
#             tree[parent+" "+str(r)] = str(parent)
#             generateTree( idx+1, t_c, parent+" "+str(r) )


# generateTree(0, taken=taken.copy(), parent="X" )  
# tree_keys = sorted(list(tree.keys()))
# tree_elements = {}
# for i in range(0, len(tree_keys)):
#     tree_elements[ tree_keys[i] ] = i

# tree_connections = []
# for i in tree.keys():
#     tree_connections.append( [ tree_elements[i] , tree_elements[tree[i]] ] )

# g = Graph(n=len(tree_connections), edges=tree_connections )

# randomId = str(time.time())
# layout = g.layout_reingold_tilford(mode="in", root=0)
# igraph.Layout.scale(layout, 8)
# visual_style = {}
# visual_style["bbox"] = (16000,2000)
# visual_style["margin"] = 120
# g.vs["label"] = list(map(lambda x: x.split(" ")[-1],tree_keys))
# g.vs["label_size"] = 21
# igraph.plot(g, "./graphs/graph-"+randomId+".svg", layout=layout, root=0, vertex_size=40, **visual_style)
# os.system(".\graphs\graph-"+randomId+".svg")

    