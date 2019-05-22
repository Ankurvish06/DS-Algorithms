problem : https://www.codechef.com/DEC12/problems/DBOY

import sys
sys.setrecursionlimit(1500)
def ways(arr,sum):
    table = [0 for i in range(sum+1)]

    table[0] = 0
    for i in range(1,sum+1):
        table[i] = sys.maxsize
    for i in range(1,sum+1):
        for j in range(len(arr)):
            if(arr[j]<=i):
                sub_res = table[i-arr[j]]
                if(sub_res!=sys.maxsize and sub_res+1<table[i]):
                    table[i]=sub_res+1
    return table[sum]

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    c = list(map(int,input().split()))
    l = 0
    for i in range(len(a)):
        l+=ways(c,2*a[i])
    print(l)


