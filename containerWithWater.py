# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 16:47:47 2021
https://leetcode.com/problems/container-with-most-water/

Take two hights such that the width * min height can hold the most water
diff of index is the width

@author: moazi
"""

import time
start_time = time.time()


height = [1,8,6,2,5,4,8,3,7]
h2 = [2,3,4,5,18,17,6]
h3 = [0,0]
h4 = [3,9,3,4,7,2,12,6]
h5 = [76,155,15,188,180,154,84,34,187,142,22,5,27,183,111,128,50,58,
      2,112,179,2,100,111,115,76,134,120,118,103,31,146,58,198,134,38,104,170,
      25,92,112,199,49,140,135,160,20,185,171,23,98,150,177,198,61,92,26,147,
      164,144,51,196,42,109,194,177,100,99,99,125,143,12,76,192,152,11,152,
      124,197,123,147,95,73,124,45,86,168,24,34,133,120,85,81,163,146,75,92,
      198,126,191]


"""
# naive approach, check all find max
def maxArea(height):
    hold = []
    maxVal = []
    for i, l in enumerate(height):
        if hold:
            val = [(i - k[0])* min(k[1],l) for k in hold]
            maxVal.append(max(val))
            if max(val) == 17:
                print(i,l,val)
        hold.append([i,l])
    return max(maxVal)
                

#// approach 2, eliminate search space
# search from outter to middle, if middle is larger eleminate edge
"""
def maxArea(height):
    lenH = len(height)
    if lenH == 2:
        return min(height)
    val = min(height[0],height[-1])*(lenH-1)
    i = 1
    for i in range(1,len(height)):
        dropLeft = min(height[i],height[-1])*(lenH-(i+1))
        dropRight = min(height[0],height[-(i+1)])*(lenH-(i+1))
        print(i,height[0],height[-1],height)
        print(val,dropLeft,dropRight)
        breakpoint()
        if dropLeft > dropRight:
            if dropLeft > val and (height[0] < height[i]):
                return max(val,maxArea(height[i:]))
        elif dropRight > val and (height[-1] < height[-(i+1)]):
            return max(val,maxArea(height[:-i]))
    return val


"""

res1 = maxArea(height)
print(res1)
"""
res2 = maxArea(h2)
print(res2)
"""
res3 = maxArea(h3)
print(res3)
res4 = maxArea(h4)
print(res4)

res5 = maxArea(h5)
print(res5)
print("--- %s seconds ---" % (time.time() - start_time))
#print(h5[99])
"""
"""
position = [i+1 for i in range(len(height))]
print(height, position)
#crossProduct = [x*y for x in height for y in position]
cross = []
for i,x in enumerate(height):
    vals = [min(x,y)*abs(i-j) for j,y in enumerate(height)]
    cross.append(vals)
    
print("\n\n")
for i in cross:
    print(i)
"""
"""
def maxArea(height):
    lenH = len(height)
    if lenH == 2:
        return min(height)
    
    val = min(height[0],height[-1])*(lenH-1)
    print(val)
    
    dropLeft = min(height[1],height[-1])*(lenH-2)
    dropRight = min(height[0],height[-2])*(lenH-2)
    print(height,val,dropLeft,dropRight)
    
    if val >= max(dropLeft,dropRight):
        return max(val,
    elif dropLeft > dropRight:
        return max(dropLeft,maxArea(height[1:]))
    elif dropLeft < dropRight:
        return max(dropRight,maxArea(height[:-1]))
    
    return max(val,maxArea(height[1:]),maxArea(height[:-1]))


def maxArea(height):
    lenH = len(height)
    if lenH == 2:
        return min(height)
    #dropLeft = min(height[1],height[-1])*(lenH-2)
    #dropRight = min(height[0],height[-2])*(lenH-2)
    val = min(height[0],height[-1])*(lenH-1)
    if height[0] < height[1]:
        return max(val,maxArea(height[1:]))
    elif height[-1] < height[-2]:
        return max(val,maxArea(height[:-1]))
    else:
"""