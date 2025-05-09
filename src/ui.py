import tkinter as tk
from tkinter import Tk, ttk, Entry
from gamestate import GameState
from scoring import Scoring
from file_reader import FileReader

class UI:
    def __init__(self, dice):
        self._root = Tk()
        self._root.geometry("300x300")
        self._root.title("YatzyGame")
        self.dice = dice
        self.gamestate = GameState()
        self.scoring = Scoring()
        self.file_reader = FileReader()
        self.current_score = tk.StringVar(self._root, f"Pisteet: {self.gamestate.get_score()}")
        self.player_name_button_clicked = False

        self.info = tk.StringVar(self._root, f"Kierros {self.gamestate.get_round()}, heitto {self.gamestate.get_throw()}")
        self.current_dice = tk.StringVar(self._root, self.dice.print_dice())
        self.dice_one_held = tk.BooleanVar()
        self.dice_two_held = tk.BooleanVar()
        self.dice_three_held = tk.BooleanVar()
        self.dice_four_held = tk.BooleanVar()
        self.dice_five_held = tk.BooleanVar()

        self.scoring_choice_list = ["Valitse pisteytyskategoria", "Ykköset", "Kakkoset", "Kolmoset", "Neloset", "Viitoset", "Kuutoset",
                                    "Yksi pari", "Kaksi paria", "Kolmoisluku", "Nelosluku", "Pieni suora", "Suuri suora", "Täyskäsi", "Sattuma", "Yatzy"]
    def start(self):
        info_label = tk.Label(master=self._root, textvariable=self.info)
        info_label.config(font=("Arial", 30))
        dice_label = tk.Label(master=self._root, textvariable=self.current_dice)
        dice_label.config(font=("Arial", 35))
        start_button = tk.Button(master=self._root, text="Heitä", command=self.__throw_button_click)

        self.scoring_combobox = ttk.Combobox(master=self._root, values=self.scoring_choice_list)
        self.scoring_combobox.set("Valitse pisteytyskategoria")
        self.scoring_button = tk.Button(master=self._root, text="Valitse", command=self.__calculate_round_score)

        self.lock_one_check = tk.Checkbutton(master=self._root, text="1", variable=self.dice_one_held, onvalue=True, offvalue=False)
        self.lock_two_check = tk.Checkbutton(master=self._root, text="2", variable=self.dice_two_held, onvalue=True, offvalue=False)
        self.lock_three_check = tk.Checkbutton(master=self._root, text="3", variable=self.dice_three_held, onvalue=True, offvalue=False)
        self.lock_four_check = tk.Checkbutton(master=self._root, text="4", variable=self.dice_four_held, onvalue=True, offvalue=False)
        self.lock_five_check = tk.Checkbutton(master=self._root, text="5", variable=self.dice_five_held, onvalue=True, offvalue=False)

        quit_button = tk.Button(master=self._root, text="Poistu", command=self._root.destroy)
        self.score_label = tk.Label(master=self._root, textvariable=self.current_score)

        info_label.grid(row=0, column=0, columnspan=5)
        dice_label.grid(row=1, column=0, columnspan=5)

        self.lock_one_check.grid(row=2, column=0)
        self.lock_two_check.grid(row=2, column=1)
        self.lock_three_check.grid(row=2, column=2)
        self.lock_four_check.grid(row=2, column=3)
        self.lock_five_check.grid(row=2, column=4)
        start_button.grid(row=3, column=0, columnspan=5)

        self.scoring_combobox.grid(row=4, column=0, columnspan=4)
        self.scoring_button.grid(row=4, column=4)

        self.score_label.grid(row=5, column=0, columnspan=5)
        quit_button.grid(row=6, column=0, columnspan=5)

        self.debug_button = tk.Button(master=self._root, text="Pisteet", command=self.__open_score_window)
        self.debug_button.grid(row=7, column=0)

        self._root.mainloop()

    def __open_score_window(self):
        score_window = tk.Toplevel()
        score_window.geometry("300x300")
        score_window.title("YatzyGame - Pisteet")

        self.scores_stringvar = tk.StringVar(score_window, f"{self.file_reader.print_score()}")
        self.player_name = tk.StringVar(score_window, "Nimimerkki")

        self.current_score.set(f"Lopputulos: {self.gamestate.get_score()}")
        final_score = tk.Label(master=score_window, textvariable=self.current_score)
        final_score.config(font=("Arial", 25))
        self.player_name_entry = Entry(score_window, textvariable=self.player_name)
        self.player_name_button = tk.Button(master=score_window, text="Tallenna", command=self.__player_name_button_click)
        self.scores_stringvar_label = tk.Label(master=score_window, textvariable=self.scores_stringvar)
        quit_button = tk.Button(master=score_window, text="Poistu", command=self._root.destroy)

        final_score.grid(row=0, column=0, columnspan=2)
        self.player_name_entry.grid(row=1, column=0)
        self.player_name_button.grid(row=1, column=1)
        self.scores_stringvar_label.grid(row=2, column=0, columnspan=2)
        quit_button.grid(row=3, column=0, columnspan=2)
        score_window.focus()
        score_window.grab_set()

    def __player_name_button_click(self):
        if not self.player_name_button_clicked:
            name = self.player_name.get()
            final_score = [[name, self.gamestate.get_score()]]
            self.file_reader.write_score(final_score)
            self.player_name_button_clicked = True

            self.scores_stringvar.set(f"{self.file_reader.print_score()}")
            self.scores_stringvar_label.grid(row=2, column=0, columnspan=2)

    def __throw_button_click(self, force_update=False):
        self.force_update = force_update
        self.__lock_selected_dice()
        self.dice.throw_dice()
        self.gamestate.next_throw()
        if self.gamestate.update(self.force_update):
            self.dice_one_held.set(False)
            self.dice_two_held.set(False)
            self.dice_three_held.set(False)
            self.dice_four_held.set(False)
            self.dice_five_held.set(False)
            self.dice.reset_dice()
        self.info.set(f"Kierros {self.gamestate.get_round()}, heitto {self.gamestate.get_throw()}")
        self.current_dice.set(self.dice.print_dice())

        if self.gamestate.get_round() > 15:
            self.__open_score_window()

    def __lock_selected_dice(self):
        if self.dice_one_held.get() is True and self.dice.get_status(1) is False:
            self.dice.change_status(1)
        if self.dice_two_held.get() is True and self.dice.get_status(2) is False:
            self.dice.change_status(2)
        if self.dice_three_held.get() is True and self.dice.get_status(3) is False:
            self.dice.change_status(3)
        if self.dice_four_held.get() is True and self.dice.get_status(4) is False:
            self.dice.change_status(4)
        if self.dice_five_held.get() is True and self.dice.get_status(5) is False:
            self.dice.change_status(5)

    def __calculate_round_score(self):
        scoring_category = self.scoring_combobox.get().lower()

        if scoring_category == "ykköset" and self.gamestate.get_scoring_method_used("ykköset") == False:
            score = self.scoring.ones(self.dice.get_dice())
            self.gamestate.update_score(score)
            self.gamestate.use_scoring_method("ykköset", score)
        elif scoring_category == "kakkoset" and self.gamestate.get_scoring_method_used("kakkoset") == False:
            score = self.scoring.twos(self.dice.get_dice())
            self.gamestate.update_score(score)
            self.gamestate.use_scoring_method("kakkoset", score)
        elif scoring_category == "kolmoset" and self.gamestate.get_scoring_method_used("kolmoset") == False:
            score = self.scoring.threes(self.dice.get_dice())
            self.gamestate.update_score(score)
            self.gamestate.use_scoring_method("kolmoset", score)
        elif scoring_category == "neloset" and self.gamestate.get_scoring_method_used("neloset") == False:
            score = self.scoring.fours(self.dice.get_dice())
            self.gamestate.update_score(score)
            self.gamestate.use_scoring_method("neloset", score)
        elif scoring_category == "viitoset" and self.gamestate.get_scoring_method_used("viitoset") == False:
            score = self.scoring.fives(self.dice.get_dice())
            self.gamestate.update_score(score)
            self.gamestate.use_scoring_method("viitoset", score)
        elif scoring_category == "kuutoset" and self.gamestate.get_scoring_method_used("kuutoset") == False:
            score = self.scoring.sixes(self.dice.get_dice())
            self.gamestate.update_score(score)
            self.gamestate.use_scoring_method("kuutoset", score)
        elif scoring_category == "yksi pari" and self.gamestate.get_scoring_method_used("yksi pari") == False:
            score = self.scoring.one_pair(self.dice.get_dice())
            self.gamestate.update_score(score)
            self.gamestate.use_scoring_method("yksi pari", score)
        elif scoring_category == "kaksi paria" and self.gamestate.get_scoring_method_used("kaksi paria") == False:
            score = self.scoring.two_pairs(self.dice.get_dice())
            self.gamestate.update_score(score)
            self.gamestate.use_scoring_method("kaksi paria", score)
        elif scoring_category == "kolmoisluku" and self.gamestate.get_scoring_method_used("kolmoisluku") == False:
            score = self.scoring.three_of_a_kind(self.dice.get_dice())
            self.gamestate.update_score(score)
            self.gamestate.use_scoring_method("kolmoisluku", score)
        elif scoring_category == "nelosluku" and self.gamestate.get_scoring_method_used("nelosluku") == False:
            score = self.scoring.four_of_a_kind(self.dice.get_dice())
            self.gamestate.update_score(score)
            self.gamestate.use_scoring_method("nelosluku", score)
        elif scoring_category == "pieni suora" and self.gamestate.get_scoring_method_used("pieni suora") == False:
            score = self.scoring.small_straight(self.dice.get_dice())
            self.gamestate.update_score(score)
            self.gamestate.use_scoring_method("pieni suora", score)
        elif scoring_category == "suuri suora" and self.gamestate.get_scoring_method_used("suuri suora") == False:
            score = self.scoring.large_straight(self.dice.get_dice())
            self.gamestate.update_score(score)
            self.gamestate.use_scoring_method("suuri suora", score)
        elif scoring_category == "täyskäsi" and self.gamestate.get_scoring_method_used("täyskäsi") == False:
            score = self.scoring.full_house(self.dice.get_dice())
            self.gamestate.update_score(score)
            self.gamestate.use_scoring_method("täyskäsi", score)
        elif scoring_category == "sattuma" and self.gamestate.get_scoring_method_used("sattuma") == False:
            score = self.scoring.chance(self.dice.get_dice())
            self.gamestate.update_score(score)
            self.gamestate.use_scoring_method("sattuma", score)
        elif scoring_category == "yatzy" and self.gamestate.get_scoring_method_used("yatzy") == False:
            score = self.scoring.yahtzee(self.dice.get_dice())
            self.gamestate.update_score(score)
            self.gamestate.use_scoring_method("yatzy", score)

        if scoring_category != "valitse pisteytyskategoria":
            self.gamestate.use_scoring_method(scoring_category, True)
            print(f"Valittu pisteytyskategoria {scoring_category}")
            self.dice.reset_dice()
            self.__throw_button_click(True)
            self.scoring_choice_list.remove(self.scoring_combobox.get())
            self.scoring_combobox = ttk.Combobox(master=self._root, values=self.scoring_choice_list)
            self.scoring_combobox.grid(row=4, column=0, columnspan=4)
            self.scoring_combobox.set("Valitse pisteytyskategoria")
        else:
            print("Ei valittu")

        self.current_score.set(f"Pisteet: {self.gamestate.get_score()}")
        print(self.gamestate.get_score())
