"""
You have to implement the trace_path() function which will take in a list of source-destination pairs
and return the correct sequence of the whole journey from the first city to the last.

Input
A Python dict containing string pairs of source-destination cities.

Output
A list of source-destination pairs in the correct order.

Sample Input
dict = {
  "NewYork": "Chicago",
  "Boston": "Texas",
  "Missouri": "NewYork",
  "Texas": "Missouri"
}
Sample Output
[["Boston", "Texas"] , ["Texas", "Missouri"] , ["Missouri", "NewYork"] , ["NewYork", "Chicago"]]
"""

def trace_path(my_dict):
    result = list()
    rev_dict = dict()
    for key, value in my_dict.items():
        rev_dict[value] = key
    from_loc = None
    rev_keys = rev_dict.keys()
    for key in my_dict.keys():
        if key not in rev_dict:
            from_loc = key
            break
    to = my_dict.get(from_loc)
    while to is not None:
        result.append([from_loc, to])
        from_loc = to
        to = my_dict.get(to)
    return result
