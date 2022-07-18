#given a string, check whether the string can be formed using copy paste method and using the selective method
#ex- INPUT-abaaba OUTPUT-YES
def copy_push(accept):

    a=0

    if(len(accept)==2):
        if(accept[0]==accept[1]):
            return "YES"
        return "NO"

    for i in range(1,len(accept)):

        left_sub=accept[0:i]
        right_sub=accept[i:len(left_sub)+i]

        print(left_sub,right_sub,a)

        if(left_sub==right_sub):
            if(i+len(left_sub)==len(accept)):
                return "YES"
            continue

        if(a==0):
            a=1
            continue

        if(a==1):
            return "NO"

    return("YES")

accept=input()
print(copy_push(accept))