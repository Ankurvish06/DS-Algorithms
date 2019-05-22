https://www.codechef.com/DEC12/problems/MGCRNK

Required Dp solution of two states:
for _ in range(int(input())):
    n = int(input())
    l,dp = [],[]
    for i in range(n):
        l.append(list(map(int,input().split())))
        dp.append([0]*n)
    for i in range(1,n):
        dp[0][i] = dp[0][i-1] + l[0][i]
        dp[i][0] = dp[i-1][0] + l[i][0]
    for i in range(1,n):
        for j in range(1,n):
            dp[i][j] = l[i][j] + max(dp[i-1][j],dp[i][j-1])
    if(dp[n-1][n-1]<0):
        print('Bad Judges')
    else:
        print(dp[n-1][n-1]/(2*n-3))
