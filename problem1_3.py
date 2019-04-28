#!/usr/bin/python

import sys
import matplotlib.pyplot as plt
import csv
import time


class Perceptron:
    def __init__(self):
        self.inputFile = "./input1.csv"
        self.outputFile = "./output1.csv"
        self.last_w_1 = 0
        self.last_w_2 = 0
        self.last_b = 0

    def start(self):

        input_data = self.csvReader(self.inputFile)

        max_x = 0
        min_x = 0

        for set_ in input_data:
            set_copy = set_[:]
            if set_copy[0] > max_x:
                max_x = set_copy[0]
            if set_copy[1] <= min_x:
                min_x = set_copy[0]

        w_1, w_2, b = 0, 0, 0

        while not self.convergence(w_1, w_2, b):

            self.last_w_1, self.last_w_2, self.last_b = w_1, w_2, b

            for set_ in input_data:
                x = set_[0]
                y = set_[1]
                Y = set_[2]

                Y_ = b + w_1 * x + w_2 * y

                if Y > 0 and Y_ <= 0:
                    w_1 = w_1 + x
                    w_2 = w_2 + y
                    b = b + 1

                elif Y <= 0 and Y_ > 0:
                    w_1 = w_1 - x
                    w_2 = w_2 - y
                    b = b - 1

            self.csvWriter(self.outputFile, [w_1, w_2, b])

            """ For debugging """

            # xlist = [min_x, max_x]
            #
            # if w_2 != 0:
            #     min_y = (-b - w_1 * min_x) / w_2
            #     max_y = (-b - w_1 * max_x) / w_2
            #
            # else:
            #     min_y = 0
            #     max_y = 0
            #
            # ylist = [min_y, max_y]

            # self.display(input_data, xlist=xlist, ylist=ylist, close=True)


    def convergence(self, w_1, w_2, b):

        if w_1 == 0 and w_2 == 0 and b == 0:    # initial state

            return False

        if w_1 == self.last_w_1 and w_2 == self.last_w_2 and b == self.last_b:

            return True

    def display(self, input_data, xlist=None, ylist=None, close=False):

        plt.figure()

        for dot in input_data:
            if int(dot[2]) == 1:
                c = "red"
            else:
                c = "blue"
            plt.scatter(int(dot[0]), int(dot[1]), c=c)

        if xlist and ylist:
            plt.plot(xlist, ylist)

        plt.grid(True)  # линии вспомогательной сетки

        plt.show()

        if close:
            time.sleep(0.5)
            plt.close()

    def csvReader(self, input_file):

        data = []
        with open(input_file, "r", newline="") as file:
                reader = csv.reader(file)
                for row in reader:
                    row_data = []
                    for value in row:
                           row_data.append(value)
                    data.append(row_data)

        file.close()

        for set in data:
            set[0] = int(set[0])
            set[1] = int(set[1])
            set[2] = int(set[2])

        return data

    def csvWriter(self, output_file, list_obj):

        with open(output_file, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(list_obj)

        file.close()

def main(input_file, output_file):
    perceptron = Perceptron()
    perceptron.inputFile = input_file
    perceptron.outputFile = output_file
    perceptron.start()

if __name__ == '__main__':
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    main(input_file, output_file)