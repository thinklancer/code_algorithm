#!/opt/local/bin/python

'''
In this assignment you will implement one or more algorithms for the all-pairs shortest-path problem. Here are data files describing three graphs: graph #1; graph #2; graph #3.
The first line indicates the number of vertices and edges, respectively. Each subsequent line describes an edge (the first two numbers are its tail and head, respectively) and its length (the third number). NOTE: some of the edge lengths are negative. NOTE: These graphs may or may not have negative-cost cycles.
Your task is to compute the "shortest shortest path". Precisely, you must first identify which, if any, of the three graphs have no negative cycles. For each such graph, you should compute all-pairs shortest paths and remember the smallest one (i.e., compute minu,v in Vd(u,v), where d(u,v) denotes the shortest-path distance from u to v).]
If each of the three graphs has a negative-cost cycle, then enter "NULL" in the box below. If exactly one graph has no negative-cost cycles, then enter the length of its shortest shortest path in the box below. If two or more of the graphs have no negative-cost cycles, then enter the smallest of the lengths of their shortest shortest paths in the box below.
OPTIONAL: You can use whatever algorithm you like to solve this question. If you have extra time, try comparing the performance of different all-pairs shortest-path algorithms!
'''


import numpy as np
import sys
maximum = 1000000

# Floyd-Warshall algorithm to solve All-Pairs Shortest Paths problem
def fw(graph,n,m):
    # initialize the A matrix
    a = np.ones((n,n,2),dtype=np.int)*maximum
    for i in range(n):
        a[i,i,0]=0
    for i in range(m):
        a[graph[i,0],graph[i,1],0] = graph[i,2]
    # start to search all shortest paths
    for k in range(1,n):
        for i in range(n):
            for j in range(n):
                a[i,j,1] = min(a[i,j,0],a[i,k,0]+a[k,j,0])
        a[:,:,0]=a[:,:,1]
    # check negative cycles
    for i in range(n):
        if a[i,i,1] < 0:
            print "error in",i
            exit()
    # output
    print a[:,:,1].min()

if __name__ == "__main__":
    n,m = np.int_(np.fromfile(sys.argv[1],count=2,sep=' '))
    graph = np.int_(np.loadtxt(sys.argv[1],skiprows=1))
    graph[:,0] = graph[:,0]-1
    graph[:,1] = graph[:,1]-1
    fw(graph,n,m)