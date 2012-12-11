#!/opt/local/bin/python
'''
    In this programming problem and the next you'll code up the clustering algorithm from lecture for computing a max-spacing k-clustering. Download the text file here. This file describes a distance function (equivalently, a complete graph with edge costs). It has the following format:
    [number_of_nodes]
    [edge 1 node 1] [edge 1 node 2] [edge 1 cost]
    [edge 2 node 1] [edge 2 node 2] [edge 2 cost]
    ...
    There is one edge (i,j) for each choice of 1<=i<j<=n, where n is the number of nodes. For example, the third line of the file is "1 3 5250", indicating that the distance between nodes 1 and 3 (equivalently, the cost of the edge (1,3)) is 5250. You can assume that distances are positive, but you should NOT assume that they are distinct.

    Your task in this problem is to run the clustering algorithm from lecture on this data set, where the target number k of clusters is set to 4. What is the maximum spacing of a 4-clustering?

    ADVICE: If you're not getting the correct answer, try debugging your algorithm using some small test cases. And then post them to the discussion forum!
'''

import sys
import numpy as np
from unionfind import *

def cluster(node1,node2,distance,k):
    nodes = set(node1).union(node2)  # all nodes we have
    uf = UnionFind()                 # Union find structure
    uf.insert_objects(nodes)
    least = 0
    id = np.argsort(distance)
    path = []
    if k == 1:
        print "1 clusting: 0"
        return 0
    for i in range(len(nodes)-k):
        while uf.find(node1[id[least]]) == uf.find(node2[id[least]]):
            least += 1
        uf.union(node1[id[least]],node2[id[least]])
    while uf.find(node1[id[least]]) == uf.find(node2[id[least]]):
        least += 1
    spacing = distance[id[least]]
    #print uf
    return spacing

if __name__ == "__main__":
    data = np.loadtxt(sys.argv[1],skiprows=1)
    print cluster(data[:,0],data[:,1],data[:,2],np.int_(sys.argv[2]))