'''
Write a function that accepts two parameters, a parent and a child string.
Determine how many times the child string - or an anagram of the child string - appears in the parent string.
'''
from itertools import permutations
def count(parent, child):
    a = [''.join(i) for i in permutations(child)]
    count = 0
    for i in a:
        if i in parent:
            count += 1

    return count

parent = raw_input("Enter parent string ")
child = raw_input("Enter child string ")
c = count(parent, child)
print c