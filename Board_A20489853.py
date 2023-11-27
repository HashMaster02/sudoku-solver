import csv
import os
import time


class Puzzle:

    def __init__(self, file):
        self.board = self.read_file(file)

    def read_file(self, file):
        rows = []
        with open(file, newline='') as file:
            data = csv.reader(file)
            for row in data:
                rows.append(list(row))
        return rows

    def write_to(self, filename):
        output_file = f"{filename.split('.')[0]}_solution.csv"
        with open(output_file, "w+") as my_csv:
            writer = csv.writer(my_csv, delimiter=',', lineterminator="\n")
            writer.writerows(self.board)

    def pprint(self):
        os.system('cls')
        for i in range(len(self.board)):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - -")

            for j in range(len(self.board[0])):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")

                if j == 8:
                    print(self.board[i][j])
                else:
                    print(self.board[i][j] + " ", end="")
