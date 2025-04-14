import os
from tkinter import Tk
from gamestate import GameState
from scoring import Scoring
from file_reader import FileReader

# TODO Graafinen käyttöliittymä


def start(dice):
    window = Tk()
    window.title("YatzyGame")
    window.mainloop()

# Väliaikainen peruskäyttöliittymä terminaalissa


def start_no_gui(dice):
    clear()

    state = GameState()
    scoring = Scoring()
    file_reader = FileReader()

    while state.get_round() <= 12:  # Peli kestää 13 kierrosta. Tällä hetkellä täyskäsi ei ole toiminnassa, joten kierroksia on vain 12
        print("Syötä komento:")
        print("[r:heitä noppia] [h:lukitse/vapauta noppa] [q:poistu]\n")
        print(f"Pisteet: {state.get_score()}")
        print(
            f"Kierros #{state.get_round()}, heitto #{state.get_throw()}: {dice}")
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
                print(
                    "Väärä komento. Kirjoita noppien 1-5 numerot peräkkäin ilman välilyöntejä.\n")
        elif command == "q":
            return
        else:
            print("Väärä komento.\n")

        if dice.all_dice_held():
            state.set_throw(3)

        if state.update() == True:
            clear()
            print_categories(dice)
            state.print_scoring_method_used()

            # Hiemän tönkkö tapa, mutta GUI versio korvaa tämän kohta
            while True:
                command = input("Valitse pisteytyskategoria: ").lower()

                if command == "ykköset" and state.get_scoring_method_used("ykköset") == False:
                    score = scoring.ones(dice.get_dice())
                    state.update_score(score)
                    state.use_scoring_method("ykköset", score)
                    break
                elif command == "kakkoset" and state.get_scoring_method_used("kakkoset") == False:
                    score = scoring.twos(dice.get_dice())
                    state.update_score(score)
                    state.use_scoring_method("kakkoset", score)
                    break
                elif command == "kolmoset" and state.get_scoring_method_used("kolmoset") == False:
                    score = scoring.threes(dice.get_dice())
                    state.update_score(score)
                    state.use_scoring_method("kolmoset", score)
                    break
                elif command == "neloset" and state.get_scoring_method_used("neloset") == False:
                    score = scoring.fours(dice.get_dice())
                    state.update_score(score)
                    state.use_scoring_method("neloset", score)
                    break
                elif command == "viitoset" and state.get_scoring_method_used("viitoset") == False:
                    score = scoring.fives(dice.get_dice())
                    state.update_score(score)
                    state.use_scoring_method("viitoset", score)
                    break
                elif command == "kuutoset" and state.get_scoring_method_used("kuutoset") == False:
                    score = scoring.sixes(dice.get_dice())
                    state.update_score(score)
                    state.use_scoring_method("kuutoset", score)
                    break
                elif command == "yksi pari" and state.get_scoring_method_used("yksi pari") == False:
                    score = scoring.one_pair(dice.get_dice())
                    state.update_score(score)
                    state.use_scoring_method("yksi pari", score)
                    break
                elif command == "kaksi paria" and state.get_scoring_method_used("kaksi paria") == False:
                    score = scoring.two_pairs(dice.get_dice())
                    state.update_score(score)
                    state.use_scoring_method("kaksi paria", score)
                    break
                elif command == "kolmoisluku" and state.get_scoring_method_used("kolmoisluku") == False:
                    score = scoring.three_of_a_kind(dice.get_dice())
                    state.update_score(score)
                    state.use_scoring_method("kolmoisluku", score)
                    break
                elif command == "nelosluku" and state.get_scoring_method_used("nelosluku") == False:
                    score = scoring.four_of_a_kind(dice.get_dice())
                    state.update_score(score)
                    state.use_scoring_method("nelosluku", score)
                    break
                elif command == "pieni suora" and state.get_scoring_method_used("pieni suora") == False:
                    score = scoring.small_straight(dice.get_dice())
                    state.update_score(score)
                    state.use_scoring_method("pieni suora", score)
                    break
                elif command == "suuri suora" and state.get_scoring_method_used("suuri suora") == False:
                    score = scoring.large_straight(dice.get_dice())
                    state.update_score(score)
                    state.use_scoring_method("suuri suora", score)
                    break
                elif command == "sattuma" and state.get_scoring_method_used("sattuma") == False:
                    score = scoring.chance(dice.get_dice())
                    state.update_score(score)
                    state.use_scoring_method("sattuma", score)
                    break
                elif command == "yatzy" and state.get_scoring_method_used("yatzy") == False:
                    score = scoring.yahtzee(dice.get_dice())
                    state.update_score(score)
                    state.use_scoring_method("yatzy", score)
                    break
                else:
                    clear()
                    print("Väärä pisteytyskategoria tai pisteytyskategoria on jo käytetty")
                    print_categories(dice)

            dice.reset_dice()
            clear()

    # TODO tulosnäkymä
    print(f"Lopputulos: {state.get_score()}")
    name = input("Kirjoita nimesi: ")
    final_score = [[name, state.get_score()]]
    file_reader.write_score(final_score)

    clear()
    file_reader.print_score()
    input("Paina enter poistuaksesi")

# Tyhjentää terminaalin (ei taida toimia Windowsilla tällä hetkellä)
def clear():
    os.system("clear")

def print_categories(dice):
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

