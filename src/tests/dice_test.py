import unittest
from dice import Dice


class testDice(unittest.TestCase):
    def setUp(self):
        self.dice = Dice()

    def test_throw_dice_randomizes_dice(self):
        self.dice = Dice()
        old_dice = []
        for die in self.dice.get_dice():
            old_dice.append(die)
        self.dice.throw_dice()

        self.assertNotEqual(old_dice, self.dice.get_dice())

    def test_get_status_returns_status(self):
        self.assertEqual(self.dice.get_status(2), False)

    def test_chance_status_changes_false_to_true(self):
        self.dice.change_status(3)

        self.assertEqual(self.dice.get_status(3), True)

    def test_chance_status_changes_true_to_false(self):
        self.dice.change_status(3)
        self.dice.change_status(3)

        self.assertEqual(self.dice.get_status(3), False)

    def test_str_returns_dice_as_string(self):
        self.assertEqual(str(self.dice), str(self.dice.get_dice()))

    def test_reset_dice_sets_all_dice_to_false(self):
        self.dice.change_status(4)

        self.dice.reset_dice()
        self.assertEqual(self.dice.get_status(4), False)

    def test_reset_dice_rerolls_dice(self):
        old_dice = []
        for die in self.dice.get_dice():
            old_dice.append(die)

        self.dice.reset_dice()
        self.assertNotEqual(old_dice, self.dice.get_dice())

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
