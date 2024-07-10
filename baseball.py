class Game:
    answer: list

    def __init__(self, answer):
        self.answer = list(str(answer))

    def count_strike(self, target_list):
        cnt = 0
        for i in range(len(self.answer)):
            if self.answer[i] == target_list[i]:
                cnt += 1
        return cnt

    def count_ball(self, target_list):
        return 0

    def check_answer(self, target):
        target_list = list(str(target))

        strike = self.count_strike(target_list)
        ball = self.count_ball(target_list)
        solved = strike == 3

        return {
            'solved': solved,
            'strike': strike,
            'ball': ball
        }
