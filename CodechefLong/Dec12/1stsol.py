https://www.codechef.com/DEC12/problems/GRANAMA

t = int(input())
for _ in range(t):
    s,l = map(str,input().split())
    s = list(s)
    l = list(l)
    g = sorted(s)
    f = sorted(l)
    h = sorted(list(set(s)))
    j = sorted(list(set(l)))
    if(g==f):
        print('YES')
    elif(h==j):
        print('NO')
    else:
        print('YES')
