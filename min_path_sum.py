#find the path that is having the minimum sum
#ex- [[1,1,5],[0,1,3],[4,0,1]] OUTPUT--3
import math
def min_path(matrix,i,j,x,y):

    if(i==x and j==y):
        return matrix[i][j]

    if(i>x or j>y):
        return math.inf#it will return a float value

    return (matrix[i][j]+(min(min_path(matrix,i,j+1,x,y),min_path(matrix,i+1,j,x,y))))#return the minimum value

matrix=[[1,1,5],[0,1,3],[4,0,1]]
print(min_path(matrix,0,0,len(matrix)-1,len(matrix[0])-1))