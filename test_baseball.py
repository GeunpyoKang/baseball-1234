from unittest import TestCase

from baseball import Game


class TestGame(TestCase):
    def get_answer_format(self, solved, strike, ball):
        return {
            'solved': solved, 'strike': strike, 'ball': ball
        }

    def test_right_answer(self):
        sut = Game(123)
        self.assertEqual(sut.check_answer(123), self.get_answer_format(True, 3, 0))

    def test_ball_answer(self):
        sut = Game(123)
        self.assertEqual(sut.check_answer(321), self.get_answer_format(False, 1, 2))
        self.assertEqual(sut.check_answer(521), self.get_answer_format(False, 1, 1))
        self.assertEqual(sut.check_answer(571), self.get_answer_format(False, 0, 1))

    def test_strike_answer(self):
        sut = Game(123)
        self.assertEqual(sut.check_answer(132), self.get_answer_format(False, 1, 2))
        self.assertEqual(sut.check_answer(125), self.get_answer_format(False, 2, 0))
        self.assertEqual(sut.check_answer(153), self.get_answer_format(False, 2, 0))

    def test_tc(self):
        sut = Game(123)
        self.assertEqual(sut.check_answer(456), self.get_answer_format(False, 0, 0))
        self.assertEqual(sut.check_answer(129), self.get_answer_format(False, 2, 0))
        self.assertEqual(sut.check_answer(240), self.get_answer_format(False, 0, 1))
        self.assertEqual(sut.check_answer(321), self.get_answer_format(False, 1, 2))
        self.assertEqual(sut.check_answer(123), self.get_answer_format(True, 3, 0))
