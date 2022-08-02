class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        length = len(matrix)
        width = len(matrix[0])
        
        verify = [[False] * width for i in range(length)]

        for i in range(length):
            for j in range(width):
                if (i == length - 1 or j == width - 1):
                    verify[i][j] = True
                    continue
                if (matrix[i][j] == matrix[i + 1][j + 1]):
                    verify[i][j] = True

        for i in range(length):
            for j in range(width):

                if (verify[i][j] == False):
                    return False
        return True
