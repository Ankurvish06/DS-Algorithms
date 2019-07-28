#https://practice.geeksforgeeks.org/problems/children-sum-parent/1

def isSumProperty(root):
    '''
    :param root: root of the given tree.
    :return: 1 or 0 , as per the above statement
    {
        # Node Class:
        class Node:
            def __init__(self,val):
                self.data = val
                self.left = None
                self.right = None
    }
    '''
    if root is None:
        return 0
    if(root.right is not None and root.left is not None and root.data==root.left.data+root.right.data):
        return 1
    else:
        return isSumProperty(root.right) and isSumProperty(root.left)
