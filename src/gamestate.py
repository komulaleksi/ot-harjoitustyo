class GameState():
    def __init__(self, round=1, throw_number=1, score=0):
        self.round = round
        self.throw_number = throw_number
        self.score = score
        self.scoring_method_used = {"ykköset": False,
                                    "kakkoset": False,
                                    "kolmoset": False,
                                    "neloset": False,
                                    "viitoset": False,
                                    "kuutoset": False,
                                    "yksi pari": False,
                                    "kaksi paria": False,
                                    "kolmoisluku": False,
                                    "nelosluku": False,
                                    "pieni suora": False,
                                    "suuri suora": False,
                                    "yatzy": False,
                                    "sattuma": False}

    def get_round(self):
        return self.round

    def set_round(self,round):
        self.round = round

    def get_throw(self):
        return self.throw_number

    def set_throw(self, throw_number):
        self.throw_number = throw_number

    def get_score(self):
        return self.score

    def set_score(self, score):
        self.score = score

    def update_score(self, score):
        self.score += score

    def get_scoring_method_used(self, method):
        return self.scoring_method_used[method]

    def return_scoring_method_used(self):
        return self.scoring_method_used

    def use_scoring_method(self,method, score):
        self.scoring_method_used[method] = score

    def next_round(self):
        self.round += 1
        self.throw_number = 1

    def next_throw(self):
        self.throw_number += 1

    def update(self):
        if self.throw_number >= 3:
            self.throw_number = 1
            self.round += 1
            return True

        return False
