def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other. 
            If they are permutations of each other, returns a 
            tuple of 3 items in this order: 
            the element occurring most, how many times it occurs, and its type
    '''
    if L1 == [] and L2 == []:
        return (None, None, None)
    if len(L1) != len(L2):
        return False
    L1d = {}
    L2d = {}
    for i in L1:
        if L1d.get(i) == None:
            L1d[i] = 1
        else:
            L1d[i] += 1
    for i in L2:
        if L2d.get(i) == None:
            L2d[i] = 1
        else:
            L2d[i] += 1
    if L1d != L2d:
        return False
    else:
        m = max(list(L1d.values()))
        mostFreq = list(L1d.keys())[list(L1d.values()).index(m)]
        return (mostFreq, m, type(mostFreq))

    





L1 = ['a', 'a', 'b']
L2 = ['a', 'b']
is_list_permutation(L1,L2) == False

L1 = ['a', 'a', 'b']
L2 = ['a', 'b', 'a']
is_list_permutation(L1,L2) == ('a', 2, str)