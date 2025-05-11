import unittest
from file_reader import FileReader
import os
import csv


class testFileReader(unittest.TestCase):
    def setUp(self):
        dirname = os.path.dirname(__file__)
        self.reader = FileReader(
            None, (os.path.join(dirname, "data", "scores.csv")))

    # TODO
    def test_write_score_writes_score_to_file(self):
        self.reader.write_score([["test", 123]])
