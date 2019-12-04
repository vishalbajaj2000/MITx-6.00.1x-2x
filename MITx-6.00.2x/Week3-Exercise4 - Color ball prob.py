import random
def trial():
    bucket = ['R']*3 + ['G']*3
    hand = []
    for i in range(3):
        x = random.choice(bucket)
        hand.append(x)
        bucket.remove(x)
    return tuple(hand)

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    sim = {}
    for i in range(numTrials):
        draw = trial()
        if draw in sim:
            sim[draw] += 1
        else:
            sim[draw] = 1
    total = sum(sim.values())
    all_same = sim[('R','R','R')] + sim[('G','G','G')]
    return float(all_same/total)

noReplacementSimulation(100000)
