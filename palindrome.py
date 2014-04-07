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

def longest_subpalindrome_slice(text):
    "Return (i, j) such that text[i:j] is the longest palindrome in text."
    current = {'l': 0, 'points': (0, 0)}
    length = len(text)
    for i in range(length + 1):
        start = current['l']
        if i + start < length:
            for j in range(length + 1)[start:]:
                a = text[i:j]
                b = a[::-1]
                if a.upper() == b.upper() and len(a) > current['l']:
                    current['l'] = len(a)
                    current['points'] = (i, j)
    return current['points']
  

L = longest_subpalindrome_slice

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



# print L('something rac e car going')