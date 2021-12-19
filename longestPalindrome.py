# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 17:52:58 2021

@author: moazi
"""
def longestPalindrome(s: str) -> str:
    min_ind, max_ind, max_size = 0, 0, 0
    if s == s[::-1]:            # hack to solve leet code edgecase in time
        return s
    for i, c in enumerate(s):
        all_cs = [ind for ind, char in enumerate(s) if char == c and ind > i]
        all_cs.sort(reverse = True)
        if len(all_cs) >= 1:
            for next_c in all_cs:
                substr = s[i+1:next_c]
                temp_size = len(substr) + 2
                if substr[:round(len(substr)/2)] == substr[::-1][:round(len(substr)/2)] and temp_size > max_size:
                    min_ind, max_ind = i, next_c
                    max_size = temp_size
                    break
                elif temp_size < max_size:
                    break
    return s[min_ind:max_ind+1]

"""
print(longestPalindrome("babad"))
print(longestPalindrome("cbbc"))
print(longestPalindrome("ac"))


#  # expecting "bb"
#longestPalindrome("ac")  # expecting "a"
## Weird edge case that takes too long for leetcode
tstcase = "abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa"
tstcase2 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

print(len(tstcase))
print(longestPalindrome(tstcase))  #should return the whole thing
print(len(tstcase2))
print(longestPalindrome(tstcase2))  #should return the whole thing
"""


###################################################
### Optimal Solution - Expand around the center ###
###################################################
# Complexity O(n^2)

def longestPalindrome(s: str):
    m = ''  # Memory to remember a palindrome
    for i in range(len(s)):  # i = start, O = n
        for j in range(len(s), i, -1):  # j = end, O = n^2
            #print(i,j,m)
            if len(m) >= j-i:  # To reduce time
                break
            elif s[i:j] == s[i:j][::-1]:
                m = s[i:j]
                break
    return m

pal1 = longestPalindrome("baabaad")
pal2 = longestPalindrome("baabaad")
pal3 = longestPalindrome("baabaad")
#print(pal1, pal2, pal3)


#  # expecting "bb"
#longestPalindrome("ac")  # expecting "a"
## Weird edge case that takes too long for leetcode
tstcase = "abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa"
tstcase2 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

#print(len(tstcase))
#print(longestPalindrome(tstcase))  #should return the whole thing
#print(len(tstcase2))
#print(longestPalindrome(tstcase2))  #should return the whole thing


# write a unit test to check if pallandrome
def isPalindrome(s: str):
    s_inv = s[::-1]
    if s == s_inv:
        return True
    else:
        return False

print(isPalindrome(pal1), isPalindrome(pal2),isPalindrome(pal3),isPalindrome("no its not"))

# add the nessicarry chars to string to make it a palindrome
def makePalindrome(s: str):
    try:
        print(int(s))
    except:
        print("Not an int string")
        return None
    inv_s = s[::-1]
    if s == inv_s:
        return s
    # starting from the end try to find the longest palindrome, the rest will be added to the end
    pInd = None
    lenS = len(s)
    for i in range(2, lenS+1):
        #print("L1", i, s[lenS - i:], inv_s[:i])
        if inv_s[:i] == s[lenS - i:]:
            pInd = i
    #print("L2", s, inv_s[pInd:])
    return s+str(inv_s[pInd:])
        

pal4 = makePalindrome("1232")
pal5 = makePalindrome("123454")
pal6 = makePalindrome("poop")
pal7 = makePalindrome("12321")
print(pal4, pal5, pal6, pal7)
