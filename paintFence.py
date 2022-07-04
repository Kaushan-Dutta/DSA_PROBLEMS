#find the number of ways the certain number of fences can be painted , such that atmost 2 fences can have the same colour
#ex INPUT-n=3 k=2  OUTPUT=6
def fences(n,k):
    if(n==0): return 0
    if(n==1): return k

    same=k
    diff=k*(k-1)

    for i in range(3,n+1):
        prenDiff=diff
        diff=(same+diff)*(k-1)
        same=prevDiff*1

    return same+diff

n,k=map(int,input().split(' '))
print(fences(n,k))