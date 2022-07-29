#ex-INPUT-[[1,1,0],[1,0,1],[0,0,0]] OUTPUT-[[1,0,0],[0,1,0],[1,1,1]]
def flip(array):
    length=len(array[0])
    for i in array:
        for j in range(length//2):
            if(i[j]==i[length-j-1]):
                i[j]=i[length-j-1]=i[j]^1
        if(length%2!=0):
            i[length//2]^=1
    return(array)

array=[[1,1,1,0],[1,0,0,1],[0,1,0,0]]
print(flip(array))