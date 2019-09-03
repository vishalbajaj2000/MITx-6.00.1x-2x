numh = 100
numl = 0
x = ['l','h','c']
check = 'l'
print('Please think of a number between 0 and 100!')

while check != 'c':
    print('Is your secret number ' + str(int((numh + numl) / 2)) + '?')
    check = input("Enter 'h' to indicate the guess is too high. Enter l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if check == 'h':
        numh = int((numh + numl) / 2)
    if check == 'l':
        numl = int((numh + numl) / 2)
    if check == 'c':
        print('Game over. Your secret number was: ' + str(int((numh + numl) / 2)))
    if check not in x:
        print('Sorry, I did not understand your input.')