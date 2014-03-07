import itertools

houses = [1, 2, 3, 4, 5]
orderings = list(itertools.permutations(houses))


def zebra_puzzle():
    "Return a tuple (WATER, ZEBRA) indicating their house numbers."
    houses = first, _, middle, _, _ = [1, 2, 3, 4, 5]
    orderings = list(itertools.permutations(houses))
    return next((WATER, ZEBRA)
            for (red, green, ivory, yellow, blue) in c(orderings)
            if imright(green, ivory)
            for (Englishman, Spaniard, Ukrainian, Japanese, Norwegian) in c(orderings)
            if Englishman is red
            if Norwegian is first
            if nextto(Norwegian, blue)
            for (dog, snails, fox, horse, ZEBRA) in c(orderings)
            if Spaniard is dog
            for (coffee, tea, milk, oj, WATER) in c(orderings)
            if coffee is green
            if Ukrainian is tea
            if milk is middle
            for (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) in c(orderings)
            if OldGold is snails
            if Kools is yellow
            if nextto(Chesterfields, fox)
            if nextto(Kools, horse)
            if LuckyStrike is oj
            if Japanese is Parliaments
            )


def instrument_fn(fn, *args):
    c.starts, c.items = 0, 0
    result = fn(*args)
    print "%s got %s with %5d iters over %7d items" % (
        fn.__name__, result, c.starts, c.items)


def c(sequence):
    """Generate items in sequence; keeping counts as we go. c.starts is the
    number of sequences started; c.items is number of items generated."""
    c.starts += 1
    for item in sequence:
        c.items += 1
        yield item 


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


def timedcalls(n, fn, *args):
    """Call fn(*args) repeatedly: n times if n is an int, or up to
    n seconds if n is a loat; return the min, avg, and max time"""
    if isinstance(n, int):
        times = [timedcall(fn, *args)[0] for _ in range(n)]
    else:
        time0 = time.clock()
        time1 = time.clock()
        times = []
        while time1 - time0 < n:
            times.append(timedcall(fn, *args)[0])
            time1 = time.clock()
        return times

    return min(times), average(times), max(times)


def average(numbers):
    "Return the average (arithmetic mean) of a sequence of numbers."
    return sum(numbers) / float(len(numbers))
