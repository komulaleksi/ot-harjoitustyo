import os
import csv


class FileReader():
    """Class that handles writing to and reading from scores.csv file.
    """

    def __init__(self, dirname=None, file_path=None):
        if dirname is None:
            self.dirname = os.path.dirname(__file__)
        else:
            self.dirname = dirname
        if file_path is None:
            self.file_path = os.path.join(self.dirname, "data", "scores.csv")
        else:
            self.file_path = file_path

        if not os.path.exists(self.file_path):
            try:
                os.mkdir(os.path.join(self.dirname, "data"))
            except FileExistsError:
                pass
            finally:
                with open(self.file_path, "x", encoding="utf-8") as file:
                    csv.reader(file)

    def write_score(self, score):
        """Writes nickname and score in csv format to data/scores.csv.

        Args:
            score (Str): nickname and score in csv format.
        """
        with open(self.file_path, "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows(score)

    def read_score(self):
        """Reads and returns all lines from data/csv.test.

        Returns:
            List: List of nicknames and scores.
        """
        with open(self.file_path, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            scores = []
            for row in reader:
                scores.append(row)

        return scores

    def print_score(self):
        """Returns top 10 scores sorted from highest to lowest as a string.

        Returns:
            Str: String of top 10 scores sorted.
        """
        with open(self.file_path, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            scores = []
            for row in reader:
                scores.append(row)

            # Järjestää pisteet suurimmasta pienimpään ja tulostaa kymmenen parasta
            top_scores = sorted(
                scores, key=lambda x: int(x[1]), reverse=True)[0:10]
            top_scores_string = ""
            for score in top_scores:
                top_scores_string += f"{score[0]}: {score[1]} \n"
            return top_scores_string
