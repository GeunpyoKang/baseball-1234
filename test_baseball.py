from unittest import TestCase

from baseball import Game


class TestGame(TestCase):

    def test_right_answer(self):
        sut = Game(123)
        self.assertEqual(sut.check_answer(123), {
            'solved': True,
            'strike': 3,
            'ball': 0
        })

    def test_ball_answer(self):
        sut = Game(123)
        self.assertEqual(sut.check_answer(321), {
            'solved': False,
            'strike': 0,
            'ball': 3
        })
        self.assertEqual(sut.check_answer(521), {
            'solved': False,
            'strike': 0,
            'ball': 2
        })
        self.assertEqual(sut.check_answer(571), {
            'solved': False,
            'strike': 0,
            'ball': 1
        })

    def test_strike_answer(self):
        sut = Game(123)
        self.assertEqual(sut.check_answer(132), {
            'solved': False,
            'strike': 1,
            'ball': 2
        })
        self.assertEqual(sut.check_answer(125), {
            'solved': False,
            'strike': 2,
            'ball': 0
        })
        self.assertEqual(sut.check_answer(153), {
            'solved': False,
            'strike': 2,
            'ball': 0
        })
