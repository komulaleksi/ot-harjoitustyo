from dice import Dice
#import ui
from ui import UI


def main():
    dice = Dice()
    gui = UI(dice)
    gui.start()

if __name__ == "__main__":
    main()
