nestedList = [[1, 2, 3],[4, [5,6]],[7, 8], 9]

def sumAll(nList):
    total = 0
    for val in nList:
        #breakpoint()
        if type(val) == type([]):
            total += sumAll(val)
        else:
            total += val
    return total

try:
    print(sum(nestedList))
except:
    print("Didn't work")

sumOfList = sumAll(nestedList)
print(sumOfList)


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n -1)

print(factorial(5))
print(factorial(6))