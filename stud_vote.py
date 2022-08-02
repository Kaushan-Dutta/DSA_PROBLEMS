#you have to find out how many nuber of students can join the student club
#for the student club he should not be disqualified

from collections import defaultdict

T = int(input())
for i in range(T):
    N, K = list(map(int, input().split()))
    A = list(map(int, input().split()))
    dit = defaultdict(int)

    for j in range(N):
        if (A[j] != j + 1):
            dit[A[j]] += 1
        else:
            dit[A[j]] = -669659885

    count = 0
    for j in dit:
        if (dit[j] >= K):
            count += 1
    print(count)
