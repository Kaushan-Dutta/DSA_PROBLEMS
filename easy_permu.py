#find the permutation in the array such that, it can have the minimum LCM
T=int(input())

for i in range(T):
    accept=int(input())
    calc=1+accept
    stri=[]
    for j in range(1,accept+1):
        stri.append(str(calc-j))

    print(' '.join(stri))
