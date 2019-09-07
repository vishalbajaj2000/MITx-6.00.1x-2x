'''
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh
'''
#Not working!
s = 'azcbobobegghakl'
wordlist = []
for i in range(len(s)):
    word = ''
    j=i
    if i+1 == len(s):
        wordlist.append(s[i])
    elif s[i] > s[i+1]:
        wordlist.append(s[i])
    else:
        lastletter = False
        while s[j] <= s[j+1]:
            word = word + (s[j])
            j += 1
            if j+1 >= len(s):
                break
            
        word = word + (s[j-1])
        print(word)
        wordlist.append(word)
print(wordlist)