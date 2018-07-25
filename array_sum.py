'''
    Calculate the sum of an array which contains integers and other arrays with integers. For example:
    array_sum([1,2,[3,4,[5]]])
    would return 15
'''

def array_sum(arr):
    sum = 0
    for item in arr:
        if isinstance(item, list):
            sum = sum + array_sum(item)
        else:
            sum = sum + item
    return sum

print array_sum([1,2,[3,4,[5]]])