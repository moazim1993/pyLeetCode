# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 21:21:01 2020

@author: moazim1993
"""

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

def fib(n):
    a, b = 0, 1
    f = True
    while f:
        a, b = b, a + b
        if n > b:
            f = False
            print(a, b, n)
    
    return a

print(fib(32))