#check whether the array can be arranged in such a way that every alternative elements are distinct

from collections import defaultdict
T=int(input())
for i in range(T):
    length=int(input())
    array=list(map(int,input().split()))

    count=defaultdict(int)
    for j in array:
        count[j]+=1

    maximum=0
    for j in count.values():
        maximum=max(maximum,j)

    if(maximum-1<=(len(array)-maximum)):
        print("Yes")
    else:
        print("No")