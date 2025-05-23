class Scoring:
    """A class that checks whether the dice fullfill the requirements of each scoring method
    and returns round score to be added to the score total.
    """

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

    def one_pair(self, dice):
        score = 0
        for i in range(1, 7):
            if dice.count(i) >= 2:
                score = max(score, i*2)

        return score

    def two_pairs(self, dice):
        score = 0
        temp_score = 0
        last_pair = 0

        # Finds and calculates score for the first pair
        for i in range(1, 7):
            if dice.count(i) >= 2:
                temp_score = max(score, i*2)
                last_pair = i

        # Removes all die with the same value as the first pair
        removed = 0
        while dice.count(last_pair) > 0:
            dice.remove(last_pair)
            removed += 1

        # Finds and calculates score for the second pair
        for i in range(1, 7):
            if dice.count(i) >= 2:
                score = max(score, i*2)

        for i in range(removed):
            dice.append(1)

        return score + temp_score

    def three_of_a_kind(self, dice):
        score = 0
        for i in range(1, 7):
            if dice.count(i) >= 3:
                score = max(score, i*3)

        return score

    def four_of_a_kind(self, dice):
        score = 0
        for i in range(1, 7):
            if dice.count(i) >= 4:
                score = max(score, i*4)

        return score

    def small_straight(self, dice):
        score = 0
        dice.sort()
        if dice == [1, 2, 3, 4, 5]:
            score = 15

        return score

    def large_straight(self, dice):
        score = 0
        dice.sort()
        if dice == [2, 3, 4, 5, 6]:
            score = 20

        return score

    def yahtzee(self, dice):
        score = 0
        for i in range(1, 7):
            if dice.count(i) == 5:
                score = 50

        return score

    def chance(self, dice):
        score = sum(dice)
        return score

    def full_house(self, dice):
        score = 0
        for i in range(1, 7):
            if dice.count(i) == 3:
                score += i*3
            elif dice.count(i) == 2:
                score += i*2

        return score
