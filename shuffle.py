import random


def shuffle1(deck):
    "Norvig's teacher's algorithm"
    #bad shuffle
    N = len(deck)
    swapped = [False] * N
    while not all(swapped):
        i, j = random.randrange(N), random.randrange(N)
        swapped[i] = swapped[j] = True
        swap(deck, i, j)


def shuffle(deck):
    "Knuth's Algorithm P."
    N = len(deck)
    for i in range(N-1):
        swap(deck, i, random.randrange(i, N))


def swap(deck, i, j):
    "Swap elements i and j of a collection."
    print 'swap', i, j
    deck[i], deck[j] = deck[j], deck[i]