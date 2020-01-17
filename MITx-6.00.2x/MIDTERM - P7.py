def solveit(test):
    """ test, a function that takes an int parameter and returns a Boolean
        Assumes there exists an int, x, such that test(x) is True
        Returns an int, x, with the smallest absolute value such that test(x) is True 
        In case of ties, return any one of them. 
    """
    x = 0
    flag = True
    while flag:
        if test(x) == True:
            return x
        elif test(-x) == True:
            return -x
        else:
            x += 1

#### This test case prints 49 ####
def f(x):
    return (x+15)**0.5 + x**0.5 == 15
print(solveit(f))

#### This test case prints 0 ####
def f(x):
    return x == 0
print(solveit(f))

def f(x):
    return x**2 == 9
print(solveit(f))

def f(x):
    return [1,2,3][-x] == 1 and x != 0
print(solveit(f))