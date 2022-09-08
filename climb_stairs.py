#given the number of stais find the number of ways to react the top of stairs if taking only 1 or 2 steps up
#ex INPUT--3 OUTPUT--3
def num_moves(stairs):

    if(stairs<0):
        return 0

    if(stairs==0):
        return 1

    return num_moves(stairs-1)+num_moves(stairs-2)#calulating the number of ways

stairs=int(input())
print(num_moves(stairs))
