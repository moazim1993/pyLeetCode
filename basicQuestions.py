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

#################################
def lengthOfLongestSubstring(s):
    hold = {}
    curL = 0
    maxL = 0
    for i, c in enumerate(s):
        if c in hold:
            curL = min( curL + 1, i - hold[c])
            hold[c] = i
        else:
            hold[c] = i
            curL += 1
        maxL = max(curL, maxL)
    return maxL

print("testing twoSUms with Input: test")
print(lengthOfLongestSubstring("test"))

print("testing twoSUms with Input: ''")
print(lengthOfLongestSubstring(""))

print("testing twoSUms with Input: abba")
print(lengthOfLongestSubstring("abba"))


print("testing twoSUms with Input: abcdabcde")
print(lengthOfLongestSubstring("abcdabcde"))



#################################
a1 = [2]
a2 = [1, 3]
a3 = [5, 6]
a4 = []
a5 = [1, 2, 3, 4, 5]

def findMedian(n1, n2):
    new = sorted(n1 + n2)
    while len(new) > 2:
        new.pop(0)
        new.pop(-1)
    return sum(new)/len(new)

print(findMedian(a2,a1))
print(findMedian(a2,a3))
print(findMedian(a4,a5))


#################################
def longestPalindrome(s):
    hld = {}
    full = start = end = bigest = ""
    for i, x in enumerate(s):
        #print("for i, x:", i, x)
        try:
            hld[x].append(i)
        except:
            hld[x] = [i]
        if len(hld[x]) > 1:
            for h in hld[x]:
                 minS, maxS = h, max(hld[x])
                 while minS <= maxS:
                     t, b = s[minS], s[maxS]
                     #print("while t, b, start, end, minS, maxS: ", t , b, start, end,minS, maxS)
                     if minS == maxS:
                         start += t
                         break
                     if t != b:
                        start = end = ""
                        break
                     else:
                        start += t
                        end = b + end
                     minS += 1
                     maxS -= 1
                 #print("end while t, b, start, end, minS, maxS: ", t , b, start, end,minS, maxS)
                 if len(start) > 0:
                    full = start + end
                    start = end = ""
                    break
        else:
            full = x
        bigest = bigest if len(full) < len(bigest) else full
        #print("biggest:", bigest)
        
    return bigest

    
print("return ",longestPalindrome("abbc"))
print("return ",longestPalindrome("abcba"))
print("return ",longestPalindrome("babadada"))