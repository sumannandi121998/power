""" Finding the position of 2^X from a list
name: Suman Nandi
Date: 06.11.2019"""

from math import *
L = [1,2,4,8,16,32,64]
X = 5
i = 0
j=0
while i< len(L):
    if 2**X == L[i]:
        print ("at index",i)
        j=j+1
    i=i+1
if j==0:
    print (X,"not found")
