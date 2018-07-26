'''
    Write a function that returns true if one string can be formed out of another by reordering ("scrambling") the characters
'''

from itertools import permutations

def check(a,b):
    x = [''.join(i) for i in permutations(a)]
    if b in x:
        return True
    else:
        return False

print check("abc", "cba")
print check("aab", "bba") 