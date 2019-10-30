'''
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2
'''
s = 'azcbobobeggbobhakl'
word = 'bob'
wordlen = len(word)
wordlist = []
wordcount = 0 
for i in range(len(s)):
    wordlist.append(s[i:i+wordlen])
for x in wordlist:
    if word == x:
        wordcount += 1
print('Number of times ' + word + ' occurs is:' +  str(wordcount))