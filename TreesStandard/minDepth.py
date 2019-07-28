#https://practice.geeksforgeeks.org/problems/minimum-depth-of-a-binary-tree/1

def minDepth(root):
    if root is None:
        return 0
    else:
        l = 1+minDepth(root.left)
        r = 1+minDepth(root.right)
        return min(l,r)
