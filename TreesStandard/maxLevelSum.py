#https://practice.geeksforgeeks.org/problems/max-level-sum-in-binary-tree/1
def maxLevelSum(root):
    if root is None:
        return 0
    elif(root.left is None and root.right is None):
        return root.data
    else:
        return max(root.data,maxLevelSum(root.left)+maxLevelSum(root.right))
