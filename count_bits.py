#find the number of 1 present in each number in binary form
#ex INPUT-3 OUTPUT-[0,1,1,2]
#in this we are using a technique which is to find the number which is halve of the number itself and checking the number of 1 that new number is having
#if the number is odd the number then it is going to have a greater 1 bits than its halved number
def countBits(num):

    array = [0, 1]

    if (n == 0): return ([0])
    if (n == 1):
        return ([0, 1])
    else:

        for i in range(2, n + 1):
            array.append(array[i >> 1] + i % 2)#>> means half of the number

    return array
num=int(input())
print(countBits(num))