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
