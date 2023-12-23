# 2022 - Rafael Urben

from tqdm import tqdm
import matplotlib.pyplot as plt
import time

from .rand import random_list

class SortingAlgorithm():
    "A class with utils for sorting algorithms"

    def __init__(self, sortingfunc, *args, **kwargs):
        "Note: args and kwargs are always passed to the sorting function"
        
        self.sortingfunc = sortingfunc
        self._args = args
        self._kwargs = kwargs

    def sort(self, data):
        "Apply the sorting algorithm"

        return self.sortingfunc(data)

    def analyze(self, lengths=5000, samples=10):
        "Create a plot with the sorting algorithm"

        print("Generating graph...")

        numberlist = range(1, lengths)
        timelist = []
        for listlength in tqdm(numberlist):
            unsortedlist = random_list(listlength)

            start = time.time()
            for _ in range(samples):
                sortedlist = self.sortingfunc(unsortedlist, *self._args, **self._kwargs)
            end = time.time()

            wholetime = (end-start)
            timelist.append(wholetime/samples)

            plt.plot(timelist, "b.")
            plt.draw()
            plt.pause(0.0001)
            plt.clf()

        plt.plot(numberlist, timelist, "b.")
        plt.show()

        return numberlist, timelist

    def test(self, length):
        "Test the algorithm with a random list with length"

        l = random_list(length)

        return self.sortingfunc(l, *self._args, **self._kwargs)
