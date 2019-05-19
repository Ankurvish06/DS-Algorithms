import sys
sys.setrecursionlimit(1500)
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
def find(root, x):
    if root.val == x:
        pre(r)
    elif root.val > x:
        find(root.left, x)
    elif root.val < x:
        find(root.right, x)
def pre(root):
    if root:
        print(root.val)
        pre(root.left)
        pre(root.right)
def height(root):
    if(root is None):
        return 0
    else:
        ldepth = height(root.left)
        rdepth = height(root.right)

        if(ldepth>rdepth):
            return ldepth+1
        else:
            return rdepth+1
n = int(input())
a = list(map(int,input().split()))
q = int(input())
r =  Node(a[0])
for i in range(1,len(a)):
    insert(r,Node(a[i]))
find(r,q)
