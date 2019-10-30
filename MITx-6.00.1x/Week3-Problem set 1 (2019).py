def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for a in secretWord:
        if a not in lettersGuessed:
            return False
        else:
            continue
    return True

secretWord = 'apple' 
lettersGuessed = ['a', 'i', 'k', 'p', 'l', 'e']
print(isWordGuessed(secretWord, lettersGuessed))