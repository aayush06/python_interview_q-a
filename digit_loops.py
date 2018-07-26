'''
    Calculate the number of "loops" in a number. A number has a loop when it has a closed circle when you draw it,
    so 6 has one loop, 1 has no loop and 8 has two loops. So 2876 has three loops
'''

a = {'6':1, '8':2, '9':1, '0':1}

count_loop = 0
digit = raw_input("Enter a sequence of numbers ")
for i in digit:
    try:
        count_loop += a[i]
    except:
        continue

print count_loop