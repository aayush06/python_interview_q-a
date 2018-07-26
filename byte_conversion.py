'''
    Convert a number to a string that represents a rounded size in bytes.
'''

def convert(n, round=2):
    size = ['B', 'KB', 'MB', 'GB', 'PB']
    id = 0
    limit = 1024
    while n>limit:
        n = float(n)/limit
        id += 1
    n = "%.{0}f".format(round) % n
    return "{0} {1}".format(n, size[id])

print convert(156833213)
print convert(8101)
print convert(12331, 3)