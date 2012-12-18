'''
    In this programming problem and the next you'll code up the knapsack algorithm from lecture. Let's start with a warm-up. Download the text file here. This file describes a knapsack instance, and it has the following format:
    [knapsack_size][number_of_items]
    [value_1] [weight_1]
    [value_2] [weight_2]
    ...
    For example, the third line of the file is "50074 659", indicating that the second item has value 50074 and size 659, respectively.
    You can assume that all numbers are positive. You should assume that item weights and the knapsack capacity are integers.

    In the box below, type in the value of the optimal solution.

    ADVICE: If you're not getting the correct answer, try debugging your algorithm using some small test cases. And then post them to the discussion forum!

answer to question 1:  2493893
'''

import numpy as np

def buildKmatric(value,weight,wlimit):
    nv = len(value)+1
    nw = wlimit+1
    ma = np.zeros([nv,nw],dtype=int)
    count = 0
    for i in range(1,nv):
        # the matrix starts from 0 to nv but value/weight starts from 1 to nv
        id = i-1
        for j in range(nw):
            if j < weight[id]:
                ma[i,j] = ma[i-1,j]
            else:
                ma[i,j] = max(ma[i-1,j],ma[i-1,j-weight[id]]+value[id])
    return ma

# reconstruct the item in use
def finditem(ma,value,weight):
    #print ma
    items = []
    target = ma[-1,-1]
    i = len(ma)-1
    j = len(ma[0])-1
    while target > 0:
        id = np.where(ma[:,j]==target)
        i = id[0][0]-1
        print '(',value[i],',',weight[i],')'
        j = j-weight[i]
        target = ma[i,j]


# return the maximum weight
def printweight(ma):
    print 'maximum weight:',ma[-1,-1]

if __name__ == "__main__":
    data = np.loadtxt('knapsack1.txt')
    wlimit = int(data[0,0])
    nelement = int(data[0,1])
    data = np.int_(data[1:])
    # sanity check
    if len(data) != nelement:
        print "!!wrong number of items!!"
        exit()
    ma = buildKmatric(data[:,0],data[:,1],wlimit)
    finditem(ma,data[:,0],data[:,1])
    printweight(ma)