import math


def wilson_score(ups, downs, z=1.96):
    """ Wilson score interval sort
    (popularized by reddit's best comment system)
    http://www.evanmiller.org/how-not-to-sort-by-average-rating.html
    """
    if ups == 0:
        return 0
    n = ups + downs
    p = ups / n
    sqrtexpr = (p * (1 - p) + z * z / (4 * n)) / n
    res = (p + z * z / (2 * n) - z * math.sqrt(sqrtexpr)) / (1 + z * z / n)
    return res
