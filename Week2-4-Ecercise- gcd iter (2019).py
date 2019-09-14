def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    temp = 0
    if a > b:
        temp = b
    else:
        temp = a
    
    for i in range(temp,1,-1):
        if a % i == 0 and b % i == 0:
            return i
        else:
            continue