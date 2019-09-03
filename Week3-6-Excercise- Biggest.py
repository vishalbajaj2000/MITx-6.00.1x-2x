def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    big = {}
    for k in aDict:
        big[k] = (len(aDict[k]))
    
    x =  max(big.values())

    for i in aDict:
        if x == len(aDict[i]):
            return i
        else:
            pass

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

print(biggest(animals))


##### EdX result
    # result = None
    # biggestValue = 0
    # for key in aDict.keys():
    #     if len(aDict[key]) >= biggestValue:
    #         result = key
    #         biggestValue = len(aDict[key])
    # return result