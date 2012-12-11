#!/opt/local/bin/python

'''
    convert the data in question 2-2 into 2-1 format
    use solution for question 2-1 to test the correctness of the code
'''

import numpy as np
import sys

if __name__ == "__main__":
    data = np.loadtxt(sys.argv[1],skiprows=1)
    nnode = len(data[0,:])

