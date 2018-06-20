import math
import datetime
from datetime import timezone


def hackernews_hot(votes, published, gravity=1.8):
    """ Hackernews' hot sort
    """

    d = datetime.datetime.now(timezone.utc) - published
    hour_age = d.total_seconds() // 3600
    res = votes / math.pow(hour_age + 2, gravity)
    return res
