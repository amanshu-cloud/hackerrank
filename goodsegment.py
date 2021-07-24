from more_itertools import pairwise



#define pairwise function if not available
def pairwise(numbers):
    return zip(numbers[:-1],numbers[1:])
    
def goodsegment(badnumbers,lower,upper):
    badnumbers = [lower-1] + sorted(x for x in badnumbers if lower <=x <= upper)
    difference = (b-a for a,b in pairwise(badnumbers))

    return max(difference) - 1