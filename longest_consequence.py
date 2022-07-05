# find the maximum length of the consecutive numbers in the array
# ex INPUT-[100,2,0,200,4,3,1,9] OUTPUT-5

def consequence(array):
    series = set(array)
    maximum = 0

    for i in series:
        if (i - 1 not in series):
            length = 0

            while (i + length in series):
                length += 1
            if (length > maximum):
                maximum = length

    return (maximum)


array = [100, 2, 0, 200, 4, 3, 1, 9]
print(consequence(array))