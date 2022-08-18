def sequence(array):
    sort=sorted(array)
    sub_1=[]
    sub_2=[]
    count=0
    for i in range(len(array)):
        if(sort[count]==array[i]):
            sub_1.append(array[i])
            count+=1
        else:
            sub_2.append(array[i])
    sub_1=sub_1+sub_2
    return(sub_1)
array=[10,6,7,8,8]
print(sequence(array))