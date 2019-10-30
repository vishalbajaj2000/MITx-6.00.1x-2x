# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 23:14:13 2018
Assume that two variables, varA and varB, are assigned values, either numbers or strings.

Write a piece of Python code that evaluates varA and varB, and then prints out one of the following messages:

"string involved" if either varA or varB are strings

"bigger" if varA is larger than varB

"equal" if varA is equal to varB

"smaller" if varA is smaller than varB
@author: visha
"""

varA = 2
varB = 1

if type(varA) == str or type(varB) == str:
    print("string involved")
elif varA > varB:
    print("bigger")
elif varA == varB:
    print("equal")
elif varA < varB:
    print("smaller")
    
num = 0
while num <= 5:
    print(num)
    num += 1

print("Outside of loop")
print(num) 