"""
In this problem, you have to implement the find_pair() function which will find two pairs, [a, b] and [c, d], in a list such that :

a+b = c+da+b=c+d

You only have to find the first two pairs in the list which satisfies the above condition.

Input
A list of distinct integers.

Output
A list containing two pairs, (a, b) and (c, d), which satisfy a + b = c + d

Sample Input
my_list = [3, 4, 7, 1, 12, 9]
Sample Output
[[4,12],[7,9]]
"""

def find_pair(my_list):
    result = []
    my_dict = dict()
    for i in range(len(my_list)):
        for j in range(i+1, len(my_list)):
            added = my_list[i] + my_list[j]
            if added not in my_dict:
                my_dict[added] = [my_list[i], my_list[j]]
            else:
                prev_pair = my_dict.get(added)
                second_pair = [my_list[i], my_list[j]]
                result.append(prev_pair)
                result.append(second_pair)
                return result
    return result
  
