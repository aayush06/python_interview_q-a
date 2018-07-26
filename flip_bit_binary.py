'''
    Create a function that takes 2 integers, m and n and flips the nth bit of m, counting from the LSB and return the resulting value.
'''

def convert(a,n):
    a = str(bin(a))[2:]
    a = list(a)
    i = len(a)-n
    if a[i] == '1':
        a[i] = '0'
    else:
        a[i] = '1'
    a = ''.join(a)
    return int(a,2)

print convert(8,3)