def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if a > b:
        iter = a
    elif b > a:
        iter = b
    elif a == b:
        return a

    while iter >= 1:
        if b % iter == 0 and a % iter == 0:
            return iter
        else:
            iter -= 1


gcdIter(8, 12)
