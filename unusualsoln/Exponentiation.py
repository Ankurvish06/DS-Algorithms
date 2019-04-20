# cook your dish here
t = int(input())
while t:
    t-=1
    v,c = map(int,input().split())
    x = str(abs(v)**(c%6))
    y = str(abs(c)**(v%6))
    sumx = 0
    sumy = 0
    for c in x:
        if c is '.':
            continue
        else:
            sumx+=int(c)
    
    for c in y:
        if c is '.':
            continue
        else:
            sumy+=int(c)
    X = sumx%9
    Y = sumy%9
    if X is 0:
        X = 9
    if Y is 0:
        Y = 9
    print(min(X,Y))
    
    
    
    https://www.codechef.com/INTL2019/problems/CHFEDR/
    
