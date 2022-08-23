# cook your dish here
from collections import defaultdict
def solve(t):
    n,c=map(int,input().split())
    d=defaultdict(int)

    mod=1000000007

    for _ in range(n-1):
        x,y=map(int,input().split())
        d[x]+=1
    ans=c
    county=1
    for ele in d:
        if county==1:
            k=c-1
            for _ in range(d[ele]):
                ans*=k
                ans%=mod
                k-=1
            county+=1
        else:
            k=c-2
            for _ in range(d[ele]):
                ans*=k
                ans%=mod
                k-=1
    return ans



t=1
print(solve(t))
