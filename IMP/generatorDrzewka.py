import pandas as pd
import matplotlib.pyplot as plt
import itertools
import igraph
from igraph import layout
from igraph import Graph
import os


def genAllPermutations(series):
    return itertools.permutations(series);

N = int(input("Podaj n: "))

root_perm = "".join( map(lambda x: str(x),range(1,N+1)) )
perm_final_cost = {}

perm_tree = { root_perm: [ root_perm, 0 ] }

def tree_connect(child, parent, weight):
    perm_tree[child] = [ parent, weight ]

def slow_sort(perm):
    c_perm = list(perm)
    sortd = False
    steps = 0;
    while not sortd:
        if c_perm[0] == 1:
            if c_perm == list(range(1, len(perm)+1)):
                sortd=True
                break
        child_perm = "".join( map(lambda x: str(x), c_perm) )
        weight = 0
        if c_perm[0] != 1:
            _temp = c_perm.index(c_perm[0]-1)
            weight = _temp
            steps+=_temp
            c_perm.remove( c_perm[0]-1 )
            c_perm.insert(0, c_perm[0]-1)
        else:
            _temp = c_perm.index(N)
            weight = _temp
            steps+=_temp
            c_perm.remove(N)
            c_perm.insert(0, N)  
        parent_perm = "".join( map(lambda x: str(x), c_perm) )
        tree_connect( child_perm, parent_perm, weight )
    perm_final_cost[ "".join( map(lambda x: str(x),perm) ) ] = steps
    return steps
 
for i in genAllPermutations( range(1, N+1) ):
    slow_sort(i)


# Generate a tree with igraph

tree_elements = {}
tree_keys = sorted(list(perm_tree.keys()))
for i in range(0, len(tree_keys)):
    tree_elements[ tree_keys[i] ] = i

tree_connections = []
weights = []
for i in perm_tree.keys():
    if i != root_perm:
        tree_connections.append( [ tree_elements[i] , tree_elements[perm_tree[i][0]] ] )
        weights.append( perm_tree[i][1] )

# print(tree_connections)
# print(weights)
g = Graph(n=len(tree_connections), edges=tree_connections )
g.vs["label"] = list(map(lambda x: perm_final_cost[x], tree_keys))
g.es["label"] = weights
g.es["lable_size"] = 40
layout = g.layout_reingold_tilford(mode="in", root=0)
igraph.Layout.scale(layout, 8)
visual_style = {}
visual_style["bbox"] = (20000,1000)
visual_style["margin"] = 80
visual_style["vertex_label_size"] = 4
igraph.plot(g, "graph-"+str(N)+".svg", layout=layout, root=0, vertex_size=0, **visual_style)


print(g)


os.system(".\graph-"+str(N)+".svg")
