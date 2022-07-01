#given an array of the money present in each house,
# being a robber you have to rob the max amount of money, but remember you cannot rob adjacent house
#ex-INPUT-[6,7,1,3,8,2,4] OUTPUT-7+8+4=19
def house_robber(array,i):

    if(i==len(array)-1):
        return array[i]

    if(i>len(array)-1):
        return 0

    cur=array[i]
    return(max(cur+house_robber(array,i+2),house_robber(array,i+1)))

array=[6,7,1,3,8,2,4]
print(house_robber(array,0))
