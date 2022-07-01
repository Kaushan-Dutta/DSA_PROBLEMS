#given 2 strings s1,s2 . find the minimum number of steps to convert s1 to s2 using insert,delte,replace operation
#ex- INPUT-s1->horse s2->ros OUTPUT-3
def edit_distance(s1,s2,i,j):

    if(i<0):
        return j+1#if any one of s1 or s2 reaches to its end then it is sure thst we have to insert the letters equal to the remaining length

    if(j<0):
        return i+1

    if(s1[i]==s2[j]): return(edit_distance(s1,s2,i-1,j-1))#if equal both letter just decrease the position

    return 1+min(edit_distance(s1,s2,i,j-1),min(edit_distance(s1,s2,i-1,j),edit_distance(s1,s2,i-1,j-1)))



s1=input()
s2=input()
print(edit_distance(s1,s2,len(s1)-1,len(s2)-1))
#done with recursion method will be uploading the tabular method later