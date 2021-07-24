from more_itertools import pairwise

def goodseg(badnumbers,lower,upper):
    badnumbers = [lower-1] + sorted(x for x in badnumbers if lower <=x <= upper)
    difference = (b-a for a,b in pairwise(badnumbers))

    return max(difference) - 1