from dice import Dice

class Scoring:
    def ones(self, dice):
        score = 0
        for die in dice:
            if die == 1:
                score += die

        return score
    
    def twos(self, dice):
        score = 0
        for die in dice:
            if die == 2:
                score += die

        return score
    
    def threes(self, dice):
        score = 0
        for die in dice:
            if die == 3:
                score += die

        return score
    
    def fours(self, dice):
        score = 0
        for die in dice:
            if die == 4:
                score += die

        return score
    
    def fives(self, dice):
        score = 0
        for die in dice:
            if die == 5:
                score += die

        return score
    
    def sixes(self, dice):
        score = 0
        for die in dice:
            if die == 6:
                score += die

        return score