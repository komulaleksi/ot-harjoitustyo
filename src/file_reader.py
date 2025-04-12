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
        
    def read_score(self):
        with open(self.file_path, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)