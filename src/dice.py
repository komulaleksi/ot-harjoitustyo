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
        for i in range(1, 6):
            if self.dieheld[i] == False:
                die = random.randint(1, 6)
                self.dice[i-1] = die

    def change_status(self, die):
        if self.dieheld[die] == False:
            self.dieheld[die] = True
        else:
            self.dieheld[die] = False

        return
        
    def __str__(self):
        return str(self.dice)
    
    def set_dice(self, dice):
        self.dice = dice

    def get_dice(self):
        return self.dice
    
    def reset_dice(self):
        for status in self.dieheld:
            self.dieheld[status] = False

        self.throw_dice()