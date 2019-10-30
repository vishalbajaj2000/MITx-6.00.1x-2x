def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    If b = 0, then the answer is a
    Otherwise, gcd(a, b) is the same as gcd(b, a % b)
    Write a function gcdRecur(a, b) that implements this idea recursively. This function takes in two positive integers and returns one integer.
    '''
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)

gcdRecur(11,12)