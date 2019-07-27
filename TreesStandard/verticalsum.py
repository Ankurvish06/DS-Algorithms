https://practice.geeksforgeeks.org/problems/vertical-sum/1
c = [0]*1000000
def vs(root,c,index):
  if root is None:
    return 
  c[index]+=root.data
  vs(root.left,c,index-1)
  vs(root.right,c,index+1)
