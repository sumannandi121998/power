""" Finding the position of 2^X from a list
name: Suman Nandi
Date: 06.11.2019"""

from math import *
L = [1,2,4,8,16,32,64]
X = 5
j=0
for i in range(len(L)):
    if 2**X == L[i]:
        s=L[i]
        j=j+1

if j==1:
    print (L.index(s))
else:
    print (X,"not found")
   
 
