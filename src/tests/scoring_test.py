import unittest
from scoring import Scoring
from dice import Dice


class TestScoring(unittest.TestCase):
    def setUp(self):
        self.scoring = Scoring()

    def test_scoring_ones_calculates_score_correctly(self):
        dice = Dice()
        dice.set_dice([1, 1, 3, 6, 1])
        score = self.scoring.ones(dice.get_dice())

        self.assertEqual(score, 3)

    def test_scoring_twos_calculates_score_correctly(self):
        dice = Dice()
        dice.set_dice([1, 2, 3, 2, 1])
        score = self.scoring.twos(dice.get_dice())

        self.assertEqual(score, 4)

    def test_scoring_threes_calculates_score_correctly(self):
        dice = Dice()
        dice.set_dice([3, 1, 3, 6, 3])
        score = self.scoring.threes(dice.get_dice())

        self.assertEqual(score, 9)

    def test_scoring_fours_calculates_score_correctly(self):
        dice = Dice()
        dice.set_dice([4, 4, 3, 6, 1])
        score = self.scoring.fours(dice.get_dice())

        self.assertEqual(score, 8)

    def test_scoring_fives_calculates_score_correctly(self):
        dice = Dice()
        dice.set_dice([1, 5, 5, 5, 5])
        score = self.scoring.fives(dice.get_dice())

        self.assertEqual(score, 20)

    def test_scoring_sixes_calculates_score_correctly(self):
        dice = Dice()
        dice.set_dice([1, 6, 3, 6, 1])
        score = self.scoring.sixes(dice.get_dice())

        self.assertEqual(score, 12)

    def test_scoring_one_pair_calculates_score_correctly(self):
        dice = Dice()
        dice.set_dice([1, 2, 3, 3, 3])
        score = self.scoring.one_pair(dice.get_dice())

        self.assertEqual(score, 6)

    def test_scoring_two_pairs_calculates_score_correctly(self):
        dice = Dice()
        dice.set_dice([2, 2, 3, 3, 3])
        score = self.scoring.two_pairs(dice.get_dice())

        self.assertEqual(score, 10)

    def test_scoring_three_of_a_kind_calculates_score_correctly(self):
        dice = Dice()
        dice.set_dice([1, 2, 3, 3, 3])
        score = self.scoring.three_of_a_kind(dice.get_dice())

        self.assertEqual(score, 9)

    def test_scoring_four_of_a_kind_calculates_score_correctly(self):
        dice = Dice()
        dice.set_dice([3, 2, 3, 3, 3])
        score = self.scoring.four_of_a_kind(dice.get_dice())

        self.assertEqual(score, 12)
    
    def test_scoring_small_straight_calculates_score_correctly(self):
        dice = Dice()
        dice.set_dice([3, 2, 4, 5, 1])
        score = self.scoring.small_straight(dice.get_dice())

        self.assertEqual(score, 15)

    def test_scoring_large_straight_calculates_score_correctly(self):
        dice = Dice()
        dice.set_dice([3, 2, 4, 5, 6])
        score = self.scoring.large_straight(dice.get_dice())

        self.assertEqual(score, 20)

    def test_scoring_yahtzee_calculates_score_correctly(self):
        dice = Dice()
        dice.set_dice([6, 6, 6, 6, 6])
        score = self.scoring.yahtzee(dice.get_dice())

        self.assertEqual(score, 50)

    def test_scoring_chance_calculates_score_correclty(self):
        dice = Dice()
        dice.set_dice([1, 2, 3, 3, 6])
        score = self.scoring.chance(dice.get_dice())

        self.assertEqual(score, 15)

    def test_scoring_full_house_calculaates_score_correctly(self):
        dice = Dice()
        dice.set_dice([2, 4, 2, 4, 4])
        score = self.scoring.full_house(dice.get_dice())

        self.assertEqual(score, 16)
