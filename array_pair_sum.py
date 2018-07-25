'''
    Given an integer array, output all pairs that sum up to a specific value k. 
    Consider the fact that the same number can add up to k with its duplicates in the array.
    Note:- Output only distinct values
    example:-[3, 4, 5, 6, 7] sum = 10, sol = [(6, 4), (7, 3)] 
'''
from itertools import combinations
def solution(l, target_sum):
    x = [j for j in combinations(l, 2) if sum(j)==target_sum]
    return x

l = raw_input("Enter space seperated numbers ")
l = l.split(' ')
l = [int(i) for i in l]
target_sum = raw_input("Enter target sum required ")
print solution(l, int(target_sum))