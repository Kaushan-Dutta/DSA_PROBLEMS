def print_grid(arr):
    for i in range(9):
        for j in range(9):
            print(arr[i][j], end=" ")
        print()


def find_empty_location(arr, l):
    for row in range(9):
        for col in range(9):
            if (arr[row][col] == 0):
                l[0] = row
                l[1] = col
                # the above change is reflected
                return True
    return False


def used_in_row(arr, row, num):
    for i in range(9):
        if (arr[row][i] == num):
            return True
    return False


def used_in_col(arr, col, num):
    for i in range(9):
        if (arr[i][col] == num):
            return True
    return False


def used_in_box(arr, row, col, num):
    for i in range(3):
        for j in range(3):
            if (arr[i + row][j + col] == num):
                return True
    return False


def check_location_is_safe(arr, row, col, num):
    return not used_in_row(arr, row, num) and not used_in_col(arr, col, num) and not used_in_box(arr, row - row % 3,
                                                                                                 col - col % 3, num)


def solve_sudoku(arr):
    l = [0, 0]

    if (not find_empty_location(arr, l)):
        print_grid(arr)
        return

    row = l[0]
    col = l[1]

    # consider digits 1 to 9
    for num in range(1, 10):


        if (check_location_is_safe(arr,
                                   row, col, num)):

            arr[row][col] = num


            solve_sudoku(arr)


            # failure, unmake & try again
            arr[row][col] = 0

    # this triggers backtracking
    return


# Driver main function to test above functions
if __name__ == "__main__":



    # assigning values to the grid
    grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
            [5, 2, 0, 0, 0, 0, 0, 0, 0],
            [0, 8, 7, 0, 0, 0, 0, 3, 1],
            [0, 0, 3, 0, 1, 0, 0, 8, 0],
            [9, 0, 0, 8, 6, 3, 0, 0, 5],
            [0, 5, 0, 0, 9, 0, 6, 0, 0],
            [1, 3, 0, 0, 0, 0, 2, 5, 0],
            [0, 0, 0, 0, 0, 0, 0, 7, 4],
            [0, 0, 5, 2, 0, 6, 3, 0, 0]]

    # if success print the grid
    if (solve_sudoku(grid)):
        print_grid(grid)
    else:
        print
        "No solution exists"
