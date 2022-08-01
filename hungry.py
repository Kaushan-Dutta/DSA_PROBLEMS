#find the number of normal and premium burgers a chef can buy if he have R amt of money and want to buy total N number of burgers
T = int(input())
for i in range(T):
    a, b, n, r = list(map(int, input().split()))

    if (n * a > r):
        print(-1)
    elif (r // b >= n):
        print("0", n)

    else:
        z = (r - n * a) // (b - a)
        print(n - z, " ", z)
