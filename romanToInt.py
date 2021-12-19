# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 13:03:32 2021

@author: moazi
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        l_count, count = 0, 0
        roman_to_int={'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        last_c = roman_to_int[s[0]]
        
        for i in s:
            val = roman_to_int[i]
            if val > last_c:
                count = val - count
            elif val < last_c:
                l_count += count
                count = val
            else:
                count += val
            last_c = val
        
        l_count += count
        return l_count


Solution = Solution()
print(Solution.romanToInt("III"))       # 3
print(Solution.romanToInt("IV"))        # 4
print(Solution.romanToInt("IX"))        # 9
print(Solution.romanToInt("LVIII"))     # 58
print(Solution.romanToInt("MCMXCIV"))  # 1994
