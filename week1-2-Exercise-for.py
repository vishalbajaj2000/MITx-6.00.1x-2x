# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 23:14:13 2018
In this problem you'll be given a chance to practice writing some while loops.

1. Convert the following into code that uses a while loop.

print 2
prints 4
prints 6
prints 8
prints 10
prints Goodbye!
@author: visha
"""
###Excercise 1
num = 2

for x in range(0,12):
       if num > 10:
              print('Goodbye!')
              break
       if num <= 10:
              print(num)
              num += 2
              x += 2


###Excercise 2
num = 12

for x in range(0,12):
       if num > 10:
              print('Hello!')
              num -= 2
              x += 2
       if num <= 10 and num > 0:
              print(num)
              num -= 2
              x += 2
       if num == 0:
              break

###Excercise 3
end = 21 ##used only to test and not on edx
num = 0

for x in range(1,end+1):
       if x <= end:
              num += x
              x += 1
       else:
              break
print(num)