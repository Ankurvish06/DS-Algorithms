t = int(input())
for _ in range(t):
    n,q = map(int,input().split())
    tree = [0 for i in range(2*n)]
    def build():
        for i in range(n-1,0,-1):
            tree[i] = min(tree[i<<1],tree[i<<1|1])

    def query(l,r):
        res = 10**6+1
        l+=n;r+=n
        while(l<r):
            if(l&1): res = min(res,tree[l]);l+=1
            if(r&1): res = min(res,tree[r-1]);r-=1
            l>>=1;r>>=1
        return res

    tree[n:2*n] = list(map(int,input().split()))
    build()
    c = []
    for _ in range(q):
        l,r = map(int,input().split())
        c.append(query(l-1,r))
    print('Case '+str(_+1)+':')
    for i in range(len(c)):
        print(c[i])
