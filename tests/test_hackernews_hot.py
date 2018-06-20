import unittest
import datetime

from ranking_sorting import hackernews_hot


class HackerNewsHotTest(unittest.TestCase):

    def test_hackernews_hot(self):
        expected = 0.0021404697161564834
        published = datetime.datetime(year=2017, month=10, day=3, hour=17, minute=32, second=45)
        score = hackernews_hot.hackernews_hot(14520, published)
        self.assertAlmostEqual(expected, score, places=5)

