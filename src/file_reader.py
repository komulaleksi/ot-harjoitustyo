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
            except:
                pass
            finally:
                f = open(self.file_path, "x")
                f.close()

    def write_score(self, score):
        with open(self.file_path, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(score)

    def read_score(self):
        with open(self.file_path, "r") as file:
            reader = csv.reader(file)
            scores = []
            for row in reader:
                scores.append(row)

        return scores

    def print_score(self):
        with open(self.file_path, "r") as file:
            reader = csv.reader(file)
            scores = []
            for row in reader:
                scores.append(row)

            # Järjestää pisteet suurimmasta pienimpään ja tulostaa kymmenen parasta
            top_scores = sorted(scores, key=lambda x: int(x[1]), reverse=True)[0:10]
            top_scores_string = ""
            for score in top_scores:
                top_scores_string += f"{score[0]}: {score[1]} \n"
            return top_scores_string
