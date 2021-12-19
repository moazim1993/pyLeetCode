# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 16:47:47 2021
https://leetcode.com/problems/container-with-most-water/

Take two hights such that the width * min height can hold the most water
diff of index is the width

@author: moazi
"""

height = [1,8,6,2,5,4,8,3,7]
h2 = [1,1]


def maxArea(height):
    hold = []
    maxVal = []
    for i, l in enumerate(height):
        if hold:
            maxVal.append(max([(i - k[0])* min(k[1],l) for k in hold]))
        hold.append([i,l])
    return max(maxVal)
                

res1 = maxArea(height)
print(res1)
res2 = maxArea(h2)
print(res2)

"""
position = [i+1 for i in range(len(height))]
print(height, position)
#crossProduct = [x*y for x in height for y in position]
crossProduct = []
for x in height:
    vals = [x*y for y in height if y>=x]
    crossProduct.append(vals)

print("\n\n")
for i in crossProduct:
    print(i)
"""