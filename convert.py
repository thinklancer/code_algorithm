#!/opt/local/bin/python

'''
    convert the data in question 2-2 into 2-1 format
    use solution for question 2-1 to test the correctness of the code
'''

import numpy as np
import sys

if __name__ == "__main__":
    data = np.loadtxt('example2.txt',skiprows=1)
    nnode = len(data[:,0])
    for i in np.arange(nnode-1):
        for j in np.arange(nnode-1-i)+1+i:
            diff = np.logical_xor(data[i,:],data[j,:])
            dist = len(np.where(diff == True)[0])
            print i,j,dist

