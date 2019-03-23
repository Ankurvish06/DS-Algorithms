n,m,k = map(int,input().split())
c = {}
for i in range(1,n+1):
    c[i]= []
for i in range(1,m+1):
    u,v = map(int,input().split())
    c[u].append(v)
    c[v].append(u)
cc = set()
l=0
p = []
for key in c:
    z = set([key]+c[key])
    if(len(z.intersection(cc))==0):
        l+=1
        cc = cc.union(z)
        p.append(len(cc))
    else:
        cc = cc.union(z)
