#Find the number of unique possible paths for the robot to reach at the bottom-right corner of the matrix if he starts from [0,0] position
#ex INPUT--row=3 colum=2 OUTPUT--POssible paths 3

def unique_paths(matrix,row,column):

    for i in range(row):#initializing the last rows to 1
        matrix[i][column-1]=1
    for i in range(column):#initializing the last columns to 1
        matrix[row-1][i]=1

    for i in range(row-2,-1,-1):#calculating the sum of the left and right box
        for j in range(column-2,-1,-1):
            matrix[i][j]=matrix[i+1][j]+matrix[i][j+1]


    return(matrix[0][0])#the no. of paths is the present element of the [0,0] position

row,column=map(int,input().split(' '))
matrix=[[0]*column for i in range(row)]#way to change every element of matrix to 0

print(unique_paths(matrix,row,column))