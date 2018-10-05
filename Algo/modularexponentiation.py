b,p=map(int,input().split())
l= (int)(1e9+7) 
  
# Using direct fast method to compute  
# (a ^ b) % p. 
d = pow(b, p, l) 
print(d)
