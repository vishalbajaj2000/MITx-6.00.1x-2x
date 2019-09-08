'''
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh
'''
s = 'ootocrklojrzrmjrdqh'
wordlist = []
wordlen = []
for i in range(len(s)):
    word = ''
    j=i
    if i+1 == len(s) or s[i] > s[i+1]:
        word = s[i]
        wordlist.append(word)
        wordlen.append(len(word))
    else:
        while s[j] <= s[j+1]:
            word = word + (s[j])
            j += 1
            if j+1 >= len(s):
                break
        word = word + (s[j])
        wordlist.append(word)
        wordlen.append(len(word))
print('Longest substring in alphabetical order is: ' + wordlist[wordlen.index(max(wordlen))])
#Mote: using a dicts and getting max index from dictionary key values did not work in edx grader!!