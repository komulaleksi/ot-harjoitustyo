class GameState():
    def __init__(self):
        self.round = 1
        self.throw_number = 1
        self.score = 0

    def get_round(self):
        return self.round
    
    def get_throw(self):
        return self.throw_number
    
    def get_score(self):
        return self.score
    
    def next_round(self):
        self.round += 1
        self.throw_number = 1

    def next_throw(self):
        self.throw_number += 1

    def update(self):
        if self.throw_number > 3:
            self.throw_number = 1
            self.round += 1