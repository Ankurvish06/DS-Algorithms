https://codeforces.com/problemset/problem/987/C
Can be used for outward for palindrome

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
sumi = []
for i in range(1,len(a)-1):
    s = 10000000000
    l = 10000000000
    for j in range(i):
        if(a[j]<a[i]):
            k = b[i]+b[j]
            if(s>k):
                s = k
    for j in range(i+1,len(a)):
        if(a[j]>a[i]):
            k = b[i]+b[j]
            if(l>k):
                l = k
    sumi.append(s+l-b[i])
if(min(sumi)>=10000000000):
    print(-1)
else:
    print(min(sumi))
