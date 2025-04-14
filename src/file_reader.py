import os
import csv

class FileReader():
    def __init__(self):
        self.dirname = os.path.dirname(__file__)
        self.file_path = os.path.join(self.dirname, "data", "scores.csv")

    def write_score(self, score):
        with open(self.file_path, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(score)
        
    def print_score(self):
        with open(self.file_path, "r") as file:
            reader = csv.reader(file)
            scores = []
            for row in reader:
               scores.append(row)
            
            # Järjestää pisteet suurimmasta pienimpään ja tulostaa kymmenen parasta
            top_scores = sorted(scores, key=lambda x: int(x[1]), reverse=True)[0:10]
            for score in top_scores:
                print(f"{score[0]}: {score[1]}")