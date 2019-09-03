def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    check = True

    for x in secretWord:
        if x in lettersGuessed:
            check = True
        else:
            check = False
            return check
    return check



secretWord = 'apple' 
lettersGuessed = ['a', 'e', 'l', 'p', 'r', 's']
print(isWordGuessed(secretWord, lettersGuessed))