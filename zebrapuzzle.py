import itertools

houses = [1, 2, 3, 4, 5]
orderings = list(itertools.permutations(houses))


def zebra_puzzle():
    "Return a tuple (WATER, ZEBRA) indicating their house numbers."
    houses = first, _, middle, _, _ = [1, 2, 3, 4, 5]
    orderings = list(itertools.permutations(houses))
    return next((WATER, ZEBRA)
            for (red, green, ivory, yellow, blue) in orderings
            if imright(green, ivory)
            for (Englishman, Spaniard, Ukrainian, Japanese, Norwegian) in orderings
            if Englishman is red
            if Norwegian is first
            if nextto(Norwegian, blue)
            for (dog, snails, fox, horse, ZEBRA) in orderings
            if Spaniard is dog
            for (coffee, tea, milk, oj, WATER) in orderings
            if coffee is green
            if Ukrainian is tea
            if milk is middle
            for (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) in orderings
            if OldGold is snails
            if Kools is yellow
            if nextto(Chesterfields, fox)
            if nextto(Kools, horse)
            if LuckyStrike is oj
            if Japanese is Parliaments
            )


def imright(h1, h2):
    "House h1 is immediately right of h2 if h1 - h2 == 1."
    return h1 - h2 == 1


def nextto(h1, h2):
    "Two houses are next to each other if they differ by 1."
    return abs(h1 - h2) == 1


import time

def timedcall(fn, *args):
    "Call function and return elapsed time."
    t0 = time.clock()
    result = fn(*args)
    t1 = time.clock()
    return t1-t0, result


print timedcall(zebra_puzzle)
