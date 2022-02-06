# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 18:25:46 2022

@author: moazi
"""
import time


h1 = [2,3,4,5,18,17,6]
h2 = [59,15,23,55,87,30,47,61,74,86,25,42,40,21,0,30,47,61,74,86,25,42,40,21,0,79,45,42,0,47,61,93,69,1,42]




def maxArea(height):
    tab = [0]*(len(height))
    for i in range(1,len(height)):
        for j in range(i):
            valL = min(height[i], height[j])*abs(i-j)
            valR = min(height[-i], height[-j])*abs(i-j)
            if valL > valR:
                val = valL
            else:
                val = valR
            if val > tab[i]:
                tab[i] = val
    return max(tab)



start_time = time.time()
res1 = maxArea(h1)
print(res1)
res2 = maxArea(h2)
print(res2)
print("--- %s seconds ---" % (time.time() - start_time))


def maxArea(height):
    lenH = len(height)
    if lenH == 2:
        return min(height)
    val = min(height[0],height[-1])*(lenH-1)
    for i in range(len(height)):
        dropLeft = min(height[i],height[-1])*(lenH-(i+1))
        dropRight = min(height[0],height[-(i+1)])*(lenH-(i+1))
        #print(val,dropLeft,dropRight)
        
        if dropLeft > dropRight:
            val = max(val,maxArea(height[i:]))
        elif dropRight > val and (height[-1] < height[-(i+1)]):
            val = max(val,maxArea(height[:-i]))
    return val

"""

res1 = maxArea(height)
print(res1)
"""
start_time = time.time()
res1 = maxArea(h1)
print(res1)
res2 = maxArea(h2)
print(res2)
print("--- %s seconds ---" % (time.time() - start_time))
