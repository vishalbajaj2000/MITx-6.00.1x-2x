# generate all combinations of N items
def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        combo = []
        for j in range(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                print(i >> j)
                combo.append(items[j])
            else:
                print('NO', i >> j, i , j)
        yield combo

def yieldAllCombos(items):
    """
      Generates all combinations of N items into two bags, whereby each 
      item is in one or zero bags.

      Yields a tuple, (bag1, bag2), where each bag is represented as 
      a list of which item(s) are in each bag.
    """
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(3**N):
        bag1 = []
        bag2 = []
        for j in range(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                #print(i >> j)
                bag1.append(items[j])
            elif (i >> j) % 3 == 1:
                bag2.append(items[j])
        yield (bag1,bag2)

#####
def power_set(it):
    for i in range(2**len(it)):
        yield [it[j] for j in range(len(it)) if (i >> j) & 1]

def yieldAllCombos(items):
    """ use power_set to generate its set of all two bags, then for each bag
        take the remaining items & split them into a set of all two remainder bags
        for each set of two remainder bags return the first + the two bags
    """
    for bag1 in power_set(items):
        remain = [i for i in items if i not in bag1]
        for bag2 in power_set(remain):
            yield bag1, bag2