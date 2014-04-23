# --------------
# User Instructions
#
# Write a function, longest_subpalindrome_slice(text) that takes 
# a string as input and returns the i and j indices that 
# correspond to the beginning and end indices of the longest 
# palindrome in the string. 
#
# Grading Notes:
# 
# You will only be marked correct if your function runs 
# efficiently enough. We will be measuring efficency by counting
# the number of times you access each string. That count must be
# below a certain threshold to be marked correct.
#
# Please do not use regular expressions to solve this quiz!


def my_longest_subpalindrome_slice(text): #not fast enough....
    "Return (i, j) such that text[i:j] is the longest palindrome in text."
    longest_palindrome = {'length': 0, 'points': (0, 0)}
    text_length = len(text)
    for i in xrange(text_length + 1):
        start = longest_palindrome['length'] + i
        if start < text_length:
            for j in xrange(start + 1, text_length + 1):
                slc = text[i:j]
                if is_palindrome(slc):
                    longest_palindrome['length'] = len(slc)
                    longest_palindrome['points'] = (i, j)
    return longest_palindrome['points']


def is_palindrome(string):
    return string.upper() == string.upper()[::-1]


def norvig_longest_subpalindrome_slice(text):
    "Return (i, j) such that text[i:j] is the longest palindrome in text."
    if text == '': return (0,0)
    def length(slice): a,b = slice; return b-a
    candidates = [grow(text, start, end)
                  for start in range(len(text))
                  for end in (start, start+1)]
    return max(candidates, key=length)


def norvig_grow(text, start, end):
    "Start with a 0- or 1- length palindrome; try to grow a bigger one."
    while (start > 0 and end < len(text)
            and text[start-1].upper() == text[end].upper()):
        start -= 1; end += 1
    return(start, end)


L = my_longest_subpalindrome_slice


def test():
    assert L('racecar') == (0, 7)
    assert L('Racecar') == (0, 7)
    assert L('RacecarX') == (0, 7)
    assert L('Race carr') == (7, 9)
    assert L('') == (0, 0)
    assert L('something rac e car going') == (8,21)
    assert L('xxxxx') == (0, 5)
    assert L('Mad am I ma dam.') == (0, 15)
    return 'tests pass'


print test()