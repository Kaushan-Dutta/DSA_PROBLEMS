
T=int(input())
for i in range(T):
    n=int(input())
    array=list(map(int,input().split()))
    result=list(input())

    mini=436

    for j in range(len(array)):
        if(result[j]=='0'):
            mini=min(mini,array[j])

    print(mini)
