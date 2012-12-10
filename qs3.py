#!/opt/local/bin/python

'''
    In this programming problem you'll code up Prim's minimum spanning tree algorithm. Download the text file here. This file describes an undirected graph with integer edge costs. It has the format
    [number_of_nodes] [number_of_edges]
    [one_node_of_edge_1] [other_node_of_edge_1] [edge_1_cost]
    [one_node_of_edge_2] [other_node_of_edge_2] [edge_2_cost]
    ...
    For example, the third line of the file is "2 3 -8874", indicating that there is an edge connecting vertex #2 and vertex #3 that has cost -8874. You should NOT assume that edge costs are positive, nor should you assume that they are distinct.
    
    Your task is to run Prim's minimum spanning tree algorithm on this graph. You should report the overall cost of a minimum spanning tree --- an integer, which may or may not be negative --- in the box below.
    
    IMPLEMENTATION NOTES: This graph is small enough that the straightforward O(mn) time implementation of Prim's algorithm should work fine. OPTIONAL: For those of you seeking an additional challenge, try implementing a heap-based version. The simpler approach, which should already give you a healthy speed-up, is to maintain relevant edges in a heap (with keys = edge costs). The superior approach stores the unprocessed vertices in the heap, as described in lecture. Note this requires a heap that supports deletions, and you'll probably need to maintain some kind of mapping between vertices and their positions in the heap.

'''

import numpy as np
import heapq
import networkx as nx
import sys

# method 1
# tested on example.txt, works fine!
def prim0(data,start):  # direct search
    path = [data[start,0]] # path of start
    length = 0
    passnode = set(path) # passed note set
    unpassnode = set(data[:,0]).union(set(data[:,1])) # unpassed note set
    unpassnode.remove(path[0])
    while len(unpassnode) != 0:
        cuts = [item for item in data if (item[0] in passnode and item[1] in unpassnode) or (item[0] in unpassnode and item[1] in passnode)]
        node1,node2,distance = zip(*cuts)
        shortest = min(distance)
        length += shortest
        id = distance.index(shortest)
        if node1[id] in passnode:
            passnode.add(node2[id])
            unpassnode.remove(node2[id])
            path.append(node2[id])
        #    print node1[id],'-',node2[id],'---',shortest
        else:
            passnode.add(node1[id])
            unpassnode.remove(node1[id])
            path.append(node1[id])
        #    print node2[id],'-',node1[id],'---',shortest
    print 'total length: ',length


# build the graph from data
def buildgraph(data):
    G = nx.Graph()
    for item in data:
        G.add_edge(item[0],item[1],weight=item[2])
    return G

# build heap based on Graph and unpassed nodes
def buildheap(G,nodes):
    pq = []
    for node in nodes:
        min = sys.maxint
        for v in G.neighbors(node):
            if v not in nodes and G[node][v]['weight'] < min :
                min = G[node][v]['weight']
        heapq.heappush(pq,(min,node))
    return pq

# low speed Prim based on Heap...
#  !!! need further study!!!
def prim1(G,startnode):
    path = [startnode]
    passnode = set(path)
    unpassnode = G.nodes()
    unpassnode.remove(path[0])
    length = 0
    while len(unpassnode) != 0:
        pq = buildheap(G,unpassnode)
        shortest, node = heapq.heappop(pq)
        passnode.add(node)
        unpassnode.remove(node)
        path.append(node)
        #    print 'to:',node,' cost: ',shortest
        length += shortest
    print 'total length: ',length


if __name__ == "__main__":
    data = np.int_(np.loadtxt('edges.txt',skiprows=1))
    prim0(data,1)
    G = buildgraph(data)
    prim1(G,1)