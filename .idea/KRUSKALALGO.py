import numpy as np
import math


class Graph:
    def __init__(self, v):
        self.v = v
        self.adjmatrix = np.full((v, v), math.inf, dtype=float)

    def addedge(self, m, l, w):
        self.adjmatrix[m-1][l-1] = w

    def adj(self, u):
        k = []
        for j in range(self.v):
            if self.adjmatrix[int(u)][j] != math.inf:
                k.append(j)
        for j in range(self.v):
            if self.adjmatrix[j][int(u)] != math.inf:
                k.append(j)
        return k


vertexlist = []
Q = []
E = []
print("Enter the number of vertex : ")
n = int(input())
G = Graph(n)
for i in range(n):
    vertexlist.append([i])
print("Enter the number of edges ")
c = int(input())
print("Enter the edge from to and weight ")
for i in range(c):
    o = input().split(" ")
    G.addedge(int(o[0]), int(o[1]), int(o[2]))
    E.append([int(o[2]), int(o[0]), int(o[1]) ])
for i in sorted(E, key= lambda x: x[0]):
    if i[1] - 1 not in vertexlist[i[2] - 1] and i[2] - 1 not in vertexlist[i[1] - 1]:
        Q.append([i[1], i[2]])
        for k in vertexlist[i[2] - 1]:
            vertexlist[i[1] - 1].append( k )
        for k in vertexlist[i[1] - 1]:
            vertexlist[i[2] - 1].append( k )
print("The Edges of  MST is ")
for i in Q:
    print("(",i[0],i[1],")")