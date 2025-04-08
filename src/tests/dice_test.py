import unittest
from dice import Dice

class testDice(unittest.TestCase):
    def setUp(self):
        self.dice = Dice()
        
    def test_all_dice_held_return_true_when_all_dice_held(self):
        self.dice.change_status(1)
        self.dice.change_status(2)
        self.dice.change_status(3)
        self.dice.change_status(4)
        self.dice.change_status(5)

        self.assertEqual(self.dice.all_dice_held(), True)

    def test_all_dice_held_return_false_when_some_dice_not_held(self):
        self.dice.change_status(2)
        self.dice.change_status(3)
        self.dice.change_status(5)

        self.assertEqual(self.dice.all_dice_held(), False)