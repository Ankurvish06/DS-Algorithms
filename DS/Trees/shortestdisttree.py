t = int(input())
for _ in range(t):
    i,j = map(int,input().split())
    l = 0
    while(True):
        if(i==j):
            break
        else:
            if(i>j):
                if(i%2==0):
                    i//=2
                    l+=1
                else:
                    i = (i-1)//2
                    l+=1
            else:
                if(j%2==0):
                    j//=2
                    l+=1
                else:
                    j = (j-1)//2
                    l+=1
    print(l)

    https://www.codechef.com/viewsolution/24031912
