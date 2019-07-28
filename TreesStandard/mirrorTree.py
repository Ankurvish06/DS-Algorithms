#https://practice.geeksforgeeks.org/problems/mirror-tree/1

def mirror(root):
    if root is None:
        return 0
    else:
        if(root.left is None and root.right is None):
            return 
        else:
            mirror(root.left)
            mirror(root.right)
            l = root.right
            root.right = root.left 
            root.left = l
