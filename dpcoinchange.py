problem : https://www.codechef.com/DEC12/problems/DBOY


import sys
sys.setrecursionlimit(1500)
def ways(arr,sum):
    if sum==0 :
        return 0
    res = sys.maxsize
    for i in range(len(arr)):
        if(arr[i]<=sum):
            sub_res = ways(arr,sum-arr[i])

            if(sub_res!=sys.maxsize and sub_res+1<res):
                res = sub_res+1
    return res

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    c = list(map(int,input().split()))
    l = 0
    for i in range(len(a)):
        l+=ways(c,2*a[i])
    print(l)


