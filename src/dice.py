import random


class Dice:
    def __init__(self):
        self.dice = [1, 1, 1, 1, 1]
        self.dieheld = {1: False,
                        2: False,
                        3: False,
                        4: False,
                        5: False}

        for i in range(1, 6):
            die = random.randint(1, 6)
            self.dice[i-1] = die

    def throw_dice(self):
        """Randomally generates values between 1 and 6 for the five dice.
        """
        for i in range(1, 6):
            if self.dieheld[i] is False:
                die = random.randint(1, 6)
                self.dice[i-1] = die

    def get_status(self, die):
        """Checks whether a given die is held or not.

        Args:
            die (int): Die number that corresponds to a key in self.dieheld.

        Returns:
            bool: Value corresponding to key in variable die.
        """
        return self.dieheld[die]

    def change_status(self, die):
        """Flips the boolean value in self.dieheld that matches the key from variable die.

        Args:
            die (int): Die number corresponding to key in self.dieheld.
        """
        if self.dieheld[die] is False:
            self.dieheld[die] = True
        else:
            self.dieheld[die] = False

    def __str__(self):
        return str(self.dice)

    def set_dice(self, dice):
        """Manually set the dice to preferred values. Used mainly for testing purposes.

        Args:
            dice (list): Dice values as a list.
        """
        self.dice = dice

    def get_dice(self):
        """Returns the dice as a list.

        Returns:
            list: Dice as a list.
        """
        return self.dice

    def reset_dice(self):
        """Sets all dice to be not held and throws(randomizes) them.
        """
        for status in self.dieheld:
            self.dieheld[status] = False

        self.throw_dice()

    def all_dice_held(self):
        """Checks whether all the dice are held.

        Returns:
            bool: False if one or more of the die is not held. True otherwise."""
        for i in range(1, 6):
            if self.dieheld[i] is False:
                return False

        return True

    def print_dice(self):
        """Prints the dice formatted properly for the UI

        Returns:
            Str: Returns the dice as a string separated by a vertical bar.
        """
        dice_string = "| "
        for die in self.dice:
            dice_string += f"{die} | "

        return dice_string
