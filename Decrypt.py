def decrypt(string):

    newstr=''
    i=len(string)-1

    while(i>=0):

        if(string[i]=='#'):
        
           hold=int(string[i-2]+string[i-1])
           newstr+=chr(97+hold-1)
           i-=3

        else:

           hold=int(string[i])
           newstr+=chr(97+hold-1)
           i-=1


    return(newstr)

string='12#123410#11#1#'
print(decrypt(list(string)))
