#find the number of ways by which we can paint the n fences with k colours such that no 2 fences are of equal colours
#ex- INPUT-n=2 k=4 OUTPUT=16
def paint_fence(n,k):

    same=0
    diff=k

    if(n==1): return(same+diff)

    for i in range(2,n+1):
        temp=(same+diff)*(k-1)
        same=diff
        diff=temp

    return(same+diff)

n,k=map(int,input().split(' '))
print(paint_fence(n,k))