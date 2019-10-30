l = 0 
h = 100
guess = int((l + h) / 2)
print('Please think of a number between 0 and 100!')
print('Is your secret number ' + str(guess)+ '?')
while True:
    hl = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if hl == 'c':
        print('Game over. Your secret number was: ' + str(guess))
        break
    elif hl == 'l':
        l = guess
        guess = int((l + h) / 2)
        print('Is your secret number ' + str(guess)+ '?')
    elif hl == 'h':
        h = guess
        guess = int((l + h) / 2)
        print('Is your secret number ' + str(guess)+ '?')
    else:
        print('Sorry, I did not understand your input.')
        print('Is your secret number ' + str(guess)+ '?')