'''
    Check whether a given binary tree is BST or not
'''

class Tree(object):

    def __init__(self, val, left=None, right=None):
        self.val, self.left, self.right = val, left, right

def is_binary_search_tree(tree, minval=float('-inf'), maxval=float('inf')):
    if not tree:
        return True
    if not minval < tree.val < maxval:
        return False
    return is_binary_search_tree(tree.left, minval, tree.val) and is_binary_search_tree(tree.right, tree.val, maxval)

'''
    create binary tree:  
                            15
                           /  \
                          18   20
'''

t1 = Tree(15,Tree(18), Tree(20))

'''
    create anothe big binary tree:
                             15
                            /  \
                           6    19
                          / \     \
                         4   8     21
'''

t2 = Tree(15,Tree(6,Tree(4), Tree(8)), Tree(19, None, Tree(21)))

print is_binary_search_tree(t1)
print is_binary_search_tree(t2)