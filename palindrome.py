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
    longest_palindrome = {'length': 0, 'points': (0, 0)}
    text_length = len(text)
    for i in xrange(text_length + 1):
        start = longest_palindrome['length'] + i
        if start < text_length:
            for j in xrange(start + 1, text_length + 1):
                slc = text[i:j]
                if is_palindrome(slc):
                    expanded = expand_palindrome(slc, text, j)
                    longest_palindrome['length'] = len(expanded[0])
                    longest_palindrome['points'] = (i, expanded[1])
    return longest_palindrome['points']


def expand_palindrome(string, text, end):
    while i <:
        try:
            
            string += text[i]
            i += 1
            print string
        except IndexError:
            break
    return string, end


def is_palindrome(string):
    return string.upper() == string.upper()[::-1]
  

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

# a = "123aaabbbobbbbb bbbaaappleRacecar"

# print L(a)
# print len(a)