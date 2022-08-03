#given a number of strings as input, you have to combine all the strings and check how many codechef word
#is there in meal to make it complete
from collections import defaultdict

T = int(input())
for i in range(T):
    accept = int(input())

    string = ""
    for j in range(accept):
        string += input()

    # codechef
    dit = {'c': 2, 'o': 1, 'd': 1, 'e': 2, 'h': 1, 'f': 1}

    hold = defaultdict(int)

    for j in string:
        hold[j] += 1

    calculate = 398578758947

    for j in dit:
        calculate = min(hold[j] // dit[j], calculate)
    print(calculate)