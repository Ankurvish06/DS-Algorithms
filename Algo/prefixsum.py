n = int(input())
a = list(map(int,input().split()))
k = sorted(a)
m = int(input())
z = [0]
l = 0
for i in range(len(a)):
    l+=a[i]
    z.append(l)
l = 0
p = [0]
for i in range(len(k)):
    l+=k[i]
    p.append(l)
for i in range(m):
    q,l,r = map(int,input().split())
    if(q==2):
        print(p[r]-p[l-1])
    if(q==1):
        print(z[r]-z[l-1])
