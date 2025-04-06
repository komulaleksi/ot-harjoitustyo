import os
from tkinter import Tk
from gamestate import GameState
from scoring import Scoring

#TODO Graafinen käyttöliittymä
def start(dice):
    window = Tk()
    window.title("YatzyGame")
    window.mainloop()

#Väliaikainen peruskäyttöliittymä terminaalissa
def start_no_gui(dice):
    clear()

    state = GameState()
    scoring = Scoring()

    while state.get_round() <= 13: # Peli kestää 13 kierrosta
        print("Syötä komento:")
        print("[r:heitä noppia] [h:lukitse/vapauta noppa] [q:poistu]\n")
        print(f"Pisteet: {state.get_score()}")
        print(f"Kierros #{state.get_round()}, heitto #{state.get_throw()}: {dice}")
        print(f"Lukitut nopat: {dice.dieheld}")
        command = input().lower()
        clear()

        if command == "r":
            dice.throw_dice()
            state.next_throw()
        elif command == "h":
            print("Kirjoita noppien numerot, jotka haluat lukita tai vapauttaa.\n")
            print(f"Heitto #{state.get_round()}: {dice}")
            hold = input()

            try:
                for die in hold:
                    dice.change_status(int(die))
                    clear()
            except:
                clear()
                print("Väärä komento. Kirjoita noppien 1-5 numerot peräkkäin ilman välilyöntejä.\n")
        elif command == "q":
            return
        else:
            print("Väärä komento.\n")

        if state.update() == True:
            clear()
            print(f"Heitto #3: {dice}")
            print("Pisteytyskategoriat: \n"
            "Ykköset \n"
            "Kakkoset \n"
            "Kolmoset \n"
            "Neloset \n"
            "Viitoset \n"
            "Kuutoset \n"
            "Yksi pari \n"
            "Kaksi paria \n"
            "Kolmoisluku \n"
            "Nelosluku \n"
            "Sattuma \n"
            "Yatzy \n")
            
            command = input("Valitse pisteytyskategoria: ").lower()

            if command == "ykköset":
                state.set_score(scoring.ones(dice.get_dice()))
            elif command == "kakkoset":
                state.set_score(scoring.twos(dice.get_dice()))
            elif command == "kolmoset":
                state.set_score(scoring.threes(dice.get_dice()))
            elif command == "neloset":
                state.set_score(scoring.fours(dice.get_dice()))
            elif command == "viitoset":
                state.set_score(scoring.fives(dice.get_dice()))
            elif command == "kuutoset":
                state.set_score(scoring.sixes(dice.get_dice()))
            elif command == "yksi pari":
                state.set_score(scoring.one_pair(dice.get_dice()))
            elif command == "kaksi paria":
                state.set_score(scoring.two_pairs(dice.get_dice()))
            elif command == "kolmoisluku":
                state.set_score(scoring.three_of_a_kind(dice.get_dice()))
            elif command == "nelosluku":
                state.set_score(scoring.four_of_a_kind(dice.get_dice()))
            elif command == "sattuma":
                state.set_score(scoring.chance(dice.get_dice()))
            elif command == "yatzy":
                state.set_score(scoring.yahtzee(dice.get_dice()))

            dice.reset_dice()
            clear()
    
    #TODO tulosnäkymä
    print(f"Lopputulos: {state.get_score()}")
    input("Paina enter poistuaksesi")

#Tyhjentää terminaalin
def clear():
    os.system("clear")