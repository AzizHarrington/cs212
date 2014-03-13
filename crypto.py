"""
  ODD
+ ODD
-----
 EVEN

 solve for O, D, E, V, N
 """

# permutations = 10! = 3mil
# lets try brute force!

"""
Concept inventory:
------------------
Concept      Representation

equations        
    original ==> str
    filled   ==> str
letters      ==> 'D'
digits       ==> '3'
assignment   ==> table 'd' -> '3'  (see str.translate)
    (letter to digit)
evaluation  (see eval())
"""

import string, re

# translate table example
table = string.maketrans('ABC', '123')

f = 'A + B == C'

def valid(f):
    "Formula f is valid if it has no numbers with leading zero and evals true."
    try:

    except ZeroDivisionError: