#given an binary array find the sum of the product of the subarray
#ex INPUT-[1,1,1,0,0] OUTPUT-6
def sum_prd(array):
    count = 0
    value = 0
    prev = 0
    for i in array:
        if (i == '1'):
            value += prev + 1
            prev += 1
        else:
            count += value
            prev = 0
            value = 0
    count += value
    return count


T = int(input())
for i in range(T):
    num = int(input())
    array = input().split(' ')

    print(sum_prd(array))