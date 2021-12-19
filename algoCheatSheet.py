# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 15:18:02 2020

@author: moazim1993

Coding excersizes from Algorithms by Aanjoy Dasgusta et all.
"""

#################################
### chp6: Dynamic programming ###
# defined as a set of problems which can be framed as a
#DAG (directed acyclical graph). Can be solved by passing through a list once
#################################
#chp6 q1
def largestSubSequence(an):
    """
    Function: given a squence find a continuous (in order) subsequence
        with the largest sum by passing through once O(nt)
    Input: sequence
    Output: an array with largest sum
    """
    sum_at_j, max_at_j = 0,0
    count = 0
    start, end = 0,0
    hold_start = [0]
    for count, j in enumerate(an):
        sum_at_j = max(j,sum_at_j+j)
        if sum_at_j <= 0:
            hold_start.append(count+1)
        if max_at_j < sum_at_j:
            end = count+1
            start = hold_start[-1]
        max_at_j = max(max_at_j,sum_at_j)
    return an[start:end]

    
    
# normal case
s = [5,15,-30,10,-5,40,10,-55]
# edge case 1
s2 = [1, 2, 3, 4, 5]
# edge case 2
s3 = [-3, -2, -1, -4, -5]
print("For sequence: ", s)
print("Here is the subsequence with the largest sum", largestSubSequence(s))

print("For sequence: ", s2)
a2 = largestSubSequence(s2)
print("Here is the subsequence with the largest sum", a2)
print(sum(a2))

print("For sequence: ", s3)
a3 = largestSubSequence(s3)
print("Here is the subsequence with the largest sum", a3)
print(sum(a3))


# chp6 q 17
def makeChange(x,v):
    """ given a set of coins avilable and a value you need to make change for
    crete an O(nt) algorithm to determine if it's possible to give exact chnage
    input x set of coin denominations, v positive value
    """
    s = [True]
    count = 0
    while v > min(x):
        count += 1
        s.append(False)
        for i in x:
            if v >= i:
                mosti = int(v/i)
                chage_by_i = mosti*i
                v = round(v-chage_by_i,2)
            if v == 0:
                s[-1] = True#last element in s
    return s[-1]

coins = [.25,.1,.05]
coins2 = [.01, .1]
v = .72
v2 = .7
print(makeChange(coins, v))
print(makeChange(coins2, v))

print(makeChange(coins, v2))
print(makeChange(coins2, v2))


###
# knapsack problem
# consider a knansack that can hold weight W
# also a set of items with varying weights and values
# you want to fill the most valueable set of items with in the weight limit
###
# whats the maximum value you can fill the bag with?
def knapSack(W, wt, val, n):
    """
    Given W weight capacity, find the maximum values of items in knapSack
    with in weight capacity, by selecting each item once at most
    input: W int weight capacity, wt weights of items, val values of items
    n number of items
    output: max value
    """
    # Base Case 
    if n == 0 or W == 0 : 
        return 0
  
    # If weight of the nth item is more than Knapsack of capacity 
    # W, then this item cannot be included in the optimal solution 
    if (wt[n-1] > W): 
        return knapSack(W, wt, val, n-1) 
  
    # return the maximum of two cases: 
    # (1) nth item included 
    # (2) not included 
    else: 
        return max(val[n-1] + knapSack(W-wt[n-1], wt, val, n-1), 
                   knapSack(W, wt, val, n-1))
        
# To test above function 
val = [1, 100, 120]
val2 = [1, 10, 100]

wt = [10, 20, 30] 
wt2 = [1, 5, 99]
W = 50
n = len(val) 
print("testing knapSack with val and wt")
print( knapSack(W, wt, val, n))

print("testing knapSack with val2 and wt")
print( knapSack(W, wt, val2, n))

print("testing knapSack with val and wt2")
print( knapSack(W, wt2, val, n))

print("testing knapSack with val2 and wt2")
print( knapSack(W, wt2, val2, n))

#chp 6 q 22
# Can you fill the exact capacity of the bag?
def knapsackWthOutR(W,wt):
    """
    Knapsack without replacement
    Give an O(nt) algorithm to determine if any subset of wt adds up to W
    input: W positive int, positive int sequence wt
    output: true if subset = W, false if subset not equal to W
    """
    # Create n nested arrays of 0 * (W + 1)
    max_vals = [[0] * (W + 1) for x in range(len(wt))]
    # Set max_vals[0] to wt[0] if wt[0] <= j
    max_vals[0] = [wt[0] if wt[0] <= j else 0 for j in range(W + 1)]
    for i in range(1, len(wt)):
        for j in range(1, W + 1):
            value = max_vals[i - 1][j]  # previous i @ same j
            if wt[i] <= j:
                val = (max_vals[i - 1][j - wt[i]]) + wt[i]
                if value < val:
                    value = val
                    max_vals[i][j] = value
                else:
                    max_vals[i][j] = value

    if max_vals[-1][-1] == W:
        return True
    else:
        return False



maxW = 25
s = [2,3,4,5,55]
s1 = [1, 2, 22, 33, 44]
s2 =[25, 1, 2, 3]
s3 = [12, 12, 1]

print("testing sequence: ", s)
print(knapsackWthOutR(maxW,s))

print("testing sequence: ", s1)
print(knapsackWthOutR(maxW,s1))

print("testing sequence: ", s2)
print(knapsackWthOutR(maxW,s2))

print("testing sequence: ", s3)
print(knapsackWthOutR(maxW,s3))



##########################
### Fibonacci Sequence ###
##########################
def fibonacci(n):
    """
    Fast iterrative fibbonacci
    input nth place of fibonacci
    output nth fibbonaci
    """
    a, b = 0, 1
    
    for i in range(n):
        a, b = b, a + b
    
    return a

print("testing fibonacci")
[print(fibonacci(x)) for x in  range(10)]



def fibonacci(n):
    """
    Recursive fibbonacci
    input nth place of fibonacci
    output nth fibbonaci
    """
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)
    
[print(fibonacci(x)) for x in  range(10)]

##########################
###### Linked List ######
##########################
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    """
    Given two linked list each with one integer of a number add the sum and
    return the value in the same format
    input l1 l2 both linked list ie) 2 > 4 > 3 & 5 > 6 > 4
    output ret linked list ie) 7 > 0> 8
    342 + 465 = 807
    """
    ttl = l1.val + l2.val
    print("1. l1, l2", l1.val, l2.val)
    c = 0
    if ttl > 9:
        ttl %= 10
        c += 1
    ret = ListNode(ttl)
    print("c, ttl:", c, ttl)
    if l1.next != None and l2.next != None:
        if c:
            l1.next.val += 1
        ret.next = addTwoNumbers(l1.next, l2.next)
    elif l2.next != None:
        ret.next = addTwoNumbers(ListNode(c), l2.next)
    elif l1.next != None:
         ret.next = addTwoNumbers(l1.next, ListNode(c))
    else:
        if c:
            ret.next = ListNode(1)
    
    return ret

n1 = ListNode(2) 
n2 = ListNode(4)
n3 = ListNode(3)

n1.next = n2
n2.next = n3

n4 = ListNode(5) 
n5 = ListNode(6)
n6 = ListNode(4)

n4.next = n5
n5.next = n6

res= addTwoNumbers(n1, n4)
print(res.val)
print(res.next.val)
print(res.next.next.val)















