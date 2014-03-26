

import string, re


def solve(formula):
    """Given a formula like 'ODD + ODD === EVEN', fill in digits to solve it.
    Input formula is a string; output is a digit-filled-in string or None."""
    return next(f for f in fill_in(formula) if valid(f))


def fill_in(formula):
    """Generate all possible fillings-in of letters in formula with digits."""
    letters = ''.join(set([a for a in formula if a.isalpha()]))
    for digits in itertools.permutations('1234567890', len(letters)):
        table = string.maketrans(letters, ''.join(digits))
        yield formula.translate(table)


def valid(f):
    "Formula f is valid if it has no numbers with leading zero and evals true."
    try:
        return not re.search(r'\b0[0-9]', f) and eval(f) is True
    except ZeroDivisionError:
        return False

