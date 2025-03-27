import os
from tkinter import Tk
from gamestate import GameState

#TODO Graafinen käyttöliittymä
def start(dice):
    window = Tk()
    window.title("YatzyGame")
    window.mainloop()

#Väliaikainen peruskäyttöliittymä terminaalissa
def start_no_gui(dice):
    clear()

    state = GameState()

    while state.get_round() <= 13: # Peli kestää 13 kierrosta
        print("Syötä komento:")
        print("[r:heitä noppia] [h:lukitse/vapauta noppa] [q:poistu]\n")
        print(f"Pisteet: {state.get_score()}")
        print(f"Kierros #{state.get_round()}, heitto #{state.get_throw()}: {dice}")
        print(f"Lukitut nopat: {dice.dieheld}")
        command = input()
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

        state.update()
    
    #TODO tulosnäkymä
    print(f"Lopputulos: {state.get_score()}")
    input("Paina enter poistuaksesi")

#Tyhjentää terminaalin
def clear():
    os.system("clear")