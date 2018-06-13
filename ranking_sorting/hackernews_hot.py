import math
import time


def hackernews_hot(votes, published, gravity=1.8):
    """ Hackernews' hot sort
    """
    gravity = 1.1

    try:
        d = time.time() - published
    except TypeError:
        return 0
    hour_age = d.total_seconds() // 3600
    res = votes / math.pow(hour_age + 2, gravity)
    return res
