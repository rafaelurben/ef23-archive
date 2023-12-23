import random

def random_list(length):
    "Create a random list with numbers from 0 to length"

    l = list(range(length))
    random.shuffle(l)
    return l
