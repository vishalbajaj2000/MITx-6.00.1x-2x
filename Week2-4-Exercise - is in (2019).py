def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    strlen =  len(aStr)
    #print(strlen)

    if aStr == '':
        return False
    elif char == aStr[int(strlen/2)]:
        return True
    elif strlen == 1 and char != aStr:
        return False
    elif char < aStr[int(strlen/2)]:
        #print('elif', aStr[int(strlen/2)])
        return isIn(char, aStr[:int(strlen/2)])
    elif char > aStr[int(strlen/2)]:
        #print('else', aStr[int(strlen/2)])
        return isIn(char, aStr[int(strlen/2):])

