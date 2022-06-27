#finding out the subarray that is having the maximum sum
#ex-INPUT--array=[-2,1,-3,4,-1,2,1,-5,4] OUTPUT--6(the array is [4,-1,2,1])

def max_subarray(array):
    max_sum=0
    sum=0#though 'sum' is a keyword we can take it as a variable in some case

    for i in range(len(array)):
        sum+=array[i]

        if(sum<0):#if we find that the sum of digits is comming negative we again reinitialize it to 0
            sum=0
        if(sum>max_sum):
            max_sum=sum

    return(max_sum)

array=[-2,1,-3,4,-1,2,1,-5,4]
print(max_subarray(array))