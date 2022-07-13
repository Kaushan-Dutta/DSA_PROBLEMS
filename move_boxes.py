#find the list such that the maximum no. of boxes can be put into other boxes
#ex Input-[0,0,1,0,1,1] Output-[11,8,5,4,3,4]

def move_boxes(array):

    boxes=[]

    for i in range(len(array)):
        count=0
        for j in range(len(array)):

            if(array[j]==1):
                count+=abs(i-j)
        boxes.append(count)

    return boxes

array=[0,0,1,0,1,1]
print(move_boxes(array))