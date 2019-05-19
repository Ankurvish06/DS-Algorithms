class Node:
    def __init__(self,key):
        self.val = key
        self.right = None
        self.left = None

def insert(root,node):
    if(root is None):
        root = node
    else:
        if(root.val<node.val):
            if(root.right is None):
                root.right = node
            else:
                insert(root.right,node)
        else:
            if(root.left is None):
                root.left = node
            else:
                insert(root.left,node)
def pre(root):
    if root:
        print(root.val)
        pre(root.left)
        pre(root.right)
