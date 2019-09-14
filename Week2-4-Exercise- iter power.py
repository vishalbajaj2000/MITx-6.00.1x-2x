def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    if exp == 0:
        return 1
    else:
        temp = base
        for i in range(1,exp):
            temp *= base
            print(temp)
        return temp