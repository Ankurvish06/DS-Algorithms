def countLeaves(root):
    if(root==None):
        return 0
    if(root.right==None or root.left==None):
        return 1
    return countLeaves(root.left)+countLeaves(root.right)
