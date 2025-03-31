import unittest
from scoring import Scoring
from dice import Dice

class TestScoring(unittest.TestCase):
    def setUp(self):
        self.scoring = Scoring()

    def test_scoring_ones_calculates_score_correctly(self):
        dice = Dice()
        dice.set_dice([1,1,3,6,1])
        score = self.scoring.ones(dice.get_dice())

        self.assertEqual(score, 3)

    def test_scoring_twos_calculates_score_correctly(self):
        dice = Dice()
        dice.set_dice([1,2,3,2,1])
        score = self.scoring.twos(dice.get_dice())

        self.assertEqual(score, 4)

    def test_scoring_threes_calculates_score_correctly(self):
        dice = Dice()
        dice.set_dice([3,1,3,6,3])
        score = self.scoring.threes(dice.get_dice())

        self.assertEqual(score, 9)

    def test_scoring_fours_calculates_score_correctly(self):
        dice = Dice()
        dice.set_dice([4,4,3,6,1])
        score = self.scoring.fours(dice.get_dice())

        self.assertEqual(score, 8)

    def test_scoring_fives_calculates_score_correctly(self):
        dice = Dice()
        dice.set_dice([1,5,5,5,5])
        score = self.scoring.fives(dice.get_dice())

        self.assertEqual(score, 20)

    def test_scoring_sixes_calculates_score_correctly(self):
        dice = Dice()
        dice.set_dice([1,6,3,6,1])
        score = self.scoring.sixes(dice.get_dice())

        self.assertEqual(score, 12)