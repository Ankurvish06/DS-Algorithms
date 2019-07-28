#https://practice.geeksforgeeks.org/problems/determine-if-two-trees-are-identical/1


def isIdentical(root1, root2):
    if root1 is None and root2 is None:
        return 1
    elif root1 is None and root2 is not None:
        return 0
    elif root1 is not None and root2 is None:
        return 0
    elif(root1.data==root2.data and (root1.left is None and root1.right is None) and (root2.left is None and root2.right is None)):
        return 1
    else:
        return root1.data==root2.data and isIdentical(root1.left,root2.left) and isIdentical(root1.right,root2.right)
        
