# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 20:39:50 2020

@author: moazim1993
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        lst = numRows * [""]
        mod = 0
        reverse = False
        
        for i,l in enumerate(s):
            lst[mod] += l
            if mod == (numRows-1):
                reverse = True
            elif mod == 0:
                reverse = False
            if numRows == 1:
                pass
            elif reverse:
                mod -= 1
            else:
                mod += 1
        
        return "".join(lst)
            



Solution = Solution()
print(Solution.convert("PAYPALISHIRING", 3))            # "PAHNAPLSIIGYIR"
print(Solution.convert("HELLOWORLD", 3))                # "HOLELWRDLO"
print(Solution.convert("AB", 1))                        # "AB"
print(Solution.convert("HEY", 1))                        # "AB"

# H  O  L
# E LW RD
# L  O
