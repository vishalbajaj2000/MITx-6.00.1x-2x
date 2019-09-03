# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

s = 'abcdefghijklmnopqrstuvwxyz'
alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
     'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
words = []
wordlen = []


###loop to find the indexes of possible sequences of letter, the loop fins the 
###min and max index and then stores the word in a new array and the length in another array.
for ix in range(0, len(s)-1):
    # if len(wordlen) > 0 and max(wordlen) == len(s):
    #     break
    for i in range(ix, len(s)-1):        
        if alph.index(s[i]) <= alph.index(s[i+1]) and i == len(s)-2:
            words.append(s[ix:i+2])
            wordlen.append(len(s[ix:i+2]))

            break
        elif alph.index(s[i]) > alph.index(s[i+1]):
            words.append(s[ix:i+1])
            wordlen.append(len(s[ix:i+1]))
            break
        else:
            i += 1

    ix += 1

###this lopp is used to find the longest words and then sort them based on the alphabetic order
allwords = []
for i, x in enumerate(wordlen):
       if x == max(wordlen):
              allwords.append(words[i])
              i += 1
       else:
              i += 1
print('Longest substring in alphabetical order is:',allwords[0])
print(words)
