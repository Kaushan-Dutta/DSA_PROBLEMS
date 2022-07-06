#longest square with all ones
#ex INPUT-[[1,1,1,1],[1,1,1,0],[0,0,1,1]] OUTPUT-11
def square_array(array):

    new_array=[[0]*len(array[0]) for i in range(len(array))]

    value=0

    for i in range(len(array)):
        for j in range(len(array[0])):

            if(array[i][j]==1):

              if(i==0 or j==0):
                new_array[i][j]=1
                value+=new_array[i][j]
              else:
                new_array[i][j]=min(array[i-1][j-1],min(array[i-1][j],array[i][j-1]))+1
                value+=new_array[i][j]

    return(value)

array=[[1,1,1,1],
       [1,1,1,0],
       [0,0,1,1]]
print(square_array(array))
#in this program we are calculating the minimum value of the left,right and the upper diagonal of the current room in the matrix and then adding 1 to it