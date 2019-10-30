import math
def polysum(n,s):
    '''
    Input - the function takes 2 inputs 'n' number of sides of a regular polygon and 's' the length of each side.
    Return - The function returns the sum of the area, and perimeter squared, of the regular polygon, rounded to 4 decimal places.
    '''
    pi = math.pi
    ployarea = (0.25 * n * s**2) / math.tan(pi / n) #Area of regular polygon
    polyperisq = (n * s)**2 #perimeter squared of regular polygon
    return round(ployarea + polyperisq, 4)