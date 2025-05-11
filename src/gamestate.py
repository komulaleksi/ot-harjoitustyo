class GameState():
    """Class that keeps track of and updates the current gamestate.
    """

    def __init__(self, round=1, throw_number=1, score=0):
        """Initializes the gamestate variables.

        Args:
            round (int, optional): Round number. Defaults to 1.
            throw_number (int, optional): Throw number. Defaults to 1.
            score (int, optional): Current score. Defaults to 0.
        """
        self.round = round
        self.throw_number = throw_number
        self.score = score
        self.scoring_method_used = {"ykköset": False,
                                    "kakkoset": False,
                                    "kolmoset": False,
                                    "neloset": False,
                                    "viitoset": False,
                                    "kuutoset": False,
                                    "yksi pari": False,
                                    "kaksi paria": False,
                                    "kolmoisluku": False,
                                    "nelosluku": False,
                                    "pieni suora": False,
                                    "suuri suora": False,
                                    "yatzy": False,
                                    "täyskäsi": False,
                                    "sattuma": False}

    def get_round(self):
        """Returns the current round.

        Returns:
            int: Current round
        """
        return self.round

    def set_round(self, round):
        """Sets the current round.

        Args:
            round (Int): Round number to be updated.
        """
        self.round = round

    def get_throw(self):
        """Returns the current throw number.

        Returns:
            Int: Current throw number.
        """
        return self.throw_number

    def set_throw(self, throw_number):
        """Sets the current throw number.

        Args:
            throw_number (Int): The round number to be updated.
        """
        self.throw_number = throw_number

    def get_score(self):
        """Returns the current score.

        Returns:
            Int: The current score.
        """
        return self.score

    def set_score(self, score):
        """Sets the current score.

        Args:
            score (Int): The score to be updated.
        """
        self.score = score

    def update_score(self, score):
        """Adds to the current score total.

        Args:
            score (int): New points to be added to the score total.
        """
        self.score += score

    def get_scoring_method_used(self, method):
        """Returns the scoring method that was used by desired scoring category.

        Args:
            method (Str): Name of the scoring method to be checked.

        Returns:
            Int: returns score saved to the scoring method.
            Defaults to False/0 if scoring method is not used.
        """
        return self.scoring_method_used[method]

    def return_scoring_method_used(self):
        """Returns list of all scoring methods and their saved score.

        Returns:
            Dict: Returns the dictionary of scoring methods.
        """
        return self.scoring_method_used

    def use_scoring_method(self, method, score):
        """Sets scoring method from False to value in the score variable.

        Args:
            method (Str): String key of self.scroring_method_used.
            score (int): Score value as determined for the selected method by class Scoring.
        """
        self.scoring_method_used[method] = score

    def next_round(self):
        """Increments round by one and resets throws.
        """
        self.round += 1
        self.throw_number = 1

    def next_throw(self):
        """Increments throws by one.
        """
        self.throw_number += 1

    def update(self, force_update=False):
        """Calls next_round() if current throw number exceeds 3.

        Args:
            force_update (bool, optional): Forces next_round() regardless of current throw number.
            Defaults to False.

        Returns:
            bool: Returns whether round was updated.
        """
        if self.throw_number > 3 or force_update:
            self.next_round()
            return True

        return False
