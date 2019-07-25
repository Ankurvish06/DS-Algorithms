#https://codeforces.com/problemset/problem/1197/C

n,k = map(int,input().split())
a = list(map(int,input().split()))
c = []
l = a[-1]-a[0]
for i in range(len(a)-1):
    c.append(a[i]-a[i+1])
c = sorted(c)
for i in range(k-1):
    l+=c[i]
print(l)

#Here we have used the logic of assigning min and max to construct a continuous subarray of k segments
