import unittest

from ranking_sorting import wilson_score


class DummyTest(unittest.TestCase):

    def test_wilson_score(self):
        expected = 0.5519636426153274
        score = wilson_score.wilson_score(10,2)
        self.assertEqual(score, expected)

    def test_wilson_score_ups_0(self):
        expected = 0
        score = wilson_score.wilson_score(0, 2)
        self.assertEqual(score, expected)
