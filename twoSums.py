# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 15:39:14 2020

@author: moazim1993
"""


def twoSum(nums, target):
    hold = {}
    for i, num in enumerate(nums):
        need = target - num
        if need in hold:
            return [hold[need], i]
        else:
            hold[num] = i
            
            

print("testing twoSUms with Input: nums = [2,7,11,15], target = 9")
print(twoSum([2, 7, 11, 15], 9))

print("testing twoSUms with Input: nums = [2,3,4], target = 6")
print(twoSum([2, 3, 4], 6))

print("testing twoSUms with Input: nums = [3,3], target = 6")
print(twoSum([3,3], 6))


print("testing twoSUms with Input: nums =[9, 1,3, 0], target = 9")
print(twoSum([9, 1,3, 0], 9))