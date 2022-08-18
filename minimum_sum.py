# cook your dish here
def gcdd(a,b):
    if (b == 0):
         return a
    return gcdd(b, a%b)

T=int(input())
for i in range(T):
    length=int(input())
    array=list(map(int,input().split()))

    gcd=9999999999
    
    for j in range(1,len(array)):

      hold=gcdd(array[j],array[j-1])
      gcd=min(gcd,hold)
      array[j]=gcd

    print(gcd*len(array))