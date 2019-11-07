###########################
# 6.00.2x Problem Set 1: Space Cows 

#from ps1_partition import get_partitions
import time
#From codereview.stackexchange.com                    
def partitions(set_):
    if not set_:
        yield []
        return
    for i in range(2**len(set_)//2):
        parts = [set(), set()]
        for item in set_:
            parts[i&1].add(item)
            i >>= 1
        for b in partitions(parts[1]):
            yield [parts[0]]+b


# This is a helper function that will fetch all of the available 
# partitions for you to use for your brute force algorithm.
def get_partitions(set_):
    for partition in partitions(set_):
        yield [list(elt) for elt in partition]

### Uncomment the following code  and run this file
### to see what get_partitions does if you want to visualize it:

# for item in (get_partitions(['a','b','c','d'])):
#     print(item)
# ================================
# Part A: Transporting Space Cows
# ================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """

    cows_temp = []
    ct = cows.copy()
    cow_weights = sorted(list(cows.values()), reverse=True)
    for i in cow_weights:
        for k,v in ct.items():
            if i == ct[k]:
                cows_temp.append((k,v))
                ct[k] = 'Used'
            else:
                pass
    trips = []
    flag = True
    used = []
    while flag:
        available = limit
        trips.append([])
        for i in cows_temp:
            if i[1] <= available:
                trips[-1].append(i[0])
                used.append(i)
                available = available - i[1]
                if available == 0:
                    break
            else:
                pass
        for i in used:
            if i in cows_temp:
                cows_temp.pop(cows_temp.index(i))
            else:
                pass
        if len(cows_temp) == 0:
            flag = False
    return trips

# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    ct =  cows.copy()
    ctp = []
    for i in get_partitions(ct):
        ctp.append(i)
    accepted = []
    for i,l in enumerate(ctp):
        combo_ok = True
        for j, sl in enumerate(l):
            tripsum = 0
            for k, ssl in enumerate(sl):
                tripsum = tripsum + ct[ssl]
            if tripsum > limit:
                combo_ok = False
                break
            else:
                pass  
        if combo_ok == True:
            accepted.append(l)

    accp_len = []
    for i in accepted:
        accp_len.append(len(i))
                    
    return accepted[accp_len.index(min(accp_len))]

        
# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    pass


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("C:\\Users\\vbajaj\\Local Files\\Dev\\MITx-6.00.1x-2x\\MITx-6.00.2x\\pset1\\ps1_cow_data.txt")
limit=100
#print(cows)

# print(greedy_cow_transport(cows, limit))
# print(greedy_cow_transport({'Muscles': 65, 'Miss Bella': 15, 'MooMoo': 85, 'Lotus': 10, 'Louis': 45, 'Horns': 50, 'Clover': 5, 'Polaris': 20, 'Milkshake': 75, 'Patches': 60}, 100))

# print(greedy_cow_transport({'Abby': 28, 'Rose': 42, 'Starlight': 54, 'Betsy': 39, 'Luna': 41, 'Buttercup': 11, 'Coco': 59, 'Willow': 59}, 120))
# print(greedy_cow_transport({'Lilly': 24, 'Abby': 38, 'Dottie': 85, 'Rose': 50, 'Betsy': 65, 'Patches': 12, 'Daisy': 50, 'Buttercup': 72, 'Coco': 10, 'Willow': 35}, 100))

start = time.time()
print(greedy_cow_transport(cows, 10))
end = time.time()
print(end - start)


start = time.time()
print(brute_force_cow_transport(cows, 10))
end = time.time()
print(end - start)
