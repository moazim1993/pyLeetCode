
"""
Leet Code Score:

Runtime: 28 ms, faster than 85.39% of Python3 online submissions for Valid Parentheses.
Memory Usage: 14.4 MB, less than 35.18% of Python3 online submissions for Valid Parentheses.
"""

def validParentheses(s):
    #print(string)
    if len(s) < 2:
        return False

    counter = {'round' : 0, 'square' : 0, 'bracket': 0}
    last = [""]
    for char in s:
        #print("char: ", char, "last : ", last)
        if char == "(":
            counter['round'] += 1
            last.append(char)
        elif char == ")":
            if last[-1] != "(":
                return False
            last.pop()
            counter['round'] -= 1
        elif char == "[":
            counter['square'] += 1
            last.append(char)
        elif char == "]":
            if last[-1] != "[":
                return False
            last.pop()
            counter['square'] -= 1
        elif char == "{":
            counter['bracket'] += 1
            last.append(char)
        elif char == "}":
            if last[-1] != "{":
                return False
            last.pop()
            counter['bracket'] -= 1

    #print(counter)
    if counter['round'] == counter['square'] == counter['bracket'] == 0:
        return True
    else:
        return False




s1 = "()"
s2 = "()[]{}"
s3 = "(]"
s4 = "([)]"
s5 = "{[]}"
s6 = "([{hi}])"
s7 = "([[hello]})"
s8 = "]"
print(validParentheses(s1)) # true
print(validParentheses(s2)) # true
print(validParentheses(s3)) # false
print(validParentheses(s4)) # false
print(validParentheses(s5)) # true
print(validParentheses(s6)) # true
print(validParentheses(s7)) # fasle
print(validParentheses(s8)) # fasle