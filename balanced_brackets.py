'''
    Write a function that accepts a string consisting entiring of brackets ([](){}) and 
    returns whether it is balanced. Every "opening" bracket must be followed by a closing bracket of the same type. 
    There can also be nested brackets, which adhere to the same rule.
'''
import sys
a = "[(])"
a = list(a)
x = []
for i in a:
    len_x = len(x)
    if x == [] and i in ['(','{','[']:
        x.append(i)                   
    elif x != []:                     
        if i in ['(', '{', '[']:
            x.append(i)         
        elif i == ')' and x[len_x-1] == '(':
            x.pop()                         
        elif i == '}' and x[len_x-1] == '{':
            x.pop()                         
        elif i== ']' and x[len_x-1] == '[': 
            x.pop()                        
        else:                              
            print 'unbalanced'
            sys.exit(0)       
    else:                     
        print 'unbalanced'
        sys.exit(0)       
print 'balanced'