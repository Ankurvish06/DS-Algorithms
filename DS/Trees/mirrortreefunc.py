def mirror(root):
    if(root==None or (root.left==None and root.right==None)):
        return 0
    mirror(root.left)
    mirror(root.right)
    root.left,root.right=root.right,root.left
    
