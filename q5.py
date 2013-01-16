'''
    In this assignment you will implement one or more algorithms for the traveling salesman problem, such as the dynamic programming algorithm covered in the video lectures. Here is a data file describing a TSP instance. The first line indicates the number of cities. Each city is a point in the plane, and each subsequent line indicates the x- and y-coordinates of a single city.
    The distance between two cities is defined as the Euclidean distance --- that is, two cities at locations (x,y) and (z,w) have distance sqrt((x-z)^2+(y-w)^2 between them.
    In the box below, type in the minimum cost of a traveling salesman tour for this instance, rounded down to the nearest integer.
    
    Large data set:
    http://www.tsp.gatech.edu/world/countries.html
'''

import numpy as np
import sys


def builddist(ncity,x,y):
    distance = np.zeros((ncity,ncity))
    for i in range(ncity):
        for j in range(i,ncity):
            distance[i,j]=distance[j,i]=np.sqrt((x[i]-x[j])**2+(y[i]-y[j])**2)

if __name__ == "__main__":
    ncity = np.fromfile(sys.argv[1],count=1,sep=' ')
    x,y = np.loadtxt(sys.argv[1],skiprows=1,unpack=True)
    builddist(ncity,x,y)

    
