'''
    Write a function that accepts a string consisting entiring of brackets ([](){}) and 
    returns whether it is balanced. Every "opening" bracket must be followed by a closing bracket of the same type. 
    There can also be nested brackets, which adhere to the same rule.
'''
from collections import Counter

a = "()[]{}(([])){[()][]}"

x = Counter(a)

if x['(']==x[')'] and x['{'] == x['}'] and x['['] == x[']']:
    print True
else:
    print False