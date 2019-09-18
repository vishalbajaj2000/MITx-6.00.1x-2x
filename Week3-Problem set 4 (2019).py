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

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    word = ''
    for a in secretWord:
        if a in lettersGuessed:
            word += (a)
        else:
            word += ('_')
    return word

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    letters = string.ascii_lowercase
    available = [i for i in letters if i not in lettersGuessed]
    return ''.join(available)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
#wordlist = loadWords()

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    secretWordLen = len(secretWord)
    # print('Loading word list from file...')
    # print(str(len) + ' words loaded.')
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is '+ str(secretWordLen) + ' letters long.')
    print('-------------')
    guesses = 8
    guess = ''
    lettersGuessed = []
    while True:
        if guesses == 0:
            print('Sorry, you ran out of guesses. The word was else.')
            break
        print('You have ' + str(guesses) + ' left.')
        print('Available letters: ' + getAvailableLetters(lettersGuessed))
        guess = input('Please guess a letter: ')
        if guess.lower() in lettersGuessed:
            print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
            print('-------------')
        elif guess.lower() not in secretWord:
            guesses -= 1
            lettersGuessed.append(guess.lower())
            print('Oops! That letter is not in my word: ' + getGuessedWord(secretWord, lettersGuessed))
            print('-------------')
        elif guess.lower() in secretWord:
            lettersGuessed.append(guess.lower())
            print('Good guess: ' + getGuessedWord(secretWord, lettersGuessed))
            print('-------------')
            if isWordGuessed(secretWord, lettersGuessed) == True:
                print('Congratulations, you won!')
                break
            

hangman('apples')